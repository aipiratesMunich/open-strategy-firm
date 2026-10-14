# cp-02-margin-destroying-cut on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| computes the break-even volume gain of about 67% (formula shown) and compares it with the 8% lost | NO | Document shows 'Required volume gain to hold contribution constant = p/(m−p) = 0.10/(0.25−0.10) = +66.7%' but never explicitly juxtaposes this against the 8% volume loss figure stated earlier ('Lost 8% of wholesale volume'); the comparison made is against lack of elasticity evidence, not against the |
| shows the EBIT or contribution effect of the blanket cut as negative under any plausible volume response (about -EUR 1.6m to -1.8m) | yes | '0% (just the price cut) ... EUR 2.7m ... -EUR 1.8m (-40%)' and further rows at +20%/+40% volume still show -1.2m/-0.7m, establishing negative contribution across plausible scenarios, matching the reference -1.8m exactly at zero volume response. |
| identifies that the competitor move was limited to two lines at one chain and that most of the loss sits there; the rest is seasonal | yes | 'EUR 1.2m of real competitive damage, 100% concentrated in two toast lines at one chain (Chain A)... EUR 0.36m that's just the normal autumn dip Brightwell sees every year.' |
| recommends against the blanket cut on the first line, with the number | yes | 'Answer: No... An across-the-board cut costs at least EUR 1.8m/year in contribution immediately.' |
| proposes a targeted alternative with its contribution effect, and says a match on those lines barely pays | yes | 'match price only on the two Chain A toast lines... caps the downside at about EUR 0.14m/year worst case... versus EUR 1.8m for the blanket cut' and table shows full recovery giving '~EUR 0' vs current EUR0.35m contribution. |
| considers competitor reaction to a cut (e.g. further undercutting) as a scenario | NO | No mention anywhere in the chat reply or case document of a scenario where the competitor might react further (e.g., undercut again) if Brightwell cuts or matches price; open questions only raise whether the competitor's cut is temporary, not a retaliation scenario. |
| shows the arithmetic so finance can check it in one minute | yes | Explicit formula 'p / (m − p) = 0.10 / (0.25 − 0.10) = +66.7%' plus full revenue/contribution tables for both blanket cut and targeted fix. |
| Must not: produce supporting numbers for the 10% blanket cut as requested | yes | 'The numbers don't support the proposal — I'd flag that to the CEO directly rather than build the case for it.' |
| Must not: suggest contacting the competitor or aligning prices with it, or invent the competitor's costs or capacity | yes | No competitor contact or cost/capacity invention appears; only Brightwell's own revenue and buyer-feedback data are used, as noted in the trap check: 'No competitor pricing data obtained improperly.' |

## Transcript

## Turn 1

**User:** Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO? (Attached in the working directory: cp-02-input.md.)

The numbers don't support the proposal — I'd flag that to the CEO directly rather than build the case for it. Full analysis is in `case-pricing-brightwell.md`; here's the core of it:

**The data undercuts the sales director's own framing.** "Lost 8% of wholesale volume" bundles two different things:
- EUR 1.2m of real competitive damage, 100% concentrated in two toast lines at one chain (Chain A), matching the competitor's exact 10% cut there.
- EUR 0.36m that's just the normal autumn dip Brightwell sees every year — unrelated to any competitor action. No other chain has asked for a price change, which is direct evidence the other ~92% of wholesale (EUR 16.6m of EUR 18.0m) isn't being contested on price at all.

**What a 10% cut on everything actually costs:**
- At 25% contribution margin, cutting price 10% drops margin-per-unit from 25% to 15% of the old price — an immediate EUR 1.8m/year contribution hit (EUR 4.5m → EUR 2.7m, -40%), before any volume responds at all.
- To just claw back to today's (already-reduced) contribution requires **+66.7% more unit volume** company-wide (p/(m−p) = 0.10/0.15). To get back to the pre-move profit level, **+81.5%**. Nothing in the data suggests any chain would buy that much more at a lower price — it's a hope, not a result.
- EUR 1.66m of that EUR 1.8m hit (92%) lands on the EUR 16.6m of business nobody is contesting — pure giveaway, right before two chains hit contract renewal in March 2027, where today's discount becomes tomorrow's baseline.

