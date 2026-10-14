# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and the existing bridge before analysing, and names H3 as the branch. | yes | Response opens with 'H3 is done' and preserves exact prior entries (H1 confirmed 2026-10-05, H2 confirmed 2026-10-08, liquidity/bridge log lines unchanged) showing prior state was read, not re-derived. |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch. | yes | Response builds directly on 'H1 confirmed' and 'H2 confirmed' without redoing either; no liquidity or bridge rework appears. |
| Handles the three planted data issues explicitly. | yes | 'Harbour's EBIT was entered in EUR k... corrected -330 to -0.33'; check '0.81+0.60+0.42+(-0.33)+0.08+(-0.53)=1.05 = reported TOTAL EBIT' excludes TOTAL from site analysis while using it to verify; 'Contribution before overhead (EBIT + 6% of revenue)' computed per site. |
| Internally consistent: no figure contradicts the same figure in its own tables. | yes | Table margins (e.g. Westgate -0.35/3.0=-11.7%, -0.53/3.0=-17.7%; Harbour 0.00/5.5=0.0%, -0.33/5.5=-6.0%) match the prose figures throughout. |
| Reports contribution before allocation per site matching reference values; Westgate only site with negative direct contribution. | yes | Table: North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35 — matches reference exactly; interpretation states 'Westgate is a genuine loss-maker on any basis' while Harbour is '0.0%'. |
| States closing Harbour would not raise group EBIT unless overhead removed, in first line or H3 verdict. | yes | H3 doc 'So what' (next to Verdict): 'Closing Harbour on today's reported-EBIT basis would not recover the overhead, only reallocate it onto the remaining five sites.' |
| Marks H3 confirmed/killed/reshaped per expected content. | yes | 02-hypotheses.md: 'H3 ... reshaped 2026-10-14 → H3b'; 'Westgate is a genuine loss-maker even before any overhead allocation' while Harbour's loss is 'the 6%-of-revenue overhead allocation landing on it'. |
| Links back to management's preferred cure and states implication (fix/exit Westgate; don't close Harbour on reported EBIT; overhead review as H4). | yes | 'Westgate ... closing it is a defensible lever'; 'Closing Harbour on today's logic would give up EUR 5.5m of revenue ... for roughly zero contribution gain'; 'That makes H4 (overhead trend / cost-centre data) the highest-impact open item'. |
| Writes h3-site-profitability.md, updates 02-hypotheses.md, adds line to 00-status.md. | yes | All three files shown with corresponding updated content, plus 04-workplan.md updated as well. |
| Does not recommend closing both sites on reported EBIT. | yes | 'the evidence so far only supports closing Westgate' / 'do not recommend Harbour closure until this lands'. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

H3 is done — and it overturns half of management's proposed fix.

