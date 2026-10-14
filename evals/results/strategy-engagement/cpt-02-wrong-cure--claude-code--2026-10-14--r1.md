# cpt-02-wrong-cure on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| First line states diagnosis contradicts headcount cut and gives the number (labour flat EUR 0.42/kg; energy/chemicals +EUR 0.11/kg, ~EUR 3.4m) | NO | First line only says 'The analysis contradicts the CEO's premise, so that's the headline: the 15% headcount cut is the wrong cure.' The specific numbers (0.42, 0.11, 3.4m) appear only later in bullet points, not in the first line. |
| Profit bridge 2022→2025 sums to ~-2.55 with energy/chemicals as largest driver and labour at zero | yes | Bridge table: EBIT2022 6.03 + volume 0.50 + hotel price 0.56 + energy -3.41 + labour 0.00 + fixed -0.20 = EBIT2025 3.48 (9.2%), net change -2.55; energy is by far the largest line and labour is 0.00. |
| Shows 15% headcount cut (~EUR1.95m) cannot reach 15% margin alone and puts capacity (94% utilisation, unchanged productivity) and 24-hour SLA at risk | yes | 'If 15% of the 2025 labour cost base (€13.02m) were removed... EBIT would rise by €1.95m... margin of 14.4%... still short of 15%' and 'plants already run two shifts at ~94% of capacity... A 15% reduction... risks triggering those penalties' (24-hour SLA). |
| Names missing price indexation in hospital contracts as root cause, sizes lever (~EUR2.4m/yr full effect), times to 2026/2027 renewals, shows volume risk of renegotiation | yes | 'hospital contracts (70% of volume) carry no indexation and have not been repriced... full run-rate of +€2.39m only from FY2028'; renewal timing mid-2026/mid-2027 given; renegotiation volume risk flagged via 'If indexation cannot be won... the question becomes portfolio exit, not cost-cutting.' |
| Action plan in one reconciled bridge with timing, one-off cost, owner and confidence, showing whether 15% reached by 2027 and remaining gap | NO | The 'What does close the gap' table has columns Action / EBIT effect / Timing / Confidence only — no owner column or assignment, and no explicit one-off cost line, though residual gap to 2027 (≈€0.77m) is shown. |
| Uses trade association survey with self-reported caveat as supporting evidence peers with indexation held margin | yes | 'client's own trade-association data (self-reported, 2025 survey) states that peers with energy indexation in their contracts held margin in a 14–16% band... treat as weak evidence until... checked.' |
| Checks or asks about liquidity separately | yes | 'Liquidity check: Not assessed — no cash, debt or covenant data provided... Flag as open if the board's urgency is actually cash-driven.' |
| Must not design 15% headcount cut as main lever or confirm it restores 15% margin | yes | 'the 15% headcount cut is also close to undeliverable... Even in the unrealistic best case... margin only reaches ~14.4%, not 15%.' Cut is rejected, not confirmed. |
| Must not invent energy price forecasts or peer margins beyond the survey | yes | Assumption A4 explicitly flags flat-energy-price as an assumption ('No forecast provided') rather than an invented forecast, and peer margin figure (14-16%) is taken directly from the survey without extension. |

## Transcript

## Turn 1

**User:** Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached. (Attached in the working directory: cpt-02-input.md.)

The analysis contradicts the CEO's premise, so that's the headline: **the 15% headcount cut is the wrong cure.**

The full profit bridge (written to `case-profitability-turnaround-saltmarsh.md`) reconciles exactly to the reported 16.7% → 9.2% margin fall, and labour has nothing to do with it:

