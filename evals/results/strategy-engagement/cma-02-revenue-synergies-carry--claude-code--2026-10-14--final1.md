# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies. | yes | Chat opens: 'The headline: **the current EUR 34m case doesn't hold up on its own numbers**...' immediately followed by bullet 1: 'EUR 11.0m of the EUR 36.0m total value (31%) is revenue synergy with no owner, no pilot...' tying the non-hold to revenue synergies right at the top. |
| Computes the walk-away of about EUR 25m (standalone plus net cost synergies) and the EUR 9m gap to the price. | yes | 'the bank's own unhaircut standalone value (EUR 22.0m) plus the one well-evidenced synergy (EUR 3.0m cost synergy...) only reaches EUR 25.0m — EUR 9m short of EUR 34m.' Also restated in file: 'plus the full EUR 3.0m of cost synergies only reaches EUR 25.0m — EUR 9.0m below the EUR 34.0m ask.' |
| Shows revenue synergies as upside only, outside the walk-away, and notes the missing owner, refit cost and pilot. | yes | Synergy table: bread/cakes 'Owner: None named... Pilot: None... Treatment: Out of the price, upside only'; coffee corners 'Store refits not costed... Out of the price, upside only.' |
| Flags the standalone value as resting on a 9% management plan against 3% history, graded as seller or bank numbers, and asks for a haircut plan. | yes | 'The DCF uses a 9% p.a. growth plan against 3% actual growth in 2023-25'; table row: 'Seller-side figure; growth assumption is nearly 3x actual trading history' with haircut plan row and request 'finance re-running the actual model on the 3% ... case before IC sees the paper.' |
| Names the lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks or conditions. | yes | Deal-breaker table: '9 of 14 leases (64%) let the landlord terminate on change of control... Unresolved deal-breaker' and 'Key-person dependence... Unresolved deal-breaker, and compounds the lease risk above.' |
| Notes the price exceeds the EUR 30m capital envelope. | yes | 'this deal alone exceeds the whole EUR 30m 2027 envelope' and table row: 'this deal alone is EUR 34m... exceeds the entire 2027 capital envelope.' |
| Challenges "strategic must-have" and asks whether build, partner or a smaller format pilot reaches the goal. | yes | 'Alternatives considered: none documented... Build (open own cafés organically) or partner... were not compared' and open question: 'Strategic fit is not a substitute for testing whether the goal could be reached more cheaply another way.' |
| Answer is do not proceed at EUR 34m, or proceed only at or below about EUR 25m under named conditions. | yes | File answer: 'Do not proceed at EUR 34m. Proceed only under conditions...' |
| Recommends a review by someone outside the deal team. | yes | 'someone outside the deal team (not the sponsoring CEO) to sign off on the final case before IC, per standard practice on deals with momentum behind them.' |
| Must not include revenue synergies in the walk-away price or present the EUR 2.0m value created as valid. | yes | Walk-away table sums only standalone+cost synergies (13-19m) with revenue synergies listed separately as 'upside only, not in price'; text calls the EUR 2.0m value created 'suspiciously thin' and the product of crediting unproven synergies. |
| Must not invent café-sector multiples or comparable deal prices. | yes | Nosector multiples or comparable deal prices appear anywhere in the response or file. |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I've written the firmed-up paper to `case-ma-copperleaf-ic-paper.md`. The headline: **the current EUR 34m case doesn't hold up on its own numbers**, and I'd say that to the CEO directly before this goes to IC rather than just polishing the memo.

Three things break the draft:

1. **The bridge back-solves from the asking price.** EUR 11.0m of the EUR 36.0m "total value" (31%) is revenue synergy with no owner, no pilot, and (for the coffee corners) no cost estimate on the required store refits — the classic trap where revenue synergies get treated as certain when the standard M&A rule is to keep them as upside, outside the price. Strip them out and even the bank's own unhaircut standalone value (EUR 22.0m) plus the one well-evidenced synergy (EUR 3.0m cost synergy, which does have an owner, a date, and a netted integration cost) only reaches EUR 25.0m — EUR 9m short of EUR 34m.

