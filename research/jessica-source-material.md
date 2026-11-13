# Source material for Jessica's section

Pulled on 2026-11-13 from `~/Documents/PhD/Application Materials` and `~/Documents/ClaudeCode`. Dates come from git histories and file timestamps. Numbers come from project READMEs and analysis docs. The rough notes are in `CLS Presentation Rough Notes.docx`.

Jessica's section is the general one, 10–15 slides in 10–15 minutes. Its themes are skills flattening, visualization as method, not being gated by other people's capacity, and bringing work to the wider team.

---

## 0. The working paper is the backbone of this section

Jack, Jessica. "What Became Possible: Iterative Visualization with an LLM as a Research Method in Computational History." *Working Papers in Critical Search*, Paper 003, 2026-06-15. doi:10.5281/zenodo.20706174

- Read: https://working-papers-in-critical-search.github.io/paper-003-iterative-visualization/
- Source: https://github.com/Working-Papers-in-Critical-Search/paper-003-iterative-visualization

The paper is a Quarto project that embeds the live visualizations (`embeds/`) and static figures of the failed experiments (`figures/`). Both can be reused directly in Quarto slides. Its license is CC-BY 4.0 for the content and MIT for the code.

**Core argument:** the method's value "lay not in the answers it produced but in the questions it made askable: the analytical work migrated from programming to history."

**Lines that would work on slides:**
- "Being able to test an idea within a session rather than across weeks changed which ideas were worth testing." A question became worth pursuing "when the time cost of trying it was an afternoon rather than a month."
- "Visualizations generated findings rather than illustrated them. Failed visualizations clarified methodological constraints rather than representing wasted effort."
- "When the cost of trying something is low, the cost of failing is low too."
- "Legibility is a functional requirement for a research tool, not a design preference."
- "The skepticism and professional rigour that AI requires are not a caveat. They are the method."
- "Historians are not ignorant of computational methods. What has kept many from exploring them is not interest nor access to digital data, but the gap between having a question and being able to usefully test it."
- "The value of this process has not been in the answers it suggested, but in the questions it allowed me to ask."

**The first prompt**, which is a good opening moment: *"I have my knowledge graph and the Historical Canadian Railroads GIS data, and I want to understand how they connect. Can you help me see that?"*

**The personal turn:** "I have lived in Saskatchewan my whole life and have experienced its distances but seeing them in railway time rather than driving time shifted my thinking." The myth of the lone pioneer gave way to something structural: "They were nodes in a network, and the network had a shape."

**The three constraints the method resolved:**
1. Cross-dataset translation: three datasets in different formats, scales and purposes.
2. Scale and speed: 429 municipalities, half a province, 50 years, on an MA timeline.
3. Not being able to code: "I had not learned programming languages beyond some basic HTML."

**What Claude Code did and didn't do:** it did not analyze the data or produce conclusions. It co-designed the tools, translated research questions into technical specifications, converted between incompatible formats and flagged misleading approaches. Over time, Jessica learned where it "fell short": its assumptions, shortcuts and questions it would miss. Catching those meant going deeper into the data, which "was where much of my historical thinking happened."

**Cost and hardware (a strong point for a CLS audience):**
- Claude Pro subscription at $20 USD / $30 CAD per month.
- Mostly Claude Sonnet, the mid-tier model: claude-sonnet-4-5 until 2026-02-16, then claude-sonnet-4-6.
- A consumer laptop with no HPC.
- Usage limits forced deliberate session planning, and "that rigour became part of my methodology."
- Sonnet is "more prone to easy but incorrect solutions," which made close checking of every output necessary.

**Four visualizations that generated questions:**
1. **One-Hour Railway Corridor.** Built within days of the first session. Shifted the frame from isolated pioneers to a network.
2. **Economic Hierarchy Map.** All 429 settlements in four commercial tiers. This became the typology at the centre of the thesis. It came from the question of whether "urban municipality" was just bureaucratic language for some farms with a post office.
3. **Network graph** with geographic and force-directed toggle. Eight multi-railway junctions emerged, including less obvious ones like Nokomis and Biggar.
4. **Railway timeline.** The network shown as a sequence of events rather than a fixed fact.

