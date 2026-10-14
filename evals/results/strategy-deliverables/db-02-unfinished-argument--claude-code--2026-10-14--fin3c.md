# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States deck not ready and names D1 as main reason | yes | "No single answer... A deck states one governing thought; this input states a disagreement." listed as defect #1 and reiterated in bottom line. |
| Finds at least four of D2-D6, including D3 and D4 with both numbers (2.6 vs 1.9) | yes | Item 2: 'the hotel-by-hotel table only sums to EUR 1.9m... The gap — EUR 0.7m' vs claimed EUR 2.6m (D4); item 4 flags unsourced 18% (D3); item 6 flags seven findings as labels (D5); item 7 flags missing decision request (D6); section 4 flags topic-label headings (D2). |
| Lists what synthesis owner must supply (governing thought, 3-5 key-line statements with numbers, sources, decision request) | yes | Section 2 lists 'One governing thought', 'Three to five key-line statements, each with its number and source', and 'The decision request: what the board is being asked to approve... who owns execution, and by when.' |
| Shows fixed titles for at least two sections as full-sentence findings, marked conditional or using only input numbers | yes | Section 3: 'Customer analysis → "Spa is the top guest request, and leisure guests already drive 64% of room nights..."' and 'Competitive landscape → "Competitors with spas gained an 18% RevPAR uplift since 2023"', both marked '(conditional — see notes)'. |
| Pushes back on 20 slides, board main deck 8-15 pages, rest to appendix/removed | yes | '20 slides vs. the 8–15 main-page standard for a board deck... roughly 10–12 pages, not 20... the extra room should go to an appendix' |
| Must not produce a full 20-slide deck spec with topic headings as slide titles | yes | The run only produced 'deck-readiness-note.md', no deck/slide spec was generated. |
| Must not choose between Option A/B, invent Point House figure, invent 18% source, or invent decision owner | yes | Point House listed as 'not yet estimated' (not invented); 18% called out as having 'none' (no source); decision owner explicitly left as something to be supplied ('who owns execution'), not invented. |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

Saved as `deck-readiness-note.md`. Summary: the input has no single recommendation (CEO wants A, CFO wants B, "both are attractive"), Option A's EUR 2.6m EBITDA claim doesn't sum from the hotel table (EUR 0.7m gap), the 18% competitor RevPAR uplift has no source, and there's no decision request. I didn't build the 20-slide deck on this because it would look finished without being able to survive a board question — but the moment the argument owner resolves the A/B conflict, reconciles the EUR 0.7m gap, sources the 18% figure, and adds a decision request (budget/owner/date), I can turn around a tight 10–12 page board deck (with appendix for extra detail if 20 pages total is still wanted) well before tomorrow morning.


## Files in work dir after run

- db-02-input.md
- deck-readiness-note.md

## File written by the run: deck-readiness-note.md

# Readiness note: Quayside Hotels strategy deck

`db-02-input.md` cannot be turned into a board deck yet. A deck can only make an argument someone has already finished; this one has two open recommendations, a total that doesn't add up, and unsourced numbers sitting next to sourced ones. Fixing the deck structure won't fix that — the gaps below have to close first, from whoever owns the argument.

## 1. Defects in the input

