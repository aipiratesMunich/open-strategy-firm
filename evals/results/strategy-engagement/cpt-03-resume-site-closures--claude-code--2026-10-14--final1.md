# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and existing bridge before analysing, and names H3 as the branch | yes | Opens with "H3 (site profitability) is done", references workplan row 3, H4's 'still waiting on cost-centre data' status, and synthesises the prior H2 bridge finding into the status page's current answer — consistent with having read all three docs plus the bridge. |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch | yes | No liquidity or bridge rework appears; only H2's conclusion is referenced, not redone. |
| Handles the three planted data issues: Harbour -330 as EUR -0.33m unit error, excludes TOTAL row from site analysis but uses it to check sum, computes contribution before 6% overhead | yes | "Harbour's EBIT was entered in EUR k, not EUR m (raw cell '-330'). Back-solving against the TOTAL row, the correct figure is -EUR 0.33m"; site table lists only the six sites (TOTAL used only in the back-solve/check equation); contribution-before-overhead table is explicit. |
| Internally consistent: no figure contradicts the same figure in its own tables | yes | Back-solve equation 0.81+0.60+0.42+Harbour+0.08-0.53=1.05 reconciles exactly with the reported-margin and contribution tables (verified by reconstructing site revenues from the contribution/margin pairs). |
| Reports contribution before allocation per site in line with reference values and identifies Westgate as the only site with negative direct contribution | yes | Findings claim 4: North 1.35, East 1.05, Central 0.78, Mill Lane 0.32, Harbour 0.00, Westgate -0.35 — matches reference exactly, and Westgate is the only negative figure. |
| States closing Harbour would not raise group EBIT unless overhead removed, on first line or in H3 verdict | yes | "Closing it wouldn't recover EUR 0.33m of group EBIT, because that overhead doesn't vanish — it redistributes onto the other five sites" appears in the top summary and is restated in the research doc's 'So what' section. |
| Marks H3 confirmed, killed, or reshaped per expected framing (Westgate true loss maker; decline mostly the group-wide H2 cost issue) | yes | 02-hypotheses.md marks H3 "confirmed, reshaped 2026-10-14"; status page ties the margin decline to H2's price/cost finding while isolating Westgate as the site-specific issue. |
| Links back to management's preferred cure and states what it means for the answer | yes | "management's 'close Harbour and Westgate' plan is only half right" and status.md: "Harbour should not be closed on that argument... Westgate is the real closure/fix/sell candidate... Next workplan rows up: H4 (overhead trend)". |
| Writes h3-site-profitability.md, updates 02-hypotheses.md, adds a line to 00-status.md | yes | All three files shown with the relevant H3 content; file list confirms research/h3-site-profitability.md was created. |
| Does not recommend closing both sites on reported EBIT | yes | "Westgate is the real problem... management's plan is only half right" — explicitly argues against closing Harbour. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

**H3 (site profitability) is done — and it overturns half of management's plan.**

The site P&L had a data error: Harbour's EBIT was entered in EUR k, not EUR m (raw cell "-330"). Back-solving against the TOTAL row, the correct figure is **-EUR 0.33m**.

More importantly, reported EBIT is *after* a 6%-of-revenue overhead allocation. Once you strip that out to see contribution per site:

| Site | Reported EBIT margin | Contribution before overhead |
|---|---|---|
| North | 9.0% | 15.0% |
| East | 8.0% | 14.0% |
| Central | 7.0% | 13.0% |
| Mill Lane | 2.0% | 8.0% |
| **Harbour** | **-6.0%** | **0.0%** |
| **Westgate** | **-17.7%** | **-11.7%** |

**Harbour breaks even before overhead** — its reported loss is purely an allocation artefact. Closing it wouldn't recover EUR 0.33m of group EBIT, because that overhead doesn't vanish — it redistributes onto the other five sites. **Westgate is the real problem**: genuinely loss-making even before any overhead is charged.

So management's "close Harbour and Westgate" plan is only half right. I've written this up in `research/h3-site-profitability.md`, updated the hypothesis (H3 confirmed, reshaped), marked workplan row 3 done, and revised the status page's current answer and biggest-risk line accordingly.