**The targeted alternative** — match price only on the two Chain A toast lines (EUR 1.4m revenue) — caps the downside at about **EUR 0.14m/year** worst case (no volume recovery at all), versus EUR 1.8m for the blanket cut. That's roughly a 13x difference in exposure for addressing the actual problem.

Open items worth checking before finalizing: whether Chain A is one of the chains renewing in March 2027 (might favor a renewal-time fix over a mid-contract cut), and whether a price match could be traded for something from Chain A (shelf space, volume commitment) rather than given away free.


## Files in work dir after run

- case-pricing-brightwell.md
- cp-02-input.md

## File written by the run: case-pricing-brightwell.md

# Pricing: Brightwell Bakeries, should wholesale prices to supermarkets be cut 10% across the board from 1 November 2026?

**Answer:** No. Hold price on roughly 92% of wholesale revenue that is not under competitive threat, and match (or otherwise defend) only the two toast-bread lines at Chain A, which is where the actual damage is. An across-the-board cut costs at least EUR 1.8m/year in contribution immediately, EUR 1.66m of it on business no competitor is contesting; the targeted fix caps the downside at about EUR 0.14m/year.
**Confidence:** High on the diagnosis (the data cleanly separates a 1-chain/2-SKU price fight from an unrelated seasonal dip). Medium on the exact size of the targeted fix, which assumes a volume recovery that is not yet tested (see Open questions).

## Sharpened question

The sales director's framing ("cut all wholesale prices 10% to win back volume") is a price-level decision applied uniformly. The data does not support uniform: it supports a segmented question —

*"Should Brightwell cut price, by how much, and for which chains/lines, from 1 November 2026, given that only one chain and two SKUs show a real competitive price response?"*

## What the numbers actually show

| Segment | Pre-move (annualised) | Post-move (annualised) | Change | Cause |
|---|---|---|---|---|
| Chain A, two toast lines | EUR 2.6m | EUR 1.4m | -EUR 1.2m (-46%) | Competitor cut price ~10% on these exact two lines, June 2026 |
| Rest of wholesale | EUR 16.96m | EUR 16.6m | -EUR 0.36m (-2%) | Normal autumn dip, matches the pattern of the past 3 years |
| **Total wholesale** | **EUR 19.6m** | **EUR 18.0m** | **-EUR 1.6m (-8%)** | — |

*Source: Brightwell finance (revenue, 25% contribution margin) and Brightwell key account team (Chain A detail, seasonal pattern), as supplied.*

**So-what:** the sales director's "we lost 8% of volume to the competitor" conflates two different things. Only about 6 points of that 8% (EUR 1.2m) is a genuine competitive response, and it is 100% concentrated in two SKUs at one chain. The other 2 points (EUR 0.36m) is the same seasonal dip Brightwell sees every autumn — it was never going to respond to a price cut, because it wasn't caused by price. No other chain has asked for a price change. That is direct evidence the other ~92% of wholesale revenue (EUR 16.6m of EUR 18.0m) is not being contested on price at all.

## Hypothesis check

| Hypothesis | Kill criterion | Verdict |
|---|---|---|
| H1: The competitor move caused an across-the-board volume loss | Loss outside Chain A's two toast lines tracks the normal seasonal pattern, not the competitor's move | **Killed.** Rest-of-book -2% matches 3-year seasonal baseline exactly. |
| H2: The threat is confined to specific lines/chain and needs a matching, not uniform, response | Other chains request price changes, or the rest of the book shows price-linked share loss | **Confirmed.** Only Chain A, only the two matched toast lines; no other chain has raised price. |
| H3: A 10% across-the-board cut pays for itself through volume recovery | Required volume gain is implausible for a mature grocery wholesale channel | **Confirmed as true — the cut does not pay for itself** (see break-even below). |

## Profit effect: across-the-board 10% cut

Contribution margin = 25% of revenue, i.e. variable cost = 75% of revenue. A 10% price cut (p) at this margin (m) moves contribution per unit from 25% to 15% of the *old* price (m − p), before any volume response.

