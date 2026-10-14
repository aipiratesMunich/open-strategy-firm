# ra-03-resume-messy-data on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: reads 00-status.md, 02-hypotheses.md and 04-workplan.md before analysing, and names H2 (workplan row 2) as the branch. | yes | Output content matches those files exactly (hypothesis wording, kill criteria, workplan row structure) and explicitly states 'H2 research is done' and 'Updated 02-hypotheses.md, 04-workplan.md, and 00-status.md to log this.' |
| Must not: ask for the hypothesis, kill criterion or problem statement again, or restart the engagement. | yes | The run proceeds directly into till-data analysis and file updates with no request to re-supply the hypothesis, kill criterion, or problem statement. |
| Must: finds and handles P1, P2 and P3 explicitly (each mentioned in the output). | yes | 'Data cleaning' section lists all three: lowercase `site b` label, revenue stored as text (`"EUR 26.4k"`), and the duplicated Site A Q2 row ('re-export' comment), each handled before analysis. |
| Must: reports revenue per visitor per site in line with the reference values (rounding to two decimals accepted). | yes | Site A EUR 1.52/1.57 (~1.55), Site B flat EUR 1.10 both quarters, Site C EUR 1.25 before → EUR 1.34 after — matches reference values closely. |
| Must: compares the result with both the EUR 1.60 target and the EUR 1.35 kill criterion and gives the verdict reshaped or open (not confirmed), with weak or medium strength. | yes | 'Verdict: open — split result; evidence strength: weak' with explicit comparisons: 'EUR 1.34 < EUR 1.35' and 'EUR 0.11 short of the EUR 1.60 target'. |
| Must: notes that two refurbished sites and one quarter after refurbishment at site C are too few to generalise to 12 centres, and names what would settle it (e.g. more months at site C, café manager interviews, comparable refurbishments elsewhere) without inventing a benchmark. | yes | 'Only one data family is in hand... it is a single pilot pair with one real before/after site'; names Site C Q3 data and café manager interviews as what would settle it; explicitly declines to invent an outside benchmark ('should not be invented'). |
| Must: notes a possible confounder (e.g. site A may differ from B and C in size, location or season), using site B's flat Q1 to Q2 as the control where relevant. | yes | Finding #2 uses Site B as control ('rules out a quarter-on-quarter seasonal effect'); Counter-evidence notes Site A's level 'cannot be distinguished from Site A always ran above the EUR 1.10 group average, refurbished or not'. |
| Must: writes engagement/marlow/research/h2-cafe-uplift.md (or prints it under that heading) in the skill's output format, updates the H2 status in 02-hypotheses.md and adds a line to 00-status.md. | yes | All three files shown with appropriate content: h2-cafe-uplift.md in full skill format, H2 row status 'open — split result, see research/h2-cafe-uplift.md', and a 2026-10-14 log entry in 00-status.md. |
| Must: states the so-what for the EUR 4.2m decision (e.g. the all-centres answer is at risk; the business case should run at EUR 1.35 to 1.55, not EUR 1.60). | yes | 'The board case should not lock in EUR 1.60... the model should be stress-tested at EUR 1.35-1.49, not EUR 1.60,' tied to the all-12-centres current answer logged in 00-status.md. |
| Must not: report site A totals including the duplicate row (76,000 visitors or EUR 118,400). | yes | Duplicate explicitly removed: 'Treated as one duplicated observation, not two; counted once'; reported figures are per-visitor rates (EUR 1.52/1.57), not inflated totals. |

## Transcript

## Turn 1

**User:** Marlow: the till data is in. Do the next research piece. (Attached in the working directory: engagement/marlow/.)

**H2 research is done** (`research/h2-cafe-uplift.md`), but the verdict is **open, not confirmed** — this is the key thing to flag:

- The till export had three cleanup issues first: Site B's row used lowercase `site b` and stored revenue as text (`"EUR 26.4k"`), and Site A's Q2 row was duplicated (`re-export` comment) — deduplicated before any math.
- **Site C** is the only site with a genuine own-site before/after reading: EUR 1.25 → EUR 1.34 per visitor. That's a real uplift, but it lands *just below* the EUR 1.35 kill criterion.
- **Site A** looks much stronger (EUR 1.52–1.57) but was refurbished before the export window starts, so there's no pre-refurbishment baseline for it in this data — its level can't yet be attributed to the refurbishment.
- Pooled across post-refurb quarters: **EUR 1.49/visitor** — clear of the kill line, but EUR 0.11 short of the EUR 1.60 target used in the board case.