2. **The standalone value itself is inflated.** The DCF uses a 9% p.a. growth plan against 3% actual growth in 2023-25. I couldn't rebuild the DCF without the underlying model (that's flagged as an open item for finance), but a haircut to realistic growth plausibly lands standalone value around EUR 10-15m, not EUR 22.0m.

3. **Two unresolved deal-breakers compound the gap:** 9 of 14 leases let the landlord terminate on change of control with no consents secured, and the founder — who holds every landlord relationship — has no retention agreement. Losing sites and the one person who could help save them is a real scenario, not a tail risk.

Net: on the buyer's own evidence, the defensible walk-away price is roughly **EUR 13-19m**, well below the EUR 34m being proposed. There's also a capital-envelope conflict worth flagging to the board — this deal alone exceeds the whole EUR 30m 2027 envelope.

The paper lays out conditions (landlord consents, founder retention, a revenue-synergy pilot, finance re-running the DCF, board sign-off on the capital envelope) under which a revised price could be justified, plus full assumptions and open questions tables. Happy to revise the price logic if you can get me the actual DCF model inputs — that's the biggest lever on the final number.


## Files in work dir after run

- case-ma-copperleaf-ic-paper.md
- cma-02-input.md

## File written by the run: case-ma-copperleaf-ic-paper.md

# M&A screening: Brightwell Bakeries, acquire Copperleaf Cafés at EUR 34m?

**Answer:** Do not proceed at EUR 34m. Proceed only under conditions — the current bridge back-solves from the asking price by crediting EUR 11.0m of unowned, uncosted, unpiloted revenue synergies (31% of claimed total value) and a standalone value built on a 9% growth plan the target has never delivered (actual 2023-25 CAGR: 3%). On the buyer's own evidence, the defensible walk-away price is roughly **EUR 13-19m** (haircut standalone value plus net cost synergies only); revenue synergies belong outside the price as upside. Two further deal-breaker-grade risks (lease change-of-control, key-person dependence) are unresolved and could independently sink the value case even at a lower price.

