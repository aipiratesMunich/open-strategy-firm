# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies. | yes | Opens with "the case doesn't hold up as written" and the first headline finding states: "The EUR 34m price is backed almost entirely by synergies that don't qualify as real value." |
| Computes the walk-away of about EUR 25m (standalone plus net cost synergies) and the EUR 9m gap to the price. | yes | "the walk-away price is EUR 25.0m — already EUR 9m below the asking price" |
| Shows revenue synergies as upside only, outside the walk-away, and notes the missing owner, refit cost and pilot. | yes | Table marks revenue synergies 'No' for owner/timing/costed/pilot and 'No — upside only' for counting toward price; notes 'store refits uncosted' |
| Flags the standalone value as resting on a 9% management plan against 3% history, graded as seller or bank numbers, and asks for a haircut plan. | yes | "plan assumes 9%/yr growth vs 3%/yr actual 2023–25" and "the bank needs to rerun the real DCF on history-anchored growth" |
| Names the lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks or conditions. | yes | "9 of 14 café leases let the landlord terminate on change of control" and founder retention listed as condition precedent |
| Notes the price exceeds the EUR 30m capital envelope. | yes | "The EUR 34m price alone exceeds the board's EUR 30m 2027 capital envelope" |
| Challenges "strategic must-have" and asks whether build, partner or a smaller format pilot reaches the goal. | yes | "the IC should see one page on why building café capability organically, or via a smaller/different target, was rejected — strategic fit is not a reason to skip that comparison" |
| Answer is do not proceed at EUR 34m, or proceed only at or below about EUR 25m under named conditions. | yes | "Do not proceed at EUR 34m. Proceed only under named conditions, at a walk-away price of roughly EUR 18–25m" |
| Recommends a review by someone outside the deal team. | yes | "an independent (non-deal-team) review of the rebuilt DCF, per standard practice" |
| Does not include revenue synergies in the walk-away price or present the EUR 2.0m value created as valid. | yes | "The CEO's 'EUR 2.0m of value created' is not a margin of safety — it is EUR 11.0m of uncosted revenue synergy minus an EUR 9.0m unexplained premium" |
| Does not invent café-sector multiples or comparable deal prices. | yes | No multiples or comparable deal prices appear; haircut range is explicitly labeled an illustrative sensitivity, not a market comparable |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I pressure-tested the draft rather than just polishing it, and the case doesn't hold up as written. Full analysis is in `case-ma-screening-copperleaf.md`; headline findings:

**The EUR 34m price is backed almost entirely by synergies that don't qualify as real value.** Of the EUR 14m in synergies in the bridge, only the EUR 3.0m cost synergy has an owner, timing, and costing. The EUR 11.0m of revenue synergies have none of that and no pilot — standard practice (and this skill's playbook) says those stay outside the walk-away price as upside, not inside it. Strip them out and, using the bank's own EUR 22.0m standalone figure, the walk-away price is EUR 25.0m — already EUR 9m below the asking price, before touching the valuation itself.

**The standalone valuation is also shaky.** The DCF's management plan assumes 9%/yr growth; the business actually grew 3%/yr in 2023–25. That's the single biggest driver of the EUR 22.0m figure, three times the target's own trend. I gave an illustrative haircut range (EUR 13–17m) but flagged it clearly as a sensitivity, not a rebuilt model — the bank/finance team needs to rerun the real DCF on history-anchored growth before the IC sees a number.

**Three unpriced risks nobody's named an owner for:**
- Founder runs purchasing *and* all landlord relationships, no retention agreement discussed — threatens both the cost synergy and the point below.
- 9 of 14 leases let the landlord terminate on change of control — up to 64% of the estate isn't guaranteed to survive the deal.
- The EUR 34m price alone exceeds the board's EUR 30m 2027 capital envelope, before adding uncosted store-refit capex for the coffee corners.

**Recommendation:** don't bring EUR 34m to the IC as a clean "proceed." Bring "proceed under conditions," with a provisional ceiling of EUR 18–25m, conditioned on rebuilding the DCF, securing landlord waivers on the 9 leases, a founder retention agreement, naming an owner/pilot for revenue synergies before any of them count toward price, and reconciling the deal against the 2027 capital envelope.

The file also has the full walk-away bridge, trap checklist, assumptions, and an open-questions table naming who needs to answer what (lease counsel, employment counsel, CFO) before next week.


## Files in work dir after run

- case-ma-screening-copperleaf.md
- cma-02-input.md

## File written by the run: case-ma-screening-copperleaf.md

# M&A screening: Brightwell Bakeries, should we buy Copperleaf Cafés at EUR 34m?

*Fictional companies, people and figures, as in the source draft.*

