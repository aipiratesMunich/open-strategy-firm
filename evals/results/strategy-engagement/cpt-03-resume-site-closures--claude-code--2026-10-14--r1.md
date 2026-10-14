# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and existing bridge before analysing, and names H3 as the branch | yes | Response opens 'Fenmoor H3 complete... (3 of 5 branches analysed)' and the data note reconciles Harbour's figure 'to the 1.05 EUR m group total' (the bridge's total), while 02-hypotheses.md preserves H1/H2 prior statuses untouched — consistent with having read all three files and the bridge first. |
| Must not re-ask the problem statement, redo the liquidity check or rebuild the bridge from scratch | yes | 00-status.md shows liquidity (2026-10-05) and bridge (2026-10-08) entries left as prior dated log lines; the new work is confined to 'site profitability before/after overhead done (research/h3-site-profitability.md)'. |
| Handles the three planted data issues explicitly (Harbour unit error, TOTAL row excluded from analysis but used to check sum, contribution before 6% overhead) | yes | 'Harbour EBIT as -330... Reading it as EUR k gives -0.33 EUR m, which reconciles exactly to the 1.05 EUR m total' plus a dedicated 'Contribution before allocated overhead' table with TOTAL row used only as a check, not as a seventh site in the narrative bullets. |
| Internally consistent: no figure contradicts the same figure in its own tables | yes | All derived figures reconcile: e.g. Harbour -0.33 EBIT + 0.33 overhead = 0.00 contribution, and contribution total 3.15 = EBIT total 1.05 + overhead total 2.10, matching across both tables. |
| Reports contribution before allocation per site in line with reference values and identifies Westgate as the only site with negative direct contribution | yes | Table gives North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35 — exactly matching reference; text states 'Westgate loses money before any overhead allocation... Harbour breaks even before overhead (0.00 contribution)'. |
| States closing Harbour would not raise group EBIT unless overhead is removed, on first line or in H3 verdict | yes | Within the Verdict section: 'Closing Harbour on the reported-EBIT logic would not [deliver the expected gain]... for no EBIT gain unless central overhead itself falls by a matching amount.' |
| Marks H3 confirmed, killed or reshaped (expected: reshaped — one true loss maker, decline mostly the group-wide cost issue already in H2) | NO | 02-hypotheses.md records H3 status as 'partially confirmed 2026-10-14', and the research verdict explicitly says 'reject in favor of concentrated losses' — reaffirming site concentration rather than reshaping toward the expected framing that the decline is mostly H2's group-wide cost issue with only |
| Links back to management's preferred cure and says what it means for the answer | yes | 'Implication for management's preferred cure: closing Westgate removes a real loss. Closing Harbour on the reported-EBIT logic would not...' and follow-up explicitly feeds into H4 (overhead trend). |
| Writes research/h3-site-profitability.md, updates 02-hypotheses.md, adds a line to 00-status.md | yes | All three files are present and updated: research/h3-site-profitability.md with full writeup, 02-hypotheses.md H3 row updated, and 00-status.md log line '2026-10-14: site profitability before/after overhead done...'. |
| Must not recommend closing both sites on reported EBIT | yes | The write-up explicitly argues against closing Harbour on reported EBIT ('Closing Harbour on the reported-EBIT logic would not [deliver the gain]'), and never recommends closing both sites on that basis. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

**Fenmoor H3 complete.** Site profitability is now done (3 of 5 branches analysed). Key findings:

- Caught a data error in finance's export: Harbour's EBIT was entered as **-330** instead of **-0.33 EUR m** (unit mismatch, EUR k vs EUR m) — confirmed by reconciling to the 1.05 EUR m group total. Flagged for finance to fix at source.
- **Westgate** loses money even before overhead allocation (-0.35 EUR m contribution, -11.7% margin) — a real operating loss.
- **Harbour** breaks even before overhead (0.00 contribution) — its reported -0.33 EBIT is entirely the 6%-of-revenue central overhead charge, not an operating shortfall.
- This splits management's "close the two weakest sites" plan: Westgate closure would remove a genuine loss; Harbour closure would not deliver the expected EBIT gain, since the 0.33 EUR m of overhead currently allocated to it would just redistribute onto the remaining sites unless central costs themselves fall.

