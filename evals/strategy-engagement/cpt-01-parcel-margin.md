# cpt-01: Margin decline with a clean profit bridge

## Prompt

> Kestrel parcel division: work the turnaround case from the data pack. Answer page for the CFO.

Input file: `cpt-01-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The happy path: full driver data for two years, contracts without indexation that renew soon, a covenant close to its limit and peers quoted but not compiled. The skill should build a bridge that sums to the reported change, split labour into wage and productivity, check liquidity separately, and build one reconciled action plan with timing tied to the 2026 renewals.

## Reference values

- Revenue 200.0 (2023) and 210.6 (2025). EBIT 16.0 (8.0%) and 5.24 (2.5%). Change -10.76.
- Bridge: volume +2.2 (2m parcels x 1.10 unit contribution), price +2.6 (52m x 0.05), variable cost per parcel -14.56 (52m x 0.28), fixed cost -1.0. Sum -10.76.
- Variable cost split: labour -9.36, fuel -4.16, subcontractors -1.04.
- Labour per parcel: wage effect 1.60 x 1.09 = about 1.744 (+0.14); productivity effect 1.744 x 18.0 / 17.6 = about 1.78 (+0.04).
- Target 6% on 2025 revenue: about EUR 12.6m EBIT, a gap of about EUR 7.4m.
- Covenant: 44 / 14.2 = about 3.1x against 3.5x; EBITDA can fall only about EUR 1.6 to 1.7m before a breach.

## Pass criteria

- Must: profit bridge from 2023 to 2025 by driver that sums to -10.76 (within rounding) and names variable cost per parcel as the largest driver.
- Must: splits variable cost into labour, fuel and subcontractors and labour into wage and productivity effects.
- Must: root cause in one sentence first: unit cost rose about EUR 0.28 per parcel (about 9.7%) while price rose EUR 0.05 (about 1.25%), in euros or percent, mainly because 60% of volume sits on fixed-price contracts without indexation.
- Must: checks liquidity separately and flags the thin covenant headroom (about 3.1x vs 3.5x, about EUR 1.6m of EBITDA) as a constraint on one-off restructuring costs and timing.
- Must: action plan in one reconciled bridge, each action with EBIT effect, range, one-off cost, timing, owner and confidence; repricing or indexation at the 2026 renewals is timed to the renewal window and its volume risk is shown.
- Must: the actions reach or show the remaining gap to about EUR 12.6m EBIT (6%) by 2027.
- Must: treats peers "held their margins" as unverified and names the peer figures to compile (normalised margin, price indexation practice) before claiming an internal cause.
- Must: no euro counted twice (e.g. price and volume effects on the same contracts shown consistently).
- Must not: propose an across-the-board cost cut before the diagnosis, or cuts to drivers and sorters without addressing productivity and service.
- Must not: invent peer margins or industry wage data.