Plus the **reserve surrender overlay**: surrendered parcels cluster near railway lines and within reach of the commercial network. In the paper's words, the overlay "did not constitute a finding; it constituted a question worth testing rigorously." The surrender data was compiled by colleagues Ashley Rabbitskin and Julian Rioux.

**Three kinds of failure, all with figures in the paper:**
1. **Pie, waffle and treemap** of the tier distribution. They removed geography, and with it the research question.
2. **Time-warped cartogram.** A compelling concept, but disorienting, and it offered no useful alternative frame of reference.
3. **429 × 429 travel-time heatmap.** Readable cells didn't fit on screen, and a screen-sized view made the cells invisible. It was replaced by a tool that looks at one connection at a time.

**Before Claude Code (summer 2025):** Jessica spent three months in archives and local history collections compiling establishment data for 409 of 429 urban municipalities, from more than 200 local history books. "What I did not fully recognize at the time was what I had built. That spreadsheet was a knowledge graph." This is a good bridge to Jacob's section.

**Data honesty:** the railway GIS data had 272 discrepancies with the knowledge graph, of which 261 were resolved by cross-referencing and 11 remain unresolved. Travel times use 40 km/h as a proxy for branch-line speeds.

---

## 0b. Active History post: collaboration, not extraction

Jack, Jessica (lead author), with Chloë Farr and Jacob Polay. "Not Just Farming: How an LLM Helped Me Study Saskatchewan's Smallest Settlements." *Active History*, 2026-10-14. This is the closing post of the "AI and Collaboration" series.
https://activehistory.ca/blog/2026/10/14/llm-saskatchewans-settlement-history/
(The site blocks automated access. The text was supplied by Jessica.)

**Thesis:** "Good AI-assisted historical research isn't a shortcut around other people's labour. It's a way of putting that labour into conversation."

**The finding (sorting by function rather than size):**
- Settlements had long been sorted by population, where larger meant more important.
- Sorted by economic function instead, **79% of the classifiable workforce in farm villages**, the smallest settlements in the census, held jobs that had nothing to do with farming. They were grain buyers, bank clerks, blacksmiths and station agents.
- "Whole local economies built around moving goods and money were hiding inside these smaller places."
- The typology has six tiers: cities, regional hubs, service towns, farm villages, grain hamlets and elevator sidings. Each "did structurally different economic work, whatever their population." The distinction "was invisible in any single source."

**Whose labour went in (a ready-made slide):**
- **Census enumerators and archivists:** about 760,000 individual 1921 census records, built for a government count.
- **University researchers:** cleaned, digitized and mapped the census.
- **A separate research project:** grain elevator licensing records, meant to track industry, not classify communities.
- **Government historians:** records of every post office opened and closed.
- **Railway historians and GIS specialists:** rail lines digitized station by station.
- **Hundreds of volunteers, local historical societies and archivists:** more than 400 community-written local history books, recording "what people in a place actually said the place was for."
- In total, **more than 600 named contributors and institutions** in the local history compilation alone.
- "Each of these datasets was built to answer a narrower question, by people who never expected their work to end up joined to others." Some were made a century apart.

**What the LLM did, step by step:** it converted the sources into spreadsheets, imported them into Neo4j, filtered for relevant information, standardized the data against chronological change, and queried the results "to answer new questions asked of old material." Jessica: "I did not use it to generate the findings." The LLM "matched historical data points that meant different things depending on who recorded them. It reconciled categories built decades apart."

**Ties to the other sections:**
- The series covers transcription (Farr), entity tagging, and a knowledge graph that "kept … sources attached to the graph, rather than letting them dissolve into a single unaccountable answer, enabling a researcher to query over a million pages." The knowledge graph piece is Jacob's material, so it makes a natural handoff.
- "Talkie" is the counterexample from the July post, "The Archive is Not a Toy." It "extracts historical and archival labour and returns one closed answer, with no path back to the people whose work it was trained on."
- "An LLM can extract as easily as it can connect … it is the user who decides which road is taken." This speaks directly to Jim's "better, not more."

