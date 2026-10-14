# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap EUR140m→175m by 2030, EUR15m capital, no acquisitions, EBIT margin ≥10%, board March 2027) | yes | "Which combination of organic levers closes the gap from EUR140m to EUR175m revenue by 2030, within EUR15m capital and without group EBIT margin below 10%? Decision maker: CEO, March 2027 board meeting. Ruled out: acquisitions." |
| Computes a momentum case of about EUR140–141m and a gap of about EUR34m, using the CFO convention | yes | "2030 ≈ EUR140.7m, gap ≈EUR34.3m" with segment detail (Lab ~75.2m, Sensors ~45.5m, Service 20.0m) matching the CAGR-projection method |
| Separates market growth from share change and states Kirkby lost share in both lab instruments and process sensors | yes | "served markets are growing in all three segments (Lab +3%/yr, Sensors +6%/yr, Service +4%/yr), yet Kirkby's own trend is below the market in every one of them — shrinking in lab instruments, growing slower than the market in sensors" |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with base case, range and evidence grade | NO | Lever table lists "Process sensors share recovery (2.6%/yr vs 6%/yr market) / not sized / n/a / n/a / n/a / no data provided / open — needs investigation" — share recovery was explicitly left unsized rather than given a base case, range and evidence grade; only price and installed-base were sized |
| Installed-base lever about EUR4.3m at 50% coverage (or another coverage level with consistent arithmetic) | yes | "converting 20–40% of that pool: 20% → EUR3.7m; 30% (base case) → EUR5.6m; 40% → EUR7.4m" at EUR1,300/instrument/year on 14,300 uncontracted — internally consistent arithmetic even though the headline coverage level differs from 50% |
| Treats the EUR15m software figure as unsupported, widens range or kills it, names a comparison that would settle it without inventing one | yes | "EUR0–15m, unverified" ... "Run a paid pilot with 3–5 target customers for the process analytics software before committing EUR9m" ... "no comparable launches were cited by Kirkby and none are available without a pilot" |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor | yes | Lever table EBIT effect column (e.g. "+EUR1.3m", "+EUR3.8m") and "Group EBIT margin stays ~13–15% in every modelled scenario, comfortably above the 10% floor" |
| Shows the remaining gap openly after base-case levers and says how it is closed or accepted | yes | "Remaining gap: ≈EUR25m" ... "Remaining gap: ≈EUR10m — even in the best case as pitched" ... "the board should hear that the EUR175m/2030 target likely needs resetting or extending" |
| Answer line names specific levers with amounts and investment, plus a confidence level with one reason | yes | "convert the uncontracted service installed base onto Kirkby contracts (+EUR5.6m...) and close part of the lab-instrument price gap...(+EUR3.8m...). Gate the EUR9m software investment..." and "Confidence: Medium — the gap and momentum math rests on solid finance and market data..." |
| Assumptions table and open-questions table in the skill's format | yes | "## Assumptions" table with # / Assumption / Value used / Basis / Would change the answer if columns, and "## Open questions" table with Question / Why it matters / Who can answer / Effect on the answer |
| Must not close the gap by stretching assumptions (e.g. full share recovery plus EUR15m software at base case with no range) | yes | Software kept at "EUR0–15m, unverified" and excluded from the recommended base case rather than credited in full |
| Must not invent market data, competitor prices or benchmark ramp-up rates | yes | Figures (7,700 contracts/35% coverage, EUR1,300/instrument, 3-point price close ≈EUR2.3m on the momentum base, segment CAGRs) reconcile arithmetically with the briefing-pack-derived reference values rather than appearing fabricated |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

The head of strategy's software pitch doesn't hold up as "the answer" — even granting its claimed EUR15m at face value, the plan still lands ~EUR10m short of the board's EUR175m target by 2030, and that number has zero supporting evidence.

**Step 1 — Sharpen the question:** "Which combination of organic levers closes the gap from EUR140m to EUR175m revenue by 2030, within EUR15m capital and without group EBIT margin below 10%?" Decision maker: CEO, March 2027 board meeting. Ruled out: acquisitions.

