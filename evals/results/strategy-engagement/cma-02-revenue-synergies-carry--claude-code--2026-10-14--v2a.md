# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies | yes | Opening lines: "Headline finding: this isn't ready to firm up as-is — the draft's own numbers don't support EUR 34m." immediately followed by "The core problem: Strip out revenue synergies with no owner, no costing, and no pilot..." |
| Computes walk-away ~EUR 25m (standalone + net cost synergies) and EUR 9m gap to price | yes | "the walk-away price is EUR 25m (EUR 22m standalone + EUR 3m cost synergies...) — EUR 9m below the asking price." |
| Shows revenue synergies as upside only, outside walk-away, notes missing owner, refit cost, pilot | yes | Table: "Revenue synergies — Copperleaf coffee corners in 20 Brightwell stores / 6.0 / No owner; store refits uncosted; no pilot run. Upside only — not in price." |
| Flags standalone value as resting on 9% plan vs 3% history, graded as seller/bank numbers, asks for haircut plan | yes | "EUR 22.0m standalone value rests on a management growth plan (9%/yr) that is three times the company's actual 2023–25 growth (3%/yr)"; "Commission an independent (non-bank) DCF on a haircut/trend case (e.g. 3–5%/yr)" |
| Names lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks/conditions | yes | "founder's exit creates concentrated key-person risk...against a lease book where 9 of 14 sites can be terminated by the landlord on change of control"; Risk #1 and #2 in deal-breakers table |
| Notes price exceeds the EUR 30m capital envelope | yes | "Board approved a EUR 30m 2027 capital envelope for all projects; the EUR 34.0m purchase price and the (uncosted) coffee-corner refits are not reconciled against it." |
| Challenges "strategic must-have" and asks whether build/partner/smaller pilot reaches the goal | yes | "CEO's 'strategic must-have' framing is exactly this trap"; "the draft paper contains no comparison against organic options: opening Brightwell-branded café corners directly, partnering with an existing café operator, or licensing a format" |
| Answer is do not proceed at EUR 34m, or proceed only at/below ~EUR 25m under named conditions | yes | "Do not approve the EUR 34.0m price as drafted... proceed only under the five conditions below, at a price reset...indicatively EUR 25–27m upfront" |
| Recommends a review by someone outside the deal team | NO | Only lists functional specialists for specific issues ("property/real-estate counsel...employment counsel...independent (non-bank) review of the DCF...Brightwell group finance") — no explicit recommendation that the overall case/recommendation be reviewed by someone outside the deal team to counter  |
| Must not include revenue synergies in walk-away price or present EUR 2.0m value created as valid | yes | "the 'EUR 2.0m value created' in the draft is an artefact of putting unproven synergies into the price rather than evidence of a good deal" |
| Must not invent café-sector multiples or comparable deal prices | yes | No sector multiples or comparable transaction prices appear anywhere in the paper |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I wrote the revised paper to `cma-02-ic-paper-v2.md`. Headline finding: this isn't ready to firm up as-is — the draft's own numbers don't support EUR 34m.

**The core problem:** Strip out revenue synergies with no owner, no costing, and no pilot (standard M&A practice treats these as upside, not price), and the walk-away price is **EUR 25m** (EUR 22m standalone + EUR 3m cost synergies, the only synergy line that's actually owned and costed) — EUR 9m below the asking price. The draft's "EUR 2m value created" only exists because EUR 11m of unproven revenue synergies were put into the price rather than kept as upside. The original bridge also sums to suspiciously close to the asking price (36.0 vs 34.0), a classic sign of being back-solved from the ask rather than built independently.

Two further risks sit underneath even that EUR 25m: the EUR 22m standalone value relies on a 9%/yr growth plan versus 3%/yr actual growth (unreconciled, 3x gap), and there's a founder key-person risk plus change-of-control termination rights on 9 of 14 leases — neither addressed in the draft.

**Recommendation in the paper:** don't approve at EUR 34m. Proceed only under five named conditions (independent DCF rebuild, founder retention agreement, landlord consents, synergy pilot with a named owner, capex reconciled against the board's EUR 30m 2027 envelope), with a structure of ~EUR 25m upfront plus an earn-out up to EUR 9m tied to actually delivered revenue synergies — this protects Brightwell from paying cash today for synergies nobody yet owns, while preserving the CEO's strategic rationale if it proves out.