**Key finding:** The site data had a units error (Harbour's EBIT was entered in EUR k, not EUR m — corrected -330 to -0.33 after tying it back to the reported TOTAL). Once overhead is stripped back out:

| Site | Margin after overhead | Margin before overhead |
|---|---|---|
| Harbour | -6.0% | **0.0%** |
| Westgate | -17.7% | **-11.7%** |

**Westgate is a genuine loss-maker** even before any overhead allocation — closing it is a defensible lever. **Harbour is breakeven before overhead** — its reported loss is just the 6%-of-revenue overhead charge landing on it like every other site. Closing Harbour on today's logic would give up EUR 5.5m of revenue (16% of group) for roughly zero contribution gain, and the overhead currently allocated to it doesn't disappear — it falls on the other five sites, unless some of it is genuinely driven by having a Harbour site rather than being fixed corporate cost.

That makes **H4 (overhead trend / cost-centre data)** the highest-impact open item: it decides whether closing Harbour would actually release any cost, or just make the remaining sites look worse. I've reflagged it as blocking in `02-hypotheses.md`.

Updated: `research/h3-site-profitability.md` (full workings, data-quality note, open questions), `02-hypotheses.md`, `04-workplan.md`, `00-status.md`.

**Next:** row 4 (H4) is still "waiting for data" — cost-centre detail from controlling. Can you chase that, or do you want me to draft the data request? Also worth deciding now: does the board brief wait for H4 before anyone commits to the Harbour closure, given the numbers above?


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

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price (confirmed). Site-level picture: losses are concentrated in Harbour and Westgate on reported EBIT, but only Westgate is a genuine loss-maker before overhead (-11.7% contribution margin); Harbour is breakeven before overhead (0.0%) and its loss is the 6%-of-revenue overhead allocation landing on it. Closing Harbour on today's reported-EBIT logic would not recover that overhead and would give up EUR 5.5m of revenue (16% of group) for roughly no contribution gain.
**Biggest open risk:** management wants to close Harbour and Westgate on the basis of reported site EBIT; the evidence so far only supports closing Westgate. Whether closing Harbour would release any real cost now depends entirely on H4 (is the allocated overhead actually avoidable).
**Data quality flag:** data/site-pl-2025.csv has Harbour's EBIT entered in EUR k (-330) instead of EUR m like every other row; corrected to -0.33 EUR m for analysis (ties to reported TOTAL). Asked finance to re-issue to avoid recurrence in the H4 pull.
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: H3 site profitability done, reshaped to H3b (research/h3-site-profitability.md). H4 (overhead trend) now the highest-impact open row — it decides whether Harbour's closure is value-creating or value-destroying.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | reshaped 2026-10-14 → H3b |
| H3b | Of the two sites management wants to close, only Westgate is a loss-maker before overhead (-11.7% contribution margin); Harbour is breakeven before overhead (0.0%) and its reported loss is the 6%-of-revenue overhead allocation | high | medium (depends on H4) | H4: is allocated overhead avoidable on site closure | H4 shows overhead is genuinely site-count-driven and would shrink if Harbour closed | open, blocks on H4 |
| H4 | Overhead grew faster than revenue | medium | medium | cost centre data | overhead per EUR of revenue stable | open — now also decides H3b, raise priority |
| H5 | Peers held margin | medium | high | trade association data | peers show the same decline | open |


## File written by the run: engagement/fenmoor/04-workplan.md

# Workplan

*Fictional company. All figures invented for evaluation.*

| Row | Hypothesis | Analysis | Source | End product | Owner | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | H1 | Liquidity check | treasury | research/liquidity.md | EM | 2026-10-05 | done |
| 2 | H2 | Group profit bridge | finance | model/bridge-v1.md | analyst | 2026-10-08 | done |
| 3 | H3 | Site profitability before and after allocated overhead | data/site-pl-2025.csv | research/h3-site-profitability.md | analyst | 2026-10-16 | done, reshaped to H3b |
| 4 | H4 | Overhead trend; also decides whether overhead allocated to Harbour is avoidable on closure (H3b) | cost centres | research/h4-overhead.md | analyst | 2026-10-23 | waiting for data — now highest-impact open row |
| 5 | H5 | Peer margins | trade association | research/h5-peers.md | analyst | 2026-10-23 | not started |


## File written by the run: engagement/fenmoor/research/h3-site-profitability.md

# Research: H3 site profitability before and after allocated overhead, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Hypothesis:** A few sites cause most of the EBIT decline (contribution before allocated overhead, FY2025, by site).
**Kill criterion:** Losses spread evenly across sites.
**Verdict:** reshaped; **evidence strength:** strong (client finance export, single source, used as audited).
**So what:** Losses are concentrated, but not the way management's reported EBIT suggests. Westgate is a genuine loss-maker even before any overhead allocation. Harbour is not — its reported loss is almost entirely the 6%-of-revenue overhead allocation landing on it; before overhead it is breakeven. Closing Harbour on today's reported-EBIT basis would not recover the overhead, only reallocate it onto the remaining five sites.

## Data quality note

`data/site-pl-2025.csv` as received shows Harbour EBIT as **-330**. The file's own header note says the site controller entered Harbour's figure in EUR k, not EUR m like every other row. Read literally, -330 (EUR m) exceeds Harbour's entire EUR 5.5m revenue by 60x, which is not possible. Corrected to **-0.33 EUR m**, this is the only value consistent with the reported TOTAL row (see check below). Treating this as a transcription unit error, not a modelling choice.

**Check:** 0.81 + 0.60 + 0.42 + (-0.33) + 0.08 + (-0.53) = 1.05 = reported TOTAL EBIT. Confirms the correction; recommend finance re-issue the file with Harbour in EUR m to avoid this recurring in the H4 cost-centre pull.

## Findings

| # | Claim | Source (origin) | Date | Type | Supports / contradicts |
|---|---|---|---|---|---|
| 1 | Central overhead is allocated to sites at a flat 6% of site revenue | `data/site-pl-2025.csv` header note, finance | 2026-10-12 | client data | context for H3 |
| 2 | Reported (post-allocation) EBIT: North +0.81, East +0.60, Central +0.42, Harbour -0.33, Mill Lane +0.08, Westgate -0.53 (EUR m) | `data/site-pl-2025.csv`, finance | 2026-10-12 | client data | supports: losses concentrated in 2 of 6 sites |
| 3 | Contribution before allocated overhead (EBIT + 6% of revenue): North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35 (EUR m) | derived from #1, #2 | 2026-10-14 | derived | contradicts management's read of #2: Harbour is breakeven, not loss-making, before overhead |

## Site economics, FY2025

| Site | Revenue (EUR m) | Allocated overhead (6%) | EBIT after overhead | Margin after overhead | Contribution before overhead | Margin before overhead |
|---|---|---|---|---|---|---|
| North | 9.0 | 0.54 | 0.81 | 9.0% | 1.35 | 15.0% |
| East | 7.5 | 0.45 | 0.60 | 8.0% | 1.05 | 14.0% |
| Central | 6.0 | 0.36 | 0.42 | 7.0% | 0.78 | 13.0% |
| Harbour | 5.5 | 0.33 | -0.33 | -6.0% | 0.00 | 0.0% |
| Mill Lane | 4.0 | 0.24 | 0.08 | 2.0% | 0.32 | 8.0% |
| Westgate | 3.0 | 0.18 | -0.53 | -17.7% | -0.35 | -11.7% |
| **TOTAL** | **35.0** | **2.10** | **1.05** | **3.0%** | **3.15** | **9.0%** |

## Interpretation

- **Westgate** is a genuine loss-maker on any basis: -11.7% contribution margin before overhead, -17.7% after. Closing or fixing it is a real lever. Revenue is the smallest of the six sites (EUR 3.0m, 8.6% of group), so closure is low-regret on the numbers seen so far.
- **Harbour** is breakeven before overhead (0.0% contribution margin) and only shows as the group's second-worst site because it absorbs EUR 0.33m of allocated central overhead, same as every other site, at 6% of its revenue. If Harbour closed tomorrow, the group would give up EUR 5.5m of revenue (16% of group revenue, the second-largest site) for a contribution loss of approximately zero — but the EUR 0.33m of overhead currently charged to Harbour does not vanish with the site. Unless some part of central overhead is genuinely driven by operating a Harbour site (a dedicated site manager, local IT, rent) rather than being a fixed corporate cost spread by a revenue key, that EUR 0.33m lands back on North, East, Central, Mill Lane and Westgate's allocations, and group EBIT does not improve by closing Harbour. It would likely fall, by whatever fixed cost (redundancy, site exit, lease break) is triggered on the way out.
- **Mill Lane** is thin after overhead (2.0% margin) but has a respectable 8.0% contribution margin before it — not a closure candidate on this evidence.
- This directly reshapes H3 and the group's framing: losses are concentrated (kill criterion for "even spread" fails, so H3 stands in that narrow sense), but the mechanism matters more than the count. **Reshaped as H3b: management's planned closures (Harbour and Westgate, chosen on reported post-allocation EBIT) only recover value for one of the two sites. Westgate's closure would plausibly help; Harbour's would not, unless H4 shows the overhead allocated to it is actually avoidable.**

## Counter-evidence considered

- Could Harbour's breakeven contribution still be the result of underpricing or a mix problem that would get worse over time? The data available (FY2025 only) cannot test a trend; this would need multi-year site P&L, which has not been requested. Flagged as an open question below rather than assumed away.
- Could the 6% allocation itself be wrong for Harbour (e.g., a site that disproportionately uses shared services, so 6% understates its true cost)? Possible, and would only strengthen the case against closing it on cost grounds, but not tested here.

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Harbour EBIT unit correction (EUR k to EUR m) | unverified | -0.33 EUR m | Finance re-issues the site P&L with Harbour in EUR m | finance |
| Whether allocated overhead is avoidable on site closure | missing | not sized | H4 cost-centre analysis: which central costs scale with site count vs are fixed corporate cost | analyst (H4, due 2026-10-23) |
| Trend (is Harbour's breakeven improving or worsening YoY) | missing | not sized | multi-year site P&L (2023-2025), not yet requested | finance |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Confirmation / re-issue of Harbour FY2025 EBIT in EUR m | email or corrected CSV | Claim #2, avoids the same unit error reappearing in H4 pull | Keep the -0.33 EUR m correction, documented here | finance |
| Site P&L 2023-2025 (3 years, same format) | CSV | Tests whether Harbour's breakeven and Westgate's loss are stable, worsening or improving | Treat FY2025 cut as a single-year snapshot, note as a limitation on the answer page | finance |
| Cost-centre detail behind the 6% overhead key (which costs, which are site-count-driven) | CSV or cost centre export | Directly decides whether closing Harbour releases any real cost (H4) | Workplan row 4 stays open; do not recommend Harbour closure until this lands | finance / controlling

