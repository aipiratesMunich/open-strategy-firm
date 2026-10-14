# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and existing bridge before analysing, and names H3 as the branch | yes | Response opens with 'H3 done' and figures/status (H2 confirmed, group EBIT 1.05/35.0) are consistent with the pre-existing bridge and hypotheses file; workplan row 3 and hypotheses H3 are updated in line with prior content. |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch | yes | No restatement of the problem, no liquidity recheck, no bridge rebuild appears anywhere in the output. |
| Handles the three planted data issues explicitly (Harbour unit error, TOTAL row excluded but used to check sum, contribution before 6% overhead) | yes | "the source file... lists Harbour's EBIT as '-330'... Corrected (÷1000, i.e. -0.33 EUR m)... ties exactly"; TOTAL row used only for "Check: EBIT + allocated overhead = contribution... Ties"; contribution before overhead computed per site (e.g. "Harbour's contribution before overhead is €0.00m"). |
| Internally consistent: no figure in the text contradicts the same figure in its own tables | yes | Site table sums reconcile (EBIT sums to 1.05, overhead to 2.10, contribution to 3.15) and all narrative figures (Harbour 0.00, Westgate -0.35) match the table exactly. |
| Reports contribution before allocation per site in line with reference values and identifies Westgate as the only site with negative direct contribution | yes | Table: North 1.35, East 1.05, Central 0.78, Mill Lane 0.32, Harbour 0.00, Westgate -0.35 — matching reference values, with Westgate the only negative entry. |
| States that closing Harbour would not raise group EBIT unless the overhead it carries is removed, on the first line or in the H3 verdict | yes | Research doc verdict/so-what: "its reported loss is an artefact of the 6% overhead allocation, so closing it will not by itself recover the €0.33m unless central overhead actually shrinks." |
| Marks H3 confirmed, killed or reshaped (expected: reshaped, Westgate true loss maker) | yes | 02-hypotheses.md: "confirmed, reshaped 2026-10-16: ... only Westgate loses money before overhead; Harbour breaks even before overhead and its loss is an allocation artefact". |
| Links back to management's preferred cure and says what it means for the answer | yes | Status file: "management wants to close Harbour and Westgate on the basis of reported site EBIT; Harbour's case does not hold up without H4"; chat response elevates H4 to decisive next test before board can "safely close both sites as proposed". |
| Writes engagement/fenmoor/research/h3-site-profitability.md, updates 02-hypotheses.md, adds line to 00-status.md | yes | All three files shown with H3-specific content; 00-status.md log entry dated 2026-10-16 describes the H3 findings. |
| Does not recommend closing both sites on reported EBIT | yes | Status file explicitly flags that closing both sites on reported EBIT "would recover less than claimed unless central overhead is shown to shrink" — the opposite of endorsing the closure. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

**H3 done — and it reshapes the closure case, not just confirms it.**

- Caught a data error first: the finance export had Harbour's EBIT as "-330," which is EUR k per the controller's note, not EUR m like the rest of the column. Taking it literally breaks the reconciliation to the group total (1.05); corrected to **-0.33 EUR m** it ties exactly.
- Concentration confirmed: Harbour + Westgate (24% of revenue) wipe out 82% of the group's underlying profit — the other four sites together make €1.91m, dragged down to €1.05m.
- But the two are not alike. **Westgate loses money even before any overhead allocation** (-0.35m contribution) — a genuine loss maker. **Harbour breaks even before overhead** (€0.00m contribution) — its entire reported loss is the 6%-of-revenue central overhead charge. Closing it won't recover that €0.33m unless central overhead actually shrinks when a site closes, which isn't known yet.
- That makes **H4 (overhead fixed vs. variable, cost-centre data — currently "waiting for data")** the decisive next test before the board can safely close both sites as proposed.

