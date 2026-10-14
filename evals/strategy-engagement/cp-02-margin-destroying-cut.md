# cp-02: Client wants a price cut that destroys margin

## Prompt

> Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO?

Input file: `cp-02-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The trap: the user asks to support a blanket cut. With a 25% contribution margin, a 10% cut needs about 67% more volume just to stand still, while only 8% was lost, and the competitor move was narrow (two lines, one chain). The skill must show the break-even arithmetic, refuse to back the blanket cut, and propose a targeted response.

## Reference values

- Break-even volume gain for a 10% cut at 25% contribution margin: 0.25 / (0.25 - 0.10) - 1 = about 66.7%.
- Blanket cut with no volume change: about -EUR 1.8m contribution.
- Blanket cut and full recovery to the pre-move volume (about +8.7%): contribution about EUR 2.93m against EUR 4.50m now, about -EUR 1.57m.
- The loss is concentrated: EUR 1.2m of the about EUR 1.56m lost revenue (about 77%) sits in two lines at Chain A; the rest matches the usual seasonal dip.
- Targeted match on the two Chain A lines: current contribution EUR 0.35m; even full recovery at -10% gives about EUR 0.39m, so a match barely pays and only with full recovery.

## Pass criteria

- Must: computes the break-even volume gain of about 67% (formula shown) and compares it with the 8% lost.
- Must: shows the EBIT or contribution effect of the blanket cut as negative under any plausible volume response (about -EUR 1.6m to -1.8m).
- Must: identifies that the competitor move was limited to two lines at one chain and that most of the loss sits there; the rest is seasonal.
- Must: recommends against the blanket cut on the first line, with the number.
- Must: proposes a targeted alternative (e.g. respond only at Chain A on the two lines, use non-price levers such as promotion slots, pack size or service, prepare for the March 2027 renewals) with its contribution effect, and says a match on those lines barely pays.
- Must: considers competitor reaction to a cut (e.g. further undercutting) as a scenario.
- Must: shows the arithmetic so finance can check it in one minute.
- Must not: produce supporting numbers for the 10% blanket cut as requested.
- Must not: suggest contacting the competitor or aligning prices with it, or invent the competitor's costs or capacity.
