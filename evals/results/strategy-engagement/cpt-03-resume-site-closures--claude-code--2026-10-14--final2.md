# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and the existing bridge before analysing, and names H3 as the branch. | yes | Response preserves and references all prior hypotheses (H1, H2, H4, H5), workplan rows 1-5, and the bridge ('independently with the group bridge'); opens with 'H3 done — research/h3-site-profitability.md.' |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch. | yes | Liquidity and bridge are only referenced for reconciliation ('model/bridge-v1.md, built 2026-10-08, before site data existed'), not redone; no restatement of the problem statement. |
| Handles the three planted data issues explicitly (Harbour unit error, TOTAL row exclusion/use as check, contribution before overhead). | yes | 'the source CSV has Harbour's EBIT entered as -330... It only reconciles with the file's own TOTAL... at -0.33 EUR m'; 'Check: contribution 3.15 - overhead 2.10 = EBIT 1.05. Reconciles to both the CSV total and the group bridge'; table has explicit 'Contribution before allocated overhead' column. |
| Internally consistent: no figure in text contradicts the same figure in its own tables. | yes | All margins (North 9.0%, East 8.0%, Central 7.0%, Harbour -6.0%, Mill Lane 2.0%, Westgate -17.7%, group 3.0%) and contribution figures (1.35, 1.05, 0.78, 0.00, 0.32, -0.35, total 3.15/9.0%) match reference values and reconcile across the table and prose. |
| Reports contribution before allocation per site matching reference values and identifies Westgate as the only site with negative direct contribution. | yes | Table shows Westgate contribution -0.35 (only negative value); 'only Westgate is a real loss-maker before overhead (-11.7% contribution margin)'. |
| States closing Harbour would not raise group EBIT unless overhead is removed, on first line or in H3 verdict. | yes | H3 file 'So what': 'Closing Harbour on the reported EBIT number would not recover the loss it appears to show... unless finance can show that part of the €0.33m allocated to it is cost that genuinely disappears on closure.' |
| Marks H3 confirmed, killed or reshaped, with substance: Westgate the true loss-maker and the decline mostly attributable to the group-wide cost issue already confirmed in H2. | NO | 02-hypotheses.md reshapes H3 and identifies Westgate as the sole loss-maker, but explicitly declines to connect the decline to H2, instead treating it as unresolved: 'cannot yet attribute the 2023-2025 decline to specific sites' and workplan row 8 defers this to future 2023 data rather than stating  |
| Links back to management's preferred cure and says what it means for the answer. | yes | 'management's "close Harbour and Westgate" plan is only half supported by the numbers... Westgate... a real closure/fix candidate... Harbour... closing it doesn't recover that money'; next step flagged as H3a (overhead avoidability), the top open item. |
| Writes h3-site-profitability.md, updates 02-hypotheses.md, adds a line to 00-status.md. | yes | All three files shown as written/updated with dated log entries, e.g. '2026-10-14: H3 analysed (research/h3-site-profitability.md)...' in 00-status.md. |
| Does not recommend closing both sites on reported EBIT. | yes | 'Closing Harbour on the reported EBIT number would not recover the loss it appears to show' — only Westgate is recommended as a closure/fix candidate. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

**H3 done — `research/h3-site-profitability.md`.**

Headline, worth flagging before anything goes near the board: management's "close Harbour and Westgate" plan is only half supported by the numbers.

- **Westgate** is a genuine loss-maker even before overhead is allocated (-11.7% contribution margin) — a real closure/fix candidate.
- **Harbour** breaks exactly even *before* overhead (0.0% contribution margin). Its reported -0.33m loss is purely the 6%-of-revenue overhead allocation landing on it. Closing it doesn't recover that money unless the underlying central costs actually shrink — otherwise that overhead just reallocates onto the other five sites and the group is no better off (and worse off in year one once exit costs are counted).
- Along the way I caught a data error: the source CSV has Harbour's EBIT entered as **-330**, with a controller's note it's in EUR k, not EUR m like every other row. Taken literally that's a bigger loss than the whole group's revenue. It only reconciles with the file's own TOTAL (and independently with the group bridge) at **-0.33 EUR m**. I used the corrected figure throughout but **flagged it as unconfirmed** — it needs sign-off from finance before this goes to the board.

