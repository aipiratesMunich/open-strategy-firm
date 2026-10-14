# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and required growth rate (about 9% a year 2026-2029), contrasts with flat history | yes | '~€9m (+29%, ~8.8% CAGR)' and 'A company flat for "years" hitting +29% in three years with no M&A is a step-change, not a trend extrapolation.' |
| Asks short grouped set of questions, ≤3 rounds, proceeds without waiting if user has no more data | yes | User stated 'That's all I've got right now'; assistant proceeded directly to a full analysis while surfacing 'Top three things I'd want from you next' and an open-questions table rather than blocking on a Q&A round. |
| Issue tree from the gap with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with hypothesis and kill criterion | NO | Output is a flat 'Levers' table (price/mix, wallet capture, one adjacency, spare capacity) with a 'Decision: option' column — there is no structured tree with a distinct 'momentum' branch or explicit per-branch kill criteria; only 3 of 4 levers get a 'kill this lever if...' condition buried in the a |
| Keeps inorganic moves out of scope or names them as ruled out by the board | yes | 'M&A / acquisitions — ruled out by the board; not assessed further.' |
| States the analysis order (momentum case and market vs share split first) | yes | 'First question before sizing anything: has the served market flat or... recoverable share...' combined with the momentum case already laid out in the gap table before levers are sized. |
| Gives provisional answer/most likely shape, labelled as hypotheses, confidence low with reason | yes | 'Confidence: Low — built on three numbers (31m, 40m, 2029) and no company, market or competitor data. Every figure below is a labelled assumption with a wide range, not a finding.' |
| Open-questions table in skill's format (question, why it matters, who can answer, effect on answer) | yes | Table headers: 'Question / Why it matters / Who can answer / Effect on the answer' |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts | yes | All figures explicitly tagged 'ASSUMPTION' or 'ASSUMPTION/outside view... not yet checked against textiles specifically'; no competitor names or market growth rate asserted as fact. |
| Must not deliver a generic list of growth frameworks unconnected to the EUR 9m gap | yes | Each lever is sized against the gap: 'Sum of kept levers (base case): ~€7.2m; remaining gap: ~€1.8m.' |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

## My take

€31m → €40m in three years, flat before that, no M&A — that's a step-change, not a trend line. On a quick pass with placeholder sizing, the obvious organic levers (price correction, cross-sell into the existing customer base, one new channel/geography, filling spare capacity) get you to roughly **€4.6m–7m of the €9m gap**, and only if two of those four land strong rather than all four landing moderate. So: plausible, but not comfortably — either there's a bigger lever not yet visible, or the board should hear that 2029 is tight.

The single fact that would most change my answer: **has revenue been flat because the market's flat, or because Pellworth has been losing share?** Those point to completely different plans — recapture share (fast, cheap) vs. find a new ceiling (adjacency, slower, more capital).

I wrote the full breakdown with assumptions and open questions to `case-growth-pellworth-textiles.md`. Top three things I'd want from you next: what Pellworth actually sells/to whom, whether there's spare manufacturing capacity, and any margin floor or capital limit the board has in mind.


## Files in work dir after run

- case-growth-pellworth-textiles.md

## File written by the run: case-growth-pellworth-textiles.md

# Growth strategy: Pellworth Textiles — which organic levers close the gap from €31m to €40m revenue by 2029?

**Answer:** Provisional, levers unverified — lead with price/mix correction and installed-base wallet capture (cheapest, fastest), add one concentrated adjacency (channel or geography, not several). On current placeholder sizing these reach roughly €4.6m–5m of the €9m gap in the base case — short of half. Either a bigger single bet exists that hasn't surfaced yet, or the 2029 target/timeline needs revisiting with the board. **Day-one hypothesis, not a sized plan.**

**Confidence:** Low — built on three numbers (31m, 40m, 2029) and no company, market or competitor data. Every figure below is a labelled assumption with a wide range, not a finding.

## The gap

| | 2026 | 2029 |
|---|---|---|
| Revenue, momentum case (flat) | €31m | ~€31m |
| Revenue, target | €31m | €40m |
| Gap | — | ~€9m (+29%, ~8.8% CAGR) |
| Constraints | No acquisitions (organic only); margin floor and capital limit not yet known |

