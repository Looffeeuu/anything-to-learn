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
| **Video file** | Use subtitles if present (`.srt`/`.vtt`, or embedded tracks). Otherwise extract the audio and transcribe if a speech-to-text tool is available; extract frames at slide changes to capture what's on screen | Long videos: chunk by topic shifts, keep timestamps (`source: lec5.mp4 23:10–31:40`) |
| **Video link (YouTube, course site)** | You usually cannot watch or download it. Ask for the transcript (many course sites and YouTube offer one), subtitle file, or the slides used in the lecture | Do not pretend to have watched it |
| **Audio / recording** | Transcribe if a tool is available; otherwise ask for a transcript | Speaker asides vs. content |
| **Web page / course site** | Fetch the page text | Paywalls and JS-only pages may fail — ask the learner to paste or save as PDF |
| **Code / repo / notebook** | Read the files; chunk by function or concept, not by file | Generated or vendored code — skip it |
| **Just a topic** | Build from general knowledge plus looked-up sources; every chunk `origin: tutor` or with its URL | Note that there is no "official" version to be examined against |
| **Past exams / problem sets** | Keep separate under `## Exam material`; they calibrate sprint mode | These show what the course actually tests — weight them heavily |

## The confirmation step

After building the pack, show the learner one screen:

```
I extracted 23 chunks from 3 files:
  lecture03.pdf  — attention, multi-head, positional encoding (S1–S9)
  board.jpg      — derivation of softmax gradient (S10)  ⚠ 2 symbols unclear
  lec3.mp4       — no subtitles; I used the slides only, the spoken parts are missing
Anything wrong or missing before we start?
```

Keep it to that size. If everything is clean, one line is enough and you can start.
