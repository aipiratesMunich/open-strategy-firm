# db-02: Unfinished argument with topic titles

## Prompt

> Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings.

Input file: `db-02-input.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The trap: the user wants a deck from a draft that has no single answer, topic-label headings, seven findings that are not findings, an unsourced key number and a total that does not tie. The skill's step 1 says a deck cannot fix an unfinished synthesis. It must stop, say exactly what is missing, and must not dress the draft up as a board deck.

## Planted defects

| # | Defect | Expected handling |
|---|---|---|
| D1 | Two competing recommendations (CEO: Option A, CFO: Option B), no governing thought | Named as the reason the deck cannot be built yet |
| D2 | Section headings are topic labels ("Market overview", "Customer analysis", "Options", "Next steps") | Named; user's request to keep them declined or shown as action-title rewrites |
| D3 | "RevPAR uplift of 18%" for competitors with spas has no source | Flagged as unsourced key number |
| D4 | Spa programme "adds EUR 2.6m EBITDA" but the table sums to EUR 1.9m with one hotel not estimated | Flagged with both numbers |
| D5 | Seven "key findings", most of them labels without numbers or so-what | Flagged: more than five points, not findings |
| D6 | No decision request with owner, budget and date ("Align management, then decide") | Flagged as missing |

## Reference values

- Spa table: 0.8 + 0.6 + 0.5 = EUR 1.9m against EUR 2.6m claimed; Point House not estimated, so the gap of EUR 0.7m is unexplained.
- Westbay and Dunmore: EUR 0.4m EBITDA on EUR 11m revenue = 3.6% margin, against Quayside total 9.8 / 71 = 13.8%.

## Pass criteria

- Must: states that the argument is not ready for a deck and names D1 (no single answer) as the main reason.
- Must: finds at least four of D2 to D6, including D3 and D4 with both numbers (2.6 vs 1.9).
- Must: lists what the synthesis owner must supply before the deck can be built (one governing thought, three to five key-line statements with numbers, sources for the key numbers, decision request).
- Must: shows what fixed titles would look like for at least two sections (full-sentence findings), clearly marked as conditional on the missing answer or using only numbers in the input (e.g. "Westbay and Dunmore earn a 3.6% EBITDA margin against 13.8% for the group").
- Must: pushes back on 20 slides (board main deck 8 to 15 pages; the rest to the appendix or removed).
- Must not: produce a full 20-slide deck spec with the topic headings as slide titles.
- Must not: choose between Option A and B on the client's behalf as if the deck could settle it, or invent the missing Point House figure, a source for the 18% or a decision owner.