Updated `02-hypotheses.md`, `04-workplan.md`, and `00-status.md` to log this. Next step per the workplan: café manager interviews (not yet done) and Site C's Q3 data, before the board model should rely on EUR 1.60 rather than something closer to EUR 1.35–1.49. H3 (refurb cost) is still waiting on contractor quotes.


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
| Analyse | Analyses per branch | 1.5 of 3 done (H2 open, needs interviews) | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 9 December 2026 | | | |

**Current best answer (v1):** Refurbish cafés in all 12 centres from 2027; payback under four years.
**Biggest open risk:** the revenue-per-visitor uplift from refurbished cafés is unproven.
**Log:**
- 2026-10-02: H1 confirmed (visitor numbers stable, see research/h1-visitor-numbers.md).
- 2026-10-09: till data for the three pilot sites received from finance, saved to data/cafe-tills-2026h1.csv. Not yet analysed.
- 2026-10-14: H2 till data analysed, see research/h2-cafe-uplift.md. Verdict open, not confirmed: Site C (the only site with a real before/after reading) comes out at EUR 1.34 per visitor, just below the EUR 1.35 kill line; Site A looks stronger (EUR 1.52-1.57) but has no pre-refurbishment baseline in the data to attribute that to the refurb. Pooled post-refurb average is EUR 1.49. Needs Site C's Q3 data and the café manager interviews (still outstanding) before this can be confirmed or killed. Biggest open risk is unchanged but now sharper: do not use EUR 1.60 in the board model yet.


## File written by the run: engagement/marlow/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

**Current answer (v1, 2026-09-18):** Refurbish cafés in all 12 centres from 2027.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Visitor numbers per centre stay at or above the 2025 level through 2028 | medium | low | footfall counters 2022-2026 | visitors fall more than 5% a year | confirmed 2026-10-02 |
| H2 | A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60 | high | high | pilot till data (sites A and C refurbished, B not), comparable sites | below EUR 1.35 per visitor after refurbishment | open — split result, see research/h2-cafe-uplift.md |
| H3 | Refurbishment costs no more than EUR 350k per centre | medium | medium | two contractor quotes | quotes above EUR 420k per centre | open |


## File written by the run: engagement/marlow/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Footfall trend | footfall counters | research/h1-visitor-numbers.md | analyst | 2026-10-02 | done |
| 2 | H2 | Revenue per visitor, refurbished vs not | data/cafe-tills-2026h1.csv, café manager interviews | research/h2-cafe-uplift.md | analyst | 2026-10-16 | till data done, open; interviews still needed |
| 3 | H3 | Cost per centre | contractor quotes | research/h3-refurb-cost.md | analyst | 2026-10-23 | waiting for quotes |


## File written by the run: engagement/marlow/research/h2-cafe-uplift.md

# Research: H2 café revenue uplift, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60.
**Kill criterion:** below EUR 1.35 per visitor after refurbishment.
**Verdict:** open — split result; **evidence strength:** weak
**So what:** the one site with a genuine before/after comparison (C) sits right on the EUR 1.35 kill line, not near the EUR 1.60 target; the site that looks strong (A) has no pre-refurbishment data point to attribute its level to the refurbishment. The board case should not lock in EUR 1.60 before Site C's next quarter and the café manager interviews land, and the model should be stress-tested at EUR 1.35-1.49, not EUR 1.60.

## Data cleaning
`data/cafe-tills-2026h1.csv` (finance export, received 2026-10-09) had three issues, corrected before analysis:
- Site B's Q1 row was labelled `site b` (not `B`) and revenue was stored as text, `"EUR 26.4k"` — read as 26,400.
- The Site A Q2 row appears twice, identical in every field except a comment reading `re-export`. Treated as one duplicated observation, not two; counted once.
- Six underlying observations remain after dedup: A×2 quarters, B×2, C×2.

