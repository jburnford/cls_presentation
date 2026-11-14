# Writing each slide type

How to write every slide type from the *Look* section of [`CLAUDE.md`](../CLAUDE.md) in Quarto Markdown. The theme (`slides.scss`) draws the lines, puts the label and title in the fixed position, and sets every size, colour and gap, so a slide only names its type and gives its content. Don't add inline styles, colours or spacing.

[`demo.html`](demo.html) shows one of each, built from exactly this markup. Open it in Chrome; add `?dark` to the address for the dark version.

## Every slide

```markdown
## Plain title {#jim-example .text label="Method"}
```

- **The type** is a class on the heading: `.text`, `.visual` and so on (list below). It sets the lines and layout. Every slide has one.
- **The section label** is `label="…"`: one or two words, the same labels as the section's divider route.
- **No title** (statement, full-screen A and B, opening, closing): leave the heading empty, `## {#id .statement label="Checking"}`.
- **IDs** start with the speaker's name: `#jim-…`, `#jessica-…`, `#jacob-…`.
- **Speaker notes** stay in `::: notes` blocks, as before.
- **Hand line breaks:** end a line with `\` where a reader would pause.
- **Secondary text** (captions, source lines, examples): `[text]{.second}` as its own paragraph.
- **Icons:** `[]{.icon-x}` and `[]{.icon-ok}` draw ✗ and ✓ (the font has no such characters). Put them at the start of the word they belong to: `[]{.icon-x}Before`.
- **Arrow** ("this came next"): `[]{.arrow}` as its own paragraph, with blank lines around it.
- **Videos and other raw HTML** go in a ```` ```{=html} ```` block. A bare `<video>` tag in Markdown breaks every slide after it.

| Type | Class | Lines |
|---|---|---|
| Title slide | `.opening` | full tracks, top and bottom |
| Talk overview | `.overview` | single line |
| Section divider | `.divider` | full track, top |
| Text slide | `.text` | half tracks, top and bottom |
| Statement | `.statement` | half tracks |
| Definition | `.definition` | half tracks |
| Big numbers | `.big-numbers` | half tracks |
| Comparison | `.comparison` (columns) or `.fork` | half tracks / single line |
| Error and fix | `.error-fix` | half tracks |
| Visual slide | `.visual` | single line |
| Two or three visuals side by side | `.side-by-side` | single line |
| Chart | `.chart` | single line |
| Source beside its record | `.source-record` | single line |
| Full-screen visual | `.full-a`, `.full-b`, `.full-c` | none / single line |
| Process, cycle, timeline | `.process`, `.cycle`, `.timeline` | single line |
| Closing slide | `.closing` | full tracks, top and bottom |

## Opening and closing

### Title slide

```markdown
## {#jim-title .opening}

::: {.title-block}
[Canadian Light Source · [TBD: date]]{.label}

Do Better, Not More

Historians Working With LLMs
:::

::: {.people}
Dr. Jim Clifford

Jacob Polay, PhD Student

Jessica Jack, PhD Student

[University of Saskatchewan]{.label}
:::

::: {.qr}
Follow along:

::: {.code}
(the QR code as an inline SVG, 240 × 240)
:::

[short deck address]
:::
```

Quarto also makes a title slide of its own from the `title` in `slides.qmd`'s front matter, in a plain layout. To use the `.opening` slide instead, front matter needs `pagetitle:` in place of `title:`/`subtitle:`/`author:`. That is a shared-file change, so agree it with the others first.

### Talk overview

```markdown
## The talk in four sections {#jim-overview .overview label="Overview"}

::: {.route}
::: {.stop}
Section 1

Section subject

Speaker
:::
::: {.stop}
Section 2

Longer subject\
on two lines

Speaker
:::
(…Section 3 and Section 4 the same way)
:::
```

In each `.stop`, the first paragraph sits above the station and the rest below it. Subjects get about 220px: break a long one by hand, two lines at most.

### Section divider

```markdown
## Section subject {#jim-divider .divider label="Section 1 of 4"}

Jim Clifford, University of Saskatchewan

::: {.route}
In this section:

::: {.stop}
Starting point
:::
::: {.stop}
Method
:::
(…one stop per label)
:::
```

### Closing slide

```markdown
## {#jim-closing .closing}

[Questions]{.big}

::: {.contacts}
Jim Clifford

::: {}
[Imperial Careers atlas](https://…)

[Working Papers in Critical Search](https://…)
:::

Jacob Polay

::: {}
[Project title](https://…)
:::
:::

::: {.qr}
(same as the title slide)
:::
```

## Text

### Text slide and comparison

```markdown
## Plain title {#jessica-example .text label="Starting point"}

::: {.lists}
::: {}
List header

- First item
- Second item
:::
::: {}
List header

- First item
- Second item
:::
:::
```

The first paragraph in each column is the bold blue header. For a comparison use `.comparison` on the heading. Four items: `::: {.lists .four}`, each column a header and one line of text. When returning to a comparison later, give the side no longer argued for `::: {.dim}` in place of `::: {}`.

### Fork (a choice between two paths)

