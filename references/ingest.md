# Ingest: any material → source pack

Goal: one `source-pack.md` the rest of the skill can teach from, where every chunk says
where it came from. Provenance is what lets the learner check you, and lets you say
"this is on slide 14" when they ask where something was.

## Source pack format

```markdown
# Source pack — <course or topic>
Built: <date> · Inputs: <list of files / links>

## [S1] <short title>
source: lecture03.pdf p.4–6
<extracted text, cleaned; formulas in LaTeX; tables as markdown>
figures: [S1-f1] diagram of the attention block — <one-line description of what it shows>

## [S2] ...
```

- Chunk by idea, not by page: one chunk ≈ one concept, definition, derivation, or example.
- Keep the original wording for definitions, formulas and anything likely to be examined
  verbatim; summarize the rest.
- Mark every uncertainty inline: `⚠ formula partly illegible — confirm`.
- Content you add from outside the material goes in a chunk tagged `origin: tutor` so it
  is never mistaken for course content.

## By input type

| Input | How | Watch for |
|---|---|---|
| **PDF (text)** | Extract text per page; render pages that are mostly figures and look at them | Two-column layouts scrambling text order; headers/footers repeated on every page |
| **PDF (scanned)** | Render pages to images and read them visually (OCR if many pages) | Low resolution — ask for a better scan rather than guess |
| **Slides (.pptx / Keynote export / PDF of slides)** | Text per slide + speaker notes; render slides whose meaning lives in a diagram | Slides are fragments: the lecture's connective reasoning is often missing — note gaps and fill them as `origin: tutor` |
| **Word / Markdown / plain text** | Direct | — |
| **Screenshots, photos, whiteboard** | Read the image; transcribe formulas to LaTeX | Handwriting: list the transcribed formulas back to the learner for confirmation before teaching from them |
| **Video file** | If you can run commands, use `scripts/video_to_source.py` (see **Video** below). Otherwise: subtitles if present, a transcript if the learner has one, and screenshots they send | Keep timestamps (`source: lec5.mp4 23:10–31:40`); say plainly what was missing (no audio transcript, no frames) |
| **Video link (YouTube, course site)** | You usually cannot watch or download it. Ask for the transcript (many course sites and YouTube offer one), subtitle file, or the slides used in the lecture | Do not pretend to have watched it |
| **Audio / recording** | Same script — it handles audio-only files (subtitles or Whisper, no frames); otherwise ask for a transcript | Speaker asides vs. content |
| **Web page / course site** | Fetch the page text | Paywalls and JS-only pages may fail — ask the learner to paste or save as PDF |
| **Code / repo / notebook** | Read the files; chunk by function or concept, not by file | Generated or vendored code — skip it |
| **Just a topic** | Build from general knowledge plus looked-up sources; every chunk `origin: tutor` or with its URL | Note that there is no "official" version to be examined against |
| **Past exams / problem sets** | Keep separate under `## Exam material`; they calibrate sprint mode | These show what the course actually tests — weight them heavily |

## Video

The skill ships an optional helper, `scripts/video_to_source.py` (Python standard
library + ffmpeg; local Whisper only when a video has no subtitles). It runs entirely on
the learner's machine.

```bash
python <skill-dir>/scripts/video_to_source.py lecture05.mp4 [--lang zh] [--subs file.srt]
```

What it does, in order:

1. **Text**: a subtitle file passed with `--subs`, else a sidecar `.srt`/`.vtt` with the
   same name, else an embedded subtitle track, else local speech-to-text with
   faster-whisper / openai-whisper if installed. Subtitles always win: they are faster
   and usually more accurate than machine transcription.
2. **Frames**: one frame each time the picture changes enough (new slide, new board,
   a slide that built up bullet by bullet), plus one every 3 minutes of no change.
3. **Output** in `<video>_source/`: `video-source.md` (chunks split at slide changes,
   each with its time range, the frames shown, and the words spoken), `transcript.srt`,
   `frames/*.jpg`, `meta.json`.

Then build the source pack from it:

- Open the frames and read them — slides carry the formulas, definitions and figures
  the transcript only refers to ("as you can see here…"). Merge each frame's content
  into its chunk.
- Re-chunk by idea where needed; keep `source: <video> mm:ss–mm:ss` on every chunk.
- Machine transcripts mishear technical terms and symbols ("soft max", "KV cash"). Fix
  them from the slides where the slide shows the term; otherwise mark `⚠ heard as …`.
- If the script reports no text source, the spoken explanation is missing. Say so in
  the confirmation step and offer: subtitles, a transcript, or `pip install faster-whisper`.

Before running it:

- **Ask first** for long videos or the first Whisper run — transcription of a 90-minute
  lecture can take minutes to an hour depending on the machine, and the first run
  downloads a speech model (hundreds of MB for `small`, more for `medium`/`large-v3`).
- **Missing tools**: if ffmpeg is not installed, tell the learner the one-line install
  for their OS (the script prints it). Never install software without asking.
- **No shell** (plain chat): skip the script; ask for subtitles, a transcript, or
  screenshots of key slides.
- **Online videos**: the script takes local files only. Ask the learner for the
  platform's subtitle/transcript export or the lecture slides; don't try to download
  videos from sites.

Useful options: `--lang zh` (also nudges Whisper toward Simplified Chinese), `--model
medium` (better accuracy, slower), `--prompt "CS336, KV cache, FlashAttention"` (course
terms help Whisper spell them), `--every 60` (fixed interval for videos where scene
detection over- or under-fires, e.g. a camera filming a whiteboard), `--no-transcribe`
(frames only).

## The confirmation step

After building the pack, show the learner one screen:

```
I extracted 23 chunks from 3 files:
  lecture03.pdf  — attention, multi-head, positional encoding (S1–S9)
  board.jpg      — derivation of softmax gradient (S10)  ⚠ 2 symbols unclear
  lec3.mp4       — 18 slides + Whisper transcript (V1–V12); 3 terms unclear ⚠
Anything wrong or missing before we start?
```

Keep it to that size. If everything is clean, one line is enough and you can start.
