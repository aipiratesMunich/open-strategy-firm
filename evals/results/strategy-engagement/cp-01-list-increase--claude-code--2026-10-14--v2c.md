# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs waterfall first and states uncapped 22% small-direct discount as the leak that could prevent list increase reaching pocket price | yes | 'for small direct accounts it will not, unless discount authority is capped' and segment table flags 'Any sales rep, no cap' / 'Highest leakage risk' for the 22% small-direct discount |
| Break-even volume loss ~11% computed with contribution margin, formula/arithmetic shown | yes | 'Break-even volume loss = 1 − m/(m+p) = 1 − 0.40/0.45 ≈ 11.1%' |
| Uses 2023 change (-2% for +3%) as revealed behaviour, compares expected loss (~3-4%) with break-even | yes | 'list prices rose 3% in January 2023; volume fell 2%... Applying the same relationship to a 5% increase gives an expected volume loss of roughly 3–4%' compared against the 11.1% break-even cushion |
| EBIT effect as a range across volume reactions with arithmetic shown | yes | Table: 0% → +1.20m, -2% → +0.98m, -3.5% → +0.82m, -7% → +0.44m, -11.1% → 0; headline states '+EUR 0.4m to +1.0m/year' |
| Differentiates by segment (OEM January renewal, distributor 60-day notice, discount cap/approval for small direct accounts) | yes | Implementation table: 'OEM key accounts... Before/at January renewal'; 'Distributors... Issue 60-day price-list notice'; 'Small direct accounts... Apply new list price; cap or re-approve discount authority' |
| Anchors recommendation on customer value and like-for-like competitor gap, not cost | yes | 'Cost sets the floor only — recommendation is anchored on the competitor benchmark (still 2–4% below market post-increase)... not on the 40% contribution margin'; price position table notes delivery performance as a value signal |
| Names competitor reaction scenario (follow/hold/undercut) and trigger for different answer | yes | 'If either competitor responds by cutting price rather than following... a scenario re-run (follow/hold/undercut) is needed before the next increase' |
| Answer line states decision type, amount, segments, date, EBIT range | yes | 'Go ahead with a 5% list price increase on the standard seal range from 1 March 2027... Expected EBIT effect... +EUR 0.4m to +1.0m a year... OEM contracts (55% of volume)... small direct accounts (15% of volume)' |
| Names source of 2023 comparison (industry association) and treats as one data point, states dependency | yes | 'market volume from the industry association's member-reported shipment statistics'; 'this is a single, confounded data point'; 'If the 2023 volume drop is shown to have a cause other than price... volume risk should be treated as unknown' |
| Must not compute break-even with gross margin or without showing formula | yes | Uses contribution margin (40%) explicitly with formula 1 − m/(m+p), not gross margin |
| Must not suggest sharing price intentions with competitors or using competitor contract data | yes | 'No step used competitor coordination — all competitor data is from public September 2026 price lists and Ravensworth's own customer audits' |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

Answer page written to `case-pricing-ravensworth.md`.

**Bottom line:** go ahead with the 5% increase — it still leaves Ravensworth 2–4% below both competitors on comparable parts, and the break-even cushion (11.1% volume loss) is wide against the estimated 2–7% loss implied by the 2023 episode. Full run-rate EBIT effect: **+EUR 0.4m to +1.0m/year**. The catch isn't price level, it's execution: OEM contracts (55% of volume) renew in January and could lock out the increase until 2028 unless it's written into those renewals now, and small direct accounts (15%) have uncapped discount authority that can discount it straight back away. Both need to be board conditions, not afterthoughts.

The file also flags where the evidence is thin and names who needs to answer what before this goes fully firm — notably the OEM renewal dates vs. the board date, and whether the 2023 volume drop was really price-driven.


## Files in work dir after run

- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth.md

# Pricing: Ravensworth Industrial Seals, can we raise standard seal range list prices 5% from 1 March 2027?

**Answer:** Go ahead with a 5% list price increase on the standard seal range from 1 March 2027 — but treat it as three separate execution problems, not one date. Expected EBIT effect once fully phased in: **+EUR 0.4m to +1.0m a year** (vs. +EUR 1.2m if zero volume is lost), comfortably inside a break-even cushion of 11.1% volume loss. The risk that overturns this isn't price level, it's **execution**: OEM contracts (55% of volume) renew in January and may lock in the old price before the increase can apply, and small direct accounts (15% of volume) have uncapped discount authority that can discount the increase away. Fix both before the board signs off, not after.

**Confidence:** Medium — price position and break-even math are solid, but the volume-loss estimate rests on a single historical episode and there is no data on competitor reaction, OEM renewal dates relative to the board date, or sales incentives.