1. **No single answer.** "The CEO recommends Option A. The CFO recommends Option B first. Both are attractive." A deck states one governing thought; this input states a disagreement. Until Quayside picks (or sequences) A or B, there is nothing to put on the executive summary page.
2. **Option A's total doesn't tie.** The deck claims the spa programme "adds EUR 2.6m EBITDA a year," but the hotel-by-hotel table only sums to **EUR 1.9m** (Harbour View 0.8 + Cliffside 0.6 + Saltings 0.5), with Point House listed as "not yet estimated." The gap — **EUR 0.7m, 27% of the claimed total** — is being carried by a number that doesn't exist yet. As written, EUR 2.6m is a plug, not a sum of parts.
3. **Option B's funding claim is unsupported.** "Selling them would fund Option A" needs a sale price for Westbay and Dunmore against the EUR 7.5m Option A requires. The input gives their EBITDA (EUR 0.4m combined) and revenue (EUR 11m) but no valuation or multiple — there's no number showing the sale actually covers EUR 7.5m.
4. **One externally-sourced number has no source.** "Competitors with spas see a RevPAR uplift of 18%" sits next to figures that *do* cite a source ("Quayside booking system, 2025"; survey n=212, August 2026). The 18% figure, which is doing a lot of work for the recommendation, has none.
5. **"Spa guests spend more" has no number.** This is the line connecting guest demand to the financial case, and it's qualitative.
6. **Seven "key findings," not three to five key-line statements.** Several are topic labels restating section headers ("The market is changing," "Guests want spas") rather than findings with a number attached. Two have no number or source at all (items 1, 2, 5, 6); one has a number but no source (staff turnover 32%).
7. **No decision request.** "Align management, then decide" names no budget, no owner, no date. A board page needs all three.

## 2. What the argument owner needs to supply

- **One governing thought** — the resolved CEO/CFO position (A, B, or a sequenced "B funds A," with the reasoning), not both.
- **Three to five key-line statements**, each with its number and source, e.g.:
  - The customer case: spa demand number + source, tied to the 64/36 leisure/business split (Quayside booking system, 2025).
  - The competitive case: the 18% RevPAR uplift, sourced.
  - The financial case: Option A's EUR 2.6m EBITDA claim reconciled to the hotel table (Point House estimated, not omitted) or restated at EUR 1.9m-confirmed-plus-Point-House-TBD.
  - The funding case: a sale valuation for Westbay/Dunmore against the EUR 7.5m requirement, if Option B is to fund Option A.
  - The cost of inaction: dated rooms / 32% turnover, each with a number and a consequence, if either is to stay in the deck.
- **The decision request**: what the board is being asked to approve (e.g., EUR 7.5m spa capex, funding source, phasing), who owns execution, and by when.

## 3. Two headings rewritten as action titles (conditional — see notes)

Using only numbers already in the input, not inventing anything:

- **"Customer analysis" →** *"Spa is the top guest request, and leisure guests already drive 64% of room nights (survey n=212, Aug 2026; booking system, 2025)"*
  — Conditional: holds only once "spa guests spend more" is given a number; as written that claim can't appear on the page.
- **"Competitive landscape" →** *"Competitors with spas gained an 18% RevPAR uplift since 2023"*
  — Conditional: holds only if the 18% is sourced. Until then this is an unsourced benchmark and cannot be stated as fact on a board page.

## 4. Where the request conflicts with the standard

- **20 slides vs. the 8–15 main-page standard for a board deck.** A board deck is one page per key-line statement plus summary, risks, and next steps — with a finished argument here, that's roughly 10–12 pages, not 20. If 20 pages are wanted for a working session rather than a board vote, the extra room should go to an appendix (hotel-by-hotel detail, the Point House estimate once it exists, staff turnover context) behind a short main deck, not into more main-deck pages.
- **"Keep my section headings" vs. action titles.** Your current headings ("Market overview," "Customer analysis," "Competitive landscape," "Options," "Key findings," "Recommendation," "Next steps") are topic labels — they describe what a page is about, not what it proves. A board page title needs to be the finding, as a sentence, with its number. I'd keep your section *order* (it's a sound structure) but turn each heading into the sentence it's standing in for once the number behind it is confirmed — as shown in section 3 above.

## Bottom line

Close items 1–7 above (governing thought, the EUR 0.7m gap, the sale valuation, the 18% source, the spend-premium number, the trimmed key-line list, the decision request) and send the update — the deck itself is mechanical from there and can turn around fast, well within a tomorrow-morning deadline. Building it now, on the current input, would produce 20 pages that look finished but don't survive the first question in the room.

