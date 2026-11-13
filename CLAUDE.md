# CLS presentation: how this deck is built

This repository holds a slide presentation built the same way as the Johns Hopkins workshop deck (*Cleaning, Structuring and Grounding Historical Data*, 15 October 2026). That deck is the reference implementation:

- Source: <https://github.com/jburnford/imperial-careers-workshop>
- Live deck: <https://jimclifford.ca/imperial-careers-workshop/slides.html?motion>

When a pattern below is unclear, open the matching file in that repository and copy it: [`slides.qmd`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides.qmd), [`slides.scss`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides.scss), [`slides-motion.html`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides-motion.html), [`workshop.js`](https://github.com/jburnford/imperial-careers-workshop/blob/main/workshop.js), [`scripts/`](https://github.com/jburnford/imperial-careers-workshop/tree/main/scripts). Don't invent a new system.

## The talk

From `CLS Presentation Rough Notes.docx`. The slide-by-slide plan is in [outline.md](outline.md).

| | |
|---|---|
| Working title | *Do better, not more* |
| Venue, date, time | CLS: TBD (full name, date, room, Zoom?) |
| Length | about 35–45 minutes, plus questions |
| Speakers, in order | Jim opens (5 min) → Jessica, general (10–15 min, 10–15 slides) → Jacob, specific and technical (10–15 min, 10–15 slides) → Jim closes (10 min) |
| Audience | TBD: confirm; probably historians, mostly not computational |
| Core argument | Coding agents flatten the skills barrier and make iteration fast, so computational history may finally grow as computational physics did. The question is how to use that to do *better* history, not just *more*. |
| Material | The speakers' own projects: Jessica's interactive visualizations, Jacob's knowledge graph and GraphRAG work, Jim's projects and editorial experience |
| Public URL | TBD (GitHub Pages from `docs/`) |

### Three speakers, one deck

**Who builds what.** Jim's agents build sections 1 and 4 (`_1-jim-open.qmd`, `_4-jim-close.qmd`). Jessica's and Jacob's agents build sections 2 and 3. Don't edit another speaker's section. If you change a shared file (`slides.qmd`, `slides.scss`, `slides-motion.html`, `CLAUDE.md`), do it in its own commit with a message that says what changed, because the other speakers' agents build on it.

Each speaker edits their own section file, which keeps merge conflicts down. `slides.qmd` holds only the front matter and the includes:

```markdown
{{< include sections/_1-jim-open.qmd >}}
{{< include sections/_2-jessica.qmd >}}
{{< include sections/_3-jacob.qmd >}}
{{< include sections/_4-jim-close.qmd >}}
```

The leading underscore stops Quarto rendering a section as a page of its own. At the start of each section, put a divider slide with the speaker's name, so the room and Zoom know who is speaking. Speaker notes stay with each speaker's slides. Each speaker's minute ranges start at 0 for their own section.

## Stack

- **Quarto + reveal.js.** The deck is `slides.qmd`, rendered to `docs/slides.html`. Speaker notes go in `::: notes` blocks in the same file.
- **Slide size** 1280 × 720, `margin: 0.08`, `transition: fade`, slide numbers on, footer showing the public URL.
- **Animations** are plain HTML/CSS/SVG driven by a small script (`slides-motion.html`). There are no animation libraries and no video for explainers. See *Animation system* below.
- **Optional companion site.** For a workshop, `index.qmd` and step pages render into the same `docs/` as a Quarto website. For a plain talk, a single `slides.qmd` and a short `index.qmd` are enough.
- **Hosting.** GitHub Pages serves `main` / `docs/`. `quarto render` deletes `docs/.nojekyll`, so recreate it every time.

Front matter to start from:

```yaml
---
title: "TBD"
subtitle: "TBD"
author: "Jim Clifford, University of Saskatchewan"
date: "TBD"
date-format: "D MMMM YYYY"
format:
  revealjs:
    theme: [default, slides.scss]
    slide-number: true
    footer: "TBD public URL"
    width: 1280
    height: 720
    margin: 0.08
    link-external-newwindow: true
    transition: fade
    background-transition: fade
    include-after-body: [workshop-responsive.html, slides-title-qr.html, slides-motion.html]
---
```

## Layout

| Path | What it is |
|---|---|
| `slides.qmd` | Front matter and includes only |
| `sections/_*.qmd` | One file per speaker section, with speaker notes |
| `outline.md` | Working slide plan; update it when the sections change |
| `slides.scss` | Theme and component classes, copied from the JHU deck; cut what isn't used |
| `slides-motion.html` | The animation driver (below) |
| `slides-title-qr.html` | QR code to the public URL on the title slide, clickable. *Not added yet: copy [the JHU version](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides-title-qr.html) once the Pages URL is settled, then add it to `include-after-body`.* |
| `workshop.js`, `workshop-responsive.html` | Touch-screen reading view: phones and tablets up to 1024 px get a scrolling page instead of tiny slides; `?present` forces slides |
| `_quarto.yml`, `index.qmd` | Plain Quarto project rendering `index.qmd` and `slides.qmd` to `docs/`. The reveal.js libraries land in `docs/slides_files/`, which must be committed (`.gitignore` ignores only the root `/*_files/`) |
| `images/`, `media/` | Screenshots, scans, maps (`world-land.svg` for SVG maps), video fallbacks |
| `scripts/check_*.py` | Playwright checks: layout, overflow, reading view. *Not added yet: adapt the JHU scripts once there is real content.* |
| `scripts/export_slides.py` | PowerPoint (animated slides embedded as MP4) and a speaker-notes PDF. *Not added yet.* |
| `exports/` | Export output; git-ignored |
| `docs/` | Rendered site; committed for Pages |

`.gitignore`: `/.quarto/`, `/_site/`, `*_files/`, `__pycache__/`, `.claude/`, `/exports/`.

## Look

Dark theme, matched to the project's own visualisations. Keep these values:

| Role | Colour |
|---|---|
| Background | `#15161a`; panels `#1d1e23`; rules `#3a3b40` |
| Body text | `#e9e4d8`; headings `#f3ead3` in Georgia |
| Accent (key term, highlight) | gold `#c9a227` |
| Secondary | blue `#7fa7d6`; links `#9cc0ea` |
| Before / error | `#c0674f` (`#e08a74` for text) |
| After / fixed | `#79a868` (`#9fcf8c` for text) |
| Muted | `#9a958a` |

Root font size 34px. Headings and source quotations are set in a serif; UI labels in a system sans.

Reusable components, all defined in this repo's `slides.scss` (copied from the JHU deck):

- `.flow` > `.node` + `.arrow`: a pipeline drawn as boxes and arrows. `.node.blue`, `.before`, `.after` and `.wide` are variants; `.loopback` draws the return path.
- `.def` with `.def-term`: **"What is X?" definition boxes.** Gloss every technical term where it first appears. `.defs` sets two of them side by side.
- `.cards` > `.card`: parallel options (with `.kicker`, `h4`, `.fact`).
- `.stats` > `.stat` (`.num`, `.lbl`): headline numbers.
- `blockquote` for printed source text, `.source-meta` for provenance, and `.caption` under images.
- Inline highlights: `.gold`, `.blue`, `.muted`, `.small`, `mark`.

## Animation system

Put `.motion` on a slide. Inside a raw HTML block, give each element `data-at="ms"`. The script adds `.on` to that element that many milliseconds after the slide opens, and the CSS animates the change.

```markdown
## Title {#slide-id .motion}

```{=html}
<div class="motion-card rise" data-at="400">…</div>
<span class="mk" data-at="1200">highlighted phrase</span>
<svg class="motion-map" viewBox="…"><path class="draw" pathLength="1" data-at="2000" d="…"/></svg>
<p class="motion-caption rise" data-at="6000">One-line takeaway.</p>
```
```

Effect classes:

| Class | `.on` does |
|---|---|
| (none) | fades in |
| `.rise` | fades in and rises 14px |
| `.mk` | highlights text in place (gold background); `.mk.co` blue; `.mk.target` underline; `.mk.diff` red outline for a disagreement |
| `.draw` (SVG `path`, `pathLength="1"`) | draws the line |
| `.exit` | fades out |
| `.strike` / `.win` | strikes out a rejected row / marks the chosen row green |

Behaviour, all handled by `slides-motion.html` (copy it verbatim):

- Every motion slide gets a **↻ Replay** button.
- **Reduced motion** (for example, Windows with animations off) shows the final frame, and the button reads **▶ Play animation**. Opening the deck with `?motion` autoplays anyway, so link the deck as `slides.html?motion` from the site and presenter notes.
- **Print/PDF and the phone reading view** show the final frame. Every animated slide must therefore read correctly as a static slide.

Core CSS (the full set is in this repo's `slides.scss`):

```scss
.reveal section.motion [data-at] { opacity: 0; transition: opacity .6s ease, transform .6s ease; }
.reveal section.motion .rise[data-at] { transform: translateY(14px); }
.reveal section.motion [data-at].on { opacity: 1; transform: none; }
.reveal section.motion .mk[data-at] { opacity: 1; border-radius: 3px; padding: 0 .1em; transition: background-color .5s, color .5s; }
.reveal section.motion .mk[data-at].on { background: #c9a227; color: #15161a; }
.reveal section.motion path.draw[data-at] { opacity: 1; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset 1.5s ease-in-out; }
.reveal section.motion path.draw[data-at].on { stroke-dashoffset: 0; }
.reveal section.motion.motion-reset [data-at] { transition: none !important; }
```

### When to animate

Use motion when the slide shows a **sequence, a change of state, or a flow**: a printed clause becoming a record, a record landing on a map, an error and its fix, a pipeline stage passing work along. Don't animate a list just to have something move. Patterns from the [JHU deck](https://jimclifford.ca/imperial-careers-workshop/slides.html?motion) worth reusing:

- **Source → structure → map.** Raw OCR text on the left; phrases highlight (`.mk`) in step with points and arcs appearing on an SVG map on the right (*Two Lists, one career, mapped*).
- **Rules vs reality.** Rows of input → output → verdict appear one at a time, then a score strip (*Real rules: mostly right, quietly wrong*).
- **Before → fix.** A wrong value in the before colour, the evidence, then the corrected value in the after colour, with a log line (*Balmer's ditto*, *Which Victoria?*).
- **Candidate filter.** A list of candidates; rejected rows `.strike`, the chosen row `.win` (*QLever*).

Timing: about 8–15 seconds per slide; first element at 300–800 ms; steps 500–1,200 ms apart; a `.motion-caption` takeaway last. The final frame should hold while you talk.

## Writing the slides

- **Audience first.** Gloss jargon where it first appears (a `.def` box), and keep a glossary if there's a companion site.
- **Fill the slide with substance.** Use a diagram, a real source excerpt or a worked example, not three lines of big text. Equally, one idea per slide; move detail to speaker notes or supporting pages.
- **Real material only.** Use real scans, real OCR and real pipeline output. Cite the file or record ID in the notes. Never invent a number, date, name or identifier; every figure must trace to a file.
- **Honest rates.** Say how a sample was selected, and never present a hand-picked set as a rate. Give measured cost and throughput (where it ran, how long it took, what it cost).
- **Errors are shown as completed corrections.** Show the found error, the source check, the fix, the rebuilt result and the check across affected records. Label old screenshots as *before*.
- **Speaker notes on every slide.** Start with the minute range (`4–5.`), then what to say, where each number comes from, and one question for the room if there is one.
- **Interaction.** Use QR codes and clickable URLs for anything the audience opens. Keep at most one network-dependent demo, with a saved fallback.
- **Video.** For a background video slide, use `<video data-autoplay controls muted playsinline poster=…>` with an MP4 and a WebM fallback and a direct link. Don't also set the poster as a reveal background image.

## Build, check, export

```bash
quarto render
touch docs/.nojekyll
python3 scripts/check_workshop_responsive.py   # phone/tablet/desktop, overflow, reading view
python3 scripts/check_workshop_browser.py      # presentation layout
python3 scripts/export_slides.py               # exports/*.pptx and *-notes.pdf
```

Copy the check and export scripts from the JHU repository's [`scripts/`](https://github.com/jburnford/imperial-careers-workshop/tree/main/scripts) and update their paths, file names and slide IDs. They need `playwright`, `python-pptx`, `lxml` and `ffmpeg`. Ask Jim to install any missing packages himself (`python3 -m pip install --break-system-packages …`).

**Before saying a slide is done:** render it and take Playwright screenshots at 1280 × 720 of each changed slide, including the final frame of any motion slide. Look at them for overflow, overlap and readability from the back of a room. Then commit.

## Working on this deck

- Three people push to this repository. Pull before you start. Touch only the section you were asked to work on; the shared files (`slides.scss`, `slides-motion.html`, front matter) need a heads-up to the others.
- Use the speakers' own words and facts. Where the notes are thin, leave a visible `[TBD: …]` on the slide rather than inventing a detail.
- Propose the cut-down version first. When things sprawl, go back to the core argument: better, not more.
- Commit in small steps, with messages that say what changed for the audience (e.g. "Open with the printed page"). Each speaker reviews their own rendered section; Jim reviews the whole deck before anything is published.
- Push only when asked.