A company flat for "years" hitting +29% in three years with no M&A is a step-change, not a trend extrapolation. First question before sizing anything: **has revenue been flat because the served market is flat, or because Pellworth has been losing share in a market that's actually grown?** Those need opposite answers — the first means the ceiling itself has to move (new offers/geographies); the second means there's recoverable share sitting with named competitors right now, which is usually the faster, cheaper fix. I don't know which, and it's the single highest-leverage fact missing.

## Levers (provisional — all ASSUMPTION, weak evidence)

| Lever | Revenue base case by 2029 | Range | Basis / evidence grade | Decision |
|---|---|---|---|---|
| Price/mix correction (close any gap to comparable players) | €1.0m | €0.7m–1.3m | ASSUMPTION: prices track ~3–5% below comparable competitors without a volume reason — unverified, needs a competitor price check. Weak. | option |
| Installed-base wallet capture (existing customers buying adjacent lines elsewhere) | €2.2m | €1.4m–3.1m | ASSUMPTION: ~15–20% of current revenue (€4.6m–6.2m) is addressable adjacent spend; capture 30–50% of it. No customer-level wallet data exists yet. Weak. | option |
| One adjacency: channel or geography (e.g. direct/e-commerce, or a neighbouring export market, using existing product and capacity) | €2.0m | €1m–3m | ASSUMPTION/outside view: comparable organic channel launches at this scale typically reach €1m–3m run-rate in 2–3 years — reference class not yet checked against textiles specifically. Weak. | option |
| Spare-capacity offer (private label / contract manufacture / value-add finishing) | €2.0m | €1.5m–3m | ASSUMPTION: unused capacity exists (common in flat-revenue manufacturers) and 10–20% incremental utilisation is sellable. Capacity-utilisation data not in hand. Likely margin-dilutive if private label. Weak. | option |

**Sum of kept levers (base case): ~€7.2m; remaining gap: ~€1.8m.** On the low end of the ranges the sum drops to ~€4.6m — under half the gap, which by the playbook's own kill criterion means the target should be reopened with the board rather than forced. On the high end (~€10.4m) it clears the gap, but that's four separate things all landing near their top case at once — the "adding up hope" trap. **Realistically: two of these four need to come in strong, not all four moderately.**

## Killed options and why

- **M&A / acquisitions** — ruled out by the board; not assessed further.

## Risks and what would change the answer

1. If the core turns out to be share loss rather than a flat market, the price and wallet levers are underpriced here — they could be worth more, and the honest first move is a win/loss and competitor-pricing read, not a new-channel launch.
2. If capacity is already near-full, the spare-capacity lever disappears entirely and the gap gets harder to close organically.
3. If none of the four levers individually exceeds ~€2–3m, closing €9m in three years without M&A may simply not be achievable on this timeline — the board needs to hear that as an option, not just a plan that quietly falls short in 2029.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Prices sit below comparable players | 3–5% gap | Unverified pattern in flat-revenue manufacturers | Pricing is already at parity — kill this lever |
| 2 | Addressable adjacent wallet spend | 15–20% of revenue | Unverified | Customers already buy the adjacent lines from Pellworth — kill this lever |
| 3 | Comparable channel launch run-rate | €1m–3m in 2–3 years | Outside-view placeholder, not checked against textiles | Reference class shows slower ramp — widen range down |
| 4 | Spare manufacturing capacity exists | 10–20% incremental utilisation sellable | Unverified | Plant is already near-full — kill this lever |
| 5 | No margin floor or capital limit stated | Not modelled | Not yet given by board | A tight margin floor rules out the private-label lever (margin-dilutive) |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the served market flat or growing, and is Pellworth gaining or losing share? | Determines whether the fix is recapturing share (fast, cheap) or needs a new ceiling (adjacency, slower) | Internal sales/market data, competitor revenue trends | Reframes which two levers to lead with |
| What's the margin floor and capital limit the board will accept? | Rules levers in or out (private label is margin-dilutive; new channel needs capex) | CFO / board brief | Could kill 1–2 levers outright |
| What does Pellworth actually make/sell — segment, channel (wholesale/retail/B2C), customer concentration? | Can't size any lever without knowing the business | Company management | Replaces every placeholder number above with a real one |
| Is there spare manufacturing capacity today? | Decides whether the capacity-offer lever exists at all | Ops/plant utilisation data | Could remove ~€2m of the base case |
| When does the board actually decide, and on what (a plan, a budget, first moves)? | Sets how much rigor and sizing the next pass needs | User | Determines whether this stays a day-one take or becomes a full engagement |

