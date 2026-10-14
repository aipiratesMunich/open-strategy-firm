# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (4/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | **Verdict:** Return |
| no Blocker findings | NO | Finding #1 listed with severity 'Blocker' |
| at most two Major findings, each with a concrete, defensible reason | NO | Three findings (#2, #3, #4) are rated 'Major' |
| names what is good and must survive | yes | '## What is good and must survive' section lists numbers tying, sourced rejections, falsifiable kill criteria, honest gap disclosure |
| does not demand a named framework, more length, or more slides | yes | No requests for frameworks, additional length, or slides found in findings |
| does not flag stated uncertainty or explicit assumptions as weaknesses | yes | Kill criteria are explicitly praised: 'this is exactly the kind of stated uncertainty that should be commended, not penalized' |
| does not claim numbers do not tie | yes | '## Numbers that do not tie\n\nNone found.' and lists recalculations confirming the math checks out |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow.

# Partner review: Brightwell catering & delivery memo, gate 3

**Verdict:** Return
**In one line:** The board is asked to decide *today* whether to revisit the 2031 revenue target or the 14% margin floor, and the memo gives them nothing to decide it with — not even what "revisit the floor" would actually unlock.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and how should it resolve the gap to the 2031 target? (*given* — stated in the To: line)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); reject suburban stores and franchising; the board must separately decide whether to lower the 2031 target or the margin floor, since the funded moves close less than half the gap.

The two answers match on decision (1). They do not match on decision (2): the memo names the choice but doesn't equip the board to make it.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Decision Maker | Line 5, 15 | Decision (2) — revisit the target or the floor — is explicitly due at this meeting, but the memo never explains what either path means in practice. It never states that lowering the floor by ~1pt (13.1% → below 14%) would make suburban stores viable, the one piece of math that would make this decision concrete. | The board either stalls on decision (2) or picks a side with no idea what it actually changes — e.g., votes to "keep the floor" without realizing they just re-closed suburban expansion, or "lower the floor" without knowing by how much or for what gain. | Add one sentence connecting the floor to the rejected alternatives (e.g., "lowering the floor to 13% would qualify the suburban stores for 2028 funding, worth up to EUR Xm"), and name who brings a target/floor recommendation back, and by when. |
| 2 | Major | Evidence Auditor | Line 9 | The bottom-up and top-down catering estimates are presented as independent triangulation, but both appear to run on the same input — the EUR 190 median order value from the 12 interviewed managers. Sample selection (customers only? random? including non-customers) is also undisclosed. | A board member who asks "how were these two estimates derived independently?" exposes that they share one small, unvetted survey input, undercutting the strongest evidence in the memo. | State whether bottom-up and top-down use the same order-value/spend-per-head figure; if so, call it one data point, not two-way triangulation. Add one line on how the 12 managers were selected. |
| 3 | Major | Skeptical CFO | Lines 9, 11 | Delivery has an outside-view benchmark (two regional chains); catering does not — the 32% margin and 4-year payback rest only on Brightwell's own 2025 P&L. Neither line shows a downside case: delivery shows only an upside (18%→EUR 3.5m), catering shows a range (2.5–3.3m) but no scenario tying that low end back through the payback math. | The board can't tell whether the central kitchen's margin/payback is realistic for a new build versus hoped-for, and has no visibility into what happens to the EUR 5.3m total (and the EUR 12.7m gap) if either line lands at the bottom of its own stated range. | Cite one external comparable for corporate-catering/central-kitchen economics, or label the gap. Add one downside row (e.g., catering at EUR 2.5m, delivery at 10% growth) and restate the resulting total and gap. |
| 4 | Major | Logician | Lines 11, 15 | The EUR 2.4m delivery figure "by 2031" implicitly requires the 12-month, 8-store pilot to succeed *and* a further network rollout — a second investment decision that isn't being funded or sized in this memo (only EUR 0.3m is asked for). | The board could believe EUR 1.5m total 2027 spend gets them most of the way to EUR 5.3m, when in fact part of that number depends on an unbudgeted future decision whose cost is never stated. | Add one sentence: the EUR 2.4m assumes a successful pilot leads to a wider rollout, to be decided in year two with its own capex, to be sized then. |
| 5 | Minor | Skeptical CFO | Line 11 | The EUR 3.10/order contribution assumes today's platform fee structure holds; no sensitivity to rising platform commissions is shown. | Low — the pilot is small (EUR 0.3m, reversible) and already gated by explicit stop/go criteria. | One line noting fee sensitivity is part of what the pilot will test before any scale decision. |
| 6 | Minor | Logician | Line 13 | "Doing nothing" isn't explicitly named among the rejected alternatives. | Low — the gap-to-target section already makes the cost of inaction clear. | Add a half-sentence: "without these moves, the gap to EUR 80m is the full EUR 18m." |
| 7 | Minor | Evidence Auditor | Line 9 | The year-by-year catering trajectory runs 2027–2030 (1.6 → 2.7); the 2031 base case (2.9) used elsewhere is never shown in that same sequence. | Low — the implied 2031 continuation is plausible and doesn't change the payback conclusion. | Add the 2031 figure to the same sequence. |

