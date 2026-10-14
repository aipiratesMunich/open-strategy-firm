# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings are rated Major or Minor; no Blocker severity appears in the table |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | E.g. finding 3: 'the board can genuinely disagree on whether to scale — reopening the EUR 0.6m rollout decision without agreed criteria'; figures cited (2.9, 2.4, 5.3, 12.7, 62, 190, 40%, 60/50 orders/day) are internally consistent and match the context's reference arithmetic |
| Names what is good and must survive | yes | '## What is good and must survive' section lists triangulated growth numbers, explicit alternatives analysis, kill criteria, actionable recommendation, and head-on treatment of both decisions |
| Does not demand a named framework, more length, or more slides | yes | Fixes are narrow additions like 'Add one clause stating the organic-growth assumption' and 'Label it explicitly' — no framework, length, or slide-count demands |
| Does not flag stated uncertainty or explicit assumptions as weaknesses | yes | Findings 2 and 6 explicitly target assumptions that are 'never connected'/'never stated' (i.e., undisclosed), not assumptions the memo already discloses |
| Does not claim numbers do not tie | yes | '## Numbers that do not tie\nNone found. The arithmetic is unusually clean for a one-pager... Flag this as a strength to preserve in the rewrite.' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

That tool call was a mistake on my part — this skill reports via markdown text, not that tool. Here's the actual review:

# Partner review: pr-03-input.md ("Fund corporate catering and a delivery pilot in 2027"), gate 3

**Verdict:** Release with fixes
**In one line:** The core recommendation is sound and the arithmetic ties end-to-end, but the kill-switch criteria for both investments have gaps a board member will catch, and the catering case and the "margin floor" decision lean on claims that aren't fully verified.

**Question the draft must answer:** Which growth moves should the board fund for 2027, and does the board need to revisit the 2031 revenue target or the margin floor? (given, from the board-meeting line)
**Answer the draft gives:** Fund the catering unit (EUR 1.2m) and the delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the 2031 target, not the floor.