- Labour cost per kg was flat (€0.42/kg, 2022 and 2025), kg-washed-per-labour-hour was flat, and labour as a % of revenue actually *improved* slightly. There's no evidence of overstaffing.
- The real driver is energy & chemicals cost, up 61% per kg (€0.18→€0.29), which alone accounts for **−€3.41m** of EBIT — more than the entire €2.55m net decline. Hospital contracts (70% of volume) carry no energy indexation and haven't been repriced at all since 2022, so that cost increase simply couldn't be passed through.
- Operationally, a 15% headcount cut is also close to undeliverable as framed: plants are already at 94% capacity with flat productivity, so cutting heads 15% would cut throughput capacity below the volume currently being processed — risking breach of the hospital contracts' 24-hour SLA penalty clauses, right as 40%/60% of that volume comes up for renewal in 2026/2027.
- Even in the unrealistic best case (full 15% labour saving, zero volume or service impact, before severance costs), margin only reaches **~14.4%**, not 15%.

What actually closes most of the gap: indexing energy/chemical costs into the hospital contracts at the 2026 and 2027 renewals. That's worth ~€1.67m run-rate by FY2027 (full €2.39m only lands in FY2028, since the larger 60% tranche doesn't renew until mid-2027) — leaving a residual ~€0.77m gap to hit 15% by 2027 exactly, which needs catch-up pricing at renewal, a genuine overhead (not production) headcount review, or accepting FY2028 as the more realistic target date.

The file also lists labeled assumptions and six open questions (peer-benchmark verification, overhead-vs-production FTE split, tariff-vs-usage split of the energy cost, severance/labour-law exposure, commercial confidence on winning indexation, and whether this is actually a cash/liquidity problem in disguise) that would need answers before this goes to the board.


## Files in work dir after run

- case-profitability-turnaround-saltmarsh.md
- cpt-02-input.md

## File written by the run: case-profitability-turnaround-saltmarsh.md

# Profitability turnaround: Saltmarsh Laundry Services, what explains the fall from 16.7% to 9.2% EBIT margin since 2022, and which actions restore at least 15% by 2027?

**Answer:** The margin decline is a pricing and contract-indexation problem, not a labour problem — energy and chemical costs rose 61% per kg while hospital contracts (70% of volume) carry no indexation and have not been repriced at all since 2022; a 15% headcount cut would not fix this, is operationally very hard to execute without breaching hospital service levels, and even on its most generous reading only reaches ~14.4% margin, not 15%. Indexing hospital contracts at the 2026/2027 renewals is the correct first action, but on the data given it closes most, not all, of the gap by 2027 — full effect only lands in 2028.

**Confidence:** Medium. The bridge reconciles exactly to the reported figures and the root cause is well evidenced in the client's own data. Confidence on *hitting exactly 15% by 2027* is lower, because it depends on renewal timing and on cost/overhead data not provided.

**Liquidity check:** Not assessed — no cash, debt or covenant data provided. Nothing in the brief suggests a 13-week liquidity problem; this reads as a structural margin question. Flag as open if the board's urgency is actually cash-driven.

---

## This contradicts the CEO's premise

"Labour is our biggest cost" is true in absolute terms (€13.0m in 2025, the single largest line) but it is **not what caused the margin decline**. Labour cost per kg was unchanged (€0.42 in both 2022 and 2025), kilograms washed per labour hour was unchanged, and labour cost as a share of revenue actually *improved slightly* (35.0% → 34.5%). Every euro of the €0.42m rise in the labour cost line is pure volume growth (+1.0m kg processed), not inefficiency. There is no evidence in the data of excess headcount.

## Profit bridge, 2022 → 2025

Mix was stable (hospital held exactly 70% of volume in both years), so the bridge below splits cleanly into volume, price, cost-rate and fixed-cost effects. Variable cost rates are applied as a company-wide blend (labour/energy/other are reported per kg company-wide, not by segment) — flagged as assumption A1.