**Decision (2026-11-13): the slides use 79%, or "four in five," which matches this post.** See section 7 for the check.

---

## 1. The timeline (the "how fast" claim)

| Date | What happened | Evidence |
|---|---|---|
| Jul–Dec 2024 | Sakitawak Traditional Land Use Study (with Dr. Cheryl Troupe). Dr. Ben Hoy teaches them HGIS software. This is the first move from anthropology toward digital history. | SSHRC Research Contributions; statement of intent |
| Feb 2025 | Starts work with Dr. Hoy on Justice of the Peace records (archival collection and cleaning) | SSHRC Research Contributions |
| Jun 2025 | Joins the Mapping Settler Colonialism project (Clifford and Troupe) | SSHRC Research Contributions |
| Summer 2025 | Three months in archives and local history collections, compiling establishment data for 409 of 429 urban municipalities. This becomes the knowledge graph. | Paper 003 |
| Sep 2025 | Starts the History MA | SSHRC Research Contributions |
| **Before 2026-01-09** | **Had never written code** | Jessica |
| **2026-01-09** | Starts using Claude Code. `~/Documents/ClaudeCode` created; first commit of the Knowledge Graph (Neo4j, 429 settlements) | folder creation date; `KnowledgeGraph` git log |
| **2026-01-19** | **First public interactive visualizations on GitHub Pages** (one-hour railway corridor, railway timeline) | `Sask_Railway_Visualizations` git log |
| 2026-01-23 | Five more visualizations added in one day (network graph, isochrone, gravity, matrix, cartogram demos) | git log |
| 2026-01-26 | Saskatchewan Community Sources website goes live (428 communities, 550 book citations, 1,764 web sources) | `Sask_Community_Sources` README |
| 2026-01-28 | Bulk downloader for Saskatchewan newspapers | `Newspapers` git log |
| Feb 2026 | Telegraph lines digitized from 1883–1915 maps and aligned to settlement and railway data | `Telegraph` notes |
| 2026-03-06 | OCR/NER pipeline built, with an in-browser annotation tool, over 142 local history books | `OCR_NER` README |
| 2026-03-16 | 25th railway visualization (Economic Hierarchy) | git log |
| Mar 2026 onward | 33 numbered quantitative findings from the knowledge graph plus the 1921 census (760,234 person records) | `KnowledgeGraph/analysis/FINDINGS.md` |
| Apr 2026 | Reserve surrender spatial analysis starts | `Reserves_Urban_Spaces` git log |
| 2026-06-01 | CHA presentation, "Unmaking the Prairies" (with Jim) | CV |
| May–Aug 2026 | Lab Supervisor / RA in the HGIS Lab, supervising interns and RAs | SSHRC Research Contributions |
| 2026 | Working paper, "What Became Possible: Iterative Visualization with an LLM as a Research Method in Computational History" (*Working Papers in Critical Search*, Paper 003 on the series site) | jjax07.github.io |
| Sep–Oct 2026 | Active History "AI and Collaboration" series with Chloë Farr and Jacob Polay. Jessica's post: "Not Just Farming: How an LLM Helped Me Study Saskatchewan's Smallest Settlements" (Oct 14) | jjax07.github.io |

**The headline:** before January 9, 2026, Jessica had never written code. It took about **10 days** to go from that starting point to publicly posted interactive visualizations, and **25 visualizations in under 10 weeks**. That's ahead of the notes' "less than a month." From there it was under five months to a CHA presentation built on the work.

Note: the submitted SSHRC Research Contributions describe the MA (from September 2025) as including "formal training in ... Python programming." That doesn't change the starting point, since Jessica had not coded before January 9. But if someone in the audience has read the SSHRC materials, the difference may be worth a sentence of explanation.

---

## 2. Scale of output (Jan–Nov 2026)

| Measure | Count |
|---|---|
| Project folders | 16 |
| Git repositories | 15, on GitHub, GitLab and USask GitLab |
| Python scripts | about 1,200 |
| HTML visualizations and pages | 80 |
| Markdown documentation files | about 840 |
| Commits, JP/OJP linkage project alone (May–Aug) | 406 |
| Commits, Knowledge Graph (Jan–Jun) | 152 |
| Commits, Railway Visualizations | 88 |