**Open before this goes to the board:** whether any of Harbour's allocated overhead is actually avoidable (feeds H4 — overhead trend, still waiting on cost-centre data), and one-off closure costs for either site. Next workplan rows up: H4 (overhead trend) and H5 (peer margins).


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

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price. On site profitability, losses are concentrated but not where management thinks: Westgate is genuinely loss-making before any overhead allocation; Harbour breaks even before overhead and its reported loss is an artefact of the overhead allocation key.
**Biggest open risk:** management wants to close Harbour and Westgate on the basis of reported (fully-allocated) site EBIT. Harbour should not be closed on that argument — the EUR 0.33m "loss" does not disappear with the site, it redistributes onto the other five sites, unless a matching amount of central overhead is also removed. Westgate is the real closure/fix/sell candidate. Still need: which part of allocated overhead is actually avoidable (feeds H4), and one-off closure costs, before any closure business case.
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: H3 site profitability done (research/h3-site-profitability.md). Corrected a unit error in Harbour's reported EBIT (-EUR 330m as entered → -EUR 0.33m, back-solved against the TOTAL row). On contribution before allocated overhead, Harbour breaks even (0.0%) and Westgate is negative (-11.7%); management's proposed closure list is not supported by the evidence as it stands.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline — but not the two sites management named: Westgate is loss-making before overhead allocation, Harbour breaks even before overhead | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | confirmed, reshaped 2026-10-14 |
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

# Research: H3 site profitability, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A few sites cause most of the 2025 EBIT decline; on a contribution basis (before the 6%-of-revenue central overhead allocation), losses are concentrated in a small number of sites, not spread evenly.
**Kill criterion:** Losses spread evenly across sites (no site below roughly group average margin on both a reported and a contribution basis).
**Verdict:** confirmed, reshaped; **evidence strength:** strong (single finance source, but the arithmetic is self-checking against the TOTAL row).
**So what:** Losses are concentrated, but not in the two sites management picked. Westgate is genuinely loss-making before any overhead allocation and is the real closure candidate. Harbour's reported EUR -0.33m is entirely the effect of the overhead allocation key; before that allocation, Harbour breaks even. Closing Harbour on the reported-EBIT argument would not recover EUR 0.33m of group EBIT — that overhead does not disappear, it would redistribute onto the five remaining sites.

## Data correction

`data/site-pl-2025.csv` carries a controller's own note: Harbour's EBIT was entered in EUR k, not EUR m, by the site controller — the raw cell reads -330. Taking the file at face value (-EUR 330m on EUR 5.5m revenue) is impossible and contradicts the TOTAL row.

Back-solving from TOTAL: 0.81 + 0.60 + 0.42 + Harbour + 0.08 - 0.53 = 1.05 → Harbour = **-0.33 EUR m**, consistent with -330 EUR k. Used throughout below.

## Findings

| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Site EBIT is stated after allocated central overhead, charged at 6% of site revenue | File header comment | 2025 FY | data/site-pl-2025.csv | client data | context for all below | strong |
| 2 | Harbour reported EBIT is -EUR 0.33m (corrected from a EUR k/EUR m entry error), not -EUR 330m | Back-solved against TOTAL row | 2025 FY | data/site-pl-2025.csv | client data | contradicts raw file value; supports corrected view | strong |
| 3 | Reported EBIT margin by site: North 9.0%, East 8.0%, Central 7.0%, Mill Lane 2.0%, Harbour -6.0%, Westgate -17.7% | Calculated, EBIT / revenue | 2025 FY | data/site-pl-2025.csv | client data | supports "two weakest sites" framing management uses | strong |
| 4 | Contribution before allocated overhead by site (reported EBIT + site's allocated overhead): North EUR 1.35m (15.0%), East EUR 1.05m (14.0%), Central EUR 0.78m (13.0%), Mill Lane EUR 0.32m (8.0%), Harbour EUR 0.00m (0.0%), Westgate -EUR 0.35m (-11.7%) | Calculated from data/site-pl-2025.csv | 2025 FY | data/site-pl-2025.csv | client data | contradicts closing Harbour on EBIT grounds; supports Westgate as the real problem site | strong |
| 5 | Total allocated central overhead across sites: EUR 2.10m (6% × EUR 35.0m revenue); contribution total EUR 3.15m; 3.15 - 2.10 = 1.05 = reported group EBIT | Calculated, ties to TOTAL row | 2025 FY | data/site-pl-2025.csv | client data | internal consistency check | strong |

## Triangulation of decisive claims

| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Harbour's corrected EBIT is -EUR 0.33m | Unit correction (EUR k → EUR m) of the raw cell | Back-solve from TOTAL minus the other five sites | Same underlying file, but two different arithmetic routes that must agree | -EUR 0.33m (exact; both routes agree) | strong |
| Harbour breaks even before overhead; Westgate does not | Contribution = reported EBIT + site's own allocated overhead (6% × site revenue) | Cross-check: sum of all six contributions minus total overhead must equal reported group EBIT (1.05) | Same file, but the cross-check is a different identity than the per-site calc | Harbour EUR 0.00m, Westgate -EUR 0.35m (exact, single source, no external benchmark) | medium — single source; no second data set confirms the 6% allocation key reflects true cost-to-serve rather than a convention |

## Outside view

Not applicable at this step: this is an internal allocation and contribution analysis, not a forecast. The open question this raises for benchmarking is whether a flat 6%-of-revenue overhead key is itself defensible — see Open questions below and workplan row 4 (H4, overhead trend).

## Counter-evidence

- Management's reported-EBIT view is not wrong as a description of the accounting result — Harbour and Westgate are indeed the two worst sites on reported EBIT. The disagreement is about what reported EBIT implies for a closure decision, not about the numbers themselves.
- It is possible some part of Harbour's allocated overhead is in fact avoidable (e.g., a site controller, local admin, or site-specific IT that would genuinely disappear on closure). The data as given cannot separate avoidable from unavoidable overhead; the 6%-of-revenue key is a pure allocation convention, not a cost trace. If a material share of Harbour's EUR 0.33m allocation is avoidable, the case for closure strengthens accordingly — this must be checked before any closure decision, not assumed.

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Harbour's true EBIT is -EUR 0.33m, not -EUR 330m or -EUR 0.330k | ASSUMPTION (strong, self-checking against TOTAL) | -EUR 0.33m | Confirm directly with the site controller or finance system of record | EM, before this goes to the board |
| The 6%-of-revenue overhead allocation key approximates each site's true draw on central resources | unverified | used as given | Activity-based or headcount-based overhead trace per site, or at minimum a split of the central overhead pool into site-specific vs genuinely shared/fixed | Analyst, feeds H4 |
| Closing a site frees any of its allocated overhead rather than only redistributing it | unverified | treated as not freed, i.e. reallocates | Finance confirmation of which central cost lines are headcount/site-count driven vs fixed regardless of site count | Analyst / finance, before closure business case |
| One-off closure costs (severance, lease exit, equipment) for Harbour and Westgate | missing | not sized here | Data request to finance/HR | Analyst |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Confirmation of Harbour's EBIT figure from finance system of record (not the controller's manual export) | single figure, EUR m, 2025 | Claim 2 — the whole Harbour conclusion rests on this correction | Keep the back-solved -EUR 0.33m, flagged as unconfirmed, on the answer page | EM |
| Breakdown of the central overhead pool into cost lines that scale with site count vs. fixed regardless of site count | table, EUR m by cost line | Determines how much of Harbour's or Westgate's allocated overhead would actually be saved on closure | Treat all allocated overhead as unavoidable (conservative; weakens the closure case further) | Analyst, workplan row 4 (H4) |
| One-off cost estimate to close Harbour and/or Westgate (severance, lease, equipment disposal) | EUR m, by site | Needed before any closure business case nets out against the contribution lost | Flag as open in the business case, do not assume zero | Analyst |

## Update to engagement hypothesis H3

Original H3: "A few sites cause most of the decline." Confirmed, but reshaped — the "few sites" are not the two management named:

- **Westgate** is the clear problem site: -11.7% contribution margin before any overhead allocation. It does not cover its own direct costs. This is the strongest closure/fix/sell candidate on the evidence so far.
- **Harbour** breaks even before overhead (0.0% contribution). Its reported loss is a product of the overhead allocation key, not of its own operations. Closing it on the reported-EBIT argument would not recover EUR 0.33m of group EBIT unless a matching EUR 0.33m of central overhead is also removed — otherwise that cost lands on North, East, Central and Mill Lane, which would show worse reported margins for no change in group EBIT.
- North, East and Central comfortably cover overhead (13-15% contribution) and are not part of the problem.
- Mill Lane is thin (8% contribution, 2% reported) and worth watching but is not in the same category as Westgate.

