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

## 3. Jacob: knowledge graphs, GraphRAG, and agentic search (15 min, 14 slides)

Drafted in `sections/_3-jacob.qmd`. More specific and technical; every term gets a `.def` box where it first appears. Minute ranges are in the speaker notes.

1. **Divider:** Jacob; knowledge graphs, GraphRAG and agentic search.
2. **Too much text, not enough reading time.** `.stats`: ~20,000 documents, ~2 million pages (MA corpus), 250M+ works in OpenAlex.
   *Needs:* real spelling variants; one real research question.
3. **What is a knowledge graph?** `.def` + a `.flow` of entity types (person → ship → commodity → place).
   *Needs:* one real fragment from the graph, with document ID.
4. **What is a vector database?** ★ `.def` boxes for *embedding* and *cosine similarity*; chunk → embed → nearest neighbours.
5. **Where cosine similarity falls short.** ★ Four `.cards`: mentions ≠ about; no aggregation; chunks lose context; two-hop facts.
   *Needs:* a real failure example from the thesis.
6. **What is GraphRAG?** ★ `.def` for *RAG*; extract → graph → communities → summaries → answer.
7. **What I built.** olmOCR → EarlyModernNER → knowledge graph → GraphRAG retrieval (Improved Scratchpad) → historian. `.def` for *NER*.
   *Needs:* one headline result and how it was measured.
8. **Why it doesn't always fulfil its promise.** Cost (~1,000× a vector index, Microsoft's LazyGraphRAG figures), compounding errors, generated summaries, upkeep. Reframe: search and ranking, not answers.
   *Needs:* Jacob's own experience of each.
9. **What changed: agentic search.** ★ `.def` for *agent*; search → read → refine loop.
10. **Semi-structured text is often enough.** Good documentation practice is now good AI practice.
11. **MCP: one plug for many sources.** `.def` for *MCP*; files, archive, OpenAlex, Wikidata, a knowledge graph as one tool among several.
12. **Linked Open Data.** `.def`; Wikidata, OpenAlex/DOIs, ORCID, ROR. Don't rebuild the world's graph; link to it.
13. **Searching millions: what fits where.** Three `.cards` by scale: agentic search (thousands); an index the agent calls through MCP (millions); Linked Open Data (hundreds of millions).
14. **Knowledge graphs still matter**, then handoff to Jim. Organization, exact queries, provenance, reuse.

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