**Specialists and review:** Legal/competition counsel should confirm the announcement of the increase to distributors and OEM accounts carries no price-signalling risk (routine check; the analysis itself uses only public price lists and Ravensworth's own data). Contracts/legal should confirm notice-period mechanics for distributor price-list changes.

## Price position
| Offer | Our price (list) | Competitor A | Competitor B | Value difference | Gap explained? |
|---|---|---|---|---|---|
| 40 comparable part numbers, Sept 2026 | Index 100 | Index 108–109 | Index 107–109 | Ravensworth 7–9% below on like-for-like spec; comparable lead times; better on-time delivery (96% vs. customers' stated 90% average, 2025 audits) | No — gap not explained by spec or service; if anything Ravensworth delivers more |

After a 5% increase, Ravensworth would still sit roughly 2–4% below both competitors on list price, while performing better on delivery. **Hypothesis confirmed: there is headroom to raise price without moving above the market.**

## Value to customer
No customer interview or value-quantification data in the pack (downtime cost avoided, cost of a competitor stockout, etc.). This branch cannot be tested from what's given — treated as an open question, not assumed. The position and revealed-behaviour evidence below substitute as a weaker but directionally consistent signal.

## Willingness to pay / volume reaction (revealed behaviour)
Only data point: list prices rose 3% in January 2023; volume fell 2% over the following 12 months against a flat market (Ravensworth sales data; market volume from the industry association's member-reported shipment statistics). That implies a rough relative elasticity of -2/3 ≈ -0.67 — i.e., each 1% price rise cost about 0.67% volume relative to the market.

Applying the same relationship to a 5% increase gives an **expected volume loss of roughly 3–4%** (wide range 2–7% given this is a single, confounded data point — no way to rule out other causes of the 2023 drop, e.g. a lost account or capacity limit unrelated to price).

**Hypothesis: expected volume loss stays well below break-even — confirmed**, provisionally, pending a sanity check with the sales director that nothing else explains the 2023 drop.

## Price waterfall (average, standard seal range)
| Step | EUR per 100 list | % of list |
|---|---|---|
| List price | 100 | 100% |
| On-invoice discount | -12 | 12% |
| Invoice price | 88 | 88% |
| Annual volume rebates | -4 | 4% |
| Free freight | -3 | 3% |
| Pocket price | 81 | 81% |

2025 pocket revenue EUR 24.0m ÷ 81% ⇒ implied 2025 list revenue ≈ **EUR 29.6m**.

By segment, on-invoice discount and who controls it:
| Segment | Share of volume | On-invoice discount | Approver | Execution risk for a list increase |
|---|---|---|---|---|
| OEM key accounts | 55% | 8% | Key account director | **Contract-timing risk** (below), not discount creep — discount itself is controlled |
| Distributors | 30% | 12% | Sales director | Controlled; main risk is the 60-day notice clock |
| Small direct accounts | 15% | 22% | **Any sales rep, no cap** | **Highest leakage risk** — nothing stops reps discounting the 5% straight back out |

Blended discount from the segment table (0.55×8 + 0.30×12 + 0.15×22 = 11.3%) runs slightly below the 12% in the aggregate waterfall — a rounding or mix gap worth asking finance about, not large enough to change the answer.

**Hypothesis: execution risk is segment-specific, not uniform — confirmed.** The increase will reach pocket price for OEM and distributor volume if the timing issues below are managed; for small direct accounts it will not, unless discount authority is capped at the same time.

## Profit effect (full run-rate, once applied to all volume)
Formula: price gain on retained volume ≈ pocket revenue × (1−loss) × 5%; contribution lost on departed volume ≈ pocket revenue × loss × 40%. Break-even volume loss = 1 − m/(m+p) = 1 − 0.40/0.45 ≈ **11.1%**.

| Volume reaction | Revenue effect | EBIT effect |
|---|---|---|
| 0% (no loss) | +EUR 1.20m | +EUR 1.20m |
| -2% (low end of estimate) | +EUR 1.18m price gain, -EUR 0.19m lost contribution | **+EUR 0.98m** |
| -3.5% (central estimate) | +EUR 1.16m price gain, -EUR 0.34m lost contribution | **+EUR 0.82m** |
| -7% (high end of estimate) | +EUR 1.12m price gain, -EUR 0.67m lost contribution | **+EUR 0.44m** |
| -11.1% (break-even) | — | EUR 0 |

**Year-one caveat:** if OEM contracts (55% of volume) renew in January before the increase can be written into them, only the distributor + small-direct base (≈45% of volume) carries the increase in 2027. Year-one EBIT effect would then be roughly **+EUR 0.2m to +0.45m**, with the full +EUR 0.4m–1.0m run-rate arriving only once OEM renews again in January 2028. This is the single biggest swing factor in the whole case — bigger than the volume-loss uncertainty — and it is a sequencing decision, not a pricing one.

## Implementation
| Step | Segment | Date | Owner | Sales rule / approval |
|---|---|---|---|---|
| Confirm exact 2027 OEM renewal dates vs. board date; write 5% into renewal terms directly | OEM key accounts (55%) | Before/at January renewal | Key account director | None currently capped — risk is timing, not authority |
| Issue 60-day price-list notice | Distributors (30%) | Immediately after board approval (to land by ~1 March) | Sales director | Confirm notice sent and acknowledged, not just mailed |
| Apply new list price; cap or re-approve discount authority | Small direct accounts (15%) | 1 March 2027 | Sales director | Introduce a discount ceiling (e.g. hold at current 22% as a cap, not a floor) so reps cannot silently discount the increase away |
| Brief sales force on competitor price gap and delivery performance as the argument for holding the line | All segments | Before 1 March 2027 | Sales director | None provided in the pack on incentive structure — see open questions |

## What would change the answer
1. If OEM renewal dates fall before the board can authorise the new price, confirm whether the increase can still be inserted into those contracts — if not, the 2027 EBIT effect is roughly half the run-rate figure and the real decision date moves to January 2028 for 55% of volume.
2. If the 2023 volume drop is shown to have a cause other than price (e.g., one account lost, a capacity constraint), the elasticity estimate is unsupported and volume risk should be treated as unknown, not 3–7%.
3. If small direct account discounting is not capped, assume the 5% increase does not reach pocket price for that 15% of volume, cutting the effect further.
4. If either competitor responds by cutting price rather than following, the "still below market after +5%" support weakens and a scenario re-run (follow/hold/undercut) is needed before the next increase.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | On-invoice discount, rebates and freight scale proportionally with list price, so a 5% list increase passes 5% through to pocket price absent discounting behaviour | 5% pass-through | Waterfall is stated entirely in % of list price | Rebates or freight are fixed EUR amounts per order rather than %-based — pass-through could be higher (freight burden shrinks as % of a higher price) or lower |
| 2 | Segment volume shares (55/30/15%) approximate segment revenue shares for the purposes of the OEM-delay sizing | Revenue split ≈ volume split | No segment-level pocket revenue given | Finance provides segment P&L showing OEM's revenue share differs materially from its volume share (plausible, since its discount is lowest) |
| 3 | The 2023 price/volume relationship (3% price → -2% relative volume) is a valid proxy for a 5% increase in 2027 | Elasticity ≈ -0.67, volume loss 2–7% (central ~3.5%) | Only historical data point in the pack | The 2023 episode had a confounding cause, or market conditions in 2027 differ materially (e.g. a competitor capacity change) |
| 4 | No board-set volume-loss tolerance exists, so break-even (11.1%) is used as the pass/fail threshold instead of a management ceiling | Break-even as threshold | Not stated in the pack | Sales director sets a tighter internal ceiling (e.g. "no more than 3%") — case would then hinge on the lower end of the volume estimate only |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What volume loss would the board/sales director accept, and over what period? | Sharpens the decision threshold instead of defaulting to break-even | Sales director / board | Could tighten or loosen the go/no-go test |
| What are the exact 2027 OEM contract renewal dates relative to the January board date? | Determines whether 55% of volume gets the increase in 2027 or only from 2028 | Key account director / contracts team | Swings year-one EBIT effect by roughly half |
| Are rebates and free-freight costs a % of invoice value or fixed EUR per order/shipment? | Changes the true pass-through rate used in the profit-effect table | Finance / pricing team | Could raise or lower the EBIT range |
| Is the 22% small-direct-account discount a deliberate policy or genuine uncapped rep discretion, and is there any existing floor? | Determines whether the "no cap" risk is real or already informally managed | Sales director | If genuinely uncapped and unmanaged, expect most of the 15% small-direct volume to see little real price gain |
| What caused the 2-point relative volume drop after the 2023 increase — was it price alone? | The entire volume-risk estimate rests on this one data point | Sales director / sales ops (account-level win/loss data) | Could remove or strengthen the only volume-reaction evidence available |
| Are competitors likely to follow, hold, or undercut given their cost position and capacity? | No signal in the pack beyond list prices; changes medium-term risk beyond year one | Competitive intelligence, from public sources only | Would inform a follow-up scenario analysis, not this decision |
| How is the sales force incentivised (on list, pocket price, or volume)? | Determines whether reps will defend or quietly erode the increase | Sales director / HR compensation | Missing incentive alignment is a known way increases get discounted away |

## Trap checks
- [x] Cost sets the floor only — recommendation is anchored on the competitor benchmark (still 2–4% below market post-increase) and revealed past behaviour, not on the 40% contribution margin.
- [ ] Stated willingness to pay cross-checked with revealed behaviour — **open**: no interview or stated-WTP data exists in the pack at all; only the 2023 revealed-behaviour episode is used, and it is a single, weakly-evidenced data point (flagged in Assumptions #3 and Open questions).
- [x] Change differs by segment where risk differs — same 5% level for all three segments (as the sales director asked), but execution controls are segment-specific (OEM timing fix, distributor notice clock, small-direct discount cap).
- [ ] Execution fixed with the level — **open**: the small-direct discount cap and the OEM renewal-timing fix are recommended here but not yet confirmed as agreed actions; board sign-off should make both conditions of approval, not afterthoughts.
- [x] Break-even volume loss computed with contribution margin (11.1%) and compared with expected loss (2–7%, central ~3.5%) — comfortable cushion.
- [ ] Sales has arguments, incentives and approval rules for the change — **open**: incentive structure unknown (see Open questions); competitor/delivery argument is available and should be briefed to the sales force.
- [x] No step used competitor coordination — all competitor data is from public September 2026 price lists and Ravensworth's own customer audits.

