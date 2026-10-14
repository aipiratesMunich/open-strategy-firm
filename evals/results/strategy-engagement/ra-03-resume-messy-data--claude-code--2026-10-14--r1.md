# ra-03-resume-messy-data on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: reads 00-status.md, 02-hypotheses.md and 04-workplan.md before analysing, and names H2 (workplan row 2) as the branch. | yes | Response opens with 'H2 (café revenue uplift) — now open with mixed, weak evidence', uses the exact target (EUR 1.60) and kill criterion (EUR 1.35) from the hypothesis, and references workplan row 2 status ('till data done, interviews still outstanding'). |
| Must not: ask for the hypothesis, kill criterion or problem statement again, or restart the engagement. | yes | No re-asking occurs; the run proceeds straight into cleaning the till data and analysing H2. |
| Must: finds and handles P1, P2 and P3 explicitly (each mentioned in the output). | yes | 'Site B's Q1 row was tagged `site b`... had revenue as text (`"EUR 26.4k"`)... the last row was an exact duplicate of site A's Q2 entry — excluded it.' All three defects listed and handled in the Data quality note. |
| Must: reports revenue per visitor per site in line with the reference values (rounding to two decimals accepted). | yes | 'Site B... flat at EUR 1.10/visitor both quarters'; 'Site A... EUR 1.55/visitor across H1'; 'Site C... rose from EUR 1.25 pre-refurb to EUR 1.34 post-refurb' — all match reference values exactly. |
| Must: compares the result with both the EUR 1.60 target and the EUR 1.35 kill criterion and gives the verdict reshaped or open (not confirmed), with weak or medium strength. | yes | 'Verdict: open; evidence mixed and weak — not confirmed, not killed.' Site A described as 'comfortably above the EUR 1.35 kill line, close to the EUR 1.60 target'; site C 'just below the kill criterion'. |
| Must: notes that two refurbished sites and one quarter after refurbishment at site C are too few to generalise to 12 centres, and names what would settle it. | yes | 'Sample is two refurbished sites, one of them with only one post-refurbishment data point — too thin to confirm or kill H2 on its own.' Next steps name café manager interviews and 'H2 2026 till data... to see whether site C's uplift builds in Q3/Q4'. |
| Must: notes a possible confounder (e.g. site A may differ from B and C in size, location or season), using site B's flat Q1 to Q2 as the control where relevant. | NO | The only explanation offered for the A/C gap is ramp-up timing ('site A has had two quarters to ramp... site C has had one'); no mention that site A could simply differ from B/C in size, location, or season — site B is used only as a baseline level, not discussed as a confounder check. |
| Must: writes engagement/marlow/research/h2-cafe-uplift.md in the skill's output format, updates the H2 status in 02-hypotheses.md and adds a line to 00-status.md. | NO | research/h2-cafe-uplift.md and the 00-status.md log line are both present, but 02-hypotheses.md is not listed among 'File written by the run' sections — no evidence its H2 status was updated. |
| Must: states the so-what for the EUR 4.2m decision (e.g. the all-centres answer is at risk; the business case should run at EUR 1.35 to 1.55, not EUR 1.60). | yes | 'So what: cannot yet support the EUR 1.60 assumption in the board paper; current pilot range is EUR 1.34–1.57.' |
| Must not: report site A totals including the duplicate row (76,000 visitors or EUR 118,400). | yes | Site A H1 reported as 'EUR 1.55 per visitor across H1 2026 (74,400/48,000)' — the duplicate-inflated 76,000/118,400 figures do not appear; duplicate explicitly excluded. |

## Transcript

## Turn 1

**User:** Marlow: the till data is in. Do the next research piece. (Attached in the working directory: engagement/marlow/.)

Analysis done. Summary:

**H2 (café revenue uplift) — now open with mixed, weak evidence**, not confirmed or killed:
- Cleaned the till export first: site B's Q1 row was tagged `site b` and had revenue as text (`"EUR 26.4k"`), and the last row was an exact duplicate of site A's Q2 entry — excluded it.
- Site B (control, unrefurbished): flat at EUR 1.10/visitor both quarters — confirms the baseline.
- Site A (refurbished Jan 2026): EUR 1.55/visitor across H1, rising Q1→Q2 — comfortably above the EUR 1.35 kill line, close to the EUR 1.60 target.
- Site C (refurbished April 2026): rose from EUR 1.25 pre-refurb to EUR 1.34 post-refurb — just *below* the kill criterion after only one quarter of post-refurb trading.

The two pilot sites disagree, and site C has had far less time to ramp than site A, so this isn't yet conclusive either way. Wrote this up in `research/h2-cafe-uplift.md`, updated the workplan (till data done, interviews still outstanding) and the status log/biggest-risk line in `00-status.md`.

