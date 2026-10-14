# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| no Blocker findings | yes | All findings are Major (4) or Minor (3); no Blocker severity present |
| every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | e.g. Finding 1: 'Board approves EUR1.2m believing there's a live off-ramp...there isn't one'; Finding 4: 'this is one of the two decisions explicitly on the board's agenda...it's a qualitative steer, not a sized comparison'; figures (0.9pp, EUR2.5m range, EUR5.3m, 8.5%, EUR12.7m) match the confirmed |
| names what is good and must survive | yes | Section 'What is good and must survive' lists five specific strengths (triangulated catering economics, external comparables, reversible pilot design, etc.) |
| does not demand a named framework, more length, or more slides | yes | Fixes requested are minimal additions ('Add one line', 'One clause', 'One footnote') or reframing sentences, not structural/framework/length demands |
| does not flag the stated uncertainty or explicit assumptions as weaknesses | yes | Findings critique methodology gaps (missing downside payback, unverifiable revenue build, unsized tradeoff) rather than penalizing the memo for stating a range or assumption |
| does not claim numbers do not tie when they do | yes | 'No internal contradictions found. Recomputed and confirmed: catering contribution...ties...payback lands in year four as stated; EUR5.3m = 2.9 + 2.4; 8.5% = 5.3/62; EUR12.7m gap = 80 − 67.3' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Release with fixes
**In one line:** The two funding asks are evidence-based and internally tight, but the catering off-ramp doesn't actually protect the EUR1.2m already spent, the delivery revenue number can't be independently checked, and the recommendation to revisit the 2031 target rather than the margin floor is argued but not sized — all fixable tonight, none of it reverses the recommendation.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and should it revisit the 2031 target or the margin floor? (given, stated in the To/Decisions line)
**Answer the draft gives:** Fund catering (EUR1.2m) and a delivery pilot (EUR0.3m); don't fund suburban stores or franchising; revisit the target, not the floor. Match: yes.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Skeptical CFO | §"Why catering" / "What would change our view" | The EUR1.2m kitchen is capex-committed and launches April 2027; the stated kill signal (40% framework-agreement take-up) isn't readable until ~month six, after the money is spent and staff hired. It reads as downside protection on the capex but isn't. | Board approves EUR1.2m believing there's a live off-ramp on the spend itself; there isn't one — only on whether to keep running/expand. | Say explicitly that the EUR1.2m is spent regardless of the six-month signal, and that the signal governs continuation/expansion only — or stage capex so a real share sits behind the signal. |
| 2 | Major | Skeptical CFO / Model | §"Why catering" | Payback ("year four") is run only on the EUR2.9m base case, even though the memo's own bottom-up/top-down range goes down to EUR2.5m. No downside payback or break-even shown for the larger, less reversible of the two asks. | Board can't judge how much cushion the EUR1.2m has if catering lands at the low end of the stated range. | Show payback at EUR2.5m (range low) and state the break-even revenue level. |
| 3 | Major | Evidence Auditor / Model | §"Why a delivery pilot" | EUR2.4m 2031 delivery revenue can't be recomputed from what's given (38→60 orders/day, EUR3.10 contribution/order — no average order value, no rollout order base for 18 stores). No contribution/payback figure is given for the implied EUR0.6m rollout, unlike catering's clear payback. | A "right number nobody can verify" on the exec summary; board can't tell if delivery is accretive or just adds top line. | Show the revenue build (orders × average order value × stores) and the rollout's expected contribution/payback, at the same level of rigor as the catering math. |
| 4 | Major | Logician | §"What it adds up to" | "Revisit the target, not the floor" rests on one sentence (floor-dependent options have the weakest evidence) with no quantification of what's forgone. Suburban stores sit only 0.9pp below the 14% floor — close enough that a board member will ask whether a small floor move closes more of the EUR12.7m gap than giving up on the target does. | This is one of the two decisions explicitly on the board's agenda; as written it's a qualitative steer, not a sized comparison, on a headline strategic call. | Add one line: EUR value suburban stores/franchising could add if the floor fell to X%, and what that would cost in blended margin. |
| 5 | Minor | Evidence Auditor | §"Why catering" | EUR190 median order value (feeds the EUR2.5-3.3m bottom-up estimate) comes from 12 interviews with no description of how they were selected. | Soft — partly offset by convergence with the independent top-down estimate. | One clause on selection method (e.g., "random sample of active accounts"), or note explicitly that it's cross-checked by the top-down figure. |
| 6 | Minor | Outsider | §"Why not suburban stores or franchising" | "Store margin" is ambiguous: Brightwell's own P&L margin (suburban) vs. a franchisee's margin net of a 6-8% royalty — not clearly the same metric against the same 14% floor. | Could cost a beat of confusion with an outside board member, not the decision. | One clause clarifying whose margin is measured in each case. |
| 7 | Minor | Evidence Auditor | §"What it adds up to" | The 3% price increase (EUR1.1m) and longer hours (EUR0.9m) figures have no stated method. | Fine for a one-pager; low stakes since both are explicitly rejected as insufficient. | One footnote/appendix pointer if available. |

## Numbers that do not tie

No internal contradictions found. Recomputed and confirmed: catering contribution 2027-2030 (0.16/0.32/0.45/0.51) ties to revenue × 32% − EUR0.35m; payback lands in year four as stated; EUR5.3m = 2.9 + 2.4; 8.5% = 5.3/62; EUR12.7m gap = 80 − 67.3. The one number that doesn't *tie* but can't be *verified* either — EUR2.4m delivery revenue — is captured in Finding 3 rather than here, since nothing elsewhere in the memo contradicts it.

## Missing outside view

- Suburban store margin (13.1%): no view on whether this is a maturity/ramp effect (newer stores) or steady state — matters directly for Finding 4.
- Catering contribution margin (32%) and EUR190 order value: internal-only, no external catering-sector reference point (acceptable as primary data, but unflagged as such).

## Premortem

1. Office catering demand reverts (hybrid-work shift resumes, or a downturn cuts corporate catering budgets) after the kitchen is built and staffed — not addressed beyond the 2025-26 trend.
2. Delivery platform fees rise or a low-cost entrant compresses the EUR3.10/order contribution, so hitting the 50-60 orders/day volume target no longer produces the assumed euros — the stated "what would change our view" test covers volume and cannibalization, not margin.
3. The new central kitchen's own delivery/logistics underperforms, reproducing the "slow delivery" complaint that justified building it — no operational readiness or capacity check is mentioned.

## What is good and must survive

- Genuinely specific recommendation: named investment, owner and launch date for both moves, plus an explicit "do not fund" on the alternatives — a board member knows exactly what to approve.
- Catering economics are triangulated (sales data + bottom-up and top-down estimates + 12 interviews) and the arithmetic ties exactly line by line — rare in a one-page memo.
- Delivery growth is benchmarked against two named external comparables (10-14% achieved by two regional chains), not just an internally invented number.
- Pre-empts the obvious objection on catering (return-to-office rebound) by showing growth continued after attendance stabilized — real causal hygiene, not just correlation.
- Delivery is structured as a genuinely reversible pilot: capped scope, explicit falsifiable pass/fail test, and the EUR0.6m rollout cost is kept out of this ask rather than buried in it.


## Files in work dir after run

- pr-03-input.md
