# ra-03-resume-messy-data on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md and 04-workplan.md before analysing, and names H2 as the branch | yes | Response opens with 'H2 is not resolved — it's genuinely split' and the updated files reproduce prior structure/wording exactly (e.g. workplan row 2 = H2, hypothesis kill-criterion phrasing), consistent with having read them first. |
| Does not ask for hypothesis/kill criterion/problem statement again or restart engagement | yes | The run proceeds directly to analysis and write-up with no clarifying questions or restart. |
| Finds and handles P1, P2, P3 explicitly | yes | Data cleaning table lists all three: duplicate row, inconsistent site naming ('site b' vs 'B'), and revenue entered as text ('EUR 26.4k'); also restated in the chat reply. |
| Reports revenue per visitor per site in line with reference values | yes | A: EUR 1.52/1.57 (avg ~1.55); B: EUR 1.10 both quarters; C: EUR 1.25 pre, EUR 1.34 post — matches reference figures. |
| Compares to both EUR 1.60 target and EUR 1.35 kill criterion; verdict open/reshaped with weak/medium strength | yes | 'Verdict: open — evidence contradictory between the two pilot sites; evidence strength: weak', with explicit comparisons to both thresholds throughout. |
| Notes two refurbished sites / one quarter at C too few to generalise to 12 centres, names what would settle it without inventing a benchmark | yes | 'needed to explain the A/C gap before this can support a 12-centre rollout'; asks for site C Q3 data and manager interviews; outside view explicitly flags 'not checked... do not assume Marlow's result is typical'. |
| Notes a possible confounder, using site B's flat trend as control where relevant | yes | Findings table calls B 'not refurbished, control' with flat EUR1.10 both quarters; gaps table flags 'Causes behind the A/C gap (layout, location, local footfall mix, management)' as unexplained. |
| Writes h2-cafe-uplift.md in skill format, updates H2 status in 02-hypotheses.md, adds line to 00-status.md | yes | All three files shown with consistent, updated content (status table log entry dated 2026-10-14, hypothesis H2 row updated to 'open — mixed...'). |
| States the so-what for the investment decision (all-centres answer at risk / revised range) | yes | 00-status.md: 'Biggest open risk: the revenue-per-visitor uplift from refurbished cafés is unproven' directly under 'Current best answer: Refurbish cafés in all 12 centres from 2027'; research doc: 'The board case cannot rest on H2 as confirmed'. |
| Does not report site A totals including the duplicate row (76,000 visitors / EUR 118,400) | yes | Duplicate 'A, 2026-Q2' row explicitly deduplicated ('counted once'); no such inflated totals appear anywhere in output. |

## Transcript

## Turn 1

**User:** Marlow: the till data is in. Do the next research piece. (Attached in the working directory: engagement/marlow/.)

**H2 is not resolved — it's genuinely split.** After cleaning the till data (one duplicate row, inconsistent site naming, revenue entered as text), the two refurbished pilot sites disagree:

- **Site A** (refurbished Jan 2026): EUR 1.52–1.57/visitor across both quarters — a real uplift over the EUR 1.10 control baseline, but short of the EUR 1.60 target.
- **Site C** (refurbished 1 Apr 2026): EUR 1.34/visitor in its first post-refurb quarter — **below the EUR 1.35 kill criterion**, on only one quarter of data, up from a pre-refurb EUR 1.25.

Written up in `engagement/marlow/research/h2-cafe-uplift.md` with full findings, triangulation, counter-evidence and data gaps. Updated `02-hypotheses.md`, `04-workplan.md`, and `00-status.md` to reflect this.

**Next, in order of impact:**
1. Café manager interviews at sites A and C (already in the workplan, not yet done) — needed to explain the A/C gap before this can support a 12-centre rollout.
2. Site C's Q3 till data — one quarter isn't enough to tell a ramp-up effect from a real result sitting on the kill line.
3. H3 (refurbishment cost) is still waiting on contractor quotes, due 2026-10-23.