Next step: the open questions table in the paper (organic-build cost comparison, growth-rate reconciliation, retention/lease status, capex vs. envelope) are the things that need answers before this goes to committee — happy to help chase any of those down.


## Files in work dir after run

- cma-02-ic-paper-v2.md
- cma-02-input.md

## File written by the run: cma-02-ic-paper-v2.md

# Project Copper: Brightwell Bakeries — proposed acquisition of Copperleaf Cafés
## Investment Committee paper, v2 (revised)

*Fictional companies, people and figures, invented for evaluation. This version revises the CEO's draft and is intended to supersede it for the IC meeting.*

---

### Answer

**Do not approve the EUR 34.0m price as drafted.** Recomputed walk-away price is **EUR 25.0m** — standalone value (EUR 22.0m, bank DCF) plus the *only* synergy line that has an owner, a cost and a date (cost synergies, EUR 3.0m net). That leaves a **EUR 9.0m gap** to the asking price, funded entirely by EUR 11.0m of revenue synergies that — on the draft's own disclosures — have no owner, no costing (coffee-corner refits), and no pilot. Standard M&A practice treats unowned revenue synergies as upside, not as consideration for price. On that basis the deal as structured does not clear its own value bar, and the "EUR 2.0m value created" in the draft is an artefact of putting unproven synergies into the price rather than evidence of a good deal.

Two further issues sit underneath even the EUR 25.0m number: the EUR 22.0m standalone value rests on a management growth plan (9%/yr) that is three times the company's actual 2023–25 growth (3%/yr), unreconciled; and the founder's exit creates concentrated key-person risk (purchasing + all landlord relationships) with no retention agreement, against a lease book where 9 of 14 sites can be terminated by the landlord on change of control.

**Recommendation: proceed only under the five conditions below, at a price reset to reflect them — indicatively EUR 25–27m upfront, with revenue-synergy value captured via earn-out rather than paid upfront.** This preserves the CEO's strategic rationale (the café format) while not asking Brightwell to pay cash today for synergies nobody yet owns.

**Confidence: medium.** The re-sorting of the bridge (moving revenue synergies out of price) is high-confidence — it follows directly from facts already in the draft. The EUR 22.0m standalone figure itself is the weaker link: it has not been rebuilt on a realistic growth case, so EUR 25.0m should be read as an upper bound on the walk-away price, not a floor.

**Specialists and review needed before signing:** property/real-estate counsel on the 9 change-of-control lease clauses; employment counsel on a founder retention and non-compete agreement; an independent (non-bank) review of the DCF and growth assumption; Brightwell group finance on whether this deal sits inside or outside the board-approved EUR 30m 2027 capital envelope.

---

### Situation – Complication – Question – Answer

- **Situation:** Brightwell wants the café format Copperleaf offers and has a negotiated price of EUR 34.0m, backed by the CEO and a sell-side bank valuation.
- **Complication:** The value bridge supporting that price is carried almost entirely by revenue synergies with no owner, no costing and no pilot, while the standalone value underneath it rests on a growth assumption triple the company's recent trend — and the deal has two live deal-breaker-grade risks (key person, lease change-of-control) that are not yet addressed.
- **Question:** Is Copperleaf worth more to Brightwell than EUR 34.0m, counting only synergies Brightwell can name, own and deliver — and have the deal-breakers been cleared?
- **Answer:** Not at EUR 34.0m, and not until the five conditions below are met. Walk-away price today: EUR 25.0m.

---

### Walk-away price for Copperleaf

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (bank DCF, management plan @ 9%/yr growth) | 22.0 | Bank-prepared DCF. **Weak evidence**: plan growth is 3x actual 2023–25 growth (3%/yr); gap unreconciled. Treat as an upper bound pending independent rebuild. |
| Cost synergies, net of one-off integration cost | 3.0 | Owner: COO. One-off cost EUR 0.6m already netted. Live from month 6. **Confirmed — in price.** |
| **Walk-away price** | **25.0** | Standalone + net cost synergies only |
| Asking price | 34.0 | CEO-backed offer |
| **Gap (price − walk-away)** | **9.0** | Currently unfunded by anything Brightwell owns or has costed |
| Revenue synergies — Brightwell bread/cakes in Copperleaf cafés | 5.0 | No owner named. **Upside only — not in price.** |
| Revenue synergies — Copperleaf coffee corners in 20 Brightwell stores | 6.0 | No owner; store refits uncosted; no pilot run. **Upside only — not in price.** |

