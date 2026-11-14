# Jessica's section: status and how to pick it up again

Last updated 2026-11-14, at the end of the third working session.

## Where things stand

- **Section 2 is drafted:** `sections/_2-jessica.qmd`, 14 slides, about 13 minutes. The slide-by-slide plan is in `outline.md` (section 2).
- **Checked in Chrome at 1280×720:** no slide overflows, and every clip autoplays and ends on its final frame.
- **The deck has a new look (pushed 2026-11-14, `a659264`).** Jessica designed it; the spec is the *Look* section of `CLAUDE.md`, `style-guide/demo.html` shows one slide of each type, and `style-guide/markup.md` gives the Markdown for each. **Section 2 is still written in the old JHU markup**, so it now renders broken (overlapping text) until it's rebuilt. That rebuild is the next job (below).
- **Pushed to GitHub on 2026-11-13** (up to `3b710cd`), including the commit that sets the talk title in the shared files. Jim needs to re-render `docs/` for the published deck to show the new title and section 2.
- **`docs/` was not re-rendered in a commit.** Jim publishes the rendered deck. Local renders (Quarto 1.9.38 here) change library hashes in `docs/` and add a line to `.gitignore`, so restore both before committing: `git checkout -- docs .gitignore && git clean -fd docs`.

## What's in the repo for this section

| Path | What it is |
|---|---|
| `sections/_2-jessica.qmd` | The slides and speaker notes. Still in the old look: section-only CSS in a `<style>` block at the top, with classes prefixed `.jj-`. The rebuild removes that block; the theme now sets every size, colour and gap. |
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
- **Audience** (`CLAUDE.md`, "Writing for this audience"): mostly STEM scientists, in person. Don't describe the room as neurodivergent; nobody knows the share. Use literal headings, the error colour only for errors and the fixed colour only for checked results (always with a word or icon too), method and sample on the slide, and history terms glossed. The section is signposted by its divider route (Starting point · Method · Results · Checking) and the same words as the label above each slide's title.
- **Scope:** Jessica works only on section 2's content. Don't edit the other speakers' sections or the shared files (`slides.qmd`, `slides.scss`, `slides-motion.html`, `CLAUDE.md`) without a heads-up.
- **New look for the whole deck:** designed by Jessica, approved, implemented and pushed on 2026-11-14. Jim and Jacob agreed to use it. `CLAUDE.md` tells their agents to show them the look and explain what changes before touching their slides; Jessica sends them the heads-up.

## Next: rebuild section 2 in the new look

Do this in its own session, one step at a time with Jessica (they prefer one decision at a time, and want only flagged things changed).

1. `git pull --rebase` first: Jim's and Jacob's agents may have pushed their own rebuilds.
2. Rebuild each slide in `sections/_2-jessica.qmd` as one of the slide types in `CLAUDE.md` (*Look* → *Slide types*), written as in `style-guide/markup.md`. Keep Jessica's words, figures and speaker notes; drop the `.jj-` style block and the old `jj-map` signpost row (the label above each title replaces it). IDs stay `#jessica-…`.
3. **Slides that hold two or three ideas** and need splitting (the guide says split rather than stretch a type). Propose a split to Jessica before building:
   - `#jessica-flattening`: a definition, the resources (big numbers), and what was built.
   - `#jessica-question`: the surrender map, the "reserve surrender" definition, and the statistical test.
4. Render locally, take Playwright screenshots at 1280×720 of every slide (final frame of motion slides) in light and dark (`?dark`), check them, then show Jessica. Update the `IDS` list in `scripts/check_jessica_slides.py` if slides are added or split.
5. Commit when Jessica approves; push only when asked.

Open content questions to raise during the rebuild (not style):

- **Knowledge graph size** for the skills-flattening slide: 406,697 nodes and 1,352,713 relationships, counted from Jessica's local Neo4j on 2026-11-13. Cite the count date in the notes if used.
- **Four vs six commercial tiers:** `#jessica-hierarchy`'s title and `#jessica-fails` say "four"; the notes and source material describe six (four census tiers plus grain hamlets and elevator sidings). Jessica hasn't decided.
- **Divider and agenda wording:** Jessica's PowerPoint template drops "Getting started, and" from the divider title and rewords the Method part as "Method: visualize, analyze, iterate, repeat."

Jessica's PowerPoint template (`Do Better, Not More Template.pptx`, project root) was used while designing the look. It stays uncommitted unless Jessica asks. When Jessica points to it, copy only the part they name.

## Talk subtitle: under discussion

The title's comma ("Do Better, Not More") is decided and in `CLAUDE.md`, but `slides.qmd` still says "Do Better Not More". Changing it is a shared-file change: ask Jessica, then its own commit and a heads-up.

Jessica finds "Working" in *Historians Working With LLMs* bland and wants a word for a more engaged process. Ruled out: "Grappling" (implies animosity) and "Experimenting" ("we're researching, not testing"). Candidates: **Researching With** (recommended), **Reading With**, Doing History With, Thinking With, Inquiring With. No decision yet. A change touches `slides.qmd` and `CLAUDE.md`, so it gets its own commit and a heads-up.

## Open items

Items marked `[TBD]` in the speaker notes:

1. **One-Hour Corridor map:** its sidebar shows Osler at "132.8 km by rail" and Dalmeny at "127.5 km by rail," yet both count as within one hour (40 km). Check the visualization's logic before the talk; the Settlement Explorer filters by rail distance, but this map may not.
2. **"Reserve surrender" definition box** (last slide): drafted for this audience, not quoted from Jessica's work. Jessica should check the wording.
3. **Working paper figures:** in the published paper (`Working-Papers-in-Critical-Search/paper-003-iterative-visualization`), `failed_pie.png` shows the waffle chart and `failed_waffle.png` shows the pie, so Figures 6a and 6b have swapped captions. The deck's copies are named correctly.

Not in the slides:

4. **Statement of intent and research statement** say "probability" of surrender where the model gives odds. The statement of intent's "smallest settlements averaged fewer than twenty-five people, yet nine out of ten…" combines two separate facts (see `jessica-source-material.md`, section 7).
5. **Clip size (settled by the guide):** a recorded clip always plays whole, app interface included, never cropped. Where its text is too small, use a full-screen visual (`CLAUDE.md`, *Full-screen visual*: options A, B, C, chosen by the slide's owner) and move side text to the notes. If re-recording, zoom the app in so its text is large.
6. **Safari** playback hasn't been tested; the clips have MP4 and WebM sources. **PowerPoint export** (`scripts/export_slides.py`) doesn't exist yet in this repo.
7. **Jim reviews** the whole deck before anything is published.

## How to preview

```bash
quarto preview slides.qmd --port 4321
# open http://localhost:4321/slides.html?motion#/jessica-divider
# add &dark for the dark version: slides.html?motion&dark#/jessica-divider
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
- **A bare `<video>` tag in Markdown breaks every slide after it** (Pandoc nests the rest of the deck inside it). Always put videos in a ```` ```{=html} ```` block.
- **Present from Chrome.** The spacing relies on `text-box: trim-both cap alphabetic`, which Firefox doesn't support yet.
- **Other agents push here too.** Jim's and Jacob's Claude sessions commit to this repo, so always `git pull --rebase` before starting and before pushing.