## Findings
| # | Claim (EUR per visitor, 2026 H1) | Source | Date | Document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site A (refurbished Jan 2026, before the export window starts): EUR 1.52 (Q1), EUR 1.57 (Q2) — both quarters post-refurbishment | Marlow till export | 2026 H1 | cafe-tills-2026h1.csv | data | supports | weak (no own-site baseline, see Assumptions) |
| 2 | Site B (not refurbished, control): flat at EUR 1.10 in both quarters, even though visitors rose 24,000 → 28,000 | Marlow till export | 2026 H1 | cafe-tills-2026h1.csv | data | supports (rules out a quarter-on-quarter seasonal effect as the explanation for A/C's higher figures) | medium |
| 3 | Site C (refurbished 1 April 2026): EUR 1.25 before refurbishment (Q1) → EUR 1.34 after (Q2), a +6.9% rise | Marlow till export | 2026 H1 | cafe-tills-2026h1.csv | data | contradicts the kill criterion (EUR 1.34 < EUR 1.35), though it is a genuine own-site before/after reading | strong as a reading, weak as a verdict basis (1 quarter, right at the ramp-up point) |
| 4 | Pooled average across all post-refurbishment quarters (A Q1, A Q2, C Q2): EUR 1.49 per visitor | Marlow till export, author's calculation | 2026 H1 | cafe-tills-2026h1.csv | data | partially supports — clear of the EUR 1.35 kill line, EUR 0.11 short of the EUR 1.60 target | weak (mixes a site with no baseline into the average) |

## Triangulation of decisive claims
| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Refurbishment lifts revenue per visitor | Till data, own-site before/after (Site C only) | Café manager interviews (workplan row 2) | would be independent | not yet triangulated — interviews not done | weak until interviews land |

Only one data family is in hand. The till data alone cannot confirm or kill H2 with confidence; it is a single pilot pair with one real before/after site.

## Outside view
No external reference class sourced for this branch. A useful one — revenue-per-visitor uplift from café refurbishments at comparable UK garden-centre or farm-shop retailers — was not requested from the user and should not be invented; see Data requests.

## Counter-evidence
- Site C's Q1→Q2 visitor count rose 13,000 → 28%→38% faster than Site B's rise over the same two quarters (24,000 → 28,000, +17%). A post-refurbishment novelty surge in footfall, not higher spend per head from existing customers, could be diluting the per-visitor figure at C — the true steady-state uplift could be higher than EUR 1.34 once the novelty visitors' lower average spend washes out, or lower if they are one-off lookers who stop returning.
- Site A's apparent EUR 1.52-1.57 level cannot be distinguished from "Site A always ran above the EUR 1.10 group average, refurbished or not" — there is no pre-refurbishment reading for A anywhere in the data provided, so attributing its level to the refurbishment is not yet supported by this export.
- Site C's own pre-refurbishment reading (EUR 1.25) was already above the EUR 1.10 figure used as the hypothesis's starting point, which weakens the EUR 1.10 figure as a reliable base rate for individual sites.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Site A's pre-refurbishment revenue per visitor | missing — refurbished before the export window opens | assumed EUR 1.10 (group baseline), unverified for A specifically | A's till data from before January 2026, if it exists | finance |
| Site C's post-refurbishment ramp-up | unverified | one quarter only; steady-state could sit above or below EUR 1.34 | Site C's Q3 2026 till data | finance |
| Café manager explanation of the gap between A and C | missing | — | café manager interviews (workplan row 2) | analyst |

## Data requests
| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Site A till data, second half of 2025 (pre-refurbishment) | csv/export, same fields | Settles whether claim 1 (A's EUR 1.52-1.57) is a refurbishment effect or A's normal level | Keep claim 1 at weak strength; do not use A alone to confirm H2 | finance |
| Site C till data, Q3 2026 | csv/export, same fields | Tests whether claim 3's EUR 1.34 was a ramp-up dip or the steady state | Hold the kill-criterion test open past the 2026-10-16 due date | finance |
| Café manager interviews at A, B, C | interview notes | Qualitative read on what is driving the A/C gap (layout, menu, staffing, local footfall mix) | Proceed on till data alone at weak strength | analyst |