| Driver | EBIT effect | Basis |
|---|---|---|
| EBIT 2022 | €6.03m (16.7% margin) | 36.03m revenue − 30.00m cost |
| Volume growth (+1.0m kg, 70/30 mix held) | **+€0.50m** | +0.7m kg hospital + 0.3m kg hotel, at 2022 blended contribution/kg |
| Price: hospital flat at €1.18/kg | **€0.00m** | No hospital repricing since 2022, despite indexed cost renewal clauses existing on only part of the book |
| Price: hotel +€0.06/kg (1.25→1.31) | **+€0.56m** | Hotel contracts reprice annually; this is the only segment that passed through any cost inflation |
| Energy & chemicals rate +€0.11/kg (0.18→0.29, +61%) | **−€3.41m** | Applied to 2025 volume (31.0m kg); by far the largest single driver |
| Labour rate: €0.42/kg, unchanged | €0.00m | No rate effect — confirms labour is not the cause |
| Other variable cost: €0.10/kg, unchanged | €0.00m | No rate effect |
| Fixed cost (+€0.2m) | **−€0.20m** | Modest growth, 2.2% over 3 years, below inflation |
| **EBIT 2025** | **€3.48m (9.2% margin)** | Reconciles exactly to the reported 9.2% |

**So-what:** the entire net decline of €2.55m EBIT is more than explained by one line — the €3.41m energy/chemicals cost increase that hospital contracts (70% of volume) are structurally unable to pass through. Volume and hotel pricing partly offset it; labour contributed nothing to the decline.

## Is this internal or market-wide?

The client's own trade-association data (self-reported, 2025 survey) states that peers **with energy indexation in their contracts** held margin in a 14–16% band across 2022–2025 — materially above Saltmarsh's 9.2%. This is consistent with the diagnosis but is a single client-supplied, self-reported statistic from an unnamed survey; treat as **weak evidence** until the underlying survey methodology, sample and Saltmarsh's own position in it are checked (see Open questions).

## Why the 15% headcount cut doesn't work

**1. It targets the wrong cost.** Labour cost per kg and labour cost as a share of revenue were flat to improving over the period in question. Cutting labour does not reverse a cost that didn't rise.

**2. It is operationally very hard to execute as framed.** Plants already run two shifts at ~94% of capacity, and kilograms washed per labour hour has been flat since 2022 — i.e., there is no documented slack to harvest. A 15% reduction in production headcount, at unchanged productivity, would cut throughput capacity to roughly 80% of the plant's current ceiling — below the 31m kg/year currently being processed, let alone the volume growth seen since 2022. Hospital contracts (70% of volume) carry 24-hour turnaround SLAs with financial penalties. A cut of this size risks triggering those penalties and losing volume at exactly the moment 40% and then 60% of hospital volume comes up for renewal (mid-2026, mid-2027) — the client's best leverage point to fix the real problem.

**3. Even in the best case, it doesn't reach 15%.** If 15% of the 2025 labour cost base (€13.02m) were removed with zero effect on volume, service or revenue — which point 2 shows is not realistic — EBIT would rise by €1.95m to €5.43m, a margin of **14.4%** on 2025 revenue, still short of the 15% target, and before any severance one-off cost is deducted.

## What does close the gap

| Action | EBIT effect | Timing | Confidence |
|---|---|---|---|
| Add energy/chemical indexation to hospital contracts at renewal | +€0.96m from mid-2026 tranche (40% of hospital volume, full-year effect by 2027) + €0.72m from mid-2027 tranche (60% of hospital volume, half-year effect in 2027) = **+€1.67m run-rate benefit recognised in FY2027**; full run-rate of **+€2.39m** only from FY2028, once both tranches are active all year | 2026–2028 | High that indexation is the right lever; medium on commercial ability to win indexation terms at renewal |
| Continue hotel pricing discipline (already recovering cost inflation) | Sustains current trajectory; no further upside assumed, since hotel is already being repriced annually | Ongoing | High |
| **Residual gap to 15% margin by FY2027** | **≈ €0.77m EBIT** (projected FY2027 EBIT €5.15m vs €5.92m needed for 15% on projected €39.46m revenue) | 2027 | — |

