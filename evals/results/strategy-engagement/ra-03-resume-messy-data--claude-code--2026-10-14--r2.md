# ra-03-resume-messy-data on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md and 04-workplan.md before analysing, and names H2 (workplan row 2) as the branch. | yes | Output references 'workplan row 2' and uses the exact hypothesis wording ('EUR 1.10 to at least EUR 1.60') and kill criterion ('below EUR 1.35') from 02-hypotheses.md, and updates 00-status.md's existing log/table structure. |
| Does not ask for the hypothesis, kill criterion or problem statement again, or restart the engagement. | yes | The run proceeds directly to analysis using data/cafe-tills-2026h1.csv with no re-ask of framing artefacts. |
| Finds and handles P1, P2 and P3 explicitly. | yes | Data notes section: 'Site B's Q1 row was labelled site b ... hand-typed as text' and 'Site A's Q2 row appeared twice, identical ... treated as a duplicate and removed' — covers mislabeling, currency-string, and duplicate-row issues. |
| Reports revenue per visitor per site in line with reference values. | yes | A: Q1 EUR1.52, Q2 EUR1.57 (avg ~1.55 matches reference); B: EUR1.10 flat both quarters; C: Q1 EUR1.25, Q2 EUR1.34 — all match reference values within rounding. |
| Compares with both EUR1.60 target and EUR1.35 kill criterion; verdict reshaped/open with weak/medium strength. | yes | 'Verdict: open — mixed; evidence strength: weak' with A 'tracking toward the EUR1.60 target' and C 'sits just under the EUR1.35 kill criterion'. |
| Notes two refurbished sites and one post-refurb quarter at C are too few to generalise to 12 centres, names what would settle it. | yes | 'Pilot is only 2 refurbished sites; board case rests on generalising to all 12 centres' and 'Need site C's Q3 2026 data' plus 'café manager interviews ... not yet done — still needed.' |
| Notes a possible confounder, using site B's flat Q1→Q2 as control where relevant. | yes | Finding #3 uses B's flat EUR1.10/EUR1.10 as control 'confirming the uplift isn't just a market-wide trend'; open question #2 flags 'layout, location, local footfall mix' as a possible confounder between sites A and C. |
| Writes h2-cafe-uplift.md in skill format, updates H2 status in 02-hypotheses.md, and adds a line to 00-status.md. | NO | h2-cafe-uplift.md and 00-status.md are shown updated, and the agent's own summary says only 'workplan row 2 and status log updated' — 02-hypotheses.md is never mentioned as edited and its content/diff is absent from the 'Files written by the run' list. |
| States the so-what for the EUR4.2m decision. | yes | 00-status.md: 'Biggest open risk: the revenue-per-visitor uplift from refurbished cafés is unproven' and research doc: 'before the board case can rely on this uplift.' |
| Does not report site A totals including the duplicate row (76,000 visitors or EUR118,400). | yes | Duplicate Q2 row explicitly 'treated as a duplicate and removed (not double-counted)'; no mention of 76,000 visitors or EUR118,400. |

## Transcript

## Turn 1

**User:** Marlow: the till data is in. Do the next research piece. (Attached in the working directory: engagement/marlow/.)

Done — H2 analysis written to `engagement/marlow/research/h2-cafe-uplift.md`, workplan row 2 and status log updated.

**Result is mixed, not a clean confirm:** after cleaning the till data (fixed a mislabeled site, a hand-typed currency string, and a duplicate row), Site A (refurbished Jan 2026) is tracking toward the €1.60 target (€1.52 → €1.57 per visitor across Q1/Q2), but Site C (refurbished Apr 2026) is at €1.34 in its first post-refurb quarter — just under the €1.35 kill criterion. The unrefurbished control site B stayed flat at €1.10, confirming the uplift isn't just a market-wide trend.

Given it's a 2-site pilot with only one quarter of post-refurb data for C, I didn't force a confirm/kill verdict — flagged it as open, with two concrete next steps already in the workplan: café manager interviews (why does A outperform C?) and Site C's Q3 data to see if it's still ramping up like A did.


## Files in work dir after run

- engagement/marlow/00-status.md
- engagement/marlow/01-problem-statement.md
- engagement/marlow/02-hypotheses.md
- engagement/marlow/04-workplan.md
- engagement/marlow/data/cafe-tills-2026h1.csv
- engagement/marlow/research/h1-visitor-numbers.md
- engagement/marlow/research/h2-cafe-uplift.md

