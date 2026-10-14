# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes gap (EUR 9m, ~29%) and required growth rate (~9%/yr 2026-2029), contrasts with flat history | yes | '+€9m, or +29% in three years (~8.9% CAGR)... On top of several years flat.' |
| Asks short grouped set of questions (<=3 rounds), proceeds without waiting if no more data | yes | 'What I'd want from you next (not required to react to the above)' lists 3 grouped questions, while the full day-one analysis is already delivered in the same turn rather than gated on answers. |
| Issue tree from the gap with branches momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with hypothesis + kill criterion | NO | The 'Ranked hypotheses' table covers momentum, market-vs-share, existing customers, price, and adjacency with kill criteria, but presents them as a flat ranked list rather than a tree, and has no distinct 'portfolio' branch — item 6 is a synthesis ('levers summed on base case'), not a portfolio-of-b |
| Keeps inorganic moves out of scope or names them as ruled out by the board | yes | 'The board wants €40m by 2029 — 29% growth in three years — with acquisitions off the table.' |
| States analysis order (momentum case and market vs share split first) | yes | Table titled 'Ranked hypotheses (to test, with kill criteria)' places momentum (#1) and market vs share (#2) first among six. |
| Gives provisional answer/likely shape, labelled as hypotheses, confidence low with reason | yes | 'Day-one answer (hypothesis, to be tested, not yet evidenced): Pellworth most plausibly closes 60–70% of the gap...' — explicitly flagged as unevidenced hypothesis, functioning as a low-confidence label with reason. |
| Open-questions table in skill's format (question, why it matters, who can answer, effect on answer) | NO | Only a bare bullet list ('Rough split of revenue by product line/segment/customer...', 'Current gross/EBIT margin...', 'Anything already ruled out...') with no columns for why it matters, who can answer, or effect on the answer. |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts | yes | Figures like 'Price gap >3–5% vs. comparable players' and '60–70%' are framed as thresholds/hypotheses to test, not asserted market facts; no specific market growth rate or competitor name is invented. |
| Must not deliver generic growth frameworks/ideas unconnected to the gap | yes | All levers (wallet capture, price/mix, adjacency) are explicitly sized against the €9m/€3-4m residual gap rather than listed generically. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

## Day-one take: Pellworth Textiles

**The gap, stated honestly:** €31m → €40m by 2029 is +€9m, or **+29% in three years (~8.9% CAGR)**. On top of several years flat. In a mature textiles market, organic growth of that scale essentially never comes from market tailwind alone — it has to come from share, mix/price, or new revenue lines. That's the real question hiding behind the board's number.

**Day-one answer (hypothesis, to be tested, not yet evidenced):** Pellworth most plausibly closes 60–70% of the gap through (1) capturing wallet share currently going to competitors from its *existing* customer base, plus (2) a price/mix correction where list prices sit below value delivered — the two cheapest, fastest levers — and the **remaining ~€3–4m requires one adjacency bet** (new product category, channel, or geography) sized and resourced like a real initiative, not a rounding error. If that adjacency doesn't exist or is too small, the honest move is to tell the board the target slips past 2029, not to stretch assumptions until the model says €40m.

### Ranked hypotheses (to test, with kill criteria)

| # | Hypothesis | Threshold | Kill criterion |
|---|---|---|---|
| 1 | Momentum case stays flat at ~€31m; gap is real and large | Gap ≥ €9m by 2029 | Gap <10% of revenue → this becomes "defend the core," not a growth case (not the situation here) |
| 2 | Revenue is flat because Pellworth is **losing share** in a market that itself is growing modestly, not because the whole market is dead | Served market growth >0% while Pellworth share falls | If share has been stable for years, there's no share to win back — weight shifts to adjacencies/new lines |
| 3 | Existing customers buy adjacent things (finishing, logistics, private label, certain product lines) from competitors that Pellworth could capture | Capturable wallet ≥ €2–3m | If third-party spend in the installed base is already small or locked by contract, this lever is minor |
| 4 | List prices sit below value/competitors without a volume reason | Price gap >3–5% vs. comparable players, explainable only partly by spec/service | If like-for-like pricing is already at parity, the lever is small |
| 5 | At least one adjacency (new product category, channel, geography) can plausibly add €3–4m+ by 2029 with a real right to win | Addressable size and win-rate support ≥€3m base case | If every adjacency is either too small or held by entrenched incumbents, the 2029 date is not credible without M&A |
| 6 | Two to three levers, summed on base case (not best case), close at least ~60% of the €9m gap | Base-case sum ≥ €5–5.5m | If base-case sum is well under half the gap, the right move is to reopen the target/date with the board, not to inflate assumptions |

### Ghost deck (titles are hypotheses, not findings yet)

- **Situation:** Pellworth has sat near €31m for several years in a mature textiles market.
- **Complication:** The board wants €40m by 2029 — 29% growth in three years — with acquisitions off the table.
- **Question:** Which organic levers can plausibly close that gap, and how much of it do they actually close?
- **Answer:** A combination of installed-base wallet capture, price/mix correction, and one sized adjacency likely closes most — not all — of the gap; the residual is a decision for the board, not an assumption to paper over.

1. *"The 2029 target implies ~8.9%/year growth against a market that has produced zero for several years — the gap is real, not rounding."* [hypothesis]
2. *"Flat revenue reflects share loss within a still-growing market, not a dead market"* — or the opposite; this is the single most important unknown. [hypothesis, open]
3. *"The installed customer base is the cheapest growth available if third-party wallet share there is material"* [hypothesis]
4. *"Prices sit below delivered value in at least one segment, giving room to lift without losing volume"* [hypothesis]
5. *"One adjacency, sized on its base case, can plausibly add €3–4m by 2029"* [hypothesis]
6. *"The kept levers close most of the gap; the honest remainder is named, not hidden"* [hypothesis]

### What would have to be true for €40m to be achievable organically
- The market Pellworth sells into isn't itself shrinking (if it is, this is a defend/reposition story, not a growth story).
- There's real, quantifiable third-party spend inside the existing customer base to take back.
- Pricing has room — textiles is often commodity-priced with thin margins, so this lever could easily be smaller than hoped.
- At least one adjacency is big enough and winnable enough to carry €3m+ on its own, with a credible 2–3 year ramp.

### What I'd want from you next (not required to react to the above)
- Rough split of revenue by product line/segment/customer, and whether the flatness is market-wide or specific to one line.
- Current gross/EBIT margin and whether the board has a margin floor alongside the €40m (a plan that hits €40m by eroding margin isn't really a win).
- Anything already "ruled out" beyond M&A (new plants, specific geographies, capital ceiling).

If you want, I can take this into a full day-one working session — size the momentum case and each lever properly rather than leaving them as placeholders — once you can give me even rough numbers on one or two of the above.


## Files in work dir after run