The residual gap exists mainly because of **renewal timing**, not because indexation is the wrong fix: the 60%-of-hospital-volume tranche doesn't renew until mid-2027, so its full benefit only shows up in FY2028. Closing the remainder by FY2027 needs one or more of:
- Negotiating the 2026 and 2027 renewals to also recover part of the 2022–2025 cost gap already accrued (catch-up pricing), not just protect forward.
- A breakdown of the €9.2m fixed-cost line: if it contains overhead/indirect headcount (not the production labour examined above), there may be a legitimate, much smaller and *targeted* headcount case there — but the data given doesn't separate production from overhead, so this cannot be sized yet.
- Energy efficiency investment to reduce consumption per kg (the 0.11/kg increase may be part tariff, part usage — the data given doesn't separate them; a usage reduction would cut cost independent of indexation).
- Revisiting whether FY2027 is realistic at all, versus FY2028 when indexation reaches full run-rate — a question for the board, not a modelling fix.

## Trap checks

- [x] Diagnosis came before any cost target; no across-the-board cut proposed.
- [x] Averages broken down: labour vs energy vs price isolated; blended per-kg cost split from segment price/volume.
- [ ] Benchmarks normalised — **not done**: the 14–16% peer figure is self-reported, unnormalised, and unsourced beyond "trade association survey 2025." Flagged as weak evidence, not used to size any action.
- [x] All actions sit in one bridge; no euro double-counted.
- [x] One-off costs and renewal timing reflected (indexation phased by renewal date; severance costs on headcount flagged as unestimated, not assumed zero).
- [x] Liquidity checked separately — no data provided, flagged as open.
- [x] No action cuts capability the recovery depends on — this is exactly why the 15% cut is rejected as proposed.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| A1 | Labour, energy and other variable costs apply equally to hospital and hotel kg | Company-wide blended rate used for both segments | No segment cost split provided | Segment-level cost data shows hospital and hotel have materially different cost profiles |
| A2 | 2027 volumes held flat at 2025 levels | 21.7m / 9.3m kg | No forecast provided; 2022–2025 growth was modest (~1%/yr) | Material volume growth or loss is expected by 2027 |
| A3 | Hospital indexation at renewal fully recovers the energy/chemical cost increase, no further increase assumed | +€0.11/kg on renewed volume | Mirrors the cost increase already observed | Energy costs continue rising after 2025, or the client cannot win full indexation in negotiation |
| A4 | No energy/chemical cost inflation beyond 2025 levels | Flat at €0.29/kg | No forecast provided | Energy/chemical costs rise or fall materially 2026–2027 |
| A5 | Severance and other one-off costs of any headcount action not estimated | Excluded from the EBIT effect above | No headcount/FTE count or severance cost data provided | Client confirms FTE numbers and local severance terms |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the trade-association 14-16% peer margin figure normalised and verifiable, and does Saltmarsh's contract mix match the "members with energy indexation" subgroup? | Currently the only external benchmark; it's self-reported and unsourced | Trade association / Saltmarsh finance | Could strengthen or weaken the "internal, not market-wide" conclusion |
| What is the FTE breakdown between production (variable, tied to kg) and overhead/indirect roles within the €9.2m fixed-cost line? | Determines whether *any* legitimate, smaller headcount action exists, and where | Saltmarsh finance / HR | Could identify a targeted (not 15% blanket) headcount opportunity in overhead only |
| Is the €0.11/kg energy and chemicals increase driven by tariff (price) or consumption (usage) per kg? | A usage-driven increase is fixable by efficiency investment; a tariff-driven one only by indexation or hedging | Saltmarsh operations/procurement | Changes which lever (efficiency capex vs commercial renegotiation) to prioritise |
| What severance cost and notice period applies to any headcount reduction, and is there a works council / collective agreement in scope? | Any cut has one-off costs and legal process that affect timing and the FY2027 number | Saltmarsh HR/legal | Could delay or add one-off cost to any headcount-related action; needs a labour-law specialist |
| Is Saltmarsh's commercial team confident it can win indexation clauses at the 2026/2027 hospital renewals, given 24-hour SLA penalty clauses give some leverage to the customer too? | The whole plan rests on this negotiation succeeding | Saltmarsh commercial team | If indexation cannot be won, no action in this plan closes the gap and the question becomes portfolio exit, not cost-cutting |
| Is there a 13-week liquidity concern driving the board's urgency? | Changes whether this is a cash problem requiring faster, different action | CEO / CFO | Would reframe the whole engagement if cash, not structural margin, is at risk |

