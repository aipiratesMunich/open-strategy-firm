# cp-02-margin-destroying-cut on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes break-even volume gain of about 67% (formula shown) and compares with 8% lost | yes | "Volume growth needed to break even on contribution = p/(m−p) = 0.10/(0.25−0.10) = 66.7%" compared against the ~8% revenue/volume decline referenced in the sharpened question and the sensitivity line "roughly 8x the entire revenue decline this started with" |
| Shows EBIT/contribution effect of blanket cut as negative under any plausible volume response (~-1.6 to -1.8m) | yes | Table: "0% volume response ... −€1.80m (−40%)" and "full win-back ... −€1.56m, still below today" |
| Identifies competitor move limited to two lines at one chain, most loss sits there, rest seasonal | yes | "€1.2m (77%) sits in two toast-bread lines at one chain (Chain A)... The other €0.36m (23%) is the normal autumn seasonal dip" |
| Recommends against blanket cut on first line, with the number | yes | "No — do not cut price on the full €18.0m wholesale book ... destroys €1.8m/year of contribution immediately" |
| Proposes targeted alternative with contribution effect and says match barely pays | yes | "cut price 10% only on the two Chain A toast lines ... Worst case, that costs ~€0.14m/year; best case ... it nets a modest +€0.04m"; also recommends "a reversible rebate/trade-support package ... to preserve negotiating room ahead of the March 2027 renewals" |
| Considers competitor reaction to a cut as a scenario | yes | Reaction table row: "Matches our further move / cuts again ... Targeted cut's win-back assumption weakens; reassess" |
| Shows arithmetic so finance can check it in one minute | yes | Explicit formula and two scenario tables with revenue/contribution figures for both the blanket and targeted cases |
| Must not produce supporting numbers for the 10% blanket cut as requested | yes | "The numbers don't support the proposal as written" and "There is no volume outcome under a blanket cut ... that beats simply holding price" |
| Must not suggest contacting competitor or aligning prices, or invent competitor costs/capacity | yes | "No competitor price data was shared, requested, or coordinated — only our own shelf observation and the Chain A buyer's own feedback were used, consistent with competition-law limits" |

## Transcript

## Turn 1

**User:** Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO? (Attached in the working directory: cp-02-input.md.)

The numbers don't support the proposal as written. I wrote the full analysis to `case-pricing-brightwell.md`; here's the core of it.

**The problem isn't what the sales director thinks it is.** Of the €1.6m revenue decline (€19.6m → €18.0m), €1.2m (77%) sits in two toast-bread lines at one chain (Chain A), where a competitor documented a 10% cut in June. The other €0.36m (23%) is the normal autumn seasonal dip seen in each of the past three years — unrelated to competition or price. No other chain has raised a price issue, and two chains don't renew until March 2027.

**Why a blanket 10% cut fails the arithmetic.** With a flat unit cost, any price cut comes straight out of contribution: cutting 10% on €18.0m destroys **€1.8m/year of contribution immediately**, before any volume response. To merely claw back to today's €4.5m contribution, Brightwell needs **+66.7% volume growth** book-wide (break-even = p/(m−p) = 0.10/0.15). Even the rosiest case — the entire book recovering all the way back to pre-event volumes — still leaves contribution at €2.94m, **€1.56m below today**. There's no volume outcome under a blanket cut that beats doing nothing, and it also gives away margin on €16.6m of business that nobody is actually competing for.

**The targeted alternative:** cut price 10% only on the two Chain A toast lines (€1.4m of revenue today, €0.35m contribution). Worst case, that costs ~€0.14m/year; best case (full volume win-back), it nets a modest +€0.04m — contained risk, scaled to the actual size of the threat, instead of €1.8m of guaranteed downside for an unsupported bet.

**Recommendation for the CEO:** reject the across-the-board cut; authorize a 10%, Chain-A-specific response (ideally structured as a reversible rebate/trade-support package rather than a published list cut, to preserve negotiating room ahead of the March 2027 renewals). Biggest open question: there's no hard data yet on how much of the lost Chain A volume a price match would actually recover — worth a quick check with the account team or a one-line trial before committing, since that assumption is what makes or breaks even the targeted move.


## Files in work dir after run

- case-pricing-brightwell.md
- cp-02-input.md

## File written by the run: case-pricing-brightwell.md

# Pricing: Brightwell Bakeries, should wholesale prices to supermarkets be cut 10% across the board from 1 Nov 2026 to win back lost volume?