```markdown
## Plain title {#jim-fork .fork label="Starting point"}

```{=html}
<svg class="fork-lines" viewBox="0 0 1280 720" overflow="visible">
  <path d="M-2021 380 H180 C250 380 250 270 320 270 H360"/>
  <path d="M-2021 380 H180 C250 380 250 490 320 490 H360"/>
  <circle cx="360" cy="270" r="11"/><circle cx="360" cy="490" r="11"/>
</svg>
```

::: {.option style="top:260px"}
More

- Point
:::

::: {.option style="top:480px"}
Better

- Point
:::
```

The `top` values place each option beside its station; keep them as they are.

### Statement

```markdown
## {#jessica-claim .statement label="Checking"}

Knowing that quickly\
was itself a research outcome.
```

A quotation keeps its lined indent: write it as `> "Quoted words."` followed by `>` and `> [Source, year, page]{.second}`.

### Definition

```markdown
## Plain title {#jessica-term .definition label="Starting point"}

::: {.define}
Skills flattening

The definition, in one or two plain sentences.

[For example: one short concrete case.]{.second}
:::
```

Two terms: two `.define` blocks one after the other.

### Big numbers

```markdown
## Plain title {#jessica-numbers .big-numbers label="Starting point"}

::: {.numbers}
[$30 CAD]{.num} [a month: a Claude Pro subscription]{.lbl}

[1 laptop]{.num} [an ordinary consumer laptop]{.lbl}
:::
```

### Error and fix

```markdown
## Plain title {#jacob-fix .error-fix label="Checking"}

::: {.steps}
::: {.before}
[]{.icon-x}Before

Wrong value

One-line caption
:::

[]{.arrow}

::: {.checked}
Checked

What it was checked against

One-line caption
:::

[]{.arrow}

::: {.after}
[]{.icon-ok}After

Corrected value

One-line caption
:::
:::
```

### Quotations and machine text

```markdown
> "Words from a printed source."
>
> [Source title, year, page]{.second}

::: {.raw}
`raw OCR or pipeline output, exactly as written`

[File or record ID]{.second}
:::
```

Put machine text in backticks so it keeps straight quotation marks.

## Visuals

### Visual slide

```markdown
## Plain title {#jessica-map .visual label="Results"}

::: {.vis-row}
::: {.vis}
```{=html}
<video data-autoplay muted playsinline controls poster="images/…-poster.jpg">
  <source src="images/….mp4" type="video/mp4">
  <source src="images/….webm" type="video/webm">
</video>
```
:::
::: {.side}
[79%]{.num}

the number's label
:::
:::
```

The visual is 800 × 450 and is never cropped: a clip or image shows whole. The side column is optional. An image is `![](images/….png)` inside `::: {.vis}`.

### Two or three visuals side by side

```markdown
## Plain title {#jessica-attempts .side-by-side label="Results"}

::: {.series .seq}
::: {.panel .bad}
[]{.icon-x}Label

::: {.vis-sm}
![](images/….png)
:::

One-line caption
:::

[]{.arrow}

::: {.panel .good}
[]{.icon-ok}Label

::: {.vis-sm}
![](images/….png)
:::

One-line caption
:::
:::
```

`.seq` and the arrows are for a sequence; leave both out for views that aren't one. Panels: `.bad` (✗, error colour), `.good` (✓, fixed colour), or neither (a neutral view, bold blue).

### Chart

```markdown
## Plain title {#jacob-scores .chart label="Results"}

::: {.vis-row}
::: {.bars}
[System one]{.name .key} [18.0]{.bar .key style="--v:.9"}

[System two]{.name} [16.0]{.bar style="--v:.8"}

[System four]{.name .worse} [[]{.icon-x}12.0 worse]{.bar .worse style="--v:.6"}
:::
::: {.side}
[18.0]{.num}

the claim's label
:::
:::
```

`--v` is the bar's length from 0 to 1 (value ÷ the largest value shown, so bars stay to scale). Sort the rows. `.key` marks the bar the slide is about; `.worse` marks a worse one.

### Source beside its record

```markdown
## Plain title {#jacob-record .source-record label="Method"}

::: {.source-pair}
::: {.raw}
`the OCR text`

[file ID]{.second}
:::

[]{.arrow}

::: {.raw}
`the record as the pipeline wrote it`

[record ID]{.second}
:::
:::
```

For a scan instead of OCR text, put the image in the left block with its file ID below.

### Full-screen visual

```markdown
## {#jacob-demo .full-a}

::: {.vis-full}
```{=html}
<video …>…</video>
```
:::
```

`.full-a` is edge to edge with no label or title. `.full-b` keeps the label (heading `## {#id .full-b label="Results"}`). `.full-c` keeps the usual label and title.

### Process, cycle and timeline

```markdown
## Plain title {#jacob-pipeline .process label="Method"}

::: {.route .five}
::: {.stop}
Stage name

Short description
:::
(…up to five stops)
:::
```

- `.route` alone spaces four stations; `.route .five` spaces five.
- **Timeline:** `.timeline` on the heading, with a date as each stop's first line.
- **Cycle:** `.cycle` on the heading, exactly four stops, then `[Repeat]{.repeat}` after the route.

## Animation

Unchanged: put `.motion` on the heading alongside the type, and `data-at="ms"` on elements inside a ```` ```{=html} ```` block. The effect classes are listed under *Animation system* in `CLAUDE.md`.