## Numbers that do not tie

None found. Catering payback math (0.16/0.32/0.45/0.51 against EUR 1.2m), the EUR 5.3m total (2.9+2.4), the 8.5% growth figure, the EUR 12.7m gap, and the "less than a quarter closed" claim on price+hours (2.0/12.7 ≈ 16%) all check out on independent recalculation. This is uncommon and worth preserving as-is.

## Missing outside view

- **Catering margin and payback (32% contribution, EUR 1.2m capex, 4-year payback):** no comparable corporate-catering or central-kitchen launch cited — only Brightwell's own 2025 P&L.
- **Downside growth case, both lines:** delivery cites a 10–14% external range but only models 12% (base) and 18% (upside); catering cites a 2.5–3.3m range but never re-runs the payback at the low end.

## Premortem

1. Growth decelerates faster than the modeled trajectory (office catering pain point gets fixed by the incumbent supplier, or hybrid-work attendance declines further) — there's no downside case showing what happens to the 4-year payback if this occurs.
2. The central kitchen's ramp-up (staffing, capacity, quality) runs slower or costlier than planned, pushing payback past year four — no capacity contingency is named for an EUR 1.2m, largely irreversible investment.
3. Platform commissions rise or discounting is needed to win delivery volume, so hitting 60 orders/day doesn't deliver the assumed EUR 3.10 contribution — not stress-tested (Finding 5).

## What is good and must survive

- The numbers tie everywhere they're checked — rare, and should survive the rewrite untouched.
- Catering's growth story draws on four independent-in-spirit sources (real sales data, interviews, bottom-up, top-down) and the memo is honest that two of those four share an input (once fixed per Finding 2, this becomes genuinely strong).
- Suburban stores and franchising are rejected with sourced, quantified reasons (13.1% vs. 14% floor; 6–8% royalty offers), not asserted.
- Explicit, falsifiable kill criteria ("40% framework agreements," "50 orders/day," "3% cannibalization") — this is exactly the kind of stated uncertainty that should be commended, not penalized.
- The memo doesn't hide the shortfall: it states the EUR 12.7m gap plainly and shows that price/hours levers don't close it, rather than papering over it.

## What "fixed" looks like

Same recommendation on catering and delivery, unchanged. For decision (2): "Lowering the margin floor to 13% would make the suburban stores (13.1% margin) viable, worth an estimated EUR Xm by 2031 at the cost of accepting lower returns network-wide; holding the floor means revisiting the EUR 80m target downward by roughly the EUR 12.7m gap, net of any downside in catering or delivery. We recommend [X] and will bring a fully costed comparison to the [date] board meeting." The EUR 5.3m total should carry one sentence noting that EUR 2.4m of it depends on a second, unbudgeted delivery rollout decision in 2028, and the catering/delivery figures should each show a stated downside case alongside the base case already given.


## Files in work dir after run

- pr-03-input.md
