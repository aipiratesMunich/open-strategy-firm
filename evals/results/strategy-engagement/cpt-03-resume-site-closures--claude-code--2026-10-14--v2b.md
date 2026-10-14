# cpt-03-resume-site-closures on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reads 00-status.md, 02-hypotheses.md, 04-workplan.md and existing bridge before analysing, and names H3 as the branch | yes | Output reconciles to 'the group bridge's 2025 EBIT of €1.05m', updates workplan row 3 and hypotheses table consistent with prior content, and explicitly frames the whole response around 'H3 done'. |
| Does not re-ask the problem statement, redo the liquidity check, or rebuild the bridge from scratch | yes | Liquidity and bridge are only referenced as already-done prior work ('research/liquidity.md', 'model/bridge-v1.md'); no re-derivation is shown. |
| Handles the three planted data issues: Harbour -330 as EUR -0.33m, excludes TOTAL from site analysis but uses it to check the sum, computes contribution before 6% overhead allocation | yes | 'Harbour's EBIT was received as -330... Reading it as EUR k gives -0.33 EUR m. This reconciles the site total exactly to the group bridge's 2025 EBIT'; TOTAL row (3.15/1.05/2.10) is used only for reconciliation, not in the per-site Finding/Verdict analysis; table explicitly labelled 'Contribution be |
| Internally consistent figures across text and tables | yes | Table sums check out: EBIT after overhead 0.81+0.60+0.42-0.33+0.08-0.53=1.05; overhead 0.54+0.45+0.36+0.33+0.24+0.18=2.10; contribution 1.35+1.05+0.78+0.00+0.32-0.35=3.15, all matching stated totals and prose. |
| Reports contribution before allocation per site matching reference values and identifies Westgate as the only site with negative direct contribution | yes | North 1.35, East 1.05, Central 0.78, Harbour 0.00, Mill Lane 0.32, Westgate -0.35 — exact match to reference; 'Westgate is the one genuine problem: contribution is negative (-0.35 EUR m)'. |
| States closing Harbour would not raise group EBIT unless overhead is removed, on first line or in H3 verdict | yes | 'Closing it removes EUR 5.5m of revenue that was carrying EUR 0.33m of central overhead — that overhead does not disappear, it lands on the remaining five sites... Closing Harbour on today's reported-EBIT basis risks manufacturing the next "weak site" rather than fixing anything.' |
| Marks H3 confirmed, killed, or reshaped (expected: refined to Westgate as the real loss-maker) | yes | 'H3 confirmed, but refined — the decline is not "a few sites," it is effectively concentrated in one site (Westgate)...' |
| Links back to management's preferred cure and states what it means for the answer | yes | 'Management's proposed cure is only half right: Westgate is genuinely loss-making before overhead and is a legitimate closure/turnaround candidate; Harbour breaks even before allocated overhead and is not... Overhead trend (H4) now matters more, not less.' |
| Writes h3-site-profitability.md, updates 02-hypotheses.md, adds a line to 00-status.md | yes | All three files are shown written with the expected content (research/h3-site-profitability.md full analysis, H3 row updated to 'confirmed, refined...', status log entry dated 2026-10-14). |
| Does not recommend closing both sites on reported EBIT | yes | 'Harbour should not be read as a closure candidate from this data'; only Westgate is called a 'legitimate closure/turnaround candidate'. |

## Transcript

## Turn 1

**User:** Continue the Fenmoor turnaround. Site numbers are in. (Attached in the working directory: engagement/fenmoor/.)

**H3 done — and it reverses half the management case.** Summary:

