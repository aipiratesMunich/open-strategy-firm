# cp-02-margin-destroying-cut on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the break-even volume gain of about 67% (formula shown) and compares it with the 8% lost. | NO | Formula and 66.7% figure are shown ('break-even volume gain = 0.10 / (0.25 − 0.10) = 66.7%'), but the document never explicitly juxtaposes this 66.7% requirement against the 8% volume actually lost — it instead compares EUR amounts ('roughly 6x the EUR 0.3m the competitor's move actually cost'). |
| Shows the EBIT or contribution effect of the blanket cut as negative under any plausible volume response (about -EUR 1.6m to -1.8m). | NO | Only a single zero-volume-response scenario is computed ('Immediate contribution given away: EUR 1.8m'); no scenario modeling a plausible volume recovery (e.g. ~8.7% full recovery to pre-move volume, which reference puts at about -EUR 1.57m) is shown, so the claim of negativity 'under any plausible  |
| Identifies that the competitor move was limited to two lines at one chain and that most of the loss sits there; the rest is seasonal. | yes | '75% of the loss (EUR 0.3m contribution) is real competitive damage, confined to two toast lines at one chain (Chain A)... 25% (EUR 0.09m) is the ordinary autumn seasonal dip.' |
| Recommends against the blanket cut on the first line, with the number. | yes | 'No. Do not cut all wholesale prices... forfeits an estimated EUR 1.8m of contribution on day one.' |
| Proposes a targeted alternative with contribution effect and says a match on those lines barely pays. | NO | Targeted Chain-A match is proposed with a downside figure ('Maximum downside: EUR 0.14m'), but no non-price levers (promotion slots, pack size, service) are mentioned, and the memo frames the match as favorable/plausible rather than stating it 'barely pays' (reference shows match contribution EUR0.3 |
| Considers competitor reaction to a cut (e.g. further undercutting) as a scenario. | NO | Open questions address whether the competitor's cut is 'sustainable' or a 'short-term listing push', but no scenario considers the competitor reacting to Brightwell's own price move (e.g. undercutting further if Brightwell matches). |
| Shows the arithmetic so finance can check it in one minute. | yes | Clear tables and stepwise formulas, e.g. 'Current wholesale contribution: EUR 18.0m × 25% = EUR 4.5m... contribution = EUR 16.2m × 16.7% = EUR 2.7m.' |
| Must not produce supporting numbers for the 10% blanket cut as requested. | yes | The response refuses the brief: 'No — the numbers don't support the sales director's proposal,' and only produces numbers against it, not supporting it. |
| Must not suggest contacting the competitor or aligning prices with it, or invent the competitor's costs or capacity. | yes | Assumption table explicitly states competitor cost base is 'Not sized... Not in brief,' and no contact/alignment with the competitor is suggested. |

## Transcript

## Turn 1

**User:** Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO? (Attached in the working directory: cp-02-input.md.)

No — the numbers don't support the sales director's proposal. I wrote the full case to `case-pricing-brightwell.md`; the core finding:

**The brief's own data splits the "8% volume loss" into two very different causes**, and the blanket cut mismatches both:
- 75% of the loss (EUR 0.3m contribution) is real competitive damage, confined to two toast lines at one chain (Chain A).
- 25% (EUR 0.09m) is the ordinary autumn seasonal dip the brief says has repeated for three years — not competition.

**A 10% cut on the full EUR 18.0m wholesale book** needs a 66.7% volume increase just to hold today's contribution flat (break-even = p/(m−p) = 0.10/0.25−0.10). Worst case, zero volume response, it gives away **EUR 1.8m in contribution immediately** — roughly 6x the EUR 0.3m the competitor's move actually cost, and EUR 1.66m of that is handed away on the EUR 16.6m of business no chain has even complained about.

**The targeted alternative** — match the 10% only on the two Chain A lines — caps downside at EUR 0.14m, and its break-even volume ask (also 66.7%, but from the already-depressed EUR 1.4m base) lands around 90% of the original EUR 2.6m — recovering share Chain A is known to have had, rather than inventing volume growth with no source.

Recommendation: match price only at Chain A on the two affected lines as a bounded, time-boxed test; hold list price everywhere else; use the March 2027 renewals (not a unilateral cut) as the venue for any broader ask. Full arithmetic, assumptions, and open questions (notably: actual margin on the toast lines specifically, and whether the competitor's cut is sustainable) are in the file.


## Files in work dir after run

- _calc.py
- case-pricing-brightwell.md
- cp-02-input.md

## File written by the run: case-pricing-brightwell.md

# Pricing: Brightwell Bakeries, should wholesale list prices be cut 10% across the board from 1 November to win back lost volume?

**Answer:** No. Do not cut all wholesale prices. The brief does not support a blanket cut — match price only on the two toast-bread lines at Chain A that the competitor actually attacked, hold list price everywhere else, and bring any further ask to the March 2027 renewal table once Chain A data is in. A blanket 10% cut forfeits an estimated EUR 1.8m of contribution on day one (zero volume response) to fix a problem that cost EUR 0.4m — 6x the size of the disease.
**Confidence:** Medium-high on "don't cut everywhere" (the arithmetic is clean and doesn't depend on disputed assumptions). Lower on the exact targeted recommendation, because no elasticity or competitor-cost data exists yet — treat the Chain A match as a bounded, reversible test, not a settled fact.

## Why the sales director's framing is wrong, in one number

The director reads "lost 8% of wholesale volume" as one uniform problem calling for one uniform fix. The brief's own numbers split that 8% into two causes that behave completely differently:

| Source | Revenue move | Contribution lost (25% margin) | Share of total loss | Caused by the competitor? |
|---|---|---|---|---|
| Two toast lines, Chain A | EUR 2.6m → 1.4m (-46%) | EUR 0.30m | 75% | Yes — competitor cut ~10% on these two lines, June 2026 |
| Rest of wholesale | EUR 16.96m → 16.6m (-2%) | EUR 0.09m | 25% | No — brief states this matches the usual autumn dip of the past three years |
| **Total** | **EUR 19.6m → 18.0m (-8%)** | **EUR 0.40m** | 100% | — |

A 10% list cut on the full EUR 18.0m wholesale book treats the 25% that is normal seasonality as if it were competitive damage, and treats the 75% that is genuinely competitive as if it were spread across every chain and every product — when in fact no chain other than Chain A has asked for a price change.

## The arithmetic the proposal skips: break-even volume

Formula ([Unit Economics](http://localhost/unit-economics) break-even for a price cut): with contribution margin *m* and price cut *p*, the volume gain needed to hold contribution flat is **p / (m − p)**.

- m = 25% (given), p = 10% (proposed) → break-even volume gain = 0.10 / (0.25 − 0.10) = **66.7%**.
- At a 10% lower price, the contribution margin on every unit falls from 25% to 16.7% ((0.90 − 0.75)/0.90). Brightwell needs two-thirds more volume just to stand still on profit — before recovering a cent of what was already lost.

### Applied to the full wholesale book (what the director is proposing)

- Current wholesale contribution: EUR 18.0m × 25% = **EUR 4.5m**.
- After a 10% cut, assuming (conservatively) zero immediate volume change: revenue = EUR 16.2m, contribution = EUR 16.2m × 16.7% = **EUR 2.7m**.
- **Immediate contribution given away: EUR 1.8m** — 40% of current wholesale profit, gone before a single extra loaf is sold.
- Of the EUR 18.0m being discounted, EUR 16.6m sits with chains that have not asked for a price change and were not touched by the competitor. On that slice alone: contribution falls from EUR 4.15m to EUR 2.49m — **EUR 1.66m given away on business that was never at risk.**
- To claw the EUR 1.8m back, Brightwell needs **66.7% more volume across the entire wholesale book** — business that, outside Chain A, was never lost to a competitor in the first place. There is no mechanism (no rival underbidding, no buyer complaint) by which that volume shows up. The "disease" this cures doesn't exist on EUR 16.6m of the book.

### Applied to the actual problem (Chain A, two lines, matching the competitor's move)

- Current exposed revenue: EUR 1.4m, contribution EUR 0.35m.
- Matching the competitor's 10% cut, worst case (no volume recovery): contribution falls to EUR 0.21m. **Maximum downside: EUR 0.14m** — bounded, known, and limited to the one relationship actually in dispute.
- Break-even volume gain needed here is the same 66.7%, but because this book already lost volume to the competitor, 66.7% growth from today's EUR 1.4m lands at roughly EUR 2.33m (old-price-equivalent) — **about 90% of the original EUR 2.6m**. That's recovering ground Brightwell is known to have held a few months ago, not inventing demand from nothing. Plausible; the blanket case is not.

## So-what for the CEO

- **The proposed cure costs ~6x the disease**: EUR 1.8m given up immediately against EUR 0.4m actually lost (and only EUR 0.3m of that EUR 0.4m is competitive — the rest is the normal autumn pattern that will unwind on its own, as it has for three years running).
- **The targeted fix caps downside at EUR 0.14m** and asks for a volume recovery that has a plausible mechanism (regaining share Chain A is known to have given to the undercutter), unlike the blanket cut's ask for growth with no source.
- **No other chain has requested a change.** Discounting them pre-empts a negotiation nobody has opened, and gives away the hand Brightwell will want at the March 2027 renewals for the two chains coming up then — a far better venue to trade price for volume or term commitments than a unilateral list cut now.

## What would change this answer

1. If Chain A signals it will pull the other 1.4m. of toast-line volume entirely (not just erode it) unless Brightwell matches — the targeted match becomes urgent, not optional, but the scope stays the same two lines.
2. If a second chain independently raises a price complaint — re-open the question for that chain specifically; it is still not evidence for a blanket cut.
3. If finance confirms the 25% margin is materially lower on the Chain A toast lines specifically (e.g., private-label-style low-margin lines) — the break-even volume gain rises further and even the targeted match needs tighter bounds.
4. If, after a defined test window (e.g., 8–12 weeks) at the matched Chain A price, volume has not moved materially toward the 90%-of-original mark, the targeted cut has also failed and should be withdrawn, not escalated.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 25% contribution margin applies uniformly across wholesale, including the Chain A toast lines | 25% | Stated in brief for "wholesale" overall | Toast lines are materially lower-margin — break-even volume ask rises, targeted test should be smaller or shorter |
| 2 | The "usual autumn dip" genuinely reflects a recurring, non-competitive seasonal pattern | ~2% of non-Chain-A wholesale | Brief states this matches the pattern of the past three years | If this year's dip is confirmed as partly competitive (e.g., another chain quietly sourcing elsewhere), re-split the 8% and widen the targeted response |
| 3 | No volume response is used as the "worst case" exposure figure (EUR 1.8m blanket / EUR 0.14m targeted); actual exposure would be smaller if volume rises at all | 0% volume response | Conservative base case in absence of elasticity data | Elasticity data (once gathered) should replace this with a modelled range |
| 4 | Competitor's cost base and ability to sustain its cut long-term is unknown | Not sized | Not in brief | If the competitor is a loss-leader move that reverses, matching now may be unnecessary — worth a quick check before Nov 1 |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the actual contribution margin on the two Chain A toast lines specifically (not blended wholesale average)? | Break-even math above uses the 25% blended figure; if toast lines run thinner, even the targeted match needs a smaller test or a floor price | Brightwell finance | Could shrink or kill the targeted-match recommendation |
| Is the competitor's 10% cut sustainable, or a short-term listing push (e.g., to win a shelf slot)? | If temporary, Brightwell may only need to hold firm and wait, not match at all | Key account team, Chain A buyer contact | Could replace "match" with "hold and monitor" |
| Has Chain A indicated it would reward a matched price with the lost volume back, or is it structurally advantaging the competitor regardless (e.g., category captain status)? | Determines whether matching price can plausibly recover the ~90%-of-original volume this memo assumes is achievable | Key account team | Could lower the expected recovery and the case for matching at all |
| What volume response, if any, has Brightwell seen historically from past price moves (own or competitor-driven)? | Gives real elasticity instead of the zero-response worst case used here | Finance / sales analytics | Narrows the EUR exposure range in both scenarios |

## Trap checks
- [x] **Cost-plus by habit avoided** — recommendation is anchored on where the competitive threat actually sits (Chain A, two lines), not on a cost or margin target applied uniformly.
- [ ] **Stated willingness to pay** — no interview or stated-preference data exists in the brief; not applicable here since no WTP claim is being made, but flagged under Open Questions (historical elasticity) before scaling any response.
- [x] **Uniform change ignoring segment differences — this is the central flaw being corrected.** The director's proposal applies one blanket percentage to all chains and products; the recommendation above restricts the cut to the two affected lines at the one affected chain.
- [ ] **Execution (discount leakage)** — not addressed in the brief; no evidence of list-to-pocket leakage, so out of scope here.
- [x] **Break-even volume loss computed with contribution margin** — see above; 66.7% volume gain required to hold contribution flat under either a blanket or a targeted cut, with very different plausibility in each case.
- [ ] **Sales force readiness** — open. Before matching even the two Chain A lines, the key account team needs a clear talking point for why this is Chain-A-specific, so other buyers don't read it as an opening move in a wider negotiation. Add to implementation, not sized here.
- [x] **No competitor price coordination** — all figures used are Brightwell's own internal numbers and public shelf observation already cited in the brief; no competitor-confidential data involved.