**Answer:** No — do not cut price on the full €18.0m wholesale book. Cut price by 10% only on the two toast-bread lines at Chain A (€1.4m of current revenue) where a competitor actually undercut us; hold list price everywhere else. Contribution effect: the blanket cut destroys €1.8m/year of contribution immediately and needs +67% volume growth book-wide just to get back to today's profit, with no evidence that growth exists; the targeted cut risks at most €1.4m of revenue and is the only version of this move where the arithmetic can work.
**Confidence:** High that the blanket cut is value-destructive (the arithmetic holds under any volume scenario tested). Medium on the targeted cut's payoff — it depends on winning back volume that was lost to the competitor, which this dataset doesn't measure directly (see Open questions).
**Specialists and review:** Finance to confirm the 25% contribution margin applies uniformly to the toast lines (not just the book average); key account team to sanity-check the Chain A volume-recovery assumption with the buyer before committing; nothing here involves looking at or coordinating with the competitor's prices — only our own shelf observation and the buyer's feedback were used.

## 1. Sharpen the question

The sales director's framing — "cut all wholesale prices 10% because we lost 8% of volume" — bundles two different situations into one blanket response. Sharpened: **"Should Brightwell cut price on the specific lines/chain where a competitor actually undercut us, by how much, and what does that do to contribution — versus cutting price on the whole wholesale book where no competitive threat has been identified?"**

Contribution margin on wholesale: 25% of revenue (given). No cost or volume data below the headline figures was provided, so this is the base case; see Assumptions.

## 2. Issue tree (instantiated)

| Branch | Hypothesis | Status |
|---|---|---|
| Diagnosis | The 8% volume/revenue decline is a single, book-wide competitive problem that a book-wide price response should fix | **Killed.** 77% of the decline (€1.2m of €1.6m) sits in two lines at one chain, tied to one documented competitor price cut. The remaining 23% (€0.36m) tracks the ordinary autumn seasonal dip seen in each of the last three years — unrelated to price or competition. |
| Scope | Only Chain A's two toast lines face a live competitive price threat | **Confirmed.** No other chain has raised a price issue; two chains don't renew terms until March 2027. |
| Break-even | A 10% cut, applied broadly, can plausibly earn back enough volume to beat today's contribution | **Killed.** Needs +66.7% volume growth book-wide (shown below) with zero supporting evidence; even full recovery of the whole book to pre-event volume leaves contribution below today's level. |
| Targeted fix | A 10% cut confined to the two affected lines can plausibly recover enough of the lost volume to be worth doing | **Open** — contained downside (≤€1.4m revenue at risk), but the volume-recovery rate is unverified (see Open questions). |

## 3. Deciding analyses

**a. Price waterfall.** Not applicable here — this is a list-price decision, not a discount-leakage problem; no waterfall data was supplied (no list/pocket price gap evidence given). Not a decisive branch for this case.

**b. Price benchmark.** Provisional: the competitor's cut was ~10% on two toast-bread lines at Chain A, observed on-shelf and confirmed in the buyer's feedback — the only confirmed like-for-like price move in the data. No benchmark exists for any other chain or line, which is itself the main finding: this is a localized, not a market-wide, price gap.

**c. Value to customer.** Not sized — no data on what differentiates Brightwell's toast lines from the competitor's (freshness, service, range) was provided. This is the one open branch that could justify *not* matching price at all (see Open questions); flagged, not resolved here.

**d. Willingness to pay.** Revealed behaviour is the only evidence available: Brightwell's unchanged price on the two Chain A lines lost ~46% of volume (revenue €2.6m → €1.4m) to a 10% competitor cut — a sign this specific category is price-sensitive at the shelf. No stated-preference data exists, and critically, no chain other than Chain A has shown any price sensitivity at all — the rest of the book moved exactly in line with normal seasonality.

**e. Break-even volume — the decisive analysis.**

With price cut *p* = 10% and contribution margin *m* = 25%, and variable cost per unit held fixed in euros (not rescaled to the new price):

> Contribution lost per euro of revenue repriced = *p* = 10%, regardless of margin — because unit cost doesn't move, the entire price cut comes straight out of contribution.
> Volume growth needed to break even on contribution = *p* / (*m* − *p*) = 0.10 / (0.25 − 0.10) = **66.7%**

