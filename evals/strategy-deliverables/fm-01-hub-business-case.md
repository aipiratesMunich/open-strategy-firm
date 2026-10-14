# fm-01: Hub business case with ranges

## Prompt

> Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer.

Input file: `fm-01-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The happy path: clean inputs with sources and evidence-based ranges, a clear decision rule. The skill should build a driver model (inputs, calculations, outputs separate), coherent down and up scenarios, a tornado with break-even values, checks, and hand recomputes.

## Reference values (computed with the stated conventions)

- Net cash flow: t0 -6.00; 2027 +0.75 (5.0 x 60% x 0.55 - 0.9); 2028 to 2034 +1.85 each.
- Base NPV at 9%: about EUR 3.23m. IRR: about 20.9%. Undiscounted payback: cumulative cash turns positive in 2030 (year 4).
- One-way swings on NPV (others at base): saving per parcel EUR 0.40 / 0.65 gives about -0.65 / +5.81; parcels 3.8m / 5.6m gives about -0.18 / +4.94; investment 5.5 / 7.5 gives about +3.73 / +1.73; fixed cost 0.7 / 1.2 gives about +4.34 / +1.57; hurdle 7% / 11% gives about +4.02 / +2.53.
- Tornado order: saving per parcel, then parcels routed, then fixed cost, then investment and hurdle rate.
- Break-even: saving per parcel about EUR 0.425 (range 0.40 to 0.65, so inside); parcels about 3.86m (range 3.8 to 5.6, so inside).
- Example down case from the planning note (parcels 3.8m, saving EUR 0.45, investment EUR 7.0m): NPV about EUR -3.1m.

## Pass criteria

- Must: states the question, the outputs (NPV, payback, IRR or similar) and the decision threshold (NPV above zero at 9%) before building.
- Must: separates inputs, calculations and outputs (script output, spreadsheet or Markdown tables); no number typed inside a formula other than 0 and 1 or a documented unit conversion.
- Must: base NPV within EUR 3.1m to 3.4m and payback in 2030 or year 4, or explains a deviating convention that the input does not support.
- Must: a tornado ranking with saving per parcel first and parcels routed second.
- Must: gives break-even values for saving per parcel (about EUR 0.42 to 0.43) and parcels (about 3.8m to 3.9m) and says both lie inside their ranges.
- Must: because a break-even lies inside the range, puts it in the headline or "decided by" line, not only in an appendix.
- Must: defines the down case as a coherent story (competitor hub: fewer parcels, lower saving, higher investment) rather than a uniform cut, and reports its NPV as negative.
- Must: a checks block and two outputs recomputed by hand with both numbers recorded.
- Must: lists the 60% ramp as a flagged assumption.
- Must: "what the deck should say" sentences carrying the model version.
- Must not: present the NPV without the range or scenarios.
- Must not: add a terminal value or tax without flagging that it departs from the agreed conventions.