Also flagged: the status table claims the Structure-phase ghost deck gate passed, but `03-ghost-deck.md` isn't on disk — worth recreating before the next partner gate, though it doesn't block this piece of work.


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
| Analyse | Analyses per branch | 1 of 3 done, 1 of 3 in progress | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 9 December 2026 | | | |

**Current best answer (v1):** Refurbish cafés in all 12 centres from 2027; payback under four years.
**Biggest open risk:** the revenue-per-visitor uplift from refurbished cafés is unproven, and the two pilot sites disagree — site A shows a real but below-target uplift, site C sits right at the kill criterion on one quarter of data.
**Log:**
- 2026-10-02: H1 confirmed (visitor numbers stable, see research/h1-visitor-numbers.md).
- 2026-10-09: till data for the three pilot sites received from finance, saved to data/cafe-tills-2026h1.csv. Not yet analysed.
- 2026-10-14: till data analysed (see research/h2-cafe-uplift.md). H2 not confirmed or killed — site A: EUR 1.52-1.57/visitor (above kill, below EUR 1.60 target); site C: EUR 1.34/visitor after refurbishment (below the EUR 1.35 kill criterion, one quarter only). Need: site A pre-refurb baseline, site C Q3 data, café manager interviews at both sites before this can go in the deck. Also noted: 03-ghost-deck.md referenced as "passed" in this status table but not present on disk — needs recreating before the next partner gate.


## File written by the run: engagement/marlow/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

**Current answer (v1, 2026-09-18):** Refurbish cafés in all 12 centres from 2027.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Visitor numbers per centre stay at or above the 2025 level through 2028 | medium | low | footfall counters 2022-2026 | visitors fall more than 5% a year | confirmed 2026-10-02 |
| H2 | A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60 | high | high | pilot till data (sites A and C refurbished, B not), comparable sites | below EUR 1.35 per visitor after refurbishment | open — mixed: site A EUR 1.52-1.57 (below target, above kill), site C EUR 1.34 (below kill, one quarter only); see research/h2-cafe-uplift.md |
| H3 | Refurbishment costs no more than EUR 350k per centre | medium | medium | two contractor quotes | quotes above EUR 420k per centre | open |


## File written by the run: engagement/marlow/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Footfall trend | footfall counters | research/h1-visitor-numbers.md | analyst | 2026-10-02 | done |
| 2 | H2 | Revenue per visitor, refurbished vs not | data/cafe-tills-2026h1.csv, café manager interviews | research/h2-cafe-uplift.md | analyst | 2026-10-16 | till data analysed, result mixed; café manager interviews still needed |
| 3 | H3 | Cost per centre | contractor quotes | research/h3-refurb-cost.md | analyst | 2026-10-23 | waiting for quotes |


## File written by the run: engagement/marlow/research/h2-cafe-uplift.md

# Research: H2 café revenue-per-visitor uplift, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60.
**Kill criterion:** below EUR 1.35 per visitor after refurbishment.
**Verdict:** open — evidence contradictory between the two pilot sites; **evidence strength:** weak
**So what:** one pilot site (A) shows a real uplift but short of target; the other (C) sits right at the kill threshold on only one quarter of post-refurb data. The board case cannot rest on H2 as confirmed; need at least one more quarter from site C and an explanation for the A/C gap before this goes into the deck.

## Data cleaning applied to `data/cafe-tills-2026h1.csv`
| Issue found | Resolution |
|---|---|
| Row "A, 2026-Q2, 28000, 44000" appears twice, second marked "re-export" | Treated as a duplicate upload; counted once |
| Site labelled "site b" in one row, "B" elsewhere | Normalised to site B |
| B/Q1 revenue entered as text "EUR 26.4k" | Parsed as EUR 26,400 |

