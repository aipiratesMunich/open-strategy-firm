# cp-01: List price increase with a leaky waterfall

## Prompt

> Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board.

Input file: `cp-01-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The happy path: a price level question, a waterfall with uncontrolled discounting in one segment, like-for-like competitor prices, one past price change as revealed behaviour, and contribution margin. The skill should run the waterfall first, compute break-even volume loss with contribution margin, compare it with expected loss, differentiate by segment, fix execution with the level, and give the EBIT effect as a range.

## Reference values

- Break-even volume loss for +5% at 40% contribution margin: 1 - 0.40 / 0.45 = about 11.1%.
- 2023 revealed response: -2% volume for +3% price (about -0.67 elasticity). Simple extrapolation for +5%: about -3.3%.
- EBIT effect on EUR 24.0m pocket revenue: 24 x ((1 - v) x 0.45 - 0.40). At v = 0: +1.20m; v = 2%: about +0.98m; v = 3.3%: about +0.84m; v = 6%: about +0.55m; v = 11.1%: about 0.
- Pocket price is 81% of list; leakage 19 points; small direct accounts get 22% with no cap.
- Like-for-like gap: 7% to 9% below competitors, so +5% keeps Ravensworth below both.

## Pass criteria

- Must: runs the price waterfall first and states that a list increase only reaches pocket price if discounts do not widen, with the uncapped 22% for small direct accounts named as the leak.
- Must: break-even volume loss of about 11% computed with contribution margin, formula or arithmetic shown.
- Must: uses the 2023 change (-2% for +3%) as revealed behaviour and compares the expected loss (about 3% to 4%, or a stated range) with the break-even.
- Must: EBIT effect as a range across volume reactions (e.g. about EUR 0.55m to 1.0m), with the arithmetic shown so finance can check it.
- Must: differentiates by segment (e.g. OEM timing at the January renewal, distributor 60-day notice, discount cap and approval rule for small direct accounts).
- Must: anchors the recommendation on customer value and the like-for-like competitor gap, not on cost.
- Must: names competitor reaction as a scenario (follow, hold, undercut) and says what would trigger a different answer.
- Must: answer line states the decision type (price level plus execution), the amount, the segments, the date and the EBIT range.
- Must: names the source of the 2023 market comparison (industry association data) and treats the 2023 response as one data point, stating whether the recommendation depends on it.
- Must not: compute break-even with gross margin or without showing the formula.
- Must not: suggest sharing price intentions with competitors or using competitor contract data.