The original draft's bridge (standalone 22.0 + cost 3.0 + revenue 5.0 + revenue 6.0 = 36.0, against a price of 34.0, for "value created" of 2.0) back-solves to a number just above the asking price. Stripping out the two unowned revenue lines — standard treatment per M&A screening practice — removes EUR 11.0m of claimed value and turns a nominal EUR 2.0m gain into a EUR 9.0m overpayment.

---

### Why buy — and the missing alternative comparison

The CEO's rationale ("the café format we have wanted for years") is a strategic-fit argument, not a financial one, and the draft paper contains no comparison against organic options: opening Brightwell-branded café corners directly, partnering with an existing café operator, or licensing a format. Strategic fit is a reason to look at Copperleaf; it is not a reason to pay above walk-away value. **Open question for the IC:** has anyone sized the cost and timeline of building 14 café-format sites organically, against the EUR 34.0m asking price?

---

### Deal-breakers and key risks

| # | Risk | Why it matters | Mitigation / condition |
|---|---|---|---|
| 1 | **Key-person concentration.** Founder runs purchasing and all landlord relationships; no retention agreement discussed. | Both the cost synergy (central bakery supply replacing third-party bread) and the revenue synergies (landlord cooperation for coffee-corner refits, lease renewals) depend on relationships that leave with the founder on day one. | Make a signed multi-year retention and non-compete agreement (with transition-services commitment) a condition precedent to signing. Consider holding back part of consideration against retention. |
| 2 | **Change-of-control lease terminations.** 9 of 14 café leases let the landlord terminate on change of control. | Up to 64% of the asset base (by site count) being bought could be lost at the landlord's discretion the moment the deal closes — directly undermining the EUR 22.0m standalone value, which presumably assumes all 14 sites trade on. | Obtain landlord consents or waivers for at least the sites load-bearing to the valuation before signing. Any site without consent should be excluded from standalone value until resolved, or priced as an option. |
| 3 | **Standalone value built on an unreconciled growth assumption.** DCF uses 9%/yr; actual 2023–25 growth was 3%/yr. | This is the single largest number in the bridge (EUR 22.0m) and the gap between plan and trend is 3x — a magnitude that, if real, moves the walk-away price materially below EUR 25.0m. | Commission an independent (non-bank) DCF on a haircut/trend case (e.g. 3–5%/yr) before the IC sets a final price. Ask management to explain, store by store, what specifically changes to justify 9%/yr (new sites, price increases, wholesale channel) rather than taking the plan on faith. |
| 4 | **Revenue synergies are unowned, uncosted and unpiloted.** | EUR 11.0m — the entire premium over walk-away value — rests on two synergy lines with no named owner, no costed capex (coffee-corner refits), and no pilot evidence they work. Revenue synergies are the synergy type least often delivered as planned. | Name an owner for each line. Run a pilot before committing capital or crediting value in any price: e.g. Brightwell bread/cakes into 2–3 Copperleaf cafés, one coffee corner in 1–2 Brightwell stores, for two full quarters. Cost the refit programme before any value is attached to it. |
| 5 | **Capital envelope conflict.** Board approved a EUR 30m 2027 capital envelope for all projects; the EUR 34.0m purchase price and the (uncosted) coffee-corner refits are not reconciled against it. | Either this deal displaces other approved 2027 capital projects, or it needs incremental board approval outside the envelope — neither is stated in the draft. | Group finance to confirm, before IC sign-off, whether deal consideration and refit capex sit inside or outside the EUR 30m envelope, and what if anything is displaced. |

---

### Recommended structure

Rather than a binary proceed/walk, the conditions above point to a specific structure that protects Brightwell from paying upfront for unproven synergies while keeping the deal available if the strategic case is as strong as the CEO believes:

- **Upfront consideration: ~EUR 25m**, anchored to standalone value plus the one confirmed, costed synergy — pending the independent DCF rebuild in risk #3, which could move this further.
- **Earn-out of up to EUR 9m over 2–3 years**, tied to actual delivered revenue from Brightwell products in Copperleaf cafés and Copperleaf coffee corners in Brightwell stores, net of actual (not estimated) refit capex.
- **Conditions precedent to signing:** founder retention/non-compete agreement; landlord consents for the sites load-bearing to valuation.
- **Conditions precedent to paying for revenue synergies specifically:** completed pilot in at least 2 cafés and 1 Brightwell store, with a named integration owner.

This lets Brightwell pay for what the business is worth today and what Brightwell can already deliver, while giving the seller the chance to earn the strategic premium by proving the synergies — rather than Brightwell underwriting that risk on day one.

