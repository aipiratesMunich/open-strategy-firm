# db-03: Minimal input, one decision, phone reader

## Prompt

> Need something for our CEO on the kiosk question, she reads everything on her phone between meetings. Findings: 3 of our 11 station kiosks lose money (Nordbahnhof -140k, Kreuzplatz -0.16m, Ostring -110,000 EBIT last year). Together they do 2.1m revenue, Brightwell total is 62m. Getting out of the leases costs about 250k one-off. Footfall at all three stations fell after the commuter rail timetable change in 2025, the other 8 kiosks are fine. Source for all of it is our 2025 store P&L and the lease register.

*Fictional company. All figures invented for evaluation.*

## What this case tests

Robustness. No engagement folder, no synthesis file, mixed units, one decision, a single reader on a phone. The skill should choose the one-page memo over a deck, normalise the numbers, flag the missing decision owner and date as proposed assumptions, and not ask a long list of questions.

## Reference values

- EBIT losses: 140k + 160k + 110k = EUR 410k a year.
- Revenue at stake: EUR 2.1m of 62m = about 3.4%.
- Lease exit EUR 250k one-off: recovered in about 7 months from the avoided losses (250 / 410 x 12 = 7.3).

## Pass criteria

- Must: chooses the one-page memo format (`format: memo` in the frontmatter or an explicit memo layout) and gives a one-line reason tied to the decision or the reader (e.g. one decision, one reader on a phone, few exhibits).
- Must: opens with the answer (close the three kiosks, or close them under a stated condition) in the first sentence or title, as a full-sentence finding.
- Must: states the EBIT effect as EUR 410k a year, the revenue at stake (EUR 2.1m of 62m, about 3 to 3.4%) and the one-off exit cost with a payback of about seven months (7.3; "under 8 months" accepted), all with a currency label and one scale per measure.
- Must: names the cause (footfall fell after the 2025 timetable change) and what would change the answer (e.g. timetable reversal, renegotiated rent).
- Must: includes a decision request with owner and date; because the prompt gives none, they are proposed and visibly flagged as assumptions.
- Must: cites the 2025 store P&L and lease register as the source.
- Must: asks at most one round of questions, or none, before delivering.
- Must not: produce a multi-slide deck.
- Must not: add facts not in the prompt (e.g. footfall percentages, rent levels, competitor kiosks).
