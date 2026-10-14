# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and the required growth rate (about 9% a year from 2026 to 2029), and contrasts it with the flat history. | yes | "€31m → €40m by 2029 is a €9m jump (29%), or about 8.9% CAGR for the next three years — up from roughly 0% for 'several years.'" |
| Asks a short, grouped set of questions the user can answer, no more than about three rounds, and proceeds without waiting if the user has no more data. | yes | "What I don't know and would ask next: which textiles segment..., what geography, current margin and any floor..., how much capital is available, and — critically — why the board picked €40m" — grouped in one round, given after the full analysis was already delivered rather than blocking on it. |
| Produces an issue tree that starts from the gap, with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with a hypothesis and a kill criterion. | yes | Table lists hypotheses 1 (momentum), 2 (market vs share), 3 (existing customers/wallet share), 4 (price), 5 (adjacency), 6 (portfolio), each with a Kill criterion column. |
| Keeps inorganic moves out of scope or names them as ruled out by the board. | yes | "Complication: ... which means roughly 9% annual growth after years of none" preceded by "organic only, no M&A" in the ghost deck. |
| States the analysis order (momentum case and market vs share split first). | yes | "First thing a real engagement would run: momentum case + market-vs-share split, because it decides whether this is 'defend and extend the core' or 'the market itself won't support €40m'" |
| Gives a provisional answer or the most likely shape of the answer, explicitly labelled as hypotheses, with confidence low and the reason. | yes | "Day-one answer (hypothesis): No single organic lever plausibly gets there... likely closes somewhere between half and three-quarters of the gap on a base case, not all of it." — hedged throughout and explicitly labeled hypothesis/unverified. |
| Open-questions table in the skill's format (question, why it matters, who can answer, effect on the answer). | NO | The closing section is a prose paragraph — "What I don't know and would ask next: which textiles segment..., what geography, current margin..." — not a table with columns for question, why it matters, who can answer, and effect on the answer. |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts. | yes | Figures like ">3–5% price gap vs. comparable competitors" are framed as hypothesis thresholds to test, not asserted facts; no competitor names or market growth rates are stated. |
| Must not deliver a generic list of growth frameworks or ideas unconnected to the EUR 9m gap. | yes | All hypotheses and the ghost deck explicitly tie back to closing "the €9m gap" rather than listing generic growth levers. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

Quick gap check first, because it changes the shape of the answer: **€31m → €40m by 2029 is a €9m jump (29%), or about 8.9% CAGR for the next three years — up from roughly 0% for "several years."** That's not a tweak, it's a different company. Worth saying plainly: if the board hasn't seen it stated this way, I'd lead with that number before anything else.

**Day-one answer (hypothesis):** No single organic lever plausibly gets there. The realistic path is wallet-share capture in the existing customer base (cheapest, fastest) plus price/mix correction on the core, plus one well-chosen adjacency (new category, segment or export geography) — and even stacked, that portfolio likely closes somewhere between half and three-quarters of the gap on a *base case*, not all of it. The rest is either an assumption the board should see explicitly, or a reason to revisit the target or the 2029 deadline.

**Ranked hypotheses**

| # | Hypothesis | Threshold | Kill criterion |
|---|---|---|---|
| 1 | Momentum case (flat) misses target by ~€9m/29% by 2029 | — | Confirmed by definition from the flat history given |
| 2 | Flat revenue reflects a flat/shrinking served market, not just share loss | market CAGR last 3yrs | If market grew while Pellworth stayed flat → share-loss problem (fixable commercially); if market itself is flat/declining → gap must come largely from outside today's served market, raising risk |
| 3 | Existing customers buy adjacent textile categories from competitors that Pellworth could supply | >10% of customer wallet addressable | If customers are near-exclusive by design (specialised mills, single-source contracts) → lever is small |
| 4 | Pellworth is underpriced relative to delivered value on some lines | >3–5% price gap vs. comparable competitors | If already at price parity in a commodity, price-taker market → lever is small |
| 5 | At least one adjacency (geography/segment/category) can add ≥€3m/yr by 2029 with a real right to win | — | If credible adjacencies need capex/capability Pellworth lacks, or are held by entrenched players |
| 6 | Portfolio of 2–3 levers closes ≥70% of the €9m gap on base case | — | If base-case sum is under ~50% of the gap → reopen the target/timeline with the board rather than stretch assumptions |

**Ghost deck**
- *Situation:* Revenue has held near €31m for several years.
- *Complication:* The board wants €40m by 2029 — organic only, no M&A — which means roughly 9% annual growth after years of none.
- *Question:* Which organic levers can plausibly close the €9m gap, and is the target achievable on that timeline at all?
- *Answer (hypothesis):* Wallet-share capture plus price correction plus one adjacency likely close most but not all of the gap; the board needs to see the remainder honestly.

Titles (all hypothesis, unverified):
1. "The momentum case reaches ~€31m by 2029, leaving a €9m gap against the target."
2. "Flat revenue is [market decline / share loss] — this determines where growth has to come from."
3. "Existing customers send a material share of adjacent spend to competitors — the fastest lever to close."
4. "Pellworth is underpriced on [specific lines] relative to delivered value."
5. "[Adjacency X] can add €X–Y m by 2029 with a credible right to win."
6. "The base-case portfolio closes [50–70]% of the gap — the remainder needs an honest decision, not an optimistic plug."

**What would have to be true, and what I'd test first:** that the served textiles market isn't structurally shrinking with no viable adjacency; that customers have real unmet wallet share; that at least one lever can actually ramp inside three years (textiles — new lines, certifications, export relationships — often don't move fast). First thing a real engagement would run: **momentum case + market-vs-share split**, because it decides whether this is "defend and extend the core" or "the market itself won't support €40m," which are different strategies entirely.

**What I don't know and would ask next:** which textiles segment (apparel, home, technical/industrial), what geography, current margin and any floor the board holds, how much capital is available, and — critically — why the board picked €40m (investor commitment? plan inherited from somewhere? arbitrary round number?). That last one matters a lot for how hard to push back.


## Files in work dir after run