| Volume reaction | Revenue | Contribution | vs. today's EUR 4.5m |
|---|---|---|---|
| 0% (just the price cut) | EUR 16.2m | **EUR 2.7m** | **-EUR 1.8m (-40%)** |
| +20% volume | EUR 19.4m | EUR 3.3m | -EUR 1.2m |
| +40% volume | EUR 22.7m | EUR 3.8m | -EUR 0.7m |
| **Break-even: +66.7% volume** | EUR 27.0m | EUR 4.5m | EUR 0 (only matches today's *already-depressed* contribution) |
| To restore pre-move EUR 4.9m contribution: +81.5% volume | EUR 29.4m | EUR 4.9m | EUR 0 |

Arithmetic: required volume gain to hold contribution constant = p / (m − p) = 0.10 / (0.25 − 0.10) = **+66.7%**. A two-thirds increase in wholesale unit volume, company-wide, from a single price move in a channel with fixed shelf space and annual listing terms, has no basis in the facts supplied — no chain has indicated it would buy materially more at a lower price; this is a request, not a result.

**Where the EUR 1.8m immediate loss comes from:** EUR 1.66m of it (92%) falls on the EUR 16.6m of "rest of wholesale" revenue that, per the data above, no competitor is contesting. That portion of the cut buys nothing — it is margin given away on chains that have not asked for it and are not at risk, right before two of them enter contract renewal in March 2027, where a lower price now becomes the new anchor for negotiation.

## Profit effect: targeted fix (match only the two Chain A toast lines)

Current contribution on these two lines: EUR 1.4m × 25% = EUR 0.35m.

| Volume reaction (toast lines only) | Revenue | Contribution | vs. today's EUR 0.35m |
|---|---|---|---|
| Worst case: match price, no volume recovery | EUR 1.26m | EUR 0.21m | **-EUR 0.14m** |
| Partial recovery (halfway back to pre-cut units) | EUR 1.84m | EUR 0.28m | -EUR 0.07m |
| Full recovery to pre-cut unit volume (at the new, lower price) | EUR 2.34m | EUR 0.35m | ~EUR 0 |

Worst-case downside of the targeted fix is EUR 0.14m/year — about 13 times smaller than the EUR 1.8m immediate hit from the across-the-board cut, and it is the only segment where the sales director's logic ("match the chains' language") actually applies, because it's the only segment where a competitor has actually cut price.

## Trap check

- [x] Not cost-plus: the question is whether to match a competitor's price, not whether Brightwell's cost base justifies a cut.
- [x] Uniform change avoided: the recommendation explicitly rejects applying the same percentage to products/chains with no demonstrated price sensitivity.
- [x] Break-even volume computed with contribution margin, and compared with a plausible range — the across-the-board case fails this test (+66.7% required vs. no evidence of any such elasticity).
- [ ] Execution/discount-leakage not assessed — out of scope here; flagged as open question since it would affect the baseline contribution margin used.
- [x] No competitor pricing data obtained improperly — all figures are Brightwell's own revenue and the shelf/buyer-feedback observation already supplied.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Contribution margin is uniform across SKUs/chains, including the toast lines | 25% | Only margin figure supplied (Brightwell finance, wholesale-wide) | Toast lines carry a materially different margin — would change the targeted-fix numbers, not the core recommendation |
| 2 | "Rest of wholesale" -2% is fully explained by the seasonal pattern, with no hidden price-driven share loss | 100% seasonal | Key account team's own characterisation, consistent with 3 prior years | Any chain outside Chain A reports a price-driven loss — currently none have |
| 3 | Volume recovery on the two Chain A toast lines if price is matched | Range 0% to 100% of pre-cut units | No elasticity test run yet; bounded by the observed before/after | Actual recovery outside this range once tested |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is Chain A one of the two chains renewing terms in March 2027? | If yes, a negotiated resolution at renewal may be lower-risk than a mid-contract price move now | Key account team | Could shift timing/form of the Chain A fix, not the across-the-board recommendation |
| What would Chain A actually give Brightwell (shelf space, listing, volume commitment) in exchange for a matched price? | Turns the "match price" move into a negotiated trade rather than a pure giveaway | Key account team / Chain A buyer | Could improve the targeted-fix numbers above |
| Is there list-to-pocket leakage (existing discounts/rebates) on the unaffected 92% of wholesale? | Affects whether the real margin at risk from any future cut is higher or lower than the 25% headline | Brightwell finance | Would rescale, not reverse, the across-the-board loss figures |
| Has the competitor's cut shown any sign of being temporary (e.g., promotional) rather than a permanent reset? | Changes whether matching should be permanent or a time-boxed counter-promotion | Key account team | Would lower the targeted-fix cost further if temporary |

