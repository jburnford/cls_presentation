# CLS presentation: how this deck is built

This repository holds a slide presentation built the same way as the Johns Hopkins workshop deck (*Cleaning, Structuring and Grounding Historical Data*, 15 October 2026). That deck is the reference implementation:

- Source: <https://github.com/jburnford/imperial-careers-workshop>
- Live deck: <https://jimclifford.ca/imperial-careers-workshop/slides.html?motion>

When a pattern below is unclear, open the matching file in that repository and copy it: [`slides.qmd`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides.qmd), [`slides.scss`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides.scss), [`slides-motion.html`](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides-motion.html), [`workshop.js`](https://github.com/jburnford/imperial-careers-workshop/blob/main/workshop.js), [`scripts/`](https://github.com/jburnford/imperial-careers-workshop/tree/main/scripts). Don't invent a new system.

## The talk

From `CLS Presentation Rough Notes.docx`. The slide-by-slide plan is in [outline.md](outline.md).

| | |
|---|---|
| Title | *Do Better, Not More: Historians Working With LLMs* (decided 13 November 2026; comma added 14 November 2026). On the title slide, "Historians Working With LLMs" is the subtitle. |
| Venue, date, time | Canadian Light Source (CLS), Saskatoon. **In person.** Date and room TBD |
| Length | about 35–45 minutes, plus questions |
| Speakers, in order | Jim opens (5 min) → Jessica, general (10–15 min, 10–15 slides) → Jacob, specific and technical (10–15 min, 10–15 slides) → Jim closes (10 min) |
| Audience | **Mostly STEM scientists.** See *Writing for this audience* below |
| Core argument | Coding agents flatten the skills barrier and make iteration fast, so computational history may finally grow as computational physics did. The question is how to use that to do *better* history, not just *more*. |
| Material | The speakers' own projects: Jessica's interactive visualizations, Jacob's knowledge graph and GraphRAG work, Jim's projects and editorial experience |
| Public URL | TBD (GitHub Pages from `docs/`) |

### Writing for this audience

Confirmed by Jacob, 13 November 2026. Every section should be built for this room.

- **They are scientists.** Don't define what they already know (vectors, cosine similarity, databases, statistics); gloss the history and the humanities methods instead. They will trust measured results with a stated method and sample far more than claims, so lead with evidence.
- **Connect to their work.** Use examples a facility like CLS recognizes: technical documentation, beamline manuals and logbooks, their own published papers. Historical sources are the worked examples, not the frame.
- **Predictable structure.** Each section opens by saying what it covers, and the same signposting appears throughout, so nobody has to guess where they are.
- **Literal headings.** A heading states the slide's point in plain words. No idioms, puns or metaphors to decode.
- **One idea per slide, low text density.** Detail goes in the speaker notes.
- **Calm motion.** Short fades and draws only; nothing flashing, fast or looping. Every animated slide still reads as a static slide (already required below).
- **Consistent colour meaning.** The error colour always means an error or failure, the fixed colour always means checked or fixed (values under *Look*). Never use them decoratively. Colour never carries meaning on its own: a word, an icon or a strike-through always says it too.
- **Let people follow at their own pace.** A QR code to the deck early on (see `slides-title-qr.html`).

### Three speakers, one deck

**Who builds what.** Jim's agents build sections 1 and 4 (`_1-jim-open.qmd`, `_4-jim-close.qmd`). Jessica's and Jacob's agents build sections 2 and 3. Don't edit another speaker's section. If you change a shared file (`slides.qmd`, `slides.scss`, `slides-motion.html`, `CLAUDE.md`), do it in its own commit with a message that says what changed, because the other speakers' agents build on it.

Each speaker edits their own section file, which keeps merge conflicts down. `slides.qmd` holds only the front matter and the includes:

```markdown
{{< include sections/_1-jim-open.qmd >}}
{{< include sections/_2-jessica.qmd >}}
{{< include sections/_3-jacob.qmd >}}
{{< include sections/_4-jim-close.qmd >}}
```

The leading underscore stops Quarto rendering a section as a page of its own. At the start of each section, put a section divider (see *Slide types* under *Look*): its title is the section's subject, with the speaker's name as a small line underneath, so the room knows who is speaking. Speaker notes stay with each speaker's slides. Each speaker's minute ranges start at 0 for their own section.

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
| `slides.scss` | Theme and component classes (see *Look*) |
| `fonts/` | Self-hosted Atkinson Hyperlegible Next and Mono files (SIL Open Font License), so the deck never depends on Google Fonts or the venue's internet |
| `slides-motion.html` | The animation driver (below) |
| `slides-title-qr.html` | QR code to the public URL on the title slide, clickable. *Not added yet: copy [the JHU version](https://github.com/jburnford/imperial-careers-workshop/blob/main/slides-title-qr.html) once the Pages URL is settled, then add it to `include-after-body`.* |
| `workshop.js`, `workshop-responsive.html` | Touch-screen reading view: phones and tablets up to 1024 px get a scrolling page instead of tiny slides; `?present` forces slides |
| `_quarto.yml`, `index.qmd` | Plain Quarto project rendering `index.qmd` and `slides.qmd` to `docs/`. The reveal.js libraries land in `docs/slides_files/`, which must be committed (`.gitignore` ignores only the root `/*_files/`) |
| `images/`, `media/` | Screenshots, scans, maps (`world-land.svg` for SVG maps), video fallbacks |
| `scripts/check_*.py` | Playwright checks: layout, overflow, reading view. *Not added yet: adapt the JHU scripts once there is real content.* |
| `scripts/export_slides.py` | PowerPoint (animated slides embedded as MP4) and a speaker-notes PDF. *Not added yet.* |
| `exports/` | Export output; git-ignored |
| `docs/` | Rendered site; committed for Pages |
| `style-guide/` | The visual style guide: the *Look* and *Writing the slides* sections with example slides. Jessica keeps it in step with this file; if the two disagree, this file wins |

`.gitignore`: `/.quarto/`, `/_site/`, `*_files/`, `__pycache__/`, `.claude/`, `/exports/`.

## Look

The look was designed by Jessica in November 2026 for this audience: light, calm and uncluttered. It replaces the JHU deck's look, so don't copy that deck's colours, fonts or boxed components. There are two versions: **light** (the default) and **dark** (for a darkened room). Only the colours differ; type, sizes, spacing, positions and lines are the same in both. Open the deck with `?dark` for the dark version, the same way `?motion` turns on autoplay.

**See it before you build.** `style-guide/index.html` shows everything in this section as example slides, including every slide type below. Open it in Chrome. **Agents:** the first time you build or change slides under this guide, tell your speaker that the deck's look changed in November 2026, and suggest they open that page before reviewing their slides.

### Principles

1. **Less clutter, more room.** One idea per slide; detail goes in the speaker notes. Minimal is not bare: keep the claim, the figure and the concrete examples; cut repetition and decoration, not explanation.
2. **Generous space** between elements.
3. **Visual character comes from railway-style lines**, not boxes, cards or panels.
4. **A light, neat background.**
5. **Sans-serif type throughout**, including headings and quotations (serif type is harder for many dyslexic readers).
6. **On a visual slide, the visual gets most of the space.** A recorded clip plays in full, app interface included; crop only static images.

### Colour

| Role | Light | Dark |
|---|---|---|
| Background | `#FDFCF9` warm off-white | `#1C1B19` warm charcoal |
| Titles | `#22272B` | `#E8DFCB` cream |
| Body text | `#404040` | `#C4C3C0` |
| Section labels, captions, number labels, slide numbers, bullets | `#5C6166` | `#9A9790` |
| Emphasis: list headers, key phrases, big numbers | `#1F5F96` | `#6699D3` |
| Error / before | `#B03A1E` | `#DC7559` |
| Fixed / after | `#1B7360` | `#4FAA90` |
| Lines (never text) | yellow `#E3B505`, light blue `#7FA7D6` | gold `#9A7424`, blue `#4D719B` |
| Placeholder or empty visual area | `#EEEBE3` | `#2B2A27` |
| Chart bars (all but the one the slide is about) | `#8C8880` | `#77746D` |
| Chart baseline | `#B7B3AA` | `#5E5B55` |
| Highlight on animated slides, main | `#F6E39A` pale yellow; text keeps its colour | `#6C5119` gold; highlighted text turns cream `#E8DFCB` |
| Highlight on animated slides, second | `#D9E5F3` pale blue | `#2C4058` blue |

Rules:

- **Colour never carries meaning on its own.** Meaning comes from words and shapes: a label, a ✗ or ✓ icon, a strike-through, the words *Before* and *After*. Colour reinforces them. A wrong value gets the error colour **and** a ✗ or strike-through; a corrected one gets the fixed colour **and** a ✓ or *After*.
- **Line colours are never used for text or numbers.** They are too faint to read. Lines are decoration only: a route-map stop always has a text label. The line colours also draw routes and arrows, and pale tints of them make the highlights on animated slides.
- **Emphasis is always bold or large as well as blue.** Never use the emphasis colour alone inside a sentence.
- **The most important text has the strongest contrast:** titles first, then body text, then labels and captions.
- **No pure white text in the dark version** (it blurs for some readers).
- All text colours pass 4.5 : 1 against their background, and the error and fixed colours stay distinct for red-green colour blindness. Check any new colour against both before adding it.

### Type

- **Atkinson Hyperlegible Next**, regular (400) and bold (700) only; no semibold or light weights. It was designed for low-vision readers and keeps confusable characters (I l 1, O 0) distinct.
- **Atkinson Hyperlegible Mono** only for raw machine text: OCR output, data records, pipeline output.
- Both are self-hosted in `fonts/`.
- **No italics anywhere.** Emphasis is bold only. Titles of works go in the source line as plain text.
- Left-aligned, ragged right; body line height 1.4. The one exception is the number column on a big-numbers slide (see *Slide types*).

One fixed set of sizes for every slide (px at 1280 × 720). Nothing the audience reads is smaller than 22px.

| Role | Size | Weight |
|---|---|---|
| Title | 54 | bold |
| Big number; the title on the title and closing slides; the sentence on a statement slide | 64 | bold (a quoted statement regular) |
| Body text, list items, list headers | 30 | regular; list headers bold |
| Raw machine text (Mono) | 26 | regular |
| Secondary: captions, number labels, source lines, the speaker line on a divider | 24 | regular |
| Section label (above the title) | 22 | bold, uppercase, letter-spaced 0.12em; one or two words |
| Slide number | 20 | regular |

**Quotations from printed sources:** body text in quotation marks, indented beside a 3px vertical line in the light-blue line colour, with the source line (title, year, page) below it in secondary text. **Raw machine text** uses the same lined indent in Mono, with its file or record ID as the source line. No large decorative quotation marks.

### Lines

Three variants, each 3px, running the full width of the slide:

- **Full track:** dash-dot / solid / dash-dot, 10px apart.
- **Half track:** dash-dot + solid, 10px apart.
- **Single line:** solid.

The dash-dot pattern is `stroke-dasharray: 22 9 3 9`. Which line goes where is set by the slide type (below), not chosen per slide, so the deck stays predictable. Lines are not a hierarchy and carry no meaning.

- When a slide has two half tracks, the bottom one is the mirror image of the top one.
- Never place two tracks close together, and never put a track behind or between lines of text. (Dense stripes can cause visual discomfort.)
- The bottom track appears only on sparse text slides and on the title and closing slides, never on visual slides.

**Arrows.** The deck has one arrow for "this came next". It has a solid 3px shaft in the light-blue line colour with an open arrowhead (14px deep, 9px either side). A dash-dot line runs 10px above and below the shaft, one dash and one dot long, ending 12px clear of the arrowhead, like a short piece of full track. Use it between visuals in a sequence, between the steps of an error-and-fix slide, and between a source and its record. The return line of a cycle keeps a plain open arrowhead.

### Spacing and position

Measure every gap from the visible letters (top of the capitals to the baseline), not from text boxes. In CSS, `text-box: trim-both cap alphabetic` makes boxes hug the letters. It works in Chrome and Safari, not Firefox, so **present from Chrome**.

| Gap | Size | Use |
|---|---|---|
| Extra small | 12px | Text attached to a mark: a route-map stop label above its circle, a word beside its icon |
| Small | 24px | Things that belong together: label and title, list header and its items, one list item and the next, a number and its label, a quotation and its source line, a lead-in and what it introduces |
| Medium | 48px | Separate groups: two list columns, a visual and its side column, two numbers in a side column, the title and the visual on a visual slide, a divider's title and its speaker line |
| Large | 96px | Title to content on a text slide |

- **Things that belong together sit closer than things that don't.** A label sits right next to what it labels.
- **No floating text.** Every piece of text is visibly tied to what it relates to, by its wording (a lead-in ends with a colon), its position or its size. If it can't be tied to anything, cut it.
- **Fixed header position.** On every slide except the title and closing slides (and full-screen visuals A and B), the section label and title sit in the same place, so nothing jumps between slides: 128px from the left edge, label top at 92px, title 24px below it, top line or track at 36px.

### Slide types

Every slide uses one of these types. The type sets the lines, header and layout, so the deck stays predictable. If a planned slide holds two or three ideas, split it instead of stretching a type to fit.

**Opening and closing**

- **Title slide.**
  - Full track in yellow at the top and full track in light blue at the bottom, each a large gap from the content (about 78px from the slide's edges). The content is centred between them.
  - Left, in a 704px column: *Canadian Light Source · date* in the section-label style; a small gap below, the title on one line at 64px bold; a small gap below, the subtitle in body text.
  - A medium gap below the subtitle, the speakers stacked one per line in secondary text: *Dr. Jim Clifford*, *Jacob Polay, PhD Student*, *Jessica Jack, PhD Student*. A small gap below them, *University of Saskatchewan* in the section-label style.
  - Right: the QR code to the deck, 240px, its top level with the label, with *Follow along:* a small gap above it and the short address a small gap below. In the dark version the code keeps a light square behind it, because some phone cameras can't read a light-on-dark code.
- **Talk overview.** Comes right after the title slide.
  - Visual-slide lines and header.
  - The four sections are stations on a light-blue line across the slide, like a divider's route. *Section 1* to *Section 4* sit in the section-label style an extra-small gap above the stations. Below each station, a small gap down, the section's subject in bold blue at body size, then the speaker in secondary text a small gap below that.
  - Subjects get about 220px each. If one needs two lines, set the break by hand where a reader would pause; never leave it to automatic wrapping. Two lines at most.
- **Section divider.** Marks a new section.
  - Full track in yellow at the top, in the top line's usual place.
  - Label *Section N of 4* and the title in the fixed header position. The title is the section's subject (not the speaker's name).
  - The speaker's name and role in secondary text, a medium gap below the title.
  - Near the bottom, the section's route: *In this section:*, then the section's labels (for example *Starting point · Method · Results · Checking*) as stops on a single light-blue line, each label an extra-small gap above its circle. Use the same labels above the titles in that section.
- **Closing slide.** On screen through the questions, as a bookend to the title slide.
  - The title slide's tracks and QR code, in exactly the same places.
  - *Questions* at 64px bold. A medium gap below, one row per speaker in the title slide's order: the name in bold blue at 24px in a 220px left column, and a medium gap to its right, their project links (24px, body colour, underlined), stacked a small gap apart. Speakers sit a medium gap apart.
  - Links are bare titles with no type tags. They can be clicked in the deck; the QR code is how people in the room reach them.

**Text**

- **Text slide.**
  - Half track in yellow at the top, with the mirrored light-blue half track at about 628px.
  - Label and title in the fixed position, then content a large gap below.
  - Two lists sit in 452px columns with a medium gap between them. Each has a bold blue header the same size as its items, and bullet markers.
- **Statement.** One sentence on its own slide: a claim, a quotation or a question for the room.
  - Text-slide lines. The section label stays in its fixed place; there is no title.
  - The sentence at 64px bold in the title colour, left-aligned at 128px and centred vertically between the tracks. About three short lines at most, broken by hand where a reader would pause.
  - A quotation keeps the lined indent and source line, at 64px regular, since they are someone else's words.
- **Definition.** Explains a term where it first comes up.
  - Text-slide lines and header.
  - Dictionary layout: the term in bold blue at body size in a 260px left column. A medium gap to its right, the definition in body text (one or two plain sentences), and a small gap below that, *For example:* and one short concrete case in secondary text.
  - Two terms stack as two rows a medium gap apart.
  - Keep the term in its own column; don't stack it above the definition. Its own position is what shows the reader it is the thing being defined.
- **Big numbers.** Two to four headline figures, without a visual.
  - Text-slide lines and header.
  - The numbers (64px bold, emphasis blue) stack in a 330px left column, right-aligned, each with its label in body text a small gap to its right, so each row reads as a sentence (*12,345 documents in the collection*). Rows sit a medium gap apart.
  - The right-aligned number column is the one exception to left-aligned text.
- **Comparison.** Two to four things side by side.
  - The text slide's two lists: each item a bold blue header with bullets beneath, in 452px columns a medium gap apart. Four items make a two-by-two grid, each a header with one line of secondary text.
  - A choice between two paths (the *more* or *better* fork) may instead use a fork, with visual-slide lines and header: a light-blue line enters from the left and splits, one branch to each option, each ending at a station with the option's header and bullets an extra-small gap to its right.
  - Returning to a comparison later in the talk: the same layout, with the side no longer argued for set in secondary grey (header too) and the other side given its new points. The section label changes.
- **Error and fix.** Same lines and header as a text slide.
  - Three steps from left to right, joined by arrows (see *Arrows*):
    1. ✗ *Before*: the wrong value, struck through, in the error colour.
    2. *Checked*: what it was checked against.
    3. ✓ *After*: the corrected value in the fixed colour.
  - Each step has a one-line caption in secondary text.

**Visuals**

- **Visual slide.**
  - Single yellow line at the top; no bottom track.
  - Label and title in the fixed position.
  - The visual sits a medium gap below the title, 800 × 450 at 128px from the left. Show a recorded clip in full.
  - An optional side column sits a medium gap to the right, for a claim, a big number and its label, or short examples.
- **Two or three visuals side by side.** A before and after, a series of attempts, or two or three views of one thing.
  - Visual-slide lines and header. The visuals sit a medium gap below the title, filling 1024px, about 340px tall, with 84px between them when there are arrows and a medium gap when there aren't.
  - Each visual has a label a small gap above it and a one-line caption a small gap below. A failure gets a ✗ and the error colour; a fix or success gets a ✓ and the fixed colour; a neutral view is bold blue with no icon.
  - When the visuals are a sequence, an arrow sits in each gap. Views that aren't a sequence have no arrows.
- **Chart.** For bar charts.
  - Visual-slide lines and header. The chart fills the 800 × 450 visual area, and the side column holds the claim as a big number and its label.
  - Horizontal bars, sorted, 28px thick, with a 4px rounded tip and a square end at the baseline. Each bar's name (24px, body colour) is right-aligned 12px left of a 2px baseline, and its value (24px, secondary) sits 12px past the tip. No axis ticks or gridlines.
  - Ordinary bars are the chart grey. The bar the slide is about is emphasis blue **and** has its name and value in bold.
  - A worse bar is the error colour, with a ✗, its value and the word *worse* in bold error colour, and its name in bold.
- **Source beside its record.**
  - Visual-slide lines and header.
  - Left, about 460px wide: the source, as OCR text in Mono with the lined indent and its file ID as the source line, or as a scan with its file ID below.
  - An arrow in an 84px gap.
  - Right: the record exactly as the pipeline wrote it, in Mono with the same lined indent and its record ID.
  - On an animated slide, each phrase and the field made from it highlight together (see *Animation system*).
- **Full-screen visual.** For a visual that needs every pixel, such as a recorded demo. This is the only type where the slide's owner chooses the layout, because the kind of demo may decide it:
  - **A. Edge to edge:** 1280 × 720, with no lines, label, title or slide number. The largest; the slide before it, or the speaker, has to say what it shows.
  - **B. Section label only:** the yellow line and the label in place, no title; the clip 988 × 556 a small gap below the label.
  - **C. Usual header:** the visual-slide header with no side column; the clip 832 × 468.
  - Always show the clip whole at 16 : 9, never cropped. Record it at 1280 × 720 with the app or browser zoomed in so its text is large; that matters more for legibility than the slide size.
- **Process.** A sequence of stages.
  - Visual-slide lines and header.
  - The stages are stations on a light-blue line across the slide. Each stage name (bold blue, body size) sits a small gap above its station, and a short description (secondary) a small gap below.
  - At most about five short stages; more means splitting the slide.
  - **Cycle:** after the last station the line turns down, runs back under the stations and up into the first station, ending in an open arrowhead, with *Repeat* in secondary text on the return line. Descriptions sit to the right of each station, clear of the return line. The main line still runs full width past the last station, because a cycle sits inside a larger research process.
  - **Timeline:** a date in place of each stage name, with the stations evenly spaced, so the spacing implies no time scale.

### Replacing the JHU deck's boxed components

| JHU component | Use instead |
|---|---|
| `.flow` pipeline | Process |
| `.def` definition box | Definition |
| `.cards` | Comparison |
| `.stats` | Big numbers |

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
| `.mk` | highlights text in place with the main highlight (pale yellow); `.mk.co` uses the second highlight (pale blue), for a second thing traced at the same time |
| `.mk.target` | outlines the word being looked up, in emphasis blue |
| `.mk.diff` | outlines a value that disagrees, in the error colour. Add a ✗ and words saying what disagrees |
| `.draw` (SVG `path`, `pathLength="1"`) | draws the line |
| `.exit` | fades out |
| `.strike` | a rejected row turns the error colour and is struck through. Give it a ✗ and the reason beside it in secondary text |
| `.win` | the chosen row turns the fixed colour and bold. Give it a ✓ |

All effects fade over about half a second. Colour never works alone here either: the ✗, ✓, strike-through, outline and words carry the meaning.

Behaviour, all handled by `slides-motion.html` (copy it verbatim):

- Every motion slide gets a **↻ Replay** button.
- **Reduced motion** (for example, Windows with animations off) shows the final frame, and the button reads **▶ Play animation**. Opening the deck with `?motion` autoplays anyway, so link the deck as `slides.html?motion` from the site and presenter notes.
- **Print/PDF and the phone reading view** show the final frame. Every animated slide must therefore read correctly as a static slide.

Core CSS (the full set is in this repo's `slides.scss`):

```scss
.reveal section.motion [data-at] { opacity: 0; transition: opacity .6s ease, transform .6s ease; }
.reveal section.motion .rise[data-at] { transform: translateY(14px); }
.reveal section.motion [data-at].on { opacity: 1; transform: none; }
// Colours as variables; ?dark adds the .dark class, which swaps them.
:root { --hl-main: #F6E39A; --hl-main-text: currentColor; --hl-second: #D9E5F3; --emphasis: #1F5F96; --error: #B03A1E; --fixed: #1B7360; }
.dark { --hl-main: #6C5119; --hl-main-text: #E8DFCB; --hl-second: #2C4058; --emphasis: #6699D3; --error: #DC7559; --fixed: #4FAA90; }

// text-box: normal so a highlight or outline isn't clipped to the capital height.
.reveal section.motion .mk[data-at] { opacity: 1; text-box: normal; border-radius: 3px; padding: 0 .1em; transition: background-color .5s, color .5s, outline-color .5s; }
.reveal section.motion .mk[data-at].on { background: var(--hl-main); color: var(--hl-main-text); }
.reveal section.motion .mk.co[data-at].on { background: var(--hl-second); color: inherit; }
.reveal section.motion .mk.target[data-at], .reveal section.motion .mk.diff[data-at] { margin: 0 .3em; padding: 0 .12em; border-radius: 4px; outline: 3px solid transparent; outline-offset: 4px; }
.reveal section.motion .mk.target[data-at].on { background: none; color: inherit; outline-color: var(--emphasis); }
.reveal section.motion .mk.diff[data-at].on { background: none; color: inherit; outline-color: var(--error); }
.reveal section.motion .strike[data-at].on { opacity: 1; color: var(--error); text-decoration: line-through 3px var(--error); }
.reveal section.motion .win[data-at].on { opacity: 1; color: var(--fixed); font-weight: 700; }
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

- **Audience first.** Gloss jargon where it first appears (a definition slide, under *Slide types*), and keep a glossary if there's a companion site.
- **Titles name the subject, plainly and briefly.** Someone who reads only the title should know what the slide is about. Keep titles short, and never repeat the slide's body. No metaphors, idioms or *from X to Y* phrasing.
- **Lists look like lists.** List items get bullet markers; never rely on colour and weight alone to separate items from their header.
- **Break lines where a reader would pause.** End a line at a phrase boundary, start the next line with connecting words (*then*, *and*), and never leave one word stranded on its own line.
- **Every detail on the slide serves the point.** Provenance such as a count date goes in the speaker notes unless the date matters to the argument.
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
