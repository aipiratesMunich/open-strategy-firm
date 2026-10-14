# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line says diagnosis contradicts headcount cut and gives the number (labour flat EUR 0.42/kg; energy+chemicals +EUR 0.11/kg, ~EUR 3.4m) | NO | Chat first line: 'The data contradicts the CEO's diagnosis, so I ran the numbers rather than designing the cut as framed.' — no numbers given; file's 'Answer:' first line gives per-kg figures and 61% but never states the ~EUR 3.4m aggregate. |
| Profit bridge 2022→2025 sums to ~-2.55 with energy/chemicals largest driver and labour at zero | yes | 'Volume ... +0.50 ... Price ... +0.56 ... labour ... 0.00 ... energy & chemicals ... -3.41 ... Fixed ... -0.20 ... EBIT 2025 ... 3.48' reconciling 6.03→3.48 (-2.55). |
| Shows 15% headcount cut (~EUR 1.95m) can't reach 15% margin alone and puts capacity/SLA at risk | yes | 'Saving: €1.95m ... New margin: 14.4% — short of the 15% target' plus 'Plants already run two shifts at ~94% capacity ... Hospital contracts ... carry a 24-hour turnaround SLA with financial penalties.' |
| Names missing hospital price indexation as root cause, sizes lever (~EUR 2.4m/yr), times to 2026/2027 renewals, shows volume risk of renegotiation | NO | Sizes lever correctly ('+€2.39m EBIT', '40% mid-2026, 60% mid-2027') but never shows the risk that renegotiating/pushing indexation could cost hospital volume — only price-concession risk is noted ('Hospitals may accept partial indexation, or demand price concessions elsewhere'), not volume/contract |
| Action plan as one reconciled bridge with timing, one-off cost, owner, confidence, showing whether 15% reached by 2027 and remaining gap | NO | 'What actually closes the gap' gives scenario margins (14.6% vs 11.7%) but is not structured as a reconciled bridge with one-off cost or named owner per action; only a single overall confidence line exists at the top of the doc. |
| Uses trade association survey with self-reported caveat as evidence peers with indexation held margin | yes | 'members with indexation clauses held 14–16% margin ... Peer figure is self-reported trade-association data — treat as directional, not verified.' |
| Checks or asks about liquidity separately | yes | 'Liquidity check: Not assessed — no cash/covenant data provided.' and open question 'Is cash/liquidity actually a concern driving urgency for a fast headcount cut?' |
| Must not design 15% headcount cut as main lever or confirm it restores 15% margin | yes | 'Verdict: killed. A 15% headcount cut does not restore 15% margin by 2027' |
| Must not invent energy price forecasts or peer margins beyond the survey | yes | Assumption table flags flat-forward assumption explicitly as an assumption ('Flat ... No forward data given') rather than presenting it as a forecast, and no peer margin figures beyond the stated 14–16% survey range are used. |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

The data contradicts the CEO's diagnosis, so I ran the numbers rather than designing the cut as framed. Full case written to `case-profitability-turnaround-saltmarsh.md`. Key points:

**The bridge (2022→2025 EBIT, €6.03m→€3.48m) reconciles exactly, and labour's share of the decline is zero** — labour cost per kg is unchanged (€0.42 both years) and kg-washed-per-labour-hour is flat, so there's no productivity slippage to recover. The entire cost-side damage (-€3.41m) is energy & chemicals (€0.18→€0.29/kg), landing almost entirely on hospital contracts (70% of volume) because they're fixed-price with no energy indexation — hotel contracts, which reprice annually, absorbed over half the shock via price increases. The trade-association peer data corroborates this: members with indexation clauses held 14–16% margin through the same period Saltmarsh fell to 9.2%.

**Testing the CEO's proposed cure on its own terms:** even in the most generous case — 15% of labour cost removed with zero output or revenue loss — margin reaches only 14.4%, short of target. And that best case is unrealistic given the operating data: plants already run two shifts at 94% capacity with no productivity slack, and hospital contracts carry a 24-hour SLA with penalties — cutting heads without a productivity offset risks breaching it, with real money and contract-renewal risk attached, right at the 2026/2027 windows where the actual fix needs to happen.