- Caught a units bug in finance's data: Harbour's EBIT was entered as `-330`, which only works as **-330 EUR k** (-0.33m), not -330m as the column header implied. Confirmed by reconciling the site total exactly to the group bridge's 2025 EBIT of €1.05m. This needs finance's written sign-off before it's in a board pack.
- Splitting EBIT into contribution before/after the 6%-of-revenue central overhead allocation: **Harbour breaks exactly even before overhead** — its entire reported loss is the allocation charge, which would just land on the other five sites if Harbour closed. **Westgate is the only site genuinely loss-making on contribution** (-€0.35m), making it the one real closure/turnaround candidate.
- Updated `02-hypotheses.md` (H3 confirmed/refined), `04-workplan.md` (row 3 done), and `00-status.md` (now 3 of 5 analyses done, best-answer and risk lines rewritten to reflect that closing Harbour isn't supported by this data, and that H4 overhead trend now matters more).

Remaining open rows: **H4** (overhead trend — still waiting for cost-centre data) and **H5** (peer margins, due 2026-10-23). Want me to chase the overhead data or start on H5 peer research next?


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

**Current best answer (v2):** Margin fell because paper and energy cost per job rose faster than price (confirmed, group bridge). Management's proposed cure is only half right: Westgate is genuinely loss-making before overhead and is a legitimate closure/turnaround candidate; Harbour breaks even before allocated overhead and is not — its reported loss is an artefact of a 6%-of-revenue central overhead charge that would simply relocate to the remaining sites if Harbour closed. Overhead trend (H4) now matters more, not less.
**Biggest open risk:** board papers go out assuming "close Harbour and Westgate" on reported EBIT; this needs correcting before the 2 December board, and the Harbour EBIT figure itself needs finance's written confirmation (see research/h3-site-profitability.md data correction).
**Log:**
- 2026-10-05: liquidity checked: 26 weeks of cash, covenant headroom adequate (research/liquidity.md).
- 2026-10-08: group bridge 2023-2025 done (model/bridge-v1.md).
- 2026-10-12: site P&L 2025 received from finance, saved to data/site-pl-2025.csv.
- 2026-10-14: site profitability before/after allocated overhead done (research/h3-site-profitability.md). Caught a units error in Harbour's EBIT (-330 read as EUR m instead of EUR k) before it reached the board pack; corrected figure reconciles exactly to the group bridge total. Finding: only Westgate is loss-making before overhead; Harbour is not a closure candidate on this data.


## File written by the run: engagement/fenmoor/02-hypotheses.md

# Hypotheses

*Fictional company. All figures invented for evaluation.*

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Cash covers at least 13 weeks | high | low | 13-week cash view | runway under 13 weeks | confirmed 2026-10-05 |
| H2 | Price did not keep up with paper and energy cost per job | high | medium | group bridge | price tracked input costs | confirmed 2026-10-08 |
| H3 | A few sites cause most of the decline | high | high | site P&L 2025, contribution before allocated overhead | losses spread evenly across sites | confirmed, refined 2026-10-14: only Westgate is loss-making before overhead; Harbour breaks even before overhead and is not a closure candidate on this basis (research/h3-site-profitability.md) |
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

# Research: H3 site profitability, before and after allocated overhead, 2026-10-14

*Fictional company. All figures invented for evaluation.*

**Source:** data/site-pl-2025.csv (finance export). EBIT as received is after central overhead, allocated to sites at 6% of site revenue.

**Data correction:** Harbour's EBIT was received as -330, which the file flags as "entered in EUR k by site controller." Taken at face value (-330 EUR m) this exceeds total group revenue and is clearly a units slip. Reading it as EUR k gives -0.33 EUR m. This reconciles the site total exactly to the group bridge's 2025 EBIT (1.05 EUR m, model/bridge-v1.md) — North through Westgate sum to 1.05 only under this reading. Using -0.33 below; flagged to finance for written confirmation before this goes in the board pack.

**Site EBIT, corrected, and contribution before allocated overhead (add back 6% of revenue):**

| Site | Revenue (EUR m) | EBIT after overhead (EUR m) | Overhead allocated (EUR m) | Contribution before overhead (EUR m) |
|---|---|---|---|---|
| North | 9.0 | 0.81 | 0.54 | 1.35 |
| East | 7.5 | 0.60 | 0.45 | 1.05 |
| Central | 6.0 | 0.42 | 0.36 | 0.78 |
| Harbour | 5.5 | -0.33 | 0.33 | 0.00 |
| Mill Lane | 4.0 | 0.08 | 0.24 | 0.32 |
| Westgate | 3.0 | -0.53 | 0.18 | -0.35 |
| **TOTAL** | **35.0** | **1.05** | **2.10** | **3.15** |

**Finding:** the two sites management proposes to close are not the same kind of problem.

- **Harbour** breaks exactly even before allocated overhead. Its entire reported loss is the 6%-of-revenue overhead charge. Closing it removes EUR 5.5m of revenue that was carrying EUR 0.33m of central overhead — that overhead does not disappear, it lands on the remaining five sites (roughly another ~1pp of revenue each), which would push Mill Lane (contribution only EUR 0.32m) close to reported loss next. Closing Harbour on today's reported-EBIT basis risks manufacturing the next "weak site" rather than fixing anything.
- **Westgate** is the one genuine problem: contribution is negative (-0.35 EUR m) even before any overhead is charged. At EUR 3.0m revenue it is also the smallest site. This is consistent with a structural issue (scale, price, or cost per job) rather than an overhead allocation artefact.

**Verdict:** H3 confirmed, but refined — the decline is not "a few sites," it is effectively concentrated in one site (Westgate) on a basis that strips out allocation effects. Harbour should not be read as a closure candidate from this data; it is a flag that central overhead (EUR 2.1m, 6% of revenue) is large enough to swing a break-even site into the group's apparent second-largest loss. That overhead level is exactly what H4 (overhead trend) needs to test next.

**Evidence strength:** moderate. One year of site data, one allocation basis, and one unconfirmed data correction. Recommend: (1) finance confirms the Harbour units correction in writing, (2) check whether Westgate's contribution shortfall is recent or structural (need 2023-2025 trend by site, not just 2025), before taking a closure recommendation to the board.