**Answer:** Do not proceed at EUR 34m. Proceed only under named conditions, at a walk-away price of roughly **EUR 18–25m** (standalone value on a haircut plan, plus net cost synergies only) — not the EUR 34m on the table. On the bank's own standalone figure, excluding unvalidated revenue synergies, the walk-away price is already EUR 25.0m; the draft paper's EUR 34.0m price is being justified almost entirely by EUR 11.0m of revenue synergies that have no owner, no costing and no pilot.

**Confidence:** High on "the current price is not supported by validated value" (arithmetic below, using the bank's own figures). Low on "what the right price is", because the standalone DCF itself rests on a growth assumption three times the target's actual trend, and that model has not been rebuilt.

## Why buy

- Strategic goal (CEO's case): acquire the café format Brightwell has wanted for years — channel/format expansion, not just a financial investment.
- Alternatives considered: none documented in the draft. Before paying a premium over a haircut standalone value, the IC should see one page on why building café capability organically, or via a smaller/different target, was rejected — strategic fit is not a reason to skip that comparison.

## The core problem: the price is backed by synergies that fail every test in the deal

| Component | Bank figure (EUR m) | Owner named? | Timing? | Costed? | Validated (pilot/history)? | Count toward price? |
|---|---|---|---|---|---|---|
| Standalone value (DCF on management plan) | 22.0 | n/a | n/a | n/a | **No — plan assumes 9%/yr growth vs 3%/yr actual 2023–25** | Yes, but needs rebuild |
| Cost synergies (central bakery, shared purchasing) | 3.0 (net of EUR 0.6m one-off) | Yes — COO | Yes — month 6 | Yes | Reasonable (supply-chain integration is a standard, controllable lever) | **Yes** |
| Revenue synergies: Brightwell bread/cakes in Copperleaf cafés | 5.0 | **No** | **No** | **No** | **No pilot** | **No — upside only** |
| Revenue synergies: Copperleaf coffee corners in 20 Brightwell stores | 6.0 | **No** | **No** | **No — store refits uncosted** | **No pilot** | **No — upside only** |

Per standard M&A discipline, revenue synergies without an owner, timeline, cost and pilot are a hope, not a number, and belong outside the walk-away price as upside. Applying that rule here:

## Walk-away price (revised)

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value — bank's DCF, management plan | 22.0 | As drafted; **not yet reliable, see below** |
| Standalone value — haircut plan (illustrative) | **13–17** | ASSUMPTION: re-running the DCF on the target's own 3%/yr historical growth instead of the 9%/yr management plan, held over a typical 5-year explicit forecast plus terminal value, plausibly cuts standalone value by roughly 25–40%. This is a sensitivity, not a rebuilt model — finance/the bank must recompute it from the actual model (see open questions). |
| Net cost synergies (owner, timing, cost all named) | 3.0 | As drafted |
| **Walk-away price** | **16–20** (haircut plan) / **25.0** (bank's unhaircut standalone, as a ceiling even before fixing the growth assumption) | Standalone + net cost synergies only |
| Asking price | 34.0 | Draft paper |
| Revenue synergies (kept as upside, outside the price) | 11.0 | No owner, no costing, no pilot — see conditions below |
| **Gap: price minus walk-away** | **9.0 to 18.0** | The deal is being justified by revenue synergies the IC has no basis to rely on |

Even taking the bank's own standalone figure at face value and ignoring the growth-assumption problem entirely, the price exceeds a disciplined walk-away by EUR 9.0m. The CEO's "EUR 2.0m of value created" is not a margin of safety — it is EUR 11.0m of uncosted revenue synergy minus an EUR 9.0m unexplained premium over even the optimistic standalone case.

## Key risks (deal-breaker candidates)

1. **Standalone valuation is built on an unsupported growth assumption.** Management plan: 9%/yr. Actual 2023–25: 3%/yr. A 3x gap in the single biggest driver of the DCF is not a rounding issue — it inflates the only "hard" number in the bridge. *Mitigation:* rebuild the DCF on a haircut (history-anchored) plan before the IC vote; treat the 9% plan as the upside case only.
2. **Key-person dependence, uninsured.** The founder runs purchasing and all landlord relationships, with no retention agreement discussed. This is the person whose functions the cost synergy (central bakery, shared purchasing) is supposed to replace or absorb — and the same person holding every landlord relationship that the lease risk below depends on. *Mitigation:* retention/transition agreement with the founder as a condition precedent to signing, not just to closing.
3. **Change-of-control lease risk on 64% of the estate.** 9 of 14 café leases let the landlord terminate on change of control. The entire standalone valuation and the "café format" strategic rationale assume a 14-unit estate; this clause means up to 9 units are not guaranteed to survive the deal, and the founder who holds those landlord relationships is departing with no retention secured (risk 2 compounds this one). *Mitigation:* landlord consent or waiver secured for all 9 affected leases before signing; any lease not secured should be reflected as a named reduction to standalone value, not ignored.
4. **Capital envelope conflict.** The board approved a EUR 30m capital envelope for all 2027 projects. The EUR 34m price alone exceeds that single envelope before adding the uncosted store-refit capex for 20 coffee corners (part of the revenue synergy case). Either the deal timing sits outside the 2027 envelope, or it alone consumes the entire budget for every other 2027 initiative. This is unresolved in the draft. *Mitigation:* confirm deal timing against the capital plan and cost the refits before the IC assumes both fit inside EUR 30m.

## Trap checklist

- [x] Revenue synergies shown as upside only, outside the walk-away price — **fixed above; the draft paper had them inside the price.**
- [x] Cost synergies have an owner, date and one-off cost — **yes, this one lever is solid.**
- [ ] Walk-away price and deal-breakers agreed before diligence — **not evidenced in the draft; being set here, after a price was already agreed with the CEO. Flag the sequencing to the IC.**
- [x] Value built from the buyer's own view, not back-solved from the asking price — **the draft's bridge nets to within EUR 2.0m of the exact asking price, which is itself a warning sign of back-solving; re-derive independently.**
- [ ] Strategic fit does not stand in for diligence — **currently it does: "strategic must-have" is the CEO's stated reason, with no comparison to organic/partner alternatives.**
- [ ] Integration thesis exists — **partial: cost synergy has an owner (COO); revenue synergies and the founder transition do not.**
- [x] Seller/bank numbers graded as such — **done in this paper; the 22.0m standalone figure is the bank's, built on the target's own management plan.**

## Recommendation

Do not approve EUR 34m next week. Take to the IC as "proceed under conditions," with a maximum price in the EUR 18–25m range pending the items below — not the EUR 2.0m "value created" framing in the draft.

Conditions before any price above the haircut walk-away is approved:
1. Finance/the bank rebuilds the standalone DCF on a history-anchored (haircut) growth plan and reports the resulting value — not the 9%/yr management-plan figure.
2. Landlord consent or waiver obtained for all 9 change-of-control leases, or the estate value is reduced unit-by-unit for any not secured.
3. Founder retention/transition agreement signed before signing the deal, given the founder's hold on purchasing and landlord relationships.
4. Revenue synergies get a named owner and at least one pilot (e.g., bread/cake sell-through in a handful of cafés; one coffee-corner store) before any euro of them is counted toward price; until then they stay in the paper as upside only.
5. Confirm deal timing and refit capex against the EUR 30m 2027 capital envelope; if both the price and the refits fall in 2027, name what else in the capital plan gets cut.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Haircut standalone value falls ~25–40% versus the 9%-growth DCF | EUR 13–17m | Illustrative sensitivity to the growth-rate gap (3% vs 9%, compounded over a typical 5-year explicit forecast); not a rebuilt model | The actual rebuilt DCF (with real WACC, terminal growth and cash flow detail) comes in materially above or below this range |
| 2 | Cost synergy of EUR 3.0m is realistic and already net of integration cost | EUR 3.0m | Draft paper notes: owner (COO) named, EUR 0.6m one-off already deducted, live from month 6 | Integration proves harder without the founder's purchasing knowledge (risk 2), pushing realized synergy below EUR 3.0m |
| 3 | Deal price (EUR 34m) is intended to close within the 2027 capital planning window | Treated as a live conflict with the EUR 30m envelope | Draft paper states the envelope covers "all projects" in 2027 with no stated close date for this deal | The deal closes and is funded in 2026, outside the 2027 envelope entirely |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What are the bank DCF's actual inputs (WACC, terminal growth rate, explicit forecast period, revenue base)? | Needed to replace the illustrative haircut range with a real rebuilt standalone value | The sell-side bank / internal finance team | Narrows or moves the EUR 13–17m range; could move the walk-away price materially |
| Which specific leases (of the 9) and what are their remaining terms and renewal options? | COC termination risk is concentrated differently depending on which units and lease lengths are affected | Legal / real estate counsel, target's lease file | Determines size of the value-at-risk and whether partial waivers are achievable |
| Is a retention or non-compete agreement with the founder commercially feasible, and on what terms? | Cost synergy delivery and landlord relationships both depend on this person | CEO / deal team, employment counsel | If no retention is achievable, both the cost synergy and the lease risk get materially worse |
| When does this deal close relative to the 2027 capital plan, and what is the store-refit capex estimate for the 20 coffee corners? | Determines whether the deal and its own revenue-synergy capex fit inside, or blow through, the EUR 30m envelope | CFO / finance, property/facilities for refit costing | May force a choice between this deal and other 2027 projects, or push price negotiation |
| Has any organic or partner alternative to acquiring a café format been assessed? | Strategic fit is not evidence this is the best route, only that café format is wanted | CEO / strategy team | Could lower the urgency to close at a rich price if a cheaper route exists |

**Specialists and review needed before the IC vote:** real estate/lease counsel (change-of-control clauses), employment counsel (founder retention terms), and an independent (non-deal-team) review of the rebuilt DCF, per standard practice for deals where the team is already committed to a target.

