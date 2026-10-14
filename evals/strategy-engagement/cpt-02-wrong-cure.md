# cpt-02: Client wants a headcount cut, the problem is price

## Prompt

> Saltmarsh's CEO has decided on a 15% headcount cut. Design the cut and confirm it restores 15% margin by 2027. Data attached.

Input file: `cpt-02-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The trap: the client arrives with a cure (cut labour). The data shows labour cost per kg is flat; energy and chemicals rose and could not be passed through because hospital contracts lack indexation. Plants run near capacity with a 24-hour service level, so a headcount cut threatens the volume the recovery needs. The skill must diagnose before cutting, say on the first line that the diagnosis contradicts the cure, with the number, and propose the price and indexation route.

## Reference values

- Revenue: 2022 about EUR 36.03m (average EUR 1.201 per kg); 2025 about EUR 37.79m (EUR 1.219 per kg).
- EBIT: 2022 about EUR 6.03m (16.7%); 2025 about EUR 3.48m (9.2%). Change about -2.55.
- Bridge: volume about +0.50 (1m kg x unit contribution), price about +0.56, energy and chemicals -3.41 (31m kg x 0.11), labour 0.00, other variable 0.00, fixed -0.20. Sum about -2.55.
- Proposed cure: 15% of labour cost (31m kg x 0.42 = 13.02) = about EUR 1.95m, not enough for 15% margin (EUR 5.67m EBIT, a gap of about EUR 2.19m) even if no volume were lost.
- Energy and chemicals indexation on hospital volume: 21.7m kg x 0.11 = about EUR 2.39m a year at full effect; about 40% of it from mid-2026, the rest from mid-2027.
- Unit contribution 2025: hospital EUR 0.37 per kg, hotel EUR 0.50 per kg.

## Pass criteria

- Must: first line of the answer says the diagnosis contradicts the headcount cut and gives the number (labour per kg flat at EUR 0.42; energy and chemicals +EUR 0.11 per kg, about EUR 3.4m).
- Must: profit bridge 2022 to 2025 that sums to about -2.55 with energy and chemicals as the largest driver and labour at zero.
- Must: shows that a 15% headcount cut (about EUR 1.95m) cannot reach 15% margin on its own and puts capacity (94% utilisation, unchanged productivity) and the 24-hour service level at risk.
- Must: names the root cause as missing price indexation in hospital contracts and sizes the indexation lever (about EUR 2.4m a year at full effect), timed to the 2026 and 2027 renewals, with the volume risk of renegotiation shown.
- Must: action plan in one reconciled bridge with timing, one-off cost, owner and confidence, showing whether 15% is reached by 2027 and any remaining gap.
- Must: uses the trade association survey with its caveat (self-reported) as supporting evidence that peers with indexation held margin.
- Must: checks or asks about liquidity separately (the input gives no cash data).
- Must not: design a 15% headcount cut as the main lever or confirm that it restores 15% margin.
- Must not: invent energy price forecasts or peer margins beyond the survey.
