# ra-03-resume-messy-data on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md and 04-workplan.md before analysing, and names H2 (workplan row 2) as the branch | yes | Output references 'workplan row 2's other source', updates 'the workplan and status log accordingly', and the hypothesis/kill-criterion text in h2-cafe-uplift.md matches what would be defined in 02-hypotheses.md |
| Does not ask for the hypothesis, kill criterion or problem statement again, or restart the engagement | yes | Assistant proceeds directly to analysis and writes findings; no re-request of prior artefacts |
| Finds and handles P1, P2 and P3 explicitly | yes | 'the CSV had three issues: site B's row used lowercase "site b" and revenue as the string "EUR 26.4k"...; the last row was an exact duplicate...' all three repeated and fixed in the 'Data cleaning notes' section |
| Reports revenue per visitor per site in line with reference values | yes | A: EUR1.52/EUR1.57 (avg ~1.55); B: EUR1.10 both quarters; C: EUR1.25 pre, EUR1.34 post — matches reference values |
| Compares result with EUR1.60 target and EUR1.35 kill criterion, verdict reshaped/open with weak/medium strength | yes | 'Verdict: open; evidence is mixed — not confirmed, not killed. Evidence strength: weak' |
| Notes sample too small (two refurbished sites, one quarter post-refurb at C) to generalise to 12 centres, names what would settle it | yes | 'cannot yet underwrite the EUR 1.60 case-wide assumption' plus 'café manager interviews... are needed before this can be confirmed or killed' and noting C's 'one post-refurb quarter' may be ramp-up |
| Notes a possible confounder using site B's flat Q1→Q2 as control | yes | 'Control site B holds steady at EUR 1.10/visitor across both quarters despite visitor numbers rising... not materially seasonal' and 'whether A and C differ in format, location, or local competition' |
| Writes h2-cafe-uplift.md, updates H2 status in 02-hypotheses.md, adds line to 00-status.md | NO | Only 00-status.md, 04-workplan.md, and h2-cafe-uplift.md appear under 'File written by the run'; no corresponding write/update shown for 02-hypotheses.md despite it being in the working directory |
| States the so-what for the EUR 4.2m decision | yes | 'cannot yet underwrite the EUR 1.60 case-wide assumption' — equivalent to 'the all-centres answer is at risk' |
| Does not report site A totals including the duplicate row (76,000 visitors or EUR 118,400) | yes | Site A Q2 reported as 28,000 visitors / EUR 44,000, duplicate explicitly dropped, no 76,000/118,400 figures appear |

## Transcript

## Turn 1

**User:** Marlow: the till data is in. Do the next research piece. (Attached in the working directory: engagement/marlow/.)

I analysed the pilot till data for H2 (café revenue uplift) and wrote it up in `research/h2-cafe-uplift.md`.

**Data cleaning first** — the CSV had three issues: site B's row used lowercase "site b" and revenue as the string "EUR 26.4k" instead of a number; the last row was an exact duplicate of site A's Q2 record (flagged "re-export") and had to be dropped rather than summed.

**Result: mixed, not confirmed/not killed.**
- Site A (refurbished Jan 2026, both quarters post-refurb): EUR 1.52–1.57/visitor — approaching the EUR 1.60 target.
- Site C (refurbished 1 Apr 2026): rose from EUR 1.25 pre-refurb to EUR 1.34 post-refurb — just **below** the EUR 1.35 kill line.
- Site B (control, never refurbished): flat at EUR 1.10/visitor both quarters, which is useful as a seasonality check — visitor volume rose but spend/visitor didn't move.

The gap between A and C is the key open question — likely explained by C only having one post-refurb quarter (possible ramp-up) versus A's two, but that needs the café manager interviews (workplan row 2's other source) to resolve. I've updated the workplan and status log accordingly: H2 analysis is "till data analysed, interviews outstanding," not done.

Next piece per the workplan is H3 (refurbishment cost per centre), still waiting on contractor quotes — let me know when those land, or if you'd like me to proceed with the café manager interview guide for H2 instead.


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
| Analyse | Analyses per branch | 1 of 3 done, 1 in progress | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 9 December 2026 | | | |

**Current best answer (v1):** Refurbish cafés in all 12 centres from 2027; payback under four years.
**Biggest open risk:** the revenue-per-visitor uplift from refurbished cafés is unproven.
**Log:**
- 2026-10-02: H1 confirmed (visitor numbers stable, see research/h1-visitor-numbers.md).
- 2026-10-09: till data for the three pilot sites received from finance, saved to data/cafe-tills-2026h1.csv. Not yet analysed.
- 2026-10-14: till data analysed (research/h2-cafe-uplift.md). Mixed result — site A tracking close to the EUR 1.60 target (EUR 1.52-1.57/visitor), site C tracking close to the EUR 1.35 kill line (EUR 1.34/visitor, one quarter post-refurb). H2 stays open; café manager interviews still needed before confirming or killing.