These match directly — no reconstruction needed, and the recommendation is specific (owner, amount, start date) for both moves.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Evidence Auditor | "Why catering" | Catering's EUR 2.9m base case has no outside-view comparator (delivery cites two regional chains; catering doesn't), and the EUR 190 median order value feeding the bottom-up model rests on only 12 interviews. | A board member asks "what did any comparable catering launch actually achieve?" and there's no answer; the per-order input carries more precision than a 12-person sample supports. | Cite one external catering/food-service benchmark, and note the interview sample size next to the EUR 190 figure. |
| 2 | Major | Logician | "What would change our view" (catering) | The kill criterion — "fewer than 40% of office customers sign framework agreements in six months" — is never connected to the orders × order-value model used to justify the EUR 1.2m spend. | The board has no real early-warning signal: hitting or missing 40% doesn't tell them whether the EUR 2.9m case is on track. | Tie the threshold to the revenue model (e.g., order volume vs. the EUR 1.6m 2027 case), or add a sentence explaining how framework-agreement signing maps to the forecast. |
| 3 | Major | Skeptical CFO | "Why a delivery pilot" + its "what would change our view" | Success is defined as "≥60 orders/day without lowering in-store transactions"; failure is "<50 orders/day or transactions down >3%." Results of 50–59 orders/day, or a 0–3% transaction dip, trigger neither rule. | At the end of the pilot, management and the board can genuinely disagree on whether to scale — reopening the EUR 0.6m rollout decision without agreed criteria. | Close the gap: one threshold pair that covers the full range (e.g., scale at ≥60/≤2% decline, kill at <50/>3% decline, extend otherwise). |
| 4 | Major | Skeptical CFO | "Why a delivery pilot" | The pilot runs in the 8 highest order-density stores, but the EUR 2.4m 2031 number assumes the same economics hold across all 18 high-street stores on rollout. | If density-dependent economics don't hold in the other 10 stores, the EUR 2.4m case could miss even if the pilot passes cleanly — the board's confidence in the second-stage number is unearned. | Flag that rollout economics in the remaining 10 stores are unproven, and that the EUR 0.6m rollout decision should re-test density sensitivity. |
| 5 | Major | Logician / Evidence Auditor | "Why not suburban stores or franchising" | The claim that 6–8% franchise royalties "would cut store margin below the floor" is asserted without showing the store margin baseline the royalty is subtracted from. | A board member can't verify the rejection and may ask for the calculation live in the meeting. | Show the baseline margin for franchise-candidate stores and the arithmetic against the 14% floor. |
| 6 | Major | Logician | "What it adds up to" | The EUR 12.7m gap (80 − 62 − 5.3) implicitly assumes the existing EUR 62m base holds flat to 2031; this assumption is never stated. | If the base business is expected to grow or shrink organically, the size of the gap — and the case for revisiting the target rather than the floor — changes. | Add one clause stating the organic-growth assumption behind the EUR 62m base. |
| 7 | Minor | Evidence Auditor | "Why not suburban stores" | The 13.1%-vs-14% suburban margin rests on one year (2025 P&L) with no trend shown. | Low — direction is plausible and this supports a "don't fund" call, not a "do fund" one. | Add a 2–3 year trend or note 2025 was representative. |
| 8 | Minor | Outsider | "Why a delivery pilot" | "(about EUR 0.6m, a separate board decision...)" is ambiguous — unclear if it's rollout capex or something else, right after a revenue figure. | A skim-reader could misread it as a revenue number. | Label it explicitly, e.g. "(rollout investment: about EUR 0.6m)." |
| 9 | Minor | Logician | "What it adds up to" | Unstated whether the 12 stores getting longer hours overlap with the 8 delivery-pilot stores. | Possible double-counted effect if they overlap, but small relative to the total. | Add one clause confirming the store lists are (or aren't) independent. |

## Numbers that do not tie

None found. The arithmetic is unusually clean for a one-pager: catering trajectory (1.6/2.1/2.5/2.7m) × 32% − EUR 0.35m fixed cost reproduces the stated profit figures exactly; 2.9 + 2.4 = 5.3; 5.3/62 = 8.5%; 80 − 62 − 5.3 = 12.7; 1.1 + 0.9 = 2.0, which is correctly "less than a quarter" of 12.7. Flag this as a strength to preserve in the rewrite.

## Missing outside view
- Catering 2031 revenue (EUR 2.9m base case): no comparable company/launch cited, unlike delivery's two regional-chain benchmark.
- Franchising royalty impact: no current store-margin baseline shown to check the 6–8% royalty claim against.

## Premortem
1. Central kitchen costs or throughput problems delay catering past the year-4 payback, and the stated kill-switch (framework agreements, finding 2) doesn't catch it because it isn't tied to the revenue/cost model.
2. Full delivery rollout underperforms because the 10 lower-density stores don't replicate the pilot's economics (finding 4) — not addressed anywhere in the memo.
3. A competitor response (existing catering supplier cuts delivery times, a delivery platform enters the region) erodes the take-up or margins the model assumes — not mentioned at all.

## What is good and must survive
- Both growth numbers are triangulated: catering by bottom-up + top-down + interviews; delivery by pilot data + two independent external comparators.
- The memo explicitly rules out the two obvious alternatives (suburban, franchising) with reasons, rather than silently dropping them.
- Explicit "what would change our view" kill criteria for both moves — rare in a one-pager and valuable; just needs tightening (findings 2–3), not removing.
- The recommendation is fully actionable: amount, owner, launch date for each move, and a clear ask on the second (target-vs-floor) decision.
- The two decisions the board actually needs (fund/not fund; target-vs-floor) are both addressed head-on, in the memo's own terms.


## Files in work dir after run

- pr-03-input.md
