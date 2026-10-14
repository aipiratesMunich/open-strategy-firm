# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and the required growth rate (about 9% a year from 2026 to 2029), and contrasts it with the flat history. | yes | "Gap — €9m (+29%, ~8.9% CAGR)" and "'flat for years' is the warning sign" |
| Asks a short, grouped set of questions the user can answer, no more than about three rounds, and proceeds without waiting if the user has no more data. | NO | The assistant lists missing data ("I don't have revenue mix, customer concentration, served markets, or margin/capital constraints yet") and ends with a question asking permission to run a full engagement and 'start by asking a tight first round' — it does not actually pose the grouped questions nor |
| Produces an issue tree that starts from the gap, with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with a hypothesis and a kill criterion. | yes | Table 'Ranked hypotheses' has rows: Gap & momentum, Core: market vs share, Core: wallet share, Core: price/mix, Adjacency, Portfolio — each with Hypothesis and Kill criterion columns. |
| Keeps inorganic moves out of scope or names them as ruled out by the board. | yes | "Constraints / no M&A..." and "Which organic levers close a €9m gap in three years?" |
| States the analysis order (momentum case and market vs share split first). | yes | "What I'd test first: Market growth vs. share (cheapest to check...), and the installed-base/wallet analysis" |
| Gives a provisional answer or the most likely shape of the answer, explicitly labelled as hypotheses, with confidence low and the reason. | NO | The day-one answer and page titles are labelled '[hypothesis]', but no explicit confidence level (e.g. 'low confidence') nor stated reason for low confidence is given anywhere in the transcript. |
| Open-questions table in the skill's format (question, why it matters, who can answer, effect on the answer). | NO | No table with columns question/why it matters/who can answer/effect on the answer appears; only a prose list: "I don't have revenue mix, customer concentration, served markets, or margin/capital constraints yet". |
| Does not invent textile market growth rates, competitor names, or benchmark figures as facts. | yes | Market growth figure given as hypothesis with kill criterion: "Served market has grown ~0–3%/yr while Pellworth held share flat" — framed as hypothesis, not asserted fact; no competitor names given. |
| Does not deliver a generic list of growth frameworks or ideas unconnected to the EUR 9m gap. | yes | All hypotheses and levers (wallet-share, price/mix, adjacency) are explicitly tied back to closing the €9m gap and sized against it (e.g. 'lever under ~€2m', 'add €3-5m'). |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

**Take: the target is plausible but not from the core alone — and "textiles, flat for years" usually means a share or structural problem, not a market one. That needs checking before any lever gets sized.**

## The gap
| | 2026 | 2029 |
|---|---|---|
| Revenue, momentum case (flat) | €31m | €31m |
| Revenue, target | €31m | €40m |
| **Gap** | — | **€9m (+29%, ~8.9% CAGR)** |
| Constraints | no M&A; capital limit and margin floor not yet stated |

€9m over three years is not a stretch target in absolute terms — it's the kind of gap one or two real levers can close. But "flat for years" is the warning sign: if the served market has been growing while Pellworth stood still, this is a share-loss problem and the fix is different (why are we losing, to whom) than if the market itself is flat (then the fix is adjacency or price, because the core has no more juice).

## Day-one answer (hypothesis)
Most likely combination: **wallet-share recovery in the existing customer base + a price/mix move**, with **one adjacency bet** (new category, channel, or geography) as the swing lever if the first two fall short — no acquisitions needed to hit €40m, but only if at least one of these levers is bigger than it looks today.

## Ranked hypotheses
| Branch | Hypothesis | Kill criterion |
|---|---|---|
| Gap & momentum | Flat trend continues without action → full €9m gap is real, not an artefact of one bad year | A recent one-off (lost customer, plant issue) explains the flatness → smaller real gap |
| Core: market vs. share | Served market has grown ~0–3%/yr while Pellworth held share flat → losing share, not just a flat market | Share stable/rising 3 years running → market itself is the ceiling, shift weight to adjacency |
| Core: wallet share | Existing customers buy adjacent products/services (finishing, private label, logistics) from competitors | Already near-fully penetrated on existing accounts → lever under ~€2m |
| Core: price/mix | List prices or mix sit below comparable players without a volume reason | Gap explained by spec, quality, or contract terms, not price |
| Adjacency | At least one adjacent category/channel/geography can add €3–5m with a plausible right to win | Addressable pool too small, or held by entrenched players with no opening |
| Portfolio | Two to three levers, base case, close ≥70% of the €9m | Base case sums to under half the gap → target needs to be reopened with the board |

## Ghost deck
- **Situation:** Pellworth has held ~€31m revenue for several years.
- **Complication:** The board wants €40m by 2029, and has ruled out M&A.
- **Question:** Which organic levers close a €9m gap in three years?
- **Answer:** A combination of wallet-share recovery, a price/mix reset, and one sized adjacency bet — *if the core is losing share rather than riding a flat market.* [hypothesis]

Page titles (all hypothesis, unvalidated):
1. "The €9m gap is real and has not been closing on its own." [hypothesis]
2. "Pellworth is losing share in a market that is not actually flat." [hypothesis]
3. "Existing customers buy adjacent products elsewhere — the cheapest growth is already in the building." [hypothesis]
4. "Prices sit below the value delivered, with no volume reason." [hypothesis]
5. "One adjacency can plausibly close the remainder of the gap." [hypothesis]
6. "The portfolio of two or three levers gets to €40m without M&A — or the target needs to be reopened." [hypothesis]

## What would have to be true
- The served market isn't structurally shrinking (if it is, €40m without M&A gets much harder).
- At least one of the top two levers (wallet share, price/mix) is worth €4m+ on its own — otherwise the plan needs a real adjacency bet, which carries execution risk and a longer ramp.
- No margin floor or capital ceiling from the board kills the levers that would otherwise work.

## What I'd test first
Market growth vs. share (cheapest to check, decides whether this is a "fix the core" or "find new ground" problem), and the installed-base/wallet analysis (usually the fastest money). I don't have revenue mix, customer concentration, served markets, or margin/capital constraints yet — those determine whether this day-one answer survives contact with your data.

Want me to run this as a full growth-strategy engagement? I'd start by asking a tight first round: product/customer segments, where the €31m breaks down geographically and by channel, what "flat" has looked like year by year, and what capital/margin constraints the board has set alongside "no M&A."


## Files in work dir after run