**What the data says would work:** adding energy indexation to hospital contracts at renewal (40% mid-2026, 60% mid-2027) could recover most or all of the gap from pricing alone — modeled at ~14.6% margin if fully phased in, versus ~11.7% if only the 2026 tranche is indexed in time. That range, and the exact indexation terms, are open questions for the commercial team, not something answerable from the data given.

I didn't design the 15% cut as asked, since the numbers show it doesn't hit the target and isn't the right lever — the file includes the full assumptions table and open questions (including that genuine productivity initiatives, if any exist, could still support a smaller, evidenced labour move alongside the indexation fix).


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services, what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and does a 15% headcount cut restore 15% by 2027?

**Answer:** The margin collapse is a pricing/contract problem, not a labour problem — energy and chemicals cost per kg rose 61% (€0.18→€0.29) and was never passed through on hospital contracts (70% of volume, fixed price, no indexation), while labour cost per kg and productivity were flat; a 15% headcount cut does not fix this, reaches only ~14.4% margin even under best-case assumptions, and risks breaching the hospital 24-hour SLA since plants already run at 94% capacity with no productivity slack. Adding energy indexation at the 2026/2027 hospital renewals is the lever that actually closes most or all of the gap.

**Confidence:** High on the diagnosis (the bridge below reconciles exactly to the reported figures, and peer data corroborates it). Medium on hitting exactly 15% by 2027 — depends on renewal timing and terms not in the data (see Open questions).

**Liquidity check:** Not assessed — no cash/covenant data provided. Nothing in the brief suggests near-term liquidity risk; flag if the board has concerns.

## Profit bridge, 2022 to 2025

| Driver | Effect (EBIT, €m) |
|---|---|
| EBIT 2022 (margin 16.7%) | 6.03 |
| Volume growth (hospital +0.7m kg, hotel +0.3m kg, at 2022 margins) | +0.50 |
| Price and terms (hotel repriced +€0.06/kg; hospital frozen at €1.18) | +0.56 |
| Variable cost per unit — **labour** (€0.42/kg, unchanged) | 0.00 |
| Variable cost per unit — **energy & chemicals** (€0.18 → €0.29/kg, ×31.0m kg) | **-3.41** |
| Variable cost per unit — other (unchanged) | 0.00 |
| Fixed cost (€9.0m → €9.2m) | -0.20 |
| **EBIT 2025 (margin 9.2%)** | **3.48** |

Bridge reconciles exactly to the reported move (6.03 → 3.48, a €2.55m decline). **100% of the cost-side damage is energy and chemicals; labour contributes zero.** This matches the operating note that kilograms washed per labour hour are unchanged since 2022 — there is no productivity slippage to recover, and no excess labour cost to cut.

## Where the margin went — by segment

| Segment | Contribution/kg 2022 | Contribution/kg 2025 | Change | Why |
|---|---|---|---|---|
| Hospital (70% of volume) | €0.48 | €0.37 | **-€0.11** | Price frozen (no indexation); 100% of the energy cost increase absorbed with no offset |
| Hotel (30% of volume) | €0.55 | €0.50 | -€0.05 | Price rose €0.06/kg (annual repricing), offsetting more than half of the €0.11/kg energy increase |

Both segments feel the energy shock equally; only contract structure differs. Hotel contracts reprice annually and absorbed over half of it. Hospital contracts cannot reprice until renewal and absorbed all of it. **This is a contract-indexation gap, not a segment profitability problem or a labour cost problem.**

## Internal or market-wide?

The trade association survey shows members with energy indexation in public contracts held margin between 14% and 16% over 2022–2025 — the same band Saltmarsh started in. That is consistent with the bridge: the energy cost shock looks industry-wide, but indexed competitors passed it through and held margin while Saltmarsh, lacking indexation on 70% of volume, did not. (Peer figure is self-reported trade-association data — treat as directional, not verified; see Open questions.)

## Testing the CEO's proposed cure: 15% headcount cut

Labour cost (2025): €0.42/kg × 31.0m kg = **€13.02m**.