These numbers support the "do better, not more" tension rather than undercutting it. The volume is real, and the question is what makes it better history.

---

## 3. Visualization as method (the core example)

**Live site:** https://jjax07.github.io/Sask_Railway_Visualizations/

There are ten main visualizations plus five exploratory demos, built over 429 settlements and about 1,121 railway connections, 1882–1920.

1. One-Hour Railway Corridor from Saskatoon (time slider, 1890–1920)
2. Settlement Explorer (any of 429 settlements, reachable neighbours within an hour by rail)
3. Railway Network Timeline (four companies expanding year by year)
4. Network Graph (geographic vs. force-directed views)
5. Journey Times (walking vs. horse and cart vs. rail, using Dijkstra routing on real track)
6. Travelling Time Simulation (animated race between modes)
7. Travel Time Comparison (isochrone)
8. Transport Eras
9. Railway Temporal Network
10. Economic Hierarchy
- Demos: centrality rankings, railway company territory, small multiples, connectivity inequality, accessibility heatmap

**The iterative story in the commit log:** the original railway visualizations went up on 2026-01-19. The Settlement Explorer followed on Jan 21, five demos on Jan 23, multi-modal journey times on Jan 30, the travel race on Feb 1 and five more demos on Feb 6. In February the log also shows data corrections that the visualizations themselves surfaced. Examples are "Correct first railway for Unity, Mossbank, Young, and Conquest" and a known-issues file. Visualization was the way errors in the data got found, as well as the output.

**A visualization that changed the analysis:** the network graph and centrality work led to Finding 1. *Railway connectivity does not predict commercial importance.* The most rail-connected places were small villages, such as Liberty (population 161). This only shows up when all 429 settlements are viewed at once.

**Contrast with ArcGIS:** in August 2026 Jessica built an "ArcGIS Colleague Package" (`Summer_JP_Work/ArcGIS_Colleague_Package`). The working map was a Leaflet web map built in code. For colleagues who work in ArcGIS, the underlying layers were exported to ArcGIS-compatible formats with styling notes. The layers were 10,890 JP appointments, 1,631 OJP appointments, 34,356 sentencing records, reserves, municipalities and railways. This is a concrete example of iterating quickly in code and then handing results to the wider team in the tools they already use.

---

## 4. Skills flattening and not being gated by other people's capacity

**Starting point: before January 9, 2026, Jessica had never written code.** Everything below was built after that date.

Each of these used to need a programmer, a web developer or a data team. Jessica built each one:

- **Knowledge graph.** The data was compiled by hand in summer 2025. In the first week of January it was loaded into a Neo4j graph of 429 settlements linked to founding events, railway lines and stations, and residential schools.
- **Public websites.** Railway visualizations, a searchable Community Sources database and a personal research site, all on GitHub Pages.
- **OCR and NER pipeline.** Entity extraction across 142 OCR'd local history books, plus a custom in-browser annotation tool for building gold standards.
- **Record linkage at scale.** 6,061 unique people across 12,521 JP/OJP appointments, linked to prison sentencing records. Delivered to an external collaborator (Kris Inwood) on 2026-08-04.
- **GIS alignment.** Telegraph lines digitized from four historical maps, then snapped to railway and settlement data with Python (GeoPandas).
- **Census analysis.** 760,234 individual 1921 census records, 33 documented findings, and an 18,000-word methodology document recording every inclusion and exclusion decision.

## 5. Bringing it to the wider team (workshopping)

- The ArcGIS Colleague Package (above).
- Handover repositories on USask GitLab (`JP_Work_Handover`, `handover_summer_jp_work`) and a frozen handover copy for Kris Inwood.
- Shared gold standards on the `history-graphrag` USask GitLab group (`gold_standards_sask`). This links to Jacob's section.
- Wikidata QID gold standards for a colleague (`Kashif_QIDs`).
- Supervising HGIS Lab interns and RAs (May–Aug 2026).
- Co-written public pieces: the Active History series (with Farr and Polay) and the OCR benchmark working paper (Clifford, Polay, Jack, Humphries, Leddy).