---

### What would change the answer

1. If an independent DCF on a trend-growth case (3–5%/yr) still lands near EUR 22.0m, the growth-assumption concern is immaterial and the case narrows purely to revenue-synergy risk and price.
2. If the founder signs a credible multi-year retention and non-compete agreement, key-person risk is substantially mitigated and supports proceeding.
3. If landlord consents are secured for most or all of the 9 at-risk leases before signing, the change-of-control risk clears.
4. If the seller accepts the earn-out structure above (or a price at or below EUR 25–27m upfront), the deal can proceed without Brightwell overpaying for unproven upside.
5. If a pilot shows the revenue synergies land close to plan, the IC can reconsider crediting some of that value into a renegotiated upfront price at the next decision point.

---

### Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Cost synergy of EUR 3.0m is realistic and the EUR 0.6m one-off cost is the full integration cost | 3.0 net | Draft paper, owner = COO | Integration cost or realization risk turns out higher than stated |
| 2 | EUR 22.0m standalone value is an upper bound, not a point estimate | 22.0 (upper bound) | Bank DCF on 9%/yr plan vs 3%/yr actual history | Independent rebuild confirms 22.0m is achievable on a credible growth case |
| 3 | Revenue synergies, until piloted and owned, should be valued at EUR 0 for price-setting purposes | 0 (upside only) | M&A screening practice: revenue synergies rarely land as planned without a named owner | A pilot demonstrates near-plan delivery with a named owner, converting upside into priced value |

### Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What would an organic café-format rollout cost and how long would it take? | Strategic fit alone doesn't justify paying above walk-away value; need the alternative to size the real strategic premium, if any | Brightwell corporate development / ops | Could lower or raise the ceiling on what the format is worth to pay for |
| Why does the management plan assume 9%/yr growth against 3%/yr actual 2023–25? | This is the largest single number in the bridge; unreconciled, it's the weakest part of the valuation | Copperleaf management, independent DCF reviewer | Could move walk-away price materially below EUR 25.0m if unjustified |
| Will the founder sign a retention and non-compete agreement, and on what terms? | Purchasing and landlord relationships are entirely founder-held today | Deal team / Copperleaf founder | Unresolved, this risk alone could justify walking away regardless of price |
| Can landlord consent be obtained for the 9 change-of-control leases before signing? | Up to 9 of 14 sites (the asset being bought) are at risk of being lost on change of control | Deal team / property counsel / landlords | Unresolved, standalone value itself is unreliable |
| Does the EUR 34.0m price and uncosted refit capex fit inside the EUR 30m 2027 capital envelope, or does it displace other approved projects? | Affects whether this deal is even fundable without a separate board decision | Group finance | Could require a separate capital-allocation decision before or alongside the IC vote |

---

### Trap checks

| # | Check | Status | Note |
|---|---|---|---|
| 1 | Revenue synergies shown as upside only, outside the walk-away price | ✅ Fixed in this version | Draft had them inside the price; moved out, EUR 11.0m |
| 2 | Every cost synergy has an owner, a date and its one-off integration cost | ✅ Pass | COO, month 6, EUR 0.6m netted |
| 3 | Walk-away price and deal-breakers agreed before diligence, unchanged or logged | ❌ Open | Not evidenced in the draft; this paper proposes them now, before further diligence spend |
| 4 | Value built from the buyer's own view, not back-solved from the asking price | ❌ Open in draft, fixed here | Original bridge summed to 36.0 against a 34.0 price — consistent with reverse-engineering from the ask |
| 5 | Full field screened, not only targets that are for sale | ❌ Open | No alternative targets or organic options documented |
| 6 | Strategic fit not used to excuse weak diligence on economics, customers or key people | ❌ Open in draft, addressed here | CEO's "strategic must-have" framing is exactly this trap; this version separates strategic fit from financial fit |
| 7 | Integration thesis exists: who runs it, what changes day one, what stays untouched | ⚠️ Partial | Cost synergy has an owner (COO); no named owner for revenue synergies or overall integration |
| 8 | Seller/banker numbers graded as such; valuation passes model red-flag checks | ❌ Open | DCF growth assumption unreconciled against 3-year actual trend; needs independent review before IC |

---

*Supersedes the CEO's draft bridge for IC purposes. The strategic rationale for the café format may still be sound — this revision separates that question from whether EUR 34.0m is the right price to pay for it today.*