Updated `02-hypotheses.md`, `04-workplan.md`, and `00-status.md` accordingly; full writeup in `research/h3-site-profitability.md`.

Next open rows: H4 (overhead trend — still waiting on cost-centre data) and H5 (peer margins, due 2026-10-23).


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

**Current best answer (v1):** Margin fell because paper and energy cost per job rose faster than price; losses are concentrated in Harbour and Westgate but for different reasons — Westgate is a genuine operating loss, Harbour only looks negative because of allocated overhead.
**Biggest open risk:** management wants to close Harbour and Westgate on the basis of reported site EBIT; Harbour's reported EBIT is overhead allocation, not an operating loss, so closing it would not deliver the EBIT saving management expects.
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: site profitability before/after overhead done (research/h3-site-profitability.md). Caught and corrected a unit error in the finance export (Harbour EBIT entered as -330 instead of -0.33 EUR m). Westgate loses money before overhead allocation; Harbour breaks even before overhead — its -0.33 EBIT is entirely the allocated central overhead charge.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | partially confirmed 2026-10-14 |
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

**Data note:** the finance export (data/site-pl-2025.csv) shows Harbour EBIT as -330, with the site controller's note that it was entered in EUR k. Taken at face value this breaks the total (sum of site EBIT would be roughly -331 EUR m against a reported group total of 1.05 EUR m). Reading it as EUR k gives -0.33 EUR m, which reconciles exactly to the 1.05 EUR m total. Corrected figure used throughout below; flagged to finance to fix at source.

**Site EBIT after allocated overhead** (central overhead allocated at 6% of site revenue):

| Site | Revenue (EUR m) | EBIT (EUR m) | EBIT margin |
|---|---|---|---|
| North | 9.0 | 0.81 | 9.0% |
| East | 7.5 | 0.60 | 8.0% |
| Central | 6.0 | 0.42 | 7.0% |
| Harbour | 5.5 | -0.33 (corrected) | -6.0% |
| Mill Lane | 4.0 | 0.08 | 2.0% |
| Westgate | 3.0 | -0.53 | -17.7% |
| TOTAL | 35.0 | 1.05 | 3.0% |

**Contribution before allocated overhead** (EBIT with the 6%-of-revenue overhead charge added back):

| Site | Allocated overhead (EUR m) | Contribution before overhead (EUR m) | Contribution margin |
|---|---|---|---|
| North | 0.54 | 1.35 | 15.0% |
| East | 0.45 | 1.05 | 14.0% |
| Central | 0.36 | 0.78 | 13.0% |
| Harbour | 0.33 | 0.00 | 0.0% |
| Mill Lane | 0.24 | 0.32 | 8.0% |
| Westgate | 0.18 | -0.35 | -11.7% |
| TOTAL | 2.10 | 3.15 | 9.0% |

**Verdict:** partially confirmed; **evidence strength:** medium (2025 snapshot only; no 2023 site-level comparator yet, so the *trend* can't be tested directly from this data — see follow-up).

- Profitability is not spread evenly: North, East and Central carry the group; Mill Lane is thin but positive; Harbour and Westgate are the two weakest sites, consistent with management's framing so far.
- But the two are not the same problem. **Westgate loses money before any overhead allocation** (-0.35 EUR m contribution, -11.7% margin) — a genuine operating loss. **Harbour breaks even before overhead** (0.00 contribution) — its reported -0.33 EBIT is entirely the allocated central overhead charge, not an operating shortfall.
- Implication for management's preferred cure: closing Westgate removes a real loss. Closing Harbour on the reported-EBIT logic would not — the 0.33 EUR m of central overhead currently allocated to Harbour doesn't disappear when Harbour closes; it lands on the other five sites (or must be cut from actual central cost). The group would give up Harbour's 5.5 EUR m revenue and its 0.33 EUR m contribution to fixed cost for no EBIT gain unless central overhead itself falls by a matching amount.
- Kill criterion ("losses spread evenly across sites") not met — reject in favour of concentrated losses, but the Harbour figure needs reframing before it goes anywhere near the board paper.

**Follow-up:** request 2023 site P&L to confirm whether Harbour/Westgate's position worsened since 2023 or was always this shape (feeds H4, overhead trend, row 4).