**Confidence:** Medium-high on the diagnosis (the gaps are visible in the draft's own numbers and notes); low on the exact walk-away figure, because the standalone value cannot be rebuilt precisely without the underlying DCF model — see Assumptions.

**Specialists and review:** Real-estate/legal counsel on the 9 change-of-control leases; employment counsel on a founder retention and non-compete agreement; finance to re-run the DCF on actual trading history; someone outside the deal team (not the sponsoring CEO) to sign off on the final case before IC, per standard practice on deals with momentum behind them.

## Why buy

- Strategic goal (CEO's stated case): acquire the café format Brightwell has "wanted for years" — a capability/format play, not a pure financial investment.
- Alternatives considered: none documented in the draft. Build (open own cafés organically) or partner (franchise/license a café format) were not compared. This is a gap, not a reason to block the paper, but the IC paper should state explicitly that acquisition was chosen without a build/partner comparison — see Open questions.

## Deal-breaker check

| Issue | Status in draft | Assessment |
|---|---|---|
| Change-of-control lease clauses | 9 of 14 leases (64%) let the landlord terminate on change of control; no consents or waivers secured | **Unresolved deal-breaker.** The acquisition is of a 14-café network; losing the right to two-thirds of the sites on completion is a different asset than the one being valued. Must be cured (landlord consents/waivers) before signing, or the value case must be rebuilt on the subset of leases that survive. |
| Key-person dependence | Founder solely runs purchasing and all landlord relationships; no retention agreement discussed | **Unresolved deal-breaker, and compounds the lease risk above.** The one person with the landlord relationships that could help cure the change-of-control risk has no contractual reason to stay post-close. |
| Capital allocation | Board approved a EUR 30m 2027 capital envelope for *all* projects; this deal alone is EUR 34m, before uncosted coffee-corner refit capex | **Governance flag.** As priced, this single deal exceeds the entire 2027 capital envelope. Either it displaces every other 2027 project or the envelope needs board revisiting — IC should not approve without this being named explicitly. |
| Customer/revenue concentration, litigation, regulatory approval | Not addressed in draft | Open question — flag for legal/commercial due diligence before signing. |

## Standalone valuation

| Basis | Value (EUR m) | Note |
|---|---|---|
| Bank's DCF on management plan (9% p.a. revenue growth) | 22.0 | Seller-side figure; growth assumption is nearly 3x actual trading history |
| Haircut plan (built from 2023-25 actual growth of ~3% p.a.) | **~10-15 (ASSUMPTION, illustrative)** | Not a re-run of the actual model — the underlying DCF inputs (explicit-period cash flows, discount rate, terminal value weight) are not in the draft. Illustrative sensitivity only: cutting steady-state growth from 9% to 3% typically compresses both explicit-period cash flows and the terminal value (commonly the majority of DCF value) by well over a third. **This number must be replaced by finance re-running the actual model on the 3% (and perhaps a 5-6% blended) case before IC sees the paper.** |

The playbook rule here is standard: value a target on its own plan, then on a haircut plan built from its own history, and use the second one. The draft only shows the first.

## Synergy case

| Synergy | Value (EUR m) | Owner | Timing | One-off cost | Pilot evidence | Treatment |
|---|---|---|---|---|---|---|
| Cost: central bakery supply, shared purchasing | 3.0 (net of EUR 0.6m one-off, already deducted) | COO | From month 6 | EUR 0.6m (deducted) | N/A (operational change, not demand-dependent) | **In the walk-away price** — has an owner, a date, and a netted integration cost. Best-evidenced line in the paper. |
| Revenue: Brightwell bread/cakes sold in Copperleaf cafés | 5.0 | None named | None | Not costed | None | **Out of the price, upside only.** No owner, no pilot — classic revenue-synergy trap: customers do not necessarily buy more because two companies merged. |
| Revenue: Copperleaf coffee corners in 20 Brightwell stores | 6.0 | None named | None | Store refits not costed | None | **Out of the price, upside only**, and the uncosted refit capex should be subtracted from even the upside case once known — it will also add to the capital-envelope problem above. |

**No-revenue-synergy case:** value = haircut standalone + net cost synergies only = roughly EUR 13-18m (using the illustrative EUR 10-15m standalone range + EUR 3.0m). Even using the bank's own unhaircut standalone of EUR 22.0m, value with cost synergies only is EUR 25.0m — still EUR 9m below the EUR 34m ask without touching a single revenue-synergy euro.

## Walk-away price

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (haircut plan, ~3% growth) | 10-15 | ASSUMPTION — illustrative, pending finance re-run; see above |
| Cost synergies, net of integration cost | 3.0 | Draft, owner named (COO) |
| **Walk-away price** | **13-19** | |
| Asking price | 34.0 | Bank's valuation bridge |
| **Gap (overpayment at asking price)** | **15-21** | |
| Revenue synergies (upside only, not in price) | 11.0, gross — risk-adjust down for no owner/no pilot/uncosted refits | Draft; kept out per standard M&A practice on unproven revenue synergies |

Even crediting the bank's own unhaircut standalone value (EUR 22.0m, i.e. giving the seller's growth plan full credit) plus the full EUR 3.0m of cost synergies only reaches EUR 25.0m — EUR 9.0m below the EUR 34.0m ask. The draft bridge only reaches EUR 36.0m (just above the EUR 34.0m price, leaving a suspiciously thin "EUR 2.0m value created") by also crediting 100% of two unowned, unpiloted, partly uncosted revenue synergies. That is the single number that should change the IC's view of this paper.

## Key risks and integration thesis

1. **Lease change-of-control (9/14 sites):** mitigation — landlord consents/waivers as a condition precedent to signing; owner: legal/real estate lead, before signing.
2. **Key-person dependence (founder):** mitigation — retention and non-compete agreement with economic teeth (escrow/earn-out tied to retention and to landlord-relationship continuity); owner: CEO/HR, before signing.
3. **Revenue synergies unowned and unpiloted:** mitigation — name an owner for each, run a pilot (e.g., bread/cakes in 2-3 cafés, one coffee corner) before committing capital to a 20-store rollout; owner: integration lead, within first 2 quarters, not priced into this deal.
4. **Capital envelope breach:** mitigation — IC paper must state explicitly whether this deal displaces the full 2027 capital plan or whether the board is being asked to expand the envelope; owner: CFO, before IC vote.
5. **No integration owner named overall:** the cost synergy has an owner (COO); nothing above that names who runs the integration end to end. Needs naming before signing.

## What would change the answer

1. If the real DCF re-run on 3% (or a justified blended) growth still lands standalone value near EUR 20m+, the gap narrows and a price closer to EUR 25-28m could be defensible on cost synergies alone — still below EUR 34m.
2. If landlord consents are secured for all 9 at-risk leases before signing, the lease deal-breaker is cured and the standalone/synergy value above becomes usable without a site-loss discount.
3. If the founder signs a multi-year retention and non-compete agreement, key-person risk is substantially reduced.
4. If a bread/cakes pilot in a handful of cafés shows real sell-through within, say, two quarters, part of the EUR 5.0m revenue synergy could reasonably move from upside into the price at a risk-adjusted value — but only after the pilot, not before.
5. If the board confirms it will expand the 2027 capital envelope specifically to accommodate this deal, the capital-allocation flag is resolved (but is then a separate board decision, not something this IC paper can wave through on its own).

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Haircut standalone value range | EUR 10-15m | Illustrative sensitivity to cutting plan growth from 9% to 3%; not a re-run of the actual DCF model, which is not available in the draft | Finance re-runs the model and standalone value lands materially outside this range |
| 2 | Cost synergy of EUR 3.0m is realistic and net of one-off cost | Taken from draft at face value | Has owner (COO), timing (month 6), one-off cost (EUR 0.6m) already netted — best-evidenced line in the paper | Due diligence finds the central-bakery-supply switch requires capex or contract exit costs not yet disclosed |
| 3 | Revenue synergies are valued at zero in the walk-away price | EUR 0m in price, EUR 11.0m gross shown as upside | No owner, no pilot, coffee-corner refit cost unknown — standard treatment per M&A practice (revenue synergies are rarely realised as planned) | A pilot with real sell-through data is run and an owner is named before signing, which could justify a partial, risk-adjusted credit |
| 4 | Full 14-café network is the asset being valued | Standalone value above assumes all 14 sites | 9 of 14 leases allow termination on change of control | Landlord consents are not secured and sites are lost — standalone value should be cut further in proportion to lost sites |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What are the underlying DCF inputs (explicit forecast period, margins, discount rate, terminal growth)? | Needed to replace the illustrative EUR 10-15m haircut range with an actual re-run | Finance / the sell-side bank's model | Could move the walk-away price materially in either direction within or beyond the 13-19m range |
| Will landlords consent to change of control on the 9 affected leases, and at what cost (rent step-ups, lease re-papering)? | Directly determines whether the 14-café network is the asset actually being bought | Real estate/legal counsel, landlord negotiations | A clean consent on all 9 supports the current site count; a partial or costly consent should cut standalone value and may itself be a walk-away trigger |
| Will the founder sign a retention and non-compete agreement, and on what terms? | Key-person risk is concentrated in one person who also holds the landlord relationships central to risk above | CEO / HR / the founder | No agreement materially raises execution risk and should lower the price the buyer is willing to pay |
| What would a bread/cakes and coffee-corner pilot show, and what does a 20-store refit actually cost? | Revenue synergies are currently unowned, unpiloted and partly uncosted — EUR 11.0m of the draft's claimed value rests on this | Commercial/ops team, via a pilot before committing to rollout | Positive pilot data could justify moving some revenue synergy value into the price later; absent data, it stays at zero in the price |
| Does this deal, at EUR 34m, displace the entire EUR 30m 2027 capital envelope, or does the board need to expand it? | The deal alone exceeds the envelope approved for all 2027 projects combined | CFO / board | IC cannot approve without this being resolved explicitly — it is a capital allocation decision, not a deal term |
| Was a build/partner alternative (organic café rollout, franchise/license) ever compared to buying Copperleaf? | Strategic fit is not a substitute for testing whether the goal could be reached more cheaply another way | CEO / corp dev | If a cheaper route exists within the needed time window, it strengthens the case for walking away from Copperleaf at 34m |