Updated `research/h3-site-profitability.md`, and reflected the result in `02-hypotheses.md`, `04-workplan.md`, and `00-status.md` (current best answer bumped to v2). Next open workplan row is H4 (overhead trend) — still blocked on cost-centre data from finance; H5 (peer margins) is also open and not blocked. Let me know when either dataset lands, or if you'd like me to draft the data request for H4 now.


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

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price (confirmed); within that, Westgate is a genuine loss maker (negative contribution before overhead) but Harbour breaks even before overhead — its reported loss is an overhead-allocation artefact, so closing both sites on reported EBIT, as management proposes, would recover less than claimed unless central overhead is shown to shrink with site count (H4, outstanding).
**Biggest open risk:** management wants to close Harbour and Westgate on the basis of reported site EBIT; Harbour's case does not hold up without H4 (overhead fixed/variable split).
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-16: H3 site profitability done (research/h3-site-profitability.md). Corrected a data error: Harbour's EBIT was entered as -330 (EUR k, per controller's note) not -0.33 EUR m; reconciled against group total to confirm. Finding: Westgate loses money before overhead (-0.35m contribution); Harbour breaks even before overhead (0.00m contribution) — its loss is the 6% overhead allocation, not a direct-cost problem. Closing Harbour will not recover €0.33m unless central overhead actually shrinks — makes H4 (overhead trend/fixed vs. variable, cost centres, due 2026-10-23, currently waiting for data) the critical next test before the board decision.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | confirmed, reshaped 2026-10-16: Harbour and Westgate cause the shortfall, but only Westgate loses money before overhead; Harbour breaks even before overhead and its loss is an allocation artefact |
| H4 | Overhead grew faster than revenue | medium | medium | cost centre data | overhead per EUR of revenue stable | open |
| H5 | Peers held margin | medium | high | trade association data | peers show the same decline | open |


## File written by the run: engagement/fenmoor/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Liquidity check | treasury | research/liquidity.md | EM | 2026-10-05 | done |
| 2 | H2 | Group profit bridge | finance | model/bridge-v1.md | analyst | 2026-10-08 | done |
| 3 | H3 | Site profitability before and after allocated overhead | data/site-pl-2025.csv | research/h3-site-profitability.md | analyst | 2026-10-16 | done |
| 4 | H4 | Overhead trend | cost centres | research/h4-overhead.md | analyst | 2026-10-23 | waiting for data |
| 5 | H5 | Peer margins | trade association | research/h5-peers.md | analyst | 2026-10-23 | not started |


## File written by the run: engagement/fenmoor/research/h3-site-profitability.md

# Research: H3, site profitability before and after allocated overhead, 2026-10-16

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A few sites cause most of the 2025 EBIT shortfall; losses are concentrated, not spread evenly across the six sites.
**Kill criterion:** Losses spread evenly across sites (no concentration).
**Verdict:** confirmed, but reshaped on the closure question; strength: medium (single internal source, one data error corrected by reconciliation, not yet independently confirmed by finance)
**So what:** Two sites destroy the equivalent of 82% of the group's underlying profit, confirming H3 — but only one of the two (Westgate) is a genuine loss maker before overhead; Harbour breaks even on its own costs and its reported loss is an artefact of the 6% overhead allocation, so closing it will not by itself recover the €0.33m unless central overhead actually shrinks.

## Data correction (log before analysis)

The source file (`data/site-pl-2025.csv`) lists Harbour's EBIT as "-330" with a controller's note: "EBIT entered in EUR k by site controller." Every other row is in EUR m. Taken literally, -330 is checked against the TOTAL row:

- As given: 0.81 + 0.60 + 0.42 **- 330** + 0.08 - 0.53 = -328.62 ≠ 1.05 (reported total). Fails the "segments sum to total" check.
- Corrected (÷1000, i.e. -0.33 EUR m): 0.81 + 0.60 + 0.42 **- 0.33** + 0.08 - 0.53 = 1.05 = reported total. Ties exactly.

Harbour's EBIT is therefore taken as **-0.33 EUR m**, not -330, for the rest of this note. This is an ASSUMPTION pending direct confirmation from the site controller (see Data requests) — the arithmetic reconciliation is strong evidence but not a substitute for the source correcting its own entry.

## Findings

| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Harbour reported EBIT is -0.33 EUR m (2025), not -330; corrected figure reconciles site sum to group total of 1.05 EUR m | Finance export, corrected per controller's note and reconciliation | 2026-10-12 (received), corrected 2026-10-16 | data/site-pl-2025.csv | client data | corrects the base data for all below | strong (arithmetic tie-out) |
| 2 | Harbour and Westgate (24% of group revenue, 8.5 of 35.0 EUR m) together report -0.86 EUR m EBIT; the other four sites report +1.91 EUR m | data/site-pl-2025.csv | 2025 | data/site-pl-2025.csv | client data | supports H3: losses concentrated in 2 of 6 sites | strong |
| 3 | Westgate's contribution before the 6%-of-revenue overhead allocation is **-0.35 EUR m** on 3.0 EUR m revenue — negative even before any central cost is attributed | Calculated: EBIT -0.53 + overhead allocation 0.18 (6% × 3.0) | 2025 | data/site-pl-2025.csv | client data, derived | supports closing Westgate on profitability grounds | strong |
| 4 | Harbour's contribution before overhead is **€0.00m** on 5.5 EUR m revenue — it covers its own direct costs exactly; its entire reported loss is the €0.33m overhead allocation | Calculated: EBIT -0.33 + overhead allocation 0.33 (6% × 5.5) | 2025 | data/site-pl-2025.csv | client data, derived | contradicts using reported EBIT alone to justify closing Harbour | strong, conditional on allocation basis being a flat 6% of revenue as stated |
| 5 | Mill Lane is weak but not loss-making: EBIT €0.08m, contribution before overhead €0.32m on €4.0m revenue | data/site-pl-2025.csv | 2025 | data/site-pl-2025.csv | client data | does not support closing Mill Lane now; watch | medium |

### Site table (EUR m, 2025)

| Site | Revenue | EBIT (after 6% allocated overhead) | Allocated overhead (6% of revenue) | Contribution before overhead |
|---|---|---|---|---|
| North | 9.0 | 0.81 | 0.54 | 1.35 |
| East | 7.5 | 0.60 | 0.45 | 1.05 |
| Central | 6.0 | 0.42 | 0.36 | 0.78 |
| Mill Lane | 4.0 | 0.08 | 0.24 | 0.32 |
| Harbour | 5.5 | **-0.33** (corrected) | 0.33 | **0.00** |
| Westgate | 3.0 | -0.53 | 0.18 | **-0.35** |
| **TOTAL** | **35.0** | **1.05** | **2.10** | **3.15** |

Check: EBIT + allocated overhead = contribution before overhead, by row and in total (1.05 + 2.10 = 3.15; sum of contribution column = 3.15). Ties.

## Triangulation of decisive claims

| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Harbour's loss is an overhead-allocation artefact, not a direct-cost problem | Reported EBIT after allocation: -0.33 EUR m | Contribution before allocation: 0.00 EUR m, i.e. direct costs exactly covered | No — both derived from the same csv; not two independent data sources | Harbour direct economics: breakeven ± rounding; true group EBIT effect of closing it depends on overhead's fixed/variable split (untested) | medium — arithmetic is solid, but needs H4 (overhead trend data, still outstanding) before it can support a closure decision |

Only one decisive claim met the bar for a triangulation row; the others are direct reads of the (corrected) P&L, not claims needing two approaches.

## Outside view

No comparable Fenmoor site-closure case or peer benchmark is on file. Whether central print-site overhead (press capacity, logistics, admin) is mostly fixed or scales with site count is a factual question for H4's cost-centre data, not something to assume from general sector knowledge — flagged as open rather than asserted.

## Counter-evidence

None found against the concentration finding itself (claim 2). Against the overhead-trap point (claim 4): if a meaningful share of the 6% allocation is genuinely variable with site count — e.g. site-specific admin or supervision booked centrally — then closing Harbour would recover closer to the full €0.33m. No cost-centre data available yet to test this; it is the single fact that would most change the recommendation.

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Harbour EBIT unit correction | ASSUMPTION (strong, via reconciliation) | -0.33 EUR m | Site controller confirms the "-330" entry was EUR k | EM, next finance contact |
| Fixed vs variable split of the 6% central overhead allocation | missing | unknown — decisive for the closure case | Cost-centre data (workplan row 4, H4) | Analyst |
| One-off closure costs (severance, lease exit, decommissioning) for Harbour / Westgate | missing | not sized | Finance / HR data request if closure is pursued | EM, next phase |
| Revenue and customer retention if a site closes (volume transfers vs. is lost) | missing | not sized | Commercial/sales input, next phase | EM, next phase |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Confirmation of Harbour's EBIT entry and unit | Email/short note from site controller | Claim 1 — base data correctness | Rely on reconciliation (already strong) | EM |
| Cost-centre breakdown of central overhead, fixed vs. variable, by driver | Spreadsheet, cost centre level | Claim 4 — decides whether closing Harbour recovers €0.33m or near-zero | Treat Harbour closure benefit as unproven until H4 lands; do not size it in the action plan | Analyst (workplan row 4) |
| Site-level one-off closure costs and notice periods, if closure proceeds to a business case | Finance/HR estimate | Needed before any closure recommendation reaches the board | Flag as open in the answer page | EM |