I reshaped H3, added a new hypothesis (H3a: is the allocated overhead actually avoidable on closure?), and added four workplan rows: confirm the Harbour figure, get the overhead cost-centre breakdown, request 2023 site P&L (we only have one year, so we can't yet say these sites caused the *decline* vs. just being weak today), and get one-off closure costs checked against the cash runway. Status and hypotheses files are updated.

Next highest-impact open item is H3a (overhead avoidability) — it directly decides whether the Harbour half of the board's preferred plan actually works.


## Files in work dir after run

- engagement/fenmoor/00-status.md
- engagement/fenmoor/01-problem-statement.md
- engagement/fenmoor/02-hypotheses.md
- engagement/fenmoor/04-workplan.md
- engagement/fenmoor/data/site-pl-2025.csv
- engagement/fenmoor/model/bridge-v1.md
- engagement/fenmoor/research/h3-site-profitability.md
- engagement/fenmoor/research/liquidity.md

## File written by the run: engagement/fenmoor/00-status.md

# Engagement status: Fenmoor Print Services, margin recovery

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-21 | EM | passed |
| Structure | Issue tree, hypotheses | v1 | EM | passed |
| Plan | Workplan | v1 | EM | passed |
| Analyse | Analyses per branch | 3 of 5 done (liquidity, bridge, site profitability) | | |
| Synthesise | Answer page | not started | | |
| Decide | Board, 2 December 2026 | | | |

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price (confirmed, H2). Of the two sites management wants to close, only Westgate is a genuine loss-maker before overhead (-11.7% contribution margin); Harbour breaks exactly even before overhead and its reported loss is an overhead-allocation artefact — closing it will not by itself recover the EUR 0.33m it appears to lose. Still open: whether allocated overhead is avoidable on closure (H3a), and whether 2023 site data would point to different sites as the cause of the *decline* rather than just the 2025 level.
**Biggest open risk:** management's board case for closing both Harbour and Westgate rests on reported site EBIT, which for Harbour is break-even before overhead — closing it may not save real cash unless central overhead genuinely shrinks. Second risk: the source data itself contained an unflagged units error on Harbour (-330 vs -0.33 EUR m) that has not yet been confirmed by finance.
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: H3 analysed (research/h3-site-profitability.md). Found and corrected a units error in Harbour's EBIT (file: -330, reconciles only at -0.33 EUR m) — flagged to finance for confirmation, not yet signed off. Reshaped H3: only Westgate is loss-making before overhead; Harbour is break-even before overhead. Added H3a (overhead avoidability on closure) and three new workplan rows: confirm Harbour figure, overhead cost-centre breakdown, 2023 site data, one-off closure costs.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | reshaped 2026-10-14: only Westgate is loss-making before overhead (-11.7% contribution margin); Harbour breaks exactly even before overhead (0.0%) — its reported loss is an overhead-allocation artefact. 2025 is a one-year snapshot; cannot yet attribute the 2023-2025 decline to specific sites (see research/h3-site-profitability.md) |
| H4 | Overhead grew faster than revenue | medium | medium | cost centre data | overhead per EUR of revenue stable | open |
| H5 | Peers held margin | medium | high | trade association data | peers show the same decline | open |
| H3a | Closing Harbour recovers close to the EUR 0.33m of overhead currently allocated to it | high | high | central overhead cost-centre breakdown: site-specific vs shared cost | allocated overhead is mostly shared/fixed cost that does not shrink if Harbour closes | open — added 2026-10-14 after H3; decides whether the Harbour half of management's closure plan pays for itself |


## File written by the run: engagement/fenmoor/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Liquidity check | treasury | research/liquidity.md | EM | 2026-10-05 | done |
| 2 | H2 | Group profit bridge | finance | model/bridge-v1.md | analyst | 2026-10-08 | done |
| 3 | H3 | Site profitability before and after allocated overhead | data/site-pl-2025.csv | research/h3-site-profitability.md | analyst | 2026-10-16 | done 2026-10-14; reshaped — see hypotheses |
| 4 | H4 | Overhead trend | cost centres | research/h4-overhead.md | analyst | 2026-10-23 | waiting for data |
| 5 | H5 | Peer margins | trade association | research/h5-peers.md | analyst | 2026-10-23 | not started |
| 6 | H3 | Confirm Harbour 2025 EBIT: file shows -330, reconciles only at -0.33 EUR m | finance / site controller | email or corrected CSV | EM | 2026-10-17 | not started — blocks any board number on Harbour |
| 7 | H3a | Central overhead cost-centre breakdown: site-specific vs shared, what ends if a site closes | finance | research/h3a-overhead-avoidability.md | analyst | 2026-10-23 | not started — decides whether closing Harbour saves anything |
| 8 | H3 | 2023 (and 2024) site P&L, same basis, to attribute the decline rather than just the 2025 level | finance | update to research/h3-site-profitability.md | analyst | 2026-10-23 | not started |
| 9 | H3/portfolio | One-off closure costs for Harbour and Westgate (severance, lease exit, notice) vs 26-week cash runway | finance / HR / legal | input to business case | analyst | 2026-10-30 | not started |


## File written by the run: engagement/fenmoor/research/h3-site-profitability.md

# Research: H3, site profitability before and after allocated overhead, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A few sites cause most of the 2023-2025 margin decline.
**Kill criterion:** Losses are spread evenly across sites.
**Verdict:** reshaped; **strength:** medium — see caveat below.
**So what:** Of the two sites management wants to close, only Westgate is a real loss-maker before overhead (-11.7% contribution margin). Harbour breaks exactly even before overhead (0.0%); its reported loss is an artefact of the 6%-of-revenue overhead allocation, not a site-level problem. Closing Harbour on the reported EBIT number would not recover the loss it appears to show, and could make the group worse off once one-off exit costs are counted — unless finance can show that part of the €0.33m allocated to it is cost that genuinely disappears on closure.

## Data quality flag (fix before this goes further)

The source file (`data/site-pl-2025.csv`) lists Harbour's EBIT as **-330**, with a controller's note that it was entered in EUR k while every other row is in EUR m. Taken literally, -330 EUR m is larger than total group revenue (EUR 35m) and is not possible. Reconciling against the file's own TOTAL row (EBIT 1.05) and against the independently-built group bridge (`model/bridge-v1.md`, EBIT 2025 = EUR 1.05m) only works if Harbour's EBIT is **-0.33 EUR m** (i.e. -330 EUR k). All figures below use -0.33. **This correction has not yet been confirmed with the site controller or finance — do before this goes to the board.**

## Findings

| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site revenue and reported EBIT, 6 sites, FY2025, EBIT stated after central overhead allocated at 6% of site revenue | Finance, site P&L export | 2026-10-12 | data/site-pl-2025.csv | client data | base data for H3 | medium — one uncorroborated field (see flag above) |
| 2 | Harbour EBIT as entered (-330) is inconsistent with the file's own TOTAL (1.05) and with the group bridge (1.05); -0.33 reconciles both exactly | Internal recalculation against data/site-pl-2025.csv and model/bridge-v1.md | 2026-10-14 | this analysis | internal check | contradicts the raw figure; supports -0.33 as the usable number | strong (arithmetic, two independent documents agree) |
| 3 | Overhead allocation rule: 6% of site revenue, all sites | CSV header note | 2026-10-12 | data/site-pl-2025.csv | client data | basis for before/after-overhead split | medium — rule stated, allocation method (why 6%, what it covers) not seen |
| 4 | Contribution before allocated overhead by site (calculated: reported EBIT + allocated overhead) | This analysis | 2026-10-14 | this analysis | derived from #1 and #3 | decisive for H3 | strong, conditional on #2 |

## Site profitability, before and after allocated overhead (FY2025, EUR m)

| Site | Revenue | EBIT (after overhead) | EBIT margin | Overhead allocated (6% rev) | Contribution before overhead | Contribution margin |
|---|---|---|---|---|---|---|
| North | 9.0 | 0.81 | 9.0% | 0.54 | 1.35 | 15.0% |
| East | 7.5 | 0.60 | 8.0% | 0.45 | 1.05 | 14.0% |
| Central | 6.0 | 0.42 | 7.0% | 0.36 | 0.78 | 13.0% |
| Harbour | 5.5 | -0.33 | -6.0% | 0.33 | **0.00** | **0.0%** |
| Mill Lane | 4.0 | 0.08 | 2.0% | 0.24 | 0.32 | 8.0% |
| Westgate | 3.0 | -0.53 | -17.7% | 0.18 | **-0.35** | **-11.7%** |
| **TOTAL** | **35.0** | **1.05** | **3.0%** | **2.10** | **3.15** | **9.0%** |

Check: contribution 3.15 - overhead 2.10 = EBIT 1.05. Reconciles to both the CSV total and the group bridge.

## Triangulation of decisive claims

| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Group EBIT 2025 = EUR 1.05m | Site P&L export summed across 6 sites (finance/site controllers) | Group profit bridge built from 2023 baseline + drivers (model/bridge-v1.md, built 2026-10-08, before site data existed) | yes — different source, different date, built before this file existed | EUR 1.05m | strong |
| Harbour's true EBIT is -0.33m, not -330 | Reconciliation against the file's own TOTAL row | Reconciliation against the independent group bridge total | partially — both checks use the same TOTAL figure, so this is one triangulation point, not two fully independent sources | -0.33 EUR m (= -330 EUR k) | medium — still needs confirmation from the controller who entered it |

## Outside view

Not applicable at site level — no peer or internal-benchmark data on site-level overhead allocation or per-site contribution margins was available. Flagged under H5 (peer margins), still open.

## Counter-evidence

- None found against the arithmetic (the reconciliation is exact, not approximate).
- Not tested: whether there are strategic reasons for closing Harbour beyond EBIT — e.g. lease break clause timing, customer overlap with East that could be consolidated, planned capex avoidance. None of this is in the data received; see open questions.

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Harbour EBIT corrected to -0.33 EUR m | unverified | -0.33 (point estimate, high confidence in the arithmetic, not yet signed off) | Confirmation from the site controller or finance that the entry was a units error, not a different error | Finance / site controller |
| 6% overhead allocation reflects real, avoidable cost if a site closes | ASSUMPTION — allocation is almost never 100% avoidable | Unknown avoidable share; treat 0.33 for Harbour and 0.18 for Westgate as upper bounds, not cash savings | Breakdown of the central overhead pool by cost type (shared IT/finance/management vs site-specific rent/local management) and which elements end if a site closes | Finance / COO |
| Decline (2023→2025) is concentrated in the same sites that are weak in 2025 | missing — only one year (2025) of site data exists; H3 as originally framed is about the *decline*, this data only tests the *current* cross-section | not tested | 2023 (and ideally 2024) site P&L on the same basis | Finance |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Confirmation of Harbour's 2025 EBIT (-0.33 EUR m vs -330 as entered) | email or corrected CSV | Everything in this note depends on it | Keep -0.33 as a flagged, unconfirmed correction; do not put -330 in front of the board | Finance / site controller |
| 2023 (and 2024, if available) site-level P&L on the same basis | CSV, same format as data/site-pl-2025.csv | Needed to test whether Harbour/Westgate caused the *decline*, or were already weak in 2023 and the decline happened elsewhere | Present H3 findings as "2025 snapshot only" and flag the gap on the ghost deck page | Finance |
| Breakdown of the central overhead pool: which costs are site-specific vs shared, and which end if a given site closes | cost-centre detail or a short memo from finance | Needed before any closure business case — determines whether closing Harbour saves EUR 0.33m, EUR 0, or something in between | Treat site closure savings as a wide range (EUR 0 to 0.33m for Harbour) pending this | Finance / COO |
| One-off closure costs for Harbour and Westgate (severance, lease exit, notice periods) | finance / HR estimate | Needed to time the cash effect of any closure decision against the 26-week liquidity runway (research/liquidity.md) | Flag as open in the business case; do not assume a closure pays back in year 1 | Finance / HR / legal |

## So what for the board

Management's preferred cure — close Harbour and Westgate — is half right and half a trap. Westgate loses money at the contribution level (-11.7%) and is a legitimate fix-or-close candidate. Harbour is exactly break-even before overhead: its reported loss is the 6%-of-revenue allocation rule doing what allocation rules do, not evidence that the site itself is unprofitable. Closing it would not, by itself, recover EUR 0.33m for the group — that overhead either moves to the other five sites' allocated cost (making their reported margins look worse without anything real changing) or is realised as cash savings only to the extent central costs genuinely shrink, which is not yet known. Recommend testing the overhead breakdown and 2023 site data (open items above) before any closure decision goes to the board on 2 December.