Next piece per the workplan is H3 (refurb cost per centre), but that's still waiting on contractor quotes — the other live gap is the café manager interviews for H2, which aren't in yet either.


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
| Analyse | Analyses per branch | H2 analysed (open, mixed), H3 waiting on quotes | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 9 December 2026 | | | |

**Current best answer (v1):** Refurbish cafés in all 12 centres from 2027; payback under four years.
**Biggest open risk:** the revenue-per-visitor uplift from refurbished cafés is still unproven — pilot till data gives EUR 1.34–1.57 per visitor, a range that straddles the EUR 1.35 kill criterion, against a EUR 1.60 target. H2 stays open.
**Log:**
- 2026-10-02: H1 confirmed (visitor numbers stable, see research/h1-visitor-numbers.md).
- 2026-10-09: till data for the three pilot sites received from finance, saved to data/cafe-tills-2026h1.csv. Not yet analysed.
- 2026-10-14: till data analysed (see research/h2-cafe-uplift.md). Site A (refurbished Jan 2026) at EUR 1.55/visitor; site C (refurbished Apr 2026) at EUR 1.34/visitor, just below the kill criterion after one quarter. H2 open — mixed, weak evidence; café manager interviews and H2 2026 data still needed.


## File written by the run: engagement/marlow/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Footfall trend | footfall counters | research/h1-visitor-numbers.md | analyst | 2026-10-02 | done |
| 2 | H2 | Revenue per visitor, refurbished vs not | data/cafe-tills-2026h1.csv, café manager interviews | research/h2-cafe-uplift.md | analyst | 2026-10-16 | till data done; interviews still outstanding |
| 3 | H3 | Cost per centre | contractor quotes | research/h3-refurb-cost.md | analyst | 2026-10-23 | waiting for quotes |


## File written by the run: engagement/marlow/research/h2-cafe-uplift.md

# Research: H2 café revenue-per-visitor uplift, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A refurbished café lifts café revenue per visitor from EUR 1.10 to at least EUR 1.60.
**Kill criterion:** below EUR 1.35 per visitor after refurbishment.
**Verdict:** open; evidence mixed and weak — not confirmed, not killed.
**So what:** cannot yet support the EUR 1.60 assumption in the board paper; current pilot range is EUR 1.34–1.57. Café manager interviews and H2 2026 data (due before the next round) are needed before this goes into the final case.

## Data quality note
The till export (`data/cafe-tills-2026h1.csv`) needed cleaning before analysis:
- Site B's Q1 row was labelled `site b` (lowercase, inconsistent key) — matched to site B.
- Site B's Q1 revenue was entered as text, `"EUR 26.4k"`, not a number — read as EUR 26,400.
- The last row (`A, 2026-Q2, 28000, 44000, re-export`) duplicates the earlier site A Q2 row exactly — excluded as a duplicate, not a fourth data point.

## Findings
| # | Claim | Source | Date | Document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site B (not refurbished, control) holds steady at EUR 1.10 per visitor in both Q1 and Q2 2026 (26,400/24,000 and 30,800/28,000) | Marlow finance, till export | 2026-10 | cafe-tills-2026h1.csv | data | supports the EUR 1.10 baseline | strong |
| 2 | Site A (refurbished Jan 2026) runs at EUR 1.55 per visitor across H1 2026 (74,400/48,000); Q1 1.52, Q2 1.57, rising | Marlow finance, till export | 2026-10 | cafe-tills-2026h1.csv | data | supports — above kill criterion, close to target | medium — no pre-refurbishment reading at this site to confirm the uplift itself, only the post-refurbishment level |
| 3 | Site C (refurbished 1 Apr 2026) rose from EUR 1.25 per visitor pre-refurbishment (Q1) to EUR 1.34 post-refurbishment (Q2) | Marlow finance, till export | 2026-10 | cafe-tills-2026h1.csv | data | contradicts — lands just below the EUR 1.35 kill criterion | weak — one quarter of post-refurbishment trading, smallest visitor base of the three sites |

## Reading across the two refurbished sites
- Site A sits well clear of the kill criterion and close to the EUR 1.60 target; site C is marginally below the kill criterion after its first quarter.
- The two sites aren't on the same clock: site A has had two quarters to ramp since its January refurbishment, site C has had one since its April refurbishment. If revenue per visitor builds over time (plausible, and consistent with site A's own Q1→Q2 rise), site C's single post-refurbishment quarter may understate its steady-state uplift.
- Sample is two refurbished sites, one of them with only one post-refurbishment data point — too thin to confirm or kill H2 on its own.

## Next steps
1. Café manager interviews (still outstanding, per workplan row 2) — qualitative read on what's driving the gap between A and C.
2. H2 2026 till data for all three pilot sites, once available, to see whether site C's uplift builds in Q3/Q4 the way site A's did between Q1 and Q2.
3. Flag the EUR 1.34–1.57 range (not a single point estimate) to synthesis, since it affects payback-period sensitivity in the board case.