## 6. "Do better, not more": guardrails that make the speed trustworthy

Useful for tying Jessica's section back to Jim's frame:

- **Audit tooling in the JP project.** Three scripts check script provenance, unapplied review decisions, and consistency of identity decisions. These were added after a stale reused function silently dropped merge decisions (the "Reusch/Madison and 14 more identities" case, 2026-07-23). The project's rule: "State out loud when this check runs and what it found — a silently-skipped check is invisible; a claimed one is checkable."
- **Methodology logged as decisions are made.** `METHODOLOGY.md`, `FINDINGS.md` (each finding records question, method, result and significance) and `DEDUP_ISSUES_LOG.md`.
- **Negative and inconclusive results are recorded.** For example, Finding 19 is "Exploratory (Inconclusive)."
- **Absences are treated as findings.** Finding 25: only 96 of 220,260 people in the 1921 municipal census are recorded as Indigenous. The census is a settler document, and the absence is the finding.
- **From the statement of intent:** the pipeline "made historical questions tractable at scale without displacing the analytical work," and it amplifies "close archival reading rather than replacing that methodology."

## 7. Research findings available as a payoff slide

These are from the research statement and statement of intent. They are findings that "required the full provincial dataset to surface; no individual case study could have identified them."

- 66% of Saskatchewan settlements preceded the nearest First Nations reserve land surrender.
- Every additional 1,000 rural residents within 25 km of a reserve increased the probability of surrender by 77%.
- Reserves that experienced a surrender (1877–1933) had on average 3.5 times as many rural settlers within 25 km.
- The railway network was architecturally complete in 1906, the same period reserve surrenders peaked.
- Railway arrival timing, not agricultural population density, was the dominant predictor of settlement type.
- 933 settlement nodes, including 435 grain hamlets that never made the census rolls.
- **In farm villages, 79% (four in five) of working residents held non-agricultural occupations.** This is the figure chosen for the slides.

### The farm village figure: 79%, verified 2026-11-13

**Wording to use:** *"In farm villages, four in five working residents held jobs that had nothing to do with farming."* Or use "79%."

**Tier:** Farm Villages, the 356 smallest incorporated settlements (Small Service Centres), with an average 1921 population of 179.

**Source:** `KnowledgeGraph/analysis/NAMED_ROLES_SYNTHESIS.md`. 17,138 of 21,708 classifiable Farm Village residents (79%) held non-agricultural occupations. Agricultural means either the industry ("Own Farm," "Agriculture") or the occupation title is farming, following the whitelist in METHODOLOGY.md §9.8. This is the same figure as the Active History post.

**Why not "nine out of ten"?** The CHA script and statement of intent used nine in ten, and it's real. Recomputed from Neo4j on the same 21,708 people, counting by *occupation title only*, about 89.6% are non-agricultural. But that count treats general labourers who worked on farms as non-agricultural. 79% is the stricter count and matches published work. If asked: *"By job title alone it's nine in ten. Counting farm labourers by the industry they worked in, it's four in five."*

**Don't reuse the statement of intent's wording** ("the smallest settlements averaged fewer than twenty-five people, yet nine out of ten…"). It combines two separate facts:
- Only 2 of the 429 incorporated settlements had fewer than 25 people, and the smallest had 22.
- The 435 grain hamlets have no 1921 population or occupation data of their own (`SECONDARY_SUBCSD_FINDINGS.md`).

**Other numbers to ignore or fix:**
- `EMPLOYMENT_URBANITY_SYNTHESIS.md` gives a Farm Village table (5,193 agricultural, 16,119 non-agricultural, 75.6%). It is divided by a different total and isn't a competing result.
- `NAMED_ROLES_SYNTHESIS.md` says agricultural workers are "8.2% of the total Farm Village classifiable population." The 8.2% is out of *all* residents. Out of classifiable residents it is about 21%.

---

## Gaps and open questions

- **Screenshots.** The live visualizations can be embedded in Quarto slides as iframes, but a static fallback image of each is safer in case the venue's Wi-Fi fails.