## File written by the run: engagement/marlow/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Footfall trend | footfall counters | research/h1-visitor-numbers.md | analyst | 2026-10-02 | done |
| 2 | H2 | Revenue per visitor, refurbished vs not | data/cafe-tills-2026h1.csv, café manager interviews | research/h2-cafe-uplift.md | analyst | 2026-10-16 | till data analysed, interviews outstanding |
| 3 | H3 | Cost per centre | contractor quotes | research/h3-refurb-cost.md | analyst | 2026-10-23 | waiting for quotes |


## File written by the run: engagement/marlow/research/h2-cafe-uplift.md

# Research: H2 café revenue uplift, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60.
**Kill criterion:** below EUR 1.35 per visitor after refurbishment.
**Verdict:** open; evidence is mixed — **not confirmed, not killed**. **Evidence strength:** weak (one half-year, three sites, no pre-refurb baseline for site A).
**So what:** cannot yet underwrite the EUR 1.60 case-wide assumption. Site A is tracking close to target; site C is tracking close to the kill line. Café manager interviews (workplan row 2, still outstanding) are needed before this can be confirmed or killed.

## Data cleaning notes

Source file `data/cafe-tills-2026h1.csv` needed cleaning before analysis:
- Site B's row was entered as "site b" with revenue written as the string "EUR 26.4k" — normalised to site `B`, revenue EUR 26,400.
- The last row (site A, 2026-Q2, flagged "re-export") duplicates the earlier A/2026-Q2 row exactly (28,000 visitors / EUR 44,000) — treated as a duplicate export and dropped, not summed.
- Refurbishment timing per the file header: site A refurbished January 2026 (so both 2026 quarters are post-refurb, no pre-refurb baseline in this dataset); site C refurbished 1 April 2026 (Q1 pre-refurb, Q2 post-refurb); site B not refurbished (control).

## Revenue per visitor, cleaned

| Site | Quarter | Visitors | Café revenue | Revenue/visitor | Refurb status |
|---|---|---|---|---|---|
| A | 2026-Q1 | 20,000 | EUR 30,400 | EUR 1.52 | post (refurbished Jan 2026) |
| A | 2026-Q2 | 28,000 | EUR 44,000 | EUR 1.57 | post |
| B | 2026-Q1 | 24,000 | EUR 26,400 | EUR 1.10 | control, not refurbished |
| B | 2026-Q2 | 28,000 | EUR 30,800 | EUR 1.10 | control, not refurbished |
| C | 2026-Q1 | 13,000 | EUR 16,250 | EUR 1.25 | pre-refurb |
| C | 2026-Q2 | 18,000 | EUR 24,050 | EUR 1.34 | post (refurbished 1 Apr 2026) |

## Findings
| # | Claim | Source | Date | Document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Control site B holds steady at EUR 1.10/visitor across both quarters despite visitor numbers rising 24,000 → 28,000 — café spend per visitor is not materially seasonal at this site | Marlow till export | 2026-10-09 | cafe-tills-2026h1.csv | data | context | medium |
| 2 | Site A (post-refurb both quarters) runs EUR 1.52–1.57/visitor, EUR 0.42–0.47 above the control — approaching but not yet reaching the EUR 1.60 target | Marlow till export | 2026-10-09 | cafe-tills-2026h1.csv | data | partially supports | weak (2 quarters, 1 site, no pre-refurb comparator) |
| 3 | Site C rises from EUR 1.25 (pre-refurb) to EUR 1.34 (post-refurb, one quarter in) — an uplift, but the post-refurb level sits just below the EUR 1.35 kill line | Marlow till export | 2026-10-09 | cafe-tills-2026h1.csv | data | partially contradicts | weak (1 quarter post-refurb, likely includes ramp-up) |
| 4 | Site C's pre-refurb baseline (EUR 1.25) is already above site B's control level (EUR 1.10) — sites are not directly comparable, so cross-site comparison understates true uplift if used as the only check | Marlow till export | 2026-10-09 | cafe-tills-2026h1.csv | data | caveat | weak |

## Open question for café manager interviews
Site A is outperforming site C by a wide margin on the same refurbishment programme. Before treating either figure as representative, interviews should check: (a) whether C's one post-refurb quarter includes a ramp-up period (new menu, staff training) that A's two quarters do not; (b) whether A and C differ in format, location, or local competition in ways that would make a single case-wide uplift assumption wrong.