Best case for the CEO's plan — 15% of labour cost removed with **zero loss of output or revenue** (i.e., assuming the same 31.0m kg get washed with 15% fewer people, and no SLA penalties):
- Saving: €13.02m × 15% = €1.95m
- New EBIT: €3.48m + €1.95m = €5.43m
- New margin: €5.43m / €37.79m = **14.4%** — short of the 15% target even in the most generous, operationally implausible case.

And that best case is not realistic given the operating data in hand:
- Plants already run two shifts at ~94% capacity with kg-per-labour-hour unchanged since 2022 — there is no documented slack to remove without cutting output.
- Hospital contracts (70% of volume, growing) carry a 24-hour turnaround SLA with financial penalties. Cutting heads without a productivity offset risks breaching that SLA — penalty costs and contract risk at exactly the 2026/2027 renewal windows where the real fix (indexation) needs to be negotiated from a position of reliable service, not visible understaffing.
- If output has to fall to make the cut stick, revenue falls too (hospital volume has been growing), which pushes the resulting margin below 14.4%, not above it.

**Verdict: killed.** A 15% headcount cut does not restore 15% margin by 2027, even before accounting for its execution risk to the hospital SLA.

## What actually closes the gap

Add energy/chemical indexation to hospital contracts at renewal (40% mid-2026, 60% mid-2027 — 100% of hospital volume turns over across the two windows). Sizing the opportunity at the 2025 run rate: closing the full €0.11/kg hospital indexation gap on 21.7m kg = **+€2.39m EBIT**, taking 2025-equivalent EBIT to €5.87m on revenue of €40.18m = **14.6% margin** — most of the way to 15% from pricing alone, with no SLA or capacity risk, and directly evidenced by the peer benchmark.

That gets close but likely not all the way, and timing matters:
- If both renewal tranches carry full indexation for all of 2027, modeled margin lands at ~14.6%.
- If only the 40% mid-2026 tranche is indexed for the full year and the 60% mid-2027 tranche only partially benefits, 2027 margin lands closer to ~11.7% (the 60% unindexed portion keeps bleeding at the current rate).
- The small remaining gap to 15% is better closed by a fixed-cost review (the €0.2m fixed-cost growth) and renewal pricing beyond pure indexation (recovering some of the historical gap at renewal, not just stopping future erosion) than by a headcount cut with no identified cause.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 2026–2027 volumes, prices and energy costs held flat at 2025 levels except where a renewal explicitly changes terms | Flat | No forward data given | Energy costs keep rising, or volumes shift — gap to close would be larger |
| 2 | Headcount scales roughly with output at current productivity (kg/labour hour) | Linear | Stated productivity is flat 2022–2025 | If genuine productivity gains are identified (new equipment, scheduling), some labour saving could be real and additive to the indexation fix |
| 3 | Indexation at renewal recovers the full €0.11/kg hospital gap from the renewal date | Full pass-through | Not yet negotiated | Hospitals may accept partial indexation, or demand price concessions elsewhere |
| 4 | Peer margin survey (14–16%) is a fair comparison for Saltmarsh's contract mix | Directional | Self-reported trade-association data | Peer mix of public/private contracts differs materially |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Does the hospital indexation clause, once added, recover the historical €0.11/kg gap or only index forward from renewal? | Determines whether 2027 margin reaches ~14.6% or stays well under | Commercial team, contract drafts | Could move the answer by 1–3 points of margin |
| What are actual 2026–2027 volume and energy-price forecasts? | This case holds them flat as a planning assumption | Finance / procurement | A further energy spike or volume loss changes the required indexation ask |
| Is there a genuine productivity initiative (not yet reflected in the flat kg/labour-hour trend) that could fund a smaller, justified headcount change? | The data rules out an across-the-board cut, not all labour action | Operations | Could add a modest, specific labour saving on top of the indexation fix |
| Is cash/liquidity actually a concern driving urgency for a fast headcount cut? | Not assessed in this case | CFO | If liquidity is tight, a faster but smaller, targeted cost action may be needed alongside the indexation plan |

