#!/usr/bin/env python3
"""
video_to_source.py — turn a local lecture video into timestamped study material.

Part of the anything-to-learn skill. Optional: the rest of the skill is plain
Markdown and works without this script.

What it does
  1. Text: uses subtitles if any exist (a file you pass, a sidecar .srt/.vtt next to
     the video, or a subtitle track embedded in the video). Otherwise it transcribes
     the audio locally with faster-whisper or openai-whisper, if one is installed.
  2. Pictures: grabs a frame each time the picture changes a lot (a new slide, a new
     board), so the agent can read what was on screen.
  3. Writes <out>/video-source.md: chunks of transcript with their time range and the
     frames shown during them, ready to fold into the skill's source-pack.md.

Requirements
  - Python 3.8+ (standard library only)
  - ffmpeg and ffprobe on PATH
  - For videos without subtitles: `pip install faster-whisper` (recommended) or
    `pip install openai-whisper`. The first run downloads the speech model.

Usage
  python video_to_source.py lecture03.mp4
  python video_to_source.py lecture03.mp4 --subs lecture03.zh.srt
  python video_to_source.py lecture03.mp4 --lang zh --model medium
  python video_to_source.py lecture03.mp4 --no-transcribe        # frames only
  python video_to_source.py lecture03.mp4 --every 60             # a frame every 60 s

Nothing is uploaded anywhere: everything runs on this machine.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SIDE_SUB_EXTS = (".srt", ".vtt")
TEXT_SUB_CODECS = {"subrip", "srt", "ass", "ssa", "webvtt", "mov_text", "text"}


# --------------------------------------------------------------------------- utils

def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def info(msg):
    print(msg, file=sys.stderr)


def run(cmd, capture=True):
    return subprocess.run(cmd, capture_output=capture, text=True, encoding="utf-8",
                          errors="replace")


def fmt_ts(sec, sep=":"):
    sec = max(0, int(round(sec)))
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}{sep}{m:02d}{sep}{s:02d}" if h else f"{m:02d}{sep}{s:02d}"


def fmt_srt_ts(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def check_tools():
    missing = [t for t in ("ffmpeg", "ffprobe") if shutil.which(t) is None]
    if missing:
        die(f"{', '.join(missing)} not found on PATH. Install ffmpeg first "
            "(macOS: brew install ffmpeg · Ubuntu: sudo apt install ffmpeg · "
            "Windows: winget install ffmpeg).")


def probe(video):
    r = run(["ffprobe", "-v", "error", "-print_format", "json",
             "-show_format", "-show_streams", str(video)])
    if r.returncode != 0:
        die(f"ffprobe could not read {video}: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout)


# ---------------------------------------------------------------------- subtitles

_TS = r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})"
_CUE = re.compile(_TS + r"\s*-->\s*" + _TS)


def _ts_to_sec(h, m, s, ms):
    return int(h or 0) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000


def _clean(line):
    line = re.sub(r"<[^>]+>", "", line)        # <i>, <c>, VTT word timestamps
    line = re.sub(r"\{\\[^}]*\}", "", line)    # {\an8} ASS-style tags
    return line.strip()


def parse_subs(path):
    """Parse .srt or .vtt into [(start, end, text)], dropping rolling duplicates."""
    text = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    cues, cur = [], None
    for raw in text.splitlines():
        m = _CUE.search(raw)
        if m:
            if cur and cur[2]:
                cues.append(cur)
            g = m.groups()
            cur = [_ts_to_sec(*g[0:4]), _ts_to_sec(*g[4:8]), []]
            continue
        if cur is None:
            continue
        line = _clean(raw)
        if not line:
            if cur[2]:
                cues.append(cur)
                cur = None
            continue
        if line.isdigit() and not cur[2]:
            continue
        cur[2].append(line)
    if cur and cur[2]:
        cues.append(cur)

    out, last_lines = [], []
    for start, end, lines in cues:
        # auto-generated captions repeat the previous line before adding a new one
        new = [ln for ln in lines if ln not in last_lines]
        last_lines = lines
        if new:
            out.append((start, end, " ".join(new)))
    return out


def find_sidecar(video):
    stem = video.with_suffix("")
    cands = sorted(p for p in video.parent.glob(stem.name + "*")
                   if p.suffix.lower() in SIDE_SUB_EXTS)
    return cands[0] if cands else None


def extract_embedded(video, meta, workdir):
    for st in meta.get("streams", []):
        if st.get("codec_type") == "subtitle" and st.get("codec_name") in TEXT_SUB_CODECS:
            out = workdir / "embedded.srt"
            r = run(["ffmpeg", "-y", "-v", "error", "-i", str(video),
                     "-map", f"0:{st['index']}", str(out)])
            if r.returncode == 0 and out.exists() and out.stat().st_size > 0:
                lang = (st.get("tags") or {}).get("language", "")
                return out, lang
    return None, None


# ------------------------------------------------------------------ transcription

def transcribe(video, workdir, lang, model_name, prompt):
    audio = workdir / "audio.wav"
    info("extracting audio …")
    r = run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-vn",
             "-ac", "1", "-ar", "16000", str(audio)])
    if r.returncode != 0:
        info(f"could not extract audio: {r.stderr.strip()[:300]}")
        return None, None

    if prompt is None and lang in ("zh", "zh-cn", "chinese"):
        prompt = "以下是普通话的课程讲解，使用简体中文。"   # nudges Whisper to Simplified

    try:
        from faster_whisper import WhisperModel  # type: ignore
        info(f"transcribing with faster-whisper ({model_name}) — this can take a while …")
        model = WhisperModel(model_name, device="auto", compute_type="default")
        segs, inf = model.transcribe(str(audio), language=lang, vad_filter=True,
                                     initial_prompt=prompt)
        out = [(s.start, s.end, s.text.strip()) for s in segs if s.text.strip()]
        return out, f"faster-whisper/{model_name} (lang={inf.language})"
    except ImportError:
        pass

    try:
        import whisper  # type: ignore
        info(f"transcribing with openai-whisper ({model_name}) — this can take a while …")
        model = whisper.load_model(model_name)
        res = model.transcribe(str(audio), language=lang, initial_prompt=prompt)
        out = [(s["start"], s["end"], s["text"].strip())
               for s in res["segments"] if s["text"].strip()]
        return out, f"openai-whisper/{model_name} (lang={res.get('language')})"
    except ImportError:
        pass

    info("no speech-to-text engine found. To transcribe videos without subtitles, run:\n"
         "    pip install faster-whisper\n"
         "Continuing with frames only.")
    return None, None


# ------------------------------------------------------------------------ frames

THUMB_W, THUMB_H, SAMPLE_FPS = 64, 36, 1


def scene_times(video, threshold):
    """Times where the picture differs from the last kept frame by > threshold.

    Compares small colour thumbnails once per second against the last *kept* frame,
    not the previous second, so slides that build up bullet by bullet still trigger
    once enough has changed. Colour is compared per channel: ffmpeg's built-in scene
    score is mostly luma and misses slides whose backgrounds differ only in hue.
    threshold = fraction of thumbnail pixels that must change (default 0.04).
    """
    frame_bytes = THUMB_W * THUMB_H * 3
    cmd = ["ffmpeg", "-v", "error", "-i", str(video), "-an", "-sn",
           "-vf", f"fps={SAMPLE_FPS},scale={THUMB_W}:{THUMB_H}",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    times, ref, i = [], None, 0
    n_px = THUMB_W * THUMB_H
    while True:
        buf = proc.stdout.read(frame_bytes)
        if len(buf) < frame_bytes:
            break
        if ref is None:
            ref = buf
        else:
            changed = 0
            for p in range(0, frame_bytes, 3):
                if (abs(buf[p] - ref[p]) + abs(buf[p + 1] - ref[p + 1])
                        + abs(buf[p + 2] - ref[p + 2])) > 48:
                    changed += 1
            if changed / n_px > threshold:
                times.append(i / SAMPLE_FPS)
                ref = buf
        i += 1
    proc.wait()
    return times


def pick_times(duration, scenes, min_gap, max_gap, every, max_frames):
    if every:
        times = [t for t in frange(0, duration, every)]
    else:
        times, last = [0.0], 0.0
        for t in sorted(scenes):
            # fill long static stretches so nothing is missed
            while max_gap and t - last > max_gap:
                last += max_gap
                times.append(last)
            if t - last >= min_gap:
                times.append(t)
                last = t
        while max_gap and duration - last > max_gap:
            last += max_gap
            times.append(last)
    if len(times) > max_frames:
        step = len(times) / max_frames
        times = [times[int(i * step)] for i in range(max_frames)]
    return times


def frange(a, b, step):
    t = a
    while t < b:
        yield t
        t += step


def grab_frames(video, times, frames_dir, offset=0.5):
    frames_dir.mkdir(parents=True, exist_ok=True)
    out = []
    for i, t in enumerate(times, 1):
        at = t + offset if t > 0 else 0.0     # just after the cut, once the slide settles
        name = f"{i:04d}_{fmt_ts(at, '-')}.jpg"
        path = frames_dir / name
        r = run(["ffmpeg", "-y", "-v", "error", "-ss", f"{at:.3f}", "-i", str(video),
                 "-frames:v", "1", "-q:v", "3", "-vf", "scale='min(1280,iw)':-2",
                 str(path)])
        if r.returncode == 0 and path.exists():
            out.append((t, f"frames/{name}"))
    return out


# ----------------------------------------------------------------------- chunking

def chunk(segments, frames, duration, target=180.0, min_len=20.0):
    """Split the timeline at slide changes; long stretches are split again near
    `target` seconds at a segment start. Segments go to the chunk holding their
    midpoint, frames to the chunk holding their time."""
    end = max([duration] + [s[1] for s in segments])

    # 1. boundaries at slide changes, dropping ones too close to the previous one
    bounds = [0.0]
    for t, _ in sorted(frames):
        if t - bounds[-1] >= min_len and end - t >= min_len:
            bounds.append(t)
    bounds.append(end)

    # 2. split long stretches at segment starts so chunks stay readable
    starts = sorted(s[0] for s in segments)
    final = [bounds[0]]
    for b in bounds[1:]:
        a = final[-1]
        while b - a > target * 1.5:
            cands = [s for s in starts if a + target * 0.6 <= s <= a + target * 1.4]
            if not cands:
                break
            a = min(cands, key=lambda s: abs(s - (final[-1] + target)))
            final.append(a)
        final.append(b)

    # 3. fill
    result = []
    for a, b in zip(final, final[1:]):
        last = b == final[-1]
        texts = [s[2] for s in segments
                 if a <= (s[0] + s[1]) / 2 < b or (last and (s[0] + s[1]) / 2 == b)]
        fr = [p for t, p in frames if a <= t < b or (last and t == b)]
        if texts or fr:
            result.append((a, b, " ".join(texts), fr))
    return result


# --------------------------------------------------------------------------- write

def write_outputs(out, video, duration, source_desc, segments, chunks, n_frames):
    if segments:
        with open(out / "transcript.srt", "w", encoding="utf-8") as f:
            for i, (a, b, t) in enumerate(segments, 1):
                f.write(f"{i}\n{fmt_srt_ts(a)} --> {fmt_srt_ts(b)}\n{t}\n\n")

    lines = [
        f"# Video source — {video.name}",
        "",
        f"duration: {fmt_ts(duration)} · text: {source_desc} · frames: {n_frames}",
        "",
        "For the agent: each chunk below becomes one or more source-pack chunks with",
        f"`source: {video.name} <start>–<end>`. Open the listed frames to read slides,",
        "formulas and board content, and merge what they show into the chunk.",
        "Machine transcription can mishear terms and formulas — mark doubtful ones with ⚠.",
        "",
    ]
    if not segments:
        lines += ["> No transcript: only frames are available. The spoken explanation is",
                  "> missing — tell the learner, and ask for subtitles or a transcript if",
                  "> the slides alone are not enough.", ""]
    for i, (a, b, text, frames) in enumerate(chunks, 1):
        lines.append(f"## [V{i}] {fmt_ts(a)}–{fmt_ts(b)}")
        lines.append(f"source: {video.name} {fmt_ts(a)}–{fmt_ts(b)}")
        if frames:
            lines.append("frames: " + " · ".join(frames))
        if text:
            lines += ["", text]
        lines.append("")
    (out / "video-source.md").write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video", type=Path, help="local video file")
    ap.add_argument("--out", type=Path, help="output folder (default: <video>_source/)")
    ap.add_argument("--subs", type=Path, help="subtitle file to use (.srt or .vtt)")
    ap.add_argument("--lang", help="spoken language for transcription, e.g. zh, en")
    ap.add_argument("--model", default="small",
                    help="Whisper model: tiny/base/small/medium/large-v3 (default: small)")
    ap.add_argument("--prompt", help="initial prompt for Whisper (terms, course name)")
    ap.add_argument("--no-transcribe", action="store_true",
                    help="never run speech-to-text; use subtitles or frames only")
    ap.add_argument("--no-frames", action="store_true", help="skip frame extraction")
    ap.add_argument("--scene", type=float, default=0.04,
                    help="share of the picture that must change for a new frame, 0–1; "
                         "lower = more frames (default 0.04)")
    ap.add_argument("--min-gap", type=float, default=20.0,
                    help="minimum seconds between frames (default 20)")
    ap.add_argument("--max-gap", type=float, default=180.0,
                    help="add a frame if nothing changed for this long; 0 = off (default 180)")
    ap.add_argument("--every", type=float, help="fixed interval in seconds instead of scene detection")
    ap.add_argument("--max-frames", type=int, default=150, help="cap on frames (default 150)")
    a = ap.parse_args()

    check_tools()
    video = a.video.expanduser().resolve()
    if not video.is_file():
        die(f"no such file: {video}")
    out = (a.out or video.with_name(video.stem + "_source")).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    work = out / ".work"
    work.mkdir(exist_ok=True)

    meta = probe(video)
    duration = float(meta.get("format", {}).get("duration") or 0)
    has_video = any(s.get("codec_type") == "video" for s in meta.get("streams", []))
    info(f"{video.name}: {fmt_ts(duration)}")

    # 1. text
    segments, source_desc = None, None
    sub_path = a.subs or find_sidecar(video)
    if sub_path:
        segments, source_desc = parse_subs(sub_path), f"subtitles ({Path(sub_path).name})"
    if not segments:
        emb, lang = extract_embedded(video, meta, work)
        if emb:
            segments = parse_subs(emb)
            source_desc = f"embedded subtitles{f' ({lang})' if lang else ''}"
    if not segments and not a.no_transcribe:
        segments, source_desc = transcribe(video, work, a.lang, a.model, a.prompt)
    segments = segments or []
    source_desc = source_desc or "none"
    info(f"text: {source_desc}, {len(segments)} segments")

    # 2. frames
    frames = []
    if has_video and not a.no_frames:
        info("finding slide / scene changes …")
        scenes = [] if a.every else scene_times(video, a.scene)
        times = pick_times(duration, scenes, a.min_gap, a.max_gap, a.every, a.max_frames)
        frames = grab_frames(video, times, out / "frames")
        info(f"frames: {len(frames)}")

    # 3. write
    chunks = chunk(segments, frames, duration)
    write_outputs(out, video, duration, source_desc, segments, chunks, len(frames))
    (out / "meta.json").write_text(json.dumps({
        "video": str(video), "duration_sec": duration, "text_source": source_desc,
        "segments": len(segments), "frames": len(frames), "chunks": len(chunks),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.rmtree(work, ignore_errors=True)

    print(out / "video-source.md")


if __name__ == "__main__":
    main()