## File written by the run: engagement/marlow/00-status.md

# Engagement status: Marlow Garden Centres, café refurbishment programme

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-04 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v1 | EM | passed |
| Plan | Workplan | v1 | EM | passed |
| Analyse | Analyses per branch | 1.5 of 3 done | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 9 December 2026 | | | |

**Current best answer (v1):** Refurbish cafés in all 12 centres from 2027; payback under four years.
**Biggest open risk:** the revenue-per-visitor uplift from refurbished cafés is unproven.
**Log:**
- 2026-10-02: H1 confirmed (visitor numbers stable, see research/h1-visitor-numbers.md).
- 2026-10-09: till data for the three pilot sites received from finance, saved to data/cafe-tills-2026h1.csv. Not yet analysed.
- 2026-10-14: H2 till data analysed (see research/h2-cafe-uplift.md). Mixed result — site A tracking toward EUR 1.60 target, site C sits just under the EUR 1.35 kill criterion in its first post-refurb quarter. Not confirmed or killed; café manager interviews still needed, plus one more quarter of site C data.


## File written by the run: engagement/marlow/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Footfall trend | footfall counters | research/h1-visitor-numbers.md | analyst | 2026-10-02 | done |
| 2 | H2 | Revenue per visitor, refurbished vs not | data/cafe-tills-2026h1.csv, café manager interviews | research/h2-cafe-uplift.md | analyst | 2026-10-16 | till data analysed; interviews still needed |
| 3 | H3 | Cost per centre | contractor quotes | research/h3-refurb-cost.md | analyst | 2026-10-23 | waiting for quotes |


## File written by the run: engagement/marlow/research/h2-cafe-uplift.md

# Research: H2 café revenue uplift, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60.
**Kill criterion:** below EUR 1.35 per visitor after refurbishment.
**Verdict:** open — mixed; **evidence strength:** weak (pilot, n=2 refurbished sites, 1-2 quarters of post-refurb data each)
**So what:** one of two refurbished pilot sites is tracking toward the EUR 1.60 target; the other sits just under the kill criterion in its first quarter post-refurb. Too early to confirm or kill — need the next 1-2 quarters of data (especially site C, and interviews on why A and C differ) before the board case can rely on this uplift.

## Data notes
Source file `data/cafe-tills-2026h1.csv` had three issues, corrected before analysis:
- Site B's Q1 row was labelled `site b` (lower case) and revenue was hand-typed as text (`"EUR 26.4k"`, i.e. EUR 26,400) rather than a number.
- Site A's Q2 row appeared twice, identical, flagged "re-export" — treated as a duplicate and removed (not double-counted).
- Site A refurbished January 2026, so both 2026 quarters are post-refurb. Site C refurbished 1 April 2026, so its Q1 is pre-refurb (baseline) and Q2 is its first post-refurb quarter. Site B was never refurbished and serves as the control.

## Findings
| # | Claim | Source | Date | Document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site A (refurbished Jan 2026) revenue per visitor: Q1 EUR 1.52, Q2 EUR 1.57, rising | Marlow café till export | 2026-10 | cafe-tills-2026h1.csv | data | supports | medium |
| 2 | Site C (refurbished 1 Apr 2026) revenue per visitor: Q1 (pre-refurb) EUR 1.25, Q2 (post-refurb) EUR 1.34 | Marlow café till export | 2026-10 | cafe-tills-2026h1.csv | data | contradicts (below EUR 1.35 kill criterion) | medium |
| 3 | Site B (unrefurbished control) revenue per visitor: Q1 EUR 1.10, Q2 EUR 1.10, flat | Marlow café till export | 2026-10 | cafe-tills-2026h1.csv | data | supports (confirms non-refurbished baseline is flat, so A and C's gains aren't a market-wide effect) | medium |
| 4 | Blended post-refurb revenue per visitor across A+C (EUR 1.49) is 35% above the B control (EUR 1.10) over the same period | Marlow café till export, analyst calculation | 2026-10 | cafe-tills-2026h1.csv | data | supports | weak (small base) |

## Open questions before this can move to confirmed/killed
1. Is site C's EUR 1.34 a ramp-up effect (its first quarter open, cf. site A's own Q1-to-Q2 rise) or a genuine shortfall? Need site C's Q3 2026 data.
2. Why does site A outperform site C at the same refurbishment stage — layout, location, local footfall mix? Café manager interviews (per workplan) not yet done — still needed.
3. Pilot is only 2 refurbished sites; board case rests on generalising to all 12 centres.

