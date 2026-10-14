# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and the existing bridge before analysing, and names H3 as the branch | yes | Response opens with 'H3 is done' and all three files are updated in place (prior H1/H2 rows, liquidity/bridge log lines preserved), consistent with having read them first. |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch | yes | 00-status.md log keeps the original liquidity (2026-10-05) and bridge (2026-10-08) entries untouched; no restatement of the problem or re-derivation of the bridge appears. |
| Handles the three planted data issues explicitly | yes | 'Reconciling against the reported group total (EUR 1.05m) confirms the fix... Harbour must be -0.33 EUR m'; TOTAL row is bolded and used only for reconciliation ('35.0','2.10','1.05','3.15') while the Reading section discusses only the six sites; table has a dedicated 'Contribution before allocated  |
| Internally consistent figures across text and tables | yes | Table figures (North 1.35/9.0%, Westgate -0.35/-17.7% after overhead, -11.7% contribution, Harbour 0.00/-6.0%, TOTAL 2.10/1.05/3.0%/3.15) all match each other and the reference values exactly. |
| Reports contribution before allocation per site matching reference and flags Westgate as the only negative-contribution site | yes | Table: North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35 — matches reference exactly; text states 'Westgate is a genuine structural loss-maker... negative contribution margin... Harbour is not... exactly break-even (0.0%)'. |
| States closing Harbour would not raise group EBIT unless its overhead is removed, stated prominently (first line or H3 verdict) | yes | Second bullet of the lead summary: 'Closing it on reported EBIT alone isn't supported yet, since that overhead doesn't vanish if it's largely fixed HQ cost — it just reallocates to the other five sites,' echoed in 00-status.md's 'Current best answer (v2)'. |
| Marks H3 confirmed, killed, or reshaped | yes | 02-hypotheses.md: 'confirmed 2026-10-14, with caveat: Westgate is contribution-negative (real); Harbour is contribution break-even (overhead-allocation artifact, not an operating loss)'. |
| Links back to management's preferred cure and states implication for the answer | yes | 'Management's plan to close "the two weakest sites" on reported EBIT conflates these... Closing Harbour on the same logic assumes its EUR 0.33m overhead allocation disappears with it — it won't... unless real fixed costs are cut,' plus carry-forward flagging H4 as the determining analysis. |
| Writes h3-site-profitability.md, updates 02-hypotheses.md, adds a line to 00-status.md | yes | All three files shown in full with H3-specific content and a 2026-10-14 log line in 00-status.md. |
| Does not recommend closing both sites on reported EBIT | yes | 'This supports management's instinct on Westgate... Closing Harbour on reported EBIT alone isn't supported yet'. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

H3 is done. Summary:

**Data problem found first:** `data/site-pl-2025.csv` had Harbour's EBIT entered as **‑330** with a note saying it was keyed in EUR k. Reconciling against the group total (1.05) confirms it should be **‑0.33**, not ‑330 — a 1000x error that, left in, would have made Harbour look catastrophically worse than every other site.

**Corrected finding:** losses are concentrated (H3 kill criterion rejected), but not the way management's plan assumes:
- **Westgate** is a real structural loss-maker — negative contribution margin (‑11.7%) even before any central overhead. Supports closing it.
- **Harbour** is contribution break-even (0.0%) — it covers its own costs, and its entire reported loss is the 6%-of-revenue overhead allocation. Closing it on reported EBIT alone isn't supported yet, since that overhead doesn't vanish if it's largely fixed HQ cost — it just reallocates to the other five sites.

Updated `02-hypotheses.md`, `04-workplan.md`, and `00-status.md` (now v2 best answer), and wrote the full workup to `research/h3-site-profitability.md`, including what's still needed: the H4 fixed-vs-variable overhead split now directly determines whether closing Harbour actually helps group EBIT.

Next up per the workplan: H4 (overhead trend, currently "waiting for data") and H5 (peer margins), both due 2026-10-23.


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

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price. Site picture: losses are concentrated, not spread evenly, but management's "close Harbour and Westgate" plan conflates two different problems — Westgate is a genuine structural loss-maker (contribution-negative before any overhead), Harbour is contribution break-even and its reported loss is almost entirely a central-overhead allocation artifact. Closing Harbour on reported EBIT alone is not yet supported.
**Biggest open risk:** management wants to close Harbour and Westgate on the basis of reported site EBIT; the Harbour figure in the source data also contained a units error (-330 entered instead of -0.33) that, if uncorrected, would have made the case for closing Harbour look far stronger than the underlying economics support.
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: H3 site profitability done (research/h3-site-profitability.md). Flagged and corrected a data entry error (Harbour EBIT entered in EUR k, not EUR m). Westgate confirmed structural loss; Harbour reported loss is an overhead-allocation artifact, not an operating loss. Need H4 (overhead fixed vs variable) to assess real EBIT impact of closing Harbour.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | confirmed 2026-10-14, with caveat: Westgate is contribution-negative (real); Harbour is contribution break-even (overhead-allocation artifact, not an operating loss) |
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

