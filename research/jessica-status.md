# Jessica's section: status and how to pick it up again

Last updated 2026-11-13, at the end of the second working session.

## Where things stand

- **Section 2 is drafted:** `sections/_2-jessica.qmd`, 14 slides, about 13 minutes. The slide-by-slide plan is in `outline.md` (section 2).
- **Checked in Chrome at 1280×720:** no slide overflows, and every clip autoplays and ends on its final frame.
- **Jessica hasn't given feedback on the slides yet.** They opened the preview at the end of the session but haven't given feedback yet.
- **Pushed to GitHub on 2026-11-13** (up to `3b710cd`), including the commit that sets the talk title in the shared files. Jim needs to re-render `docs/` for the published deck to show the new title and section 2.
- **`docs/` was not re-rendered in a commit.** Jim publishes the rendered deck. Local renders (Quarto 1.9.38 here) change library hashes in `docs/` and add a line to `.gitignore`, so restore both before committing: `git checkout -- docs .gitignore && git clean -fd docs`.

## What's in the repo for this section

| Path | What it is |
|---|---|
| `sections/_2-jessica.qmd` | The slides and speaker notes. Section-only CSS is in a `<style>` block at the top, with classes prefixed `.jj-`. |
| `research/jessica-source-material.md` | All source material and verified figures, with file paths |
| `images/jessica/` | 5 clips (`.mp4`, `.webm`, `-poster.jpg`), the working paper's figures, and the reserve surrender map |
| `scripts/record_jessica_clips.py` | Re-records the clips from the local `Sask_Railway_Visualizations` repo |
| `scripts/check_jessica_slides.py` | Screenshots every slide of the section and flags overflow |
| `scripts/range_server.py` | Static server with HTTP Range support, used by the check script |

## Decisions made (don't re-litigate)