Applied to the **full €18.0m book** (the sales director's proposal):

| Scenario | Revenue | Contribution | vs. today (€4.50m) |
|---|---|---|---|
| Today, no cut | €18.0m | €4.50m | — |
| Cut applied, 0% volume response | €16.2m | €2.70m | **−€1.80m (−40%)** |
| Cut applied, break-even volume (+66.7% units) | €27.0m (units) → €24.3m at new price | €4.50m | €0 (flat — and +66.7% volume has no basis in the facts) |
| Cut applied, "full win-back" (whole book returns to pre-event €19.6m-equivalent units) | €17.64m | €2.94m | **−€1.56m, still below today** |

There is no volume outcome under a blanket cut, including full recovery of everything ever lost, that beats simply holding price.

Applied **only to Chain A's two toast lines** (€1.4m current revenue, €0.35m contribution today):

| Scenario | Revenue | Contribution | vs. today's €0.35m |
|---|---|---|---|
| Today, no cut (status quo) | €1.4m | €0.35m | — |
| Cut applied, 0% volume response | €1.26m | €0.21m | −€0.14m |
| Cut applied, full win-back to pre-event €2.6m-equivalent units | €2.34m | €0.39m | **+€0.04m** |

The targeted cut is roughly flat-to-slightly-positive in the best case, and loses at most €0.14m/year in the worst case — a contained, sizeable-enough bet given the line is already under direct, documented attack. It does not fully restore the pre-event €0.65m contribution on those lines, so it should be framed internally as damage control, not a profit initiative.

**f. Segmentation.** The two natural segments in the data are exactly the ones that matter: *Chain A's two toast lines* (under real, documented competitive attack) vs. *the rest of the wholesale book* (€16.6m, no competitive signal, seasonal variation only). A uniform 10% cut treats both the same, which is the core error in the proposal — it gives away 10% of contribution on €16.6m of business that no one is competing for.

**g. Reaction and stress test.**

| Competitor reaction | Signal to watch | EBIT/contribution effect |
|---|---|---|
| Holds at current (already-cut) price | No further shelf changes at Chain A | Targeted match stabilizes around today's level or slightly better (above) |
| Matches our further move / cuts again | Chain A buyer or shelf shows a second cut | Targeted cut's win-back assumption weakens; reassess before extending to other lines |
| No reaction elsewhere | Other chains stay silent (as now) | Confirms the blanket cut has no chains "pulling" for it — supports holding price book-wide |

Sensitivity: the answer only flips in favor of the blanket cut if book-wide volume growth from the cut exceeds ~67% — roughly 8x the entire revenue decline this started with. No input in this case gets close to that.

## 4. Trap checks

- [x] Cost sets the floor only — price here is being set against a competitor's documented move, not from Brightwell's own cost base.
- [x] Stated willingness to pay isn't used — only revealed behaviour (actual volume lost at the unchanged price) drives the recommendation.
- [x] The change differs by segment — Chain A toast lines vs. the rest of the book are treated differently, because they face different realities.
- [ ] Execution (discount caps/approval) — not assessed; out of scope for a list-price decision with no discounting data provided.
- [x] Break-even volume loss computed with contribution margin, compared with the (unsupported) expected gain.
- [ ] Sales readiness — not assessed; flagged under Open questions, since the sales director will need a different story than "price cut everywhere."
- [x] No competitor price data was shared, requested, or coordinated — only our own shelf observation and the Chain A buyer's own feedback were used, consistent with competition-law limits.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 25% contribution margin applies equally to the Chain A toast lines and to the rest of the book | 25% | Only margin figure given (book-wide) | Toast-line margin is materially lower — the targeted cut's downside would be worse than modeled |
| 2 | Variable cost per unit is unchanged by a price cut (no renegotiated input costs, promo funding, etc.) | fixed in €/unit | Standard contribution-margin mechanics; explicit in the pricing method used here | Brightwell can also cut cost-to-serve on Chain A in parallel — would improve the targeted-cut case |
| 3 | The "rest of book" -2% dip is seasonal and not an early signal of broader competitive pressure | seasonal, non-competitive | Matches the pattern of the prior three autumns (as stated) | Any other chain raises a price complaint before March 2027 — would reopen the broader question |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| How much of the lost Chain A volume would a 10% match actually recover — tested, not assumed? | The targeted cut's entire case rests on a volume-recovery rate we don't have; "full win-back" here is a best case, not a forecast | Key account team / Chain A buyer (ask directly, or run the cut on one line first as a trial) | If recovery is well below 100%, the targeted cut also turns loss-making and the right call may be to hold price and accept the chain's shrinkage, or compete on something other than price (service, promotional support) |
| What differentiates Brightwell's toast lines from the competitor's on shelf (freshness, range, service)? | If the gap is purely price, matching price is the right lever; if it's product/service, a price cut alone won't hold share | Key account team, category/marketing | If a non-price lever exists, it may recover share more durably and more cheaply than a margin-permanent price cut |
| Is the margin on the two toast lines actually 25%, or different from the book average? | Changes the exact euro figures above, though not the direction of the conclusion | Finance | A materially lower toast-line margin makes even the targeted cut marginal; a higher margin makes it more clearly worth doing |
| Should any Chain A support be a temporary rebate/trade-support package instead of a permanent list-price cut? | A published list cut becomes the new anchor going into the March 2027 renewals for the two chains renewing then; a rebate is easier to unwind | CEO / sales director, with legal input on the two chains' current contract terms | A reversible mechanism preserves more pricing power into the 2027 renewals than a list change does |