# Research: H3 site profitability before and after allocated overhead, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Verdict:** partially confirmed, with an important correction; **evidence strength:** strong (reconciles to the cent against group EBIT).

## Data quality flag — raised to finance, correct before this goes near the board

`data/site-pl-2025.csv` shows Harbour EBIT as **-330**, with the controller's own note that it was "entered in EUR k." Taken literally, that is an EBIT margin of roughly -6,000% on EUR 5.5m of revenue — not a plausible operating result, and large enough that if it reached board materials unchanged it would make Harbour look like the clear #1 closure candidate by an order of magnitude.

Reconciling against the reported group total (EUR 1.05m) confirms the fix: North (0.81) + East (0.60) + Central (0.42) + Mill Lane (0.08) + Westgate (-0.53) = 1.38. For the total to equal 1.05, Harbour must be **-0.33 EUR m**, i.e. the -330 is EUR k, not EUR m, as the note says. All analysis below uses -0.33.

**Action:** get finance/the site controller to confirm and correct the source file before it's used in any board-facing document.

## Site economics, corrected

Overhead is allocated at 6% of site revenue (per the file header). Contribution before allocated overhead = reported EBIT + overhead allocated back.

| Site | Revenue (EUR m) | Overhead allocated | EBIT after overhead | EBIT margin | Contribution before overhead | Contribution margin |
|---|---|---|---|---|---|---|
| North | 9.0 | 0.54 | 0.81 | 9.0% | 1.35 | 15.0% |
| East | 7.5 | 0.45 | 0.60 | 8.0% | 1.05 | 14.0% |
| Central | 6.0 | 0.36 | 0.42 | 7.0% | 0.78 | 13.0% |
| Harbour | 5.5 | 0.33 | **-0.33** | -6.0% | **0.00** | 0.0% |
| Mill Lane | 4.0 | 0.24 | 0.08 | 2.0% | 0.32 | 8.0% |
| Westgate | 3.0 | 0.18 | -0.53 | -17.7% | **-0.35** | -11.7% |
| **TOTAL** | **35.0** | **2.10** | **1.05** | **3.0%** | **3.15** | **9.0%** |

## Reading

- Losses are concentrated, not evenly spread — the kill criterion for H3 ("losses spread evenly") is rejected. But the two loss-making sites are not the same kind of problem:
  - **Westgate is a genuine structural loss-maker.** Its contribution margin is negative (-11.7%) even before any central overhead is allocated to it. It does not cover its own direct costs. This supports management's instinct on Westgate.
  - **Harbour is not.** On a contribution basis it is exactly break-even (0.0%) — it covers its direct costs in full but contributes nothing toward central overhead. Its entire reported loss is the overhead allocation, not an operating problem at the site.
- Management's plan to close "the two weakest sites" on reported EBIT conflates these. Closing Westgate removes a real drag. Closing Harbour on the same logic assumes its EUR 0.33m overhead allocation disappears with it — it won't, if central overhead (HQ, etc.) is largely fixed. That cost gets reallocated across the remaining five sites, so group EBIT would improve by roughly Harbour's contribution (~EUR 0.00m), not its reported EBIT (-EUR 0.33m), unless real fixed costs are cut alongside the closure.

## Still needed before this can support a closure recommendation

1. Split of the 6% central overhead pool into variable-with-site-count vs fixed (HQ) — determines how much, if any, actually exits if Harbour closes.
2. One-off closure costs (redundancy, lease exit, customer transfer/loss risk) for Harbour and Westgate individually.
3. H4 (overhead trend) should answer point 1 directly — flagging this as a dependency.

## Carry-forward for H4/overhead workstream

Given finding above, H4's research note should explicitly test what share of the 6%-of-revenue allocation is fixed vs variable — this now has direct bearing on whether closing Harbour helps group EBIT at all.