- **Starting point:** before 9 January 2026, Jessica had never written code. The working paper says "beyond some basic HTML," so say "never written code."
- **Timeline:** first commit 9 January 2026, then public interactive maps on 19 January (**ten days**), from the git histories.
- **Farm villages: 79%** ("four in five") of classifiable residents held non-agricultural jobs: 17,138 of 21,708 (`KnowledgeGraph/analysis/NAMED_ROLES_SYNTHESIS.md`). This matches the Active History post. "Nine in ten" counts by job title only (about 89.6%); keep it only as the answer if someone asks.
- **Surrender result:** "+77% **odds**," not probability. Logistic regression on 128 reserves: OR 1.77, 95% CI 1.44–2.17, p < 0.001 (`Reserves_Urban_Spaces/analysis/06b_LOGISTIC_REGRESSION_SYNTHESIS.md`, model M1).
- **Census:** 760,234 records is all of Saskatchewan in 1921; 220,260 people lived in the 429 settlements.
- **Audience** (Jim's `CLAUDE.md`, "Writing for this audience"): mostly STEM scientists, many neurodivergent, in person. Use literal headings, red only for errors and green only for checked results, method and sample on the slide, and history terms glossed. Slides are signposted with a four-part map (1 Starting point · 2 Method · 3 Results · 4 Checking), as in Jacob's section.
- **Scope:** Jessica works only on section 2's content. Don't edit the other speakers' sections or the shared files (`slides.qmd`, `slides.scss`, `slides-motion.html`, `CLAUDE.md`) without a heads-up.
- **New visual style for the whole deck:** Jessica is designing it, and Jim and Jacob have agreed to use it. Everything is open to change: colours, fonts, background, layout and spacing, and how visualizations sit on the slide.

## Next: the new visual style

1. **Jessica's template.** Jessica is making example slides in PowerPoint (16:9). They're filling one with the text of the Economic Hierarchy slide (`#jessica-hierarchy`). When it arrives, read the `.pptx` for its exact colours, fonts, sizes and spacing, and render it to an image. Don't commit the `.pptx` unless asked.
2. **Sample slides on a Claude Design canvas** (1280×720 artboards): the template, plus real deck slides restyled to match (title, speaker divider, a definition slide, a pipeline slide, a visualization slide). Jessica tweaks them there.
3. **A Claude Design System artifact** recording the chosen look (colours, type, spacing, components), as the shared spec for Jim's and Jacob's agents.
4. **Copy it into `slides.scss` and the "Look" section of `CLAUDE.md`**, in their own commits, with a heads-up to Jim and Jacob.

Still to ask Jessica: what exactly is wrong with how the visualizations are shown now.

## Talk subtitle: under discussion

Jessica finds "Working" in *Historians Working With LLMs* bland and wants a word for a more engaged process. Ruled out: "Grappling" (implies animosity) and "Experimenting" ("we're researching, not testing"). Candidates: **Researching With** (recommended), **Reading With**, Doing History With, Thinking With, Inquiring With. No decision yet. A change touches `slides.qmd` and `CLAUDE.md`, so it gets its own commit and a heads-up.

## Open items

Items marked `[TBD]` in the speaker notes:

1. **One-Hour Corridor map:** its sidebar shows Osler at "132.8 km by rail" and Dalmeny at "127.5 km by rail," yet both count as within one hour (40 km). Check the visualization's logic before the talk; the Settlement Explorer filters by rail distance, but this map may not.
2. **"Reserve surrender" definition box** (last slide): drafted for this audience, not quoted from Jessica's work. Jessica should check the wording.
3. **Working paper figures:** in the published paper (`Working-Papers-in-Critical-Search/paper-003-iterative-visualization`), `failed_pie.png` shows the waffle chart and `failed_waffle.png` shows the pie, so Figures 6a and 6b have swapped captions. The deck's copies are named correctly.

Not in the slides:

4. **Statement of intent and research statement** say "probability" of surrender where the model gives odds. The statement of intent's "smallest settlements averaged fewer than twenty-five people, yet nine out of ten…" combines two separate facts (see `jessica-source-material.md`, section 7).
5. **Clip size:** the clips show the whole web page, so their sidebar text is small. An option is to make each clip fill the slide and move the side text into the notes.
6. **Safari** playback hasn't been tested; the clips have MP4 and WebM sources. **PowerPoint export** (`scripts/export_slides.py`) doesn't exist yet in this repo.
7. **Jim reviews** the whole deck before anything is published.

## How to preview

```bash
quarto preview slides.qmd --port 4321
# open http://localhost:4321/slides.html?motion#/jessica-divider
```

Use the arrow keys to move, **S** for speaker notes, **F** for full screen and **Esc** for an overview. Preview rewrites `docs/`, so restore it before committing (see above).

## How to check the slides

```bash
quarto render slides.qmd
python3 scripts/check_jessica_slides.py docs /tmp/jessica-check   # needs Google Chrome and playwright
git checkout -- docs .gitignore && git clean -fd docs             # before committing
```

If you add, remove or reorder slides, update the `IDS` list at the top of the script.

## How to re-record the clips

Needed only if a visualization changes. The recorder needs a full ffmpeg; there's no Homebrew on this Mac, so use a throwaway virtual environment:

```bash
python3 -m venv /tmp/clipenv
/tmp/clipenv/bin/pip install playwright==1.58.0 imageio-ffmpeg
/tmp/clipenv/bin/python scripts/record_jessica_clips.py ~/Documents/ClaudeCode/Sask_Railway_Visualizations images/jessica
# or only some clips: ... images/jessica network-graph one-hour-corridor
```

Each clip's script (button clicks, slider moves, zoom, timing) is in the `CLIPS` table in the script. The page clock is frozen and stepped one frame at a time, so the clips are smooth at 25 fps.

## Gotchas found this session

- **Python's `http.server` breaks video in Chrome.** It doesn't support HTTP Range requests, so `<video>` fails with a decode error. Use `quarto preview` or `scripts/range_server.py`. GitHub Pages is fine.
- **Headless Chrome's screencast drops frames,** which is why the recorder steps the page clock instead.
- **Playwright's bundled ffmpeg** can only write VP8 WebM and can't read from a pipe. That's why the recorder uses `imageio-ffmpeg`.
- **Other agents push here too.** Jim's and Jacob's Claude sessions commit to this repo, so always `git pull --rebase` before starting and before pushing.
