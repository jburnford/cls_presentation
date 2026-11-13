# Slide outline: first draft

Drafted from `CLS Presentation Rough Notes.docx`. Each speaker should cut, reorder or rewrite their own section. **Needs** lists material only that speaker can supply. ★ marks a slide that would gain from animation (see *Animation system* in `CLAUDE.md`).

Thread through the whole talk: **coding agents make computational work cheap and fast, so the scarce thing is judgement. Do better, not more.**

---

## 1. Jim: opening (5 min, 3–4 slides)

1. **Title**: *Do better, not more*, with three names and a QR code to the deck.
2. **Computational history's long minority.** It had a trajectory similar to computational physics but never took off the same way. Why? The skills barrier, the time cost, and the software we were stuck with.
   *Needs:* Jim's framing, and one or two concrete examples or citations. Use no numbers unless they are sourced.
3. **On the precipice?** ★ A path forks into **more** (more documents, more maps, more output) and **better** (better questions, better-checked evidence, better arguments). Leave the question open: "As a journal editor, I haven't nailed this down yet."
4. **What's coming:** Jessica on getting started and visualization as method; Jacob on knowledge graphs and search; Jim back at the end on what "better" might mean.

## 2. Jessica: getting started, and visualization as method (10–15 min, 10–15 slides)

General and positive. The theme is skills flattening: no longer gated by other people's capacity.

1. **Divider:** Jessica, plus a one-line description of the project.
2. **Where I started.** Had never used a command line.
   *Needs:* project and research question.
3. **How fast.** ★ A timeline: never used a command line → interactive visualizations on GitHub in **under a month** → [TBD: what was reached at **under six months**]. *Confirm the two milestones and their wording.*
4. **What "skills flattening" means.** A `.def` box: the gap between knowing what a computer could do and being able to make it do it has narrowed. You are no longer waiting on someone else's time.
5. **The old way.** Specific software dictated the output (ArcGIS for mapping, for example). Each version of a map took days, so you made few versions.
6. **The new way.** ★ An iteration loop (ask → build → look → notice a problem → change → rebuild) cycles several times, with a clock beside it reading **days → minutes**.
7. **Visualization as method.** The visualization is a way of finding things out, including problems in the data, not just the final figure.
   *Needs:* one example where a visualization showed something unexpected, with a before/after screenshot.
8. **A worked example.** ★ One visualization shown in 3–4 successive versions, each annotated with what prompted the change.
   *Needs:* screenshots or a live link.
9. **Testing at scale, as a grad student.** Problems and outcomes can now be tested at a scale that used to need a funded team.
10. **Try it, then bring it to the team.** Experiment alone, then workshop it with the group. *Needs:* one example of something brought to the team and what came of it.
11. **What still needed judgement.** Where did a human have to decide, check or say no? This sets up Jim's close.
12. **Handoff to Jacob.**

## 3. Jacob: knowledge graphs, GraphRAG, and agentic search (15 min, 15 slides)

Built in `sections/_3-jacob.qmd` for the confirmed audience (STEM scientists, many neurodivergent). Every number comes from Jacob's MA thesis (*Loud Yet Invisible*, chapters 1–3) or the OpenAlex API (checked 13 Nov 2026); sources are in the speaker notes. A four-part progress strip (Problem · Graphs · Agents · Scale) sits on every slide.

1. **Divider** with a four-part agenda.
2. **Nobody can read everything in a large collection.** 20,646 documents, ~2M pages, 1.22B words; Barbados in four spellings; the sugar test question (1 of 8 systems answered it).
3. **Nearest in meaning is not the same as relevant.** ★ Schematic of nearest neighbours; plain RAG scored 13.0/25 and could not answer quantitative questions.
4. **My pipeline.** ★ olmOCR-2 (WER 0.075) → EarlyModernNER (451,404 mentions) → graph (218k nodes, 692k edges) → 8 retrieval systems → historian.
5. **Existing entity taggers failed, so I trained one.** ★ Bar chart, strict F1: spaCy 0.198 … Gemini 3 Pro 0.665, EarlyModernNER 0.775; SER 0.331 vs 0.672; 6.5 GB GPU.
6. **A knowledge graph stores entities and typed relationships.** Real fragments: spelling variants merged to Barbados; muscovado/molasses IS_VARIANT_OF sugar; 43,000 customs rows.
7. **GraphRAG: the graph decides which documents to read.** ★ The thesis's graph-directed pipeline.
8. **Results: 8 systems, 30 questions.** ★ Bar chart; KG+RAG worse than RAG (red); Improved Scratchpad 17.90. Method limits stated on the slide.
9. **Why graph-directed retrieval plateaued near 15.7.** Four failure cards.
10. **What worked: an agent that takes notes on each source.** ★ Improved Scratchpad flow; 63 of 70 head-to-head wins; cost 593 s per question.
11. **The larger model asked the graph a narrower question.** ★ Before/fix: Claude Opus 4.7 (red, partial record) vs local Qwen (green, full record).
12. **For thousands of documents, well-organised text is enough.** Semi-structured text; a facility's manuals and logbooks.
13. **MCP and Linked Open Data.** Two `.def` boxes; CLS's real ROR and OpenAlex identifiers.
14. **Demo: an agent searching CLS's own papers** through an OpenAlex MCP connector. *Needs:* the question, a run, and a saved fallback recording.
15. **Which approach fits which collection size**, then handoff to Jim.

## 4. Jim: closing (10 min, 6–8 slides)

1. **Two things combined.** Skills flattening (Jessica) plus knowledge organization (Jacob): researchers can now build and query their own structured sources.
2. **Breaking silos.** A few years ago, a task we *knew* a computer could do meant weeks of broken code and Stack Overflow. Projects got deferred.
3. **"A research assistant who has read everything but can't remember where it read it."** Give the line its own slide. It is useful, and it is why sources and checking still matter.
4. **Deferred projects, now done.** ★ One before/after: what was shelved, and what it became.
   *Needs:* an example from Jim's own projects; the Imperial Careers atlas is a candidate.
5. **More vs better, revisited.** ★ Return to the opening fork. What makes work *better*: checked against the source, honest about coverage, and decisions recorded with their evidence.
6. **The editor's view.** What a journal should ask of AI-assisted computational history. Leave it as an open question rather than an answer.
7. **Questions.** Three names, the QR code, and links to each speaker's project.

---

## Open questions

- ~~What does CLS stand for?~~ Canadian Light Source, in person. Date and room still TBD.
- ~~Who is the audience?~~ Mostly STEM scientists, many neurodivergent. See *Writing for this audience* in `CLAUDE.md`.
- One deck, or each speaker presenting from their own machine? (One deck is recommended: a single URL and no switching.)
- Will there be live demos? Keep at most one, with a saved fallback.
