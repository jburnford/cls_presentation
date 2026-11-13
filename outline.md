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

## 3. Jacob: knowledge graphs, GraphRAG, and agentic search (10–15 min, 10–15 slides)

More specific and technical. Gloss every term where it first appears.

1. **Divider:** Jacob, plus the project, especially the technical documentation use case.
2. **The problem.** A large body of text, and a question that needs facts from many places in it.
   *Needs:* the real corpus and a real example question.
3. **What is a knowledge graph?** A `.def` box, then a small real fragment: entities as nodes, relationships as edges. Knowledge graphs organize material and give access to it.
4. **What is a vector database?** ★ Text becomes points in space; a question finds its nearest neighbours by cosine similarity. `.def` boxes for *embedding* and *cosine similarity*.
5. **Where cosine similarity falls short.** ★ A question that retrieves passages which *sound* similar but don't hold the fact, or which misses a fact that needs two hops to reach.
   *Needs:* a real example of the failure.
6. **What is GraphRAG?** ★ A flow: question → retrieve from the graph and the text → hand to the model → answer. A `.def` box for *RAG* (retrieval-augmented generation).
7. **Why it doesn't always fulfil its promise.** The cost of building the graph, extraction errors, and the upkeep.
   *Needs:* Jacob's experience.
8. **What changed: agentic search.** ★ A loop: the model searches by keyword → reads → refines the query → searches again → answers with sources. A `.def` box for *agent* and *MCP* (a standard way to give a model tools such as a search box or a database).
9. **Semi-structured text is often enough.** Models are now good enough at agentic search that you may not need a whole system.
10. **When each one fits.** A three-column `.cards` slide: agentic search over semi-structured text (small to medium corpora); vector search (fuzzy recall); knowledge graph or GraphRAG (millions of documents, exact relationships, reuse across projects).
11. **Knowledge graphs still matter.** Why: organization, exact queries, provenance, reuse.
12. **Handoff to Jim.**

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

- What does CLS stand for? Date, room, and whether there's a Zoom audience.
- Who is the audience? That decides how much glossing Jacob's section needs.
- One deck, or each speaker presenting from their own machine? (One deck is recommended: a single URL and no switching.)
- Will there be live demos? Keep at most one, with a saved fallback.