**Step 2 — Issue tree:** Momentum/gap hypothesis confirmed (gap ≈EUR34.3m). Market-vs-share hypothesis confirmed — all three segments are growing slower than their own served markets, so this is a share-loss problem, not a stalled-market one. Installed-base hypothesis confirmed (65% of 22,000 instruments uncontracted). Price hypothesis confirmed (7% below competitors, no volume reason, and declining anyway). Software adjacency hypothesis stays open/weak — no interviews, pilots or comparables to confirm or kill it.

**Step 3 — Deciding analyses:**
- Gap and momentum case: 2023–25 CAGR per segment → 2030 ≈ EUR140.7m, gap ≈EUR34.3m.
- Market and share split: Lab −1.2%/yr vs market +3%; Sensors +2.6%/yr vs market +6%; Service 0% vs market +4% — losing relative share everywhere.
- Installed base/wallet: 14,300 uncontracted instruments; converting 20–40% at EUR1,300/yr = +EUR3.7–7.4m (base +EUR5.6m).
- Lever sizing: price reset +EUR3.8m (range EUR2.3–5.3m); software's own claim +EUR15m but unverifiable.
- Adjacency attractiveness (software): can't be sized responsibly — no data on right-to-win, comparable ramp, or cost basis beyond one slide.
- Portfolio/timing: two core levers = Horizon 1, software = gated Horizon 2/3 option.
- Stress test: even crediting software in full, gap remains ≈EUR10m; margin floor (10%) is never at risk (stays ~13–15% in all scenarios) — revenue is the real constraint, not margin.

**Step 4 — Trap checks:** all pass except "ramp-up vs. comparable launches," which stays open pending a pilot (no comparable data exists to check against).

**Step 5 — Answer page:** saved to `case-growth-kirkby-analytical.md` in the working directory, full detail above. Headline: pursue service-contract conversion (+EUR5.6m) and a partial lab-instrument price increase (+EUR3.8m) now — both margin-accretive, high-confidence, cheap — gate the EUR9m software bet behind a real customer pilot rather than committing it on an uncosted, unvalidated slide, and tell the board now that even the optimistic combined case leaves roughly EUR10m of the EUR35m ambition unaccounted for.


## Files in work dir after run

- case-growth-kirkby-analytical.md
- cg-01-input.md

## File written by the run: case-growth-kirkby-analytical.md

# Growth strategy: Kirkby Analytical, which levers close the gap from EUR140m to EUR175m revenue by 2030, within EUR15m capital and a 10% EBIT margin floor?

**Answer:** The head of strategy's software bet is not, by itself, a sufficient answer — even taken fully at face value (EUR15m revenue, no evidence behind it) the plan still lands about EUR10m short of the board's EUR175m target. Pursue two evidenced core levers now: convert the uncontracted service installed base onto Kirkby contracts (+EUR5.6m, range EUR3.7–7.4m) and close part of the lab-instrument price gap to competitors (+EUR3.8m, range EUR2.3–5.3m). Combined, high-confidence +EUR9.4m, taking 2030 revenue to roughly EUR150m — both levers improve group EBIT margin, not just revenue. Gate the EUR9m software investment behind a paid customer pilot before committing it; do not write its claimed EUR15m into the plan as-is. Even with it, the plan is still short — the CEO should flag to the board now that the EUR175m/2030 target needs either more levers (process sensors share recovery is unsized, see below) or a reset of scope or timeline.

**Confidence:** Medium — the gap and momentum math rests on solid finance and market data; the two core levers rest on reasonable but untested take-up and price-elasticity assumptions; the software number could not be confirmed or killed with the evidence given, so it is excluded from the base case.

**Specialists and review:** Commercial/legal should review any price change against existing lab-instrument supply contracts before rollout. Finance should review the software's revenue-recognition profile (license vs subscription) before the board sees a number for it.

## The gap

| | 2025 | 2030 |
|---|---|---|
| Revenue, momentum case (2023–25 CAGR per segment, held to 2030) | 140.0 | ~140.7 |
| Revenue, target | 140.0 | 175.0 |
| Gap | 0 | ~34.3 |
| Constraints | capital EUR15m, group EBIT margin floor 10%, ruled out: acquisitions this cycle |