## Findings
| # | Claim | Source | Date | Document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site A (refurbished Jan 2026): EUR 1.52/visitor in Q1, EUR 1.57/visitor in Q2 | Marlow café till export | 2026-10-09 | data/cafe-tills-2026h1.csv | data | supports (uplift real, but below EUR 1.60 target both quarters) | medium |
| 2 | Site B (not refurbished, control): EUR 1.10/visitor in both Q1 and Q2 | Marlow café till export | 2026-10-09 | data/cafe-tills-2026h1.csv | data | neutral — validates the EUR 1.10 baseline used in H2 | strong |
| 3 | Site C pre-refurbishment (Q1): EUR 1.25/visitor | Marlow café till export | 2026-10-09 | data/cafe-tills-2026h1.csv | data | n/a — baseline for C, already above the EUR 1.10 group baseline before any refurbishment | medium |
| 4 | Site C post-refurbishment (Q2, refurbished 1 Apr): EUR 1.34/visitor | Marlow café till export | 2026-10-09 | data/cafe-tills-2026h1.csv | data | contradicts — below the EUR 1.35 kill criterion | weak (one quarter only, possible ramp-up effect) |

## Triangulation of decisive claims
| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| EUR 1.10 group baseline used in H2 | Stated in hypothesis (02-hypotheses.md, set before data) | Measured directly from control site B, both quarters, in the till data | yes — hypothesis threshold set before data arrived | EUR 1.10, confirmed | strong |
| Post-refurbishment uplift exists at all | Site A, own quarter-on-quarter trend post-refurb (1.52 → 1.57) | Site A and C both sit above their respective pre-refurb/control levels | partially — same dataset, but two different sites and comparison bases | some uplift present, magnitude ranges EUR +0.09 (C) to +0.45 (A, vs. control) | medium |

No second, independent data source (e.g. café manager interviews) is in hand yet — see data requests below. Until that arrives, triangulation rests entirely on one till export.

## Outside view
| Forecast | Reference class | Range achieved | Where this case sits and why |
|---|---|---|---|
| Café refurbishment revenue-per-visitor uplift | Comparable garden centre or retail café refits | not checked — no web access this session | Cannot be stated without external benchmarking; flag as a check still to do, do not assume Marlow's result is typical |

## Counter-evidence
Site C is itself the counter-evidence: one full quarter after refurbishment, revenue per visitor (EUR 1.34) is barely above its own pre-refurb level (EUR 1.25) and below the kill criterion. If this holds over a second quarter, H2 would be killed on the C evidence alone, regardless of site A's stronger result. The gap between A (+0.42 to +0.47 over control) and C (+0.09 over own baseline) is unexplained by the till data and is the single biggest risk to the board case.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Site A's pre-refurbishment revenue per visitor | missing — A was refurbished in January 2026, before this data window starts | used site B (control) as a proxy baseline of EUR 1.10 | Marlow finance to pull Q4 2025 till data for site A | analyst |
| Whether site C's Q2 result is a stable level or a ramp-up artefact | unverified | treat EUR 1.34 as provisional, not final | one more quarter of site C till data (Q3 2026) | analyst |
| Why site C's pre-refurb baseline (EUR 1.25) was already above the group baseline (EUR 1.10) | unverified | not explained by till data alone | café manager interview, site C | analyst |
| Causes behind the A/C gap (layout, location, local footfall mix, management) | missing | — | café manager interviews at A and C (already in workplan row 2 as a source, not yet done) | analyst |

## Data requests
| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Site A till data, Q3–Q4 2025 (pre-refurbishment) | same csv export format | gives A a true before/after comparison instead of relying on B as proxy | keep using B as control proxy, widen uncertainty range | finance |
| Site C till data, Q3 2026 | same csv export format | confirms whether EUR 1.34 holds or moves after ramp-up | flag H2 as undecided in the board deck, no Q3 figure to cite | finance |
| Café manager interviews, sites A and C | interview notes (see workplan row 2) | explains the A/C gap — needed before recommending refurbishment at all 12 centres on this evidence | note in deck that uplift driver is not yet understood | analyst |

