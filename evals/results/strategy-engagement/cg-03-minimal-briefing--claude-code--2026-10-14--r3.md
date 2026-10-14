# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and required growth rate (~9%/yr 2026-2029), contrasted with flat history | yes | "31m (2026) → 40m by 2029 is +9m, +29% in three years, ≈8.9%/yr compound — after years of flat growth." |
| Asks a short, grouped set of questions (≤~3 rounds), proceeds without waiting if user has no more data | NO | User explicitly said 'That's all I've got right now, what's your take?' yet the answer ends by asking permission to proceed: "Want me to go that route, or keep this at the 'take' level for now?" rather than proceeding with the best available analysis. |
| Issue tree from the gap with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with hypothesis and kill criterion | NO | The response gives a flat 'Ranked hypotheses' table (market/share, pricing, wallet share, adjacency, lever-sum) with kill criteria, but never structures it as a tree with explicit 'momentum' or 'portfolio' branches as required. |
| Keeps inorganic moves out of scope or names them as ruled out by the board | yes | "with M&A off the table, a 29% lift almost never comes from one lever" |
| States analysis order (momentum case and market vs share split first) | NO | Market-vs-share is flagged as the key first question, but no mention of a 'momentum case' being analyzed first; the required explicit analysis-order statement is absent. |
| Provisional answer/most likely shape, explicitly labelled as hypothesis with low confidence and reason | yes | "Day-one hypothesis (low confidence, provisional): with M&A off the table, a 29% lift almost never comes from one lever..." |
| Open-questions table in skill's format (question, why it matters, who can answer, effect on the answer) | NO | Table only has two columns: "/ Question / Why it matters /" — missing 'who can answer' and 'effect on the answer' columns. |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts | yes | "(ASSUMPTION flag: I'm not treating any textile-market growth rate as fact — that needs checking, not recalling.)" |
| Must not deliver a generic list of growth frameworks/ideas unconnected to the EUR 9m gap | yes | All hypotheses (pricing, wallet share, adjacency) are explicitly tied back to closing the 9m gap, not generic framework listing. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

**Answer:** Can't size this yet, but the shape of the problem is clear enough to say where to look first. Here's the take, with what's assumed flagged as assumption.

**The gap:** 31m (2026) → 40m by 2029 is +9m, +29% in three years, ≈8.9%/yr compound — after years of flat growth. That's a real inflection, not a tweak. Before anything else, the question that decides everything else: **has revenue been flat because the market is flat, or because Pellworth has been losing share in a market that's actually growing?** Those two situations need opposite playbooks (defend/reprice vs. go win adjacencies), and right now I don't know which one you're in. *(ASSUMPTION flag: I'm not treating any textile-market growth rate as fact — that needs checking, not recalling.)*

**Day-one hypothesis (low confidence, provisional):** with M&A off the table, a 29% lift almost never comes from one lever. It's more likely a combination of (a) price/mix — moving revenue toward higher-value or less commoditized lines if Pellworth is underpriced relative to value delivered, (b) wallet share on the existing customer base — services, finishing, private label, anything currently leaking to third parties, and (c) one adjacency (new channel, geography, or customer segment) where Pellworth already has a right to win. Pure core-volume growth in a mature textiles market is the least likely single answer to carry 9m.

**Ranked hypotheses, with kill criteria:**

| # | Hypothesis | Kill criterion |
|---|---|---|
| 1 | Market is flat/shrinking, not just share loss — core growth alone can't close the gap | Market data shows >2–3%/yr growth with Pellworth share stable or rising for 3 years → reframe as a share problem, not a market problem |
| 2 | Pellworth is underpriced vs. value delivered | Like-for-like price gap fully explained by spec/service differences → kill, look elsewhere |
| 3 | Meaningful wallet share (services, adjacent SKUs) currently goes to competitors on Pellworth's own customer base | Third-party spend on the installed base is small or already captured → lever below ~1–2m, not material |
| 4 | At least one adjacency (segment/geography/channel) exists where Pellworth has a right to win without capital beyond what the board will fund | No adjacency clears a basic Five Forces / right-to-win test → organic plan can't close the gap, board needs to hear that early |
| 5 | Two or three levers, on base case, can plausibly close ≥70% of the 9m within the margin floor | Base case sums to well under half the gap → the 2029 target itself needs to go back to the board, not get stretched with hopeful assumptions |

**What I actually need from you to move past "take" into a real sizing exercise:**

| Question | Why it matters |
|---|---|
| Margin today, and the margin floor the board will accept while growing | Revenue growth that dilutes margin below the floor fails the brief even if it hits 40m |
| Why has revenue been flat — demand, price competition (e.g. import pressure), capacity, customer losses? | Determines whether this is a market problem, a share problem, or a cost/capacity problem wearing a growth costume |
| Product/customer mix behind the 31m, and any concentration risk | Tells us where the installed-base and adjacency levers actually sit |
| Capital available for the plan, and anything else ruled out besides M&A (new plants, dilution, specific geographies) | A plan that needs capital or moves the board won't fund isn't an answer |
| Decision date and what the board is actually approving (a plan, a budget, first moves) | Shapes how much rigor vs. speed this needs |

If you can give me even rough answers on margin, the flat-vs-share question, and what's off-limits beyond M&A, I can turn this into an actual sized plan rather than a structural guess. Want me to go that route, or keep this at the "take" level for now?


## Files in work dir after run