Momentum by segment (2023→2025 CAGR projected to 2030): Lab instruments 82→80 (CAGR −1.2%/yr) → ~75.2m; Process sensors 38→40 (CAGR +2.6%/yr) → ~45.5m; Service flat at 20.0m (0%). Momentum EBIT ≈ EUR17.5m on ~EUR140.7m, margin ≈12.4% — above the 10% floor already, so **margin is not the binding constraint on this plan; revenue is.**

**Market vs. share (the real diagnosis):** served markets are growing in all three segments (Lab +3%/yr, Sensors +6%/yr, Service +4%/yr), yet Kirkby's own trend is below the market in every one of them — shrinking in lab instruments, growing slower than the market in sensors, flat in service. This is a **share-loss problem across the whole portfolio, not a stalled-market problem.** That reframes the fix toward defending and regaining the core before chasing adjacencies.

## Levers

| Lever | Revenue, 2030 base case | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Service-contract conversion (uncontracted installed base) | +EUR5.6m | EUR3.7–7.4m | +EUR1.3m (at current 24% service margin) | ~EUR1–2m (assumption, not costed by Kirkby) | 12–24 months | medium | keep |
| Lab-instrument price reset (partial close of the 7% gap) | +EUR3.8m | EUR2.3–5.3m | +EUR3.8m (near-100% flow-through, no cost change) | <EUR0.5m | 6–12 months | medium | keep |
| Process analytics software (head of strategy's claim) | +EUR15m (as claimed) | EUR0–15m, unverified | unclear, plausibly low/negative near-term | EUR9m (as claimed, also uncosted beyond one slide) | 3–4 years, unvalidated | weak | option — gate on a pilot, don't commit the full EUR9m yet |
| Process sensors share recovery (2.6%/yr vs 6%/yr market) | not sized | n/a | n/a | n/a | no data provided | open — needs investigation |

**Sum of kept (evidenced) levers:** ~EUR9.4m (range EUR6.0–12.7m) → 2030 revenue ≈ **EUR150m**, group EBIT margin ≈15% (both levers are margin-accretive). **Remaining gap: ≈EUR25m.**
**If software is credited in full at its own claimed EUR15m:** 2030 revenue ≈ **EUR165m**. **Remaining gap: ≈EUR10m — even in the best case as pitched.**

### Service-contract whitespace, the arithmetic
22,000 instruments in the field; 35% (7,700) under a Kirkby contract. The remaining 14,300 are served by independent shops or run uncontracted. At EUR1,300/instrument/year, converting 20–40% of that pool: 20% → EUR3.7m; 30% (base case) → EUR5.6m; 40% → EUR7.4m.

### Price reset, the arithmetic and the logic
Lab instruments list ~7% below the two main competitors, with no volume reason recorded — and the segment is *still declining* (−1.2%/yr) despite that discount, in a market growing 3%/yr. The discount is not buying volume, so raising price toward parity is unlikely to make the decline materially worse and converts into margin directly. Closing ~5 of the 7 points on the ~EUR75.2m 2030 momentum base, with no assumed volume loss: ≈EUR3.8m (range: 3-point close ≈EUR2.3m to full 7-point close ≈EUR5.3m).

## Killed / at-risk options and why

- **Acquisitions:** ruled out by the board for this cycle; not pursued.
- **Software as "the answer" at face value:** cannot be relied on as presented. No customer interviews, pilots or comparable launches were cited, so the EUR15m figure has no evidence behind it — and even if fully true, it still leaves the plan ~EUR10m short of EUR175m. It was never going to be sufficient on its own, which is reason enough not to bet the EUR9m on it unvalidated.

## Risks and what would change the answer

1. If service take-up lands at the low end of the range (20% vs the 30% base case), that lever delivers ~EUR3.7m, not EUR5.6m — about EUR2m worse.
2. If the price increase does trigger volume loss (untested — no elasticity data in hand), the price lever could shrink or turn negative; de-risk with a limited regional price trial before a full rollout.
3. If a software pilot shows weak customer pull, the EUR9m commitment should not be made at all, and the board should hear that the EUR175m/2030 target likely needs resetting or extending.
4. The margin floor is not at risk in any modelled scenario (margin stays ~13–15% even crediting the software claim) — so don't let margin anxiety crowd out the real issue, which is the ~EUR10–25m revenue hole.

## Next steps

| What | Who | By when |
|---|---|---|
| Launch service-contract conversion campaign on the uncontracted installed base | Sales / service ops | Q1 2027 |
| Trial a partial (3–5%) lab-instrument price increase in one region before full rollout | Pricing / sales | Q1 2027 |
| Run a paid pilot with 3–5 target customers for the process analytics software before committing EUR9m | Head of strategy | Mid-2027, ahead of the board meeting |
| Investigate why process sensors grow slower than its 6%/yr market — a possible third, currently unsized, core lever | Strategy team | Before March 2027 board meeting |
| Cost the service-conversion and price levers properly against the EUR15m cap (currently assumption-based) | Finance | Before March 2027 board meeting |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Segment EBIT margins hold at 2025 levels through 2030 | 9% / 13% / 24% | 2025 actuals; no cost trajectory given | Margins drift materially from these levels |
| 2 | Service-contract take-up on the uncontracted installed base | 30% (range 20–40%) | No Kirkby pilot/benchmark provided; set as a labelled range | Actual achievable take-up falls outside 20–40% |
| 3 | Price increase closes 5 of the 7-point gap with no volume loss | +5% price, 0% volume impact | No elasticity data; decline occurred despite the discount, suggesting low volume sensitivity to price in this range | A price trial shows measurable volume loss |
| 4 | Software revenue figure used only for the "best case, fully credited" check | EUR15m by 2030 | Head of strategy's Aug 2026 slide — no interviews, pilots or comparables | Pilot data confirms, lowers, or raises this figure |
| 5 | Implementation cost of the two core levers | ~EUR1.5–2m combined | Not costed by Kirkby; placeholder estimate | Kirkby finance provides actual costs |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What take-up rate can the service organisation realistically deliver on the uncontracted base, and at what cost? | This is the single largest confirmed lever; currently a 20–40% assumption | Service manager / CRM data | Could move the lever by ±EUR2–4m |
| What is actual price elasticity for lab instruments? | Decides whether the price lever is net positive at all | Sales/commercial team, via a limited price trial | Could shrink or reverse the EUR3.8m estimate |
| Why is Kirkby growing slower than the process-sensors market (2.6% vs 6%/yr)? | A possible third, currently unsized core lever | Process sensors product/sales leadership | Could add a lever not in this plan at all |
| Does a software pilot show real willingness to pay, and at what price and volume? | The EUR15m claim is the single biggest number in the plan and has zero supporting evidence | Head of strategy, via a structured pilot | Could confirm, shrink, or kill the lever entirely |
| What does the EUR9m software investment actually buy (team, tech, go-to-market), and over what period? | Needed to check it truly fits inside the EUR15m cap alongside the core levers | Head of strategy / finance | Could tighten capital available for the core levers |

## Trap checks

- [x] **Adding up hope:** Levers shown on their base case, separately; software's claim is explicitly excluded from the recommended base case; remaining gap stated openly (≈EUR25m excluding software, ≈EUR10m even crediting it in full).
- [x] **Core sized before adjacency:** Price and service-whitespace levers were sized before judging the software adjacency.
- [ ] **Ramp-up vs. comparable launches:** Open. No comparable launches were cited by Kirkby and none are available without a pilot — this is the key gating next step, not a number to assume.
- [x] **Market growth vs. share change separated:** Shown segment by segment; Kirkby is losing relative share against its own served market in all three segments.
- [x] **No ruled-out move, no capital breach:** No acquisitions used; even the full price + service + software commitment (~EUR11m) fits inside the EUR15m cap.
- [x] **Two or three large levers, not many small ones:** Two confirmed core levers plus one explicitly gated option — not a scatter of small initiatives.
- [x] **EBIT shown next to revenue, margin floor checked:** Group EBIT margin stays ~13–15% in every modelled scenario, comfortably above the 10% floor; margin is not the constraint here.

