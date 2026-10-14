# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States argument not ready for deck, names D1 as main reason | yes | Title 'readiness note (not a deck)'; 'A deck can't paper over that'; first blocking item is 'which of A/B the board is actually being asked to decide' |
| Finds at least four of D2-D6, including D3 and D4 with both numbers | yes | D2 topic-label headings (#7), D3 '18% ... no source (whose data, what period, which competitors)', D4 'adds EUR 2.6m EBITDA ... sums to EUR 1.9m ... Point House not yet estimated', D5 '7 ("Key findings" caps at 3–5)... most carry no number', D6 'No decision request... names no ask, no budget, no own |
| Lists what synthesis owner must supply: governing thought, 3-5 key-line statements with numbers, sources, decision request | yes | Section '2. What the argument owner must supply' lists 'One governing thought', 'Three to five key-line statements, each with its own number and source', and 'A decision request' |
| Shows fixed titles for at least two sections, conditional | yes | Section 3 gives two rewritten headings each marked '(conditional on sourcing the 18% figure)' and '(conditional on backing...)' |
| Pushes back on 20 slides | yes | '20 slides exceeds the 8–15 main-page board-deck standard.' |
| Does not produce full 20-slide deck spec with topic headings as titles | yes | Output is a readiness note, not a deck; no slide-by-slide spec produced |
| Does not choose between A/B, invent Point House figure, invent 18% source, or invent decision owner | yes | 'state whether A and B are alternatives, a sequence, or a combined ask' (no choice made); '18% RevPAR uplift — sourced to a named benchmark' (flagged as missing, not invented); 'who owns execution' listed as something still needed, not supplied |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

Saved to `quayside-readiness-note.md`. Bottom line: the input has two unreconciled recommendations (CEO wants Option A, CFO wants Option B first, text just says "both are attractive"), and the headline EUR 2.6m EBITDA claim doesn't tie to its own backup table (which sums to EUR 1.9m with Point House still "not yet estimated"). A deck can't paper over that.

Three things would unblock a real deck today: (1) which of A/B the board is actually being asked to decide — or how they relate, (2) a fix or explicit flag on the EUR 2.6m vs EUR 1.9m gap, (3) a named owner and date for the ask. Everything else (sourcing the 18% RevPAR figure, costing Option C, backing "spa guests spend more") can go in as flagged assumptions rather than block the work. Send those three and I'll turn the deck around.


## Files in work dir after run

- db-02-input.md
- quayside-readiness-note.md

## File written by the run: quayside-readiness-note.md

# Quayside strategy review: readiness note (not a deck)

The input has two unreconciled recommendations and a headline number that doesn't tie to its own backup table. Fixing those is faster than building slides around them twice.

## 1. Defects

1. **No single answer.** The CEO recommends Option A (spa expansion); the CFO recommends Option B first (sell Westbay and Dunmore); the draft then says "Both are attractive" without saying whether A and B are alternatives, a sequence (sell to fund the build), or both needed. A board page needs one governing thought — this has none.

2. **Key findings don't work as key-line statements.** There are 7 ("Key findings" caps at 3–5), and most carry no number:
   - "The market is changing" — no metric.
   - "Guests want spas" — no metric here (the metric — survey n=212 — sits in a different section).
   - "Competitors are investing" — no metric here (the 18% RevPAR figure sits elsewhere).
   - "Two hotels are weak" — no metric here (the EUR 0.4m/EUR 11m figures sit elsewhere).
   - "Rooms are dated in some hotels" — no metric, no cost, and ties to an option (C) that isn't costed.
   - "Business travel has not fully recovered" — no metric.
   - "Staff turnover is high (32%)" — has a number but no stated link to the A/B decision on the table.

3. **A total doesn't tie.** Option A claims the spa programme "adds EUR 2.6m EBITDA a year," but the per-hotel table sums to **EUR 1.9m** (Harbour View 0.8 + Cliffside 0.6 + Saltings 0.5), with Point House "not yet estimated." The EUR 2.6m figure requires Point House alone to contribute **EUR 0.7m** — more than any of the three estimated hotels, and unverified.

4. **No decision request.** "Align management, then decide" names no ask, no budget, no owner, no date.

5. **Option C can't be compared.** "Refurbish rooms in all hotels" is listed as a live option but has no cost at all, so it can't be weighed against A or B.

6. **Unsourced or missing numbers:**
   - "Competitors with spas see a RevPAR uplift of 18%" — no source (whose data, what period, which competitors).
   - "Spa guests spend more" — no number, no source.
   - The EUR 7.5m spa investment cost — no source.
   - Staff turnover 32% — no source, and no stated relevance to Option A or B.

7. **Topic-label headings throughout** — "Market overview," "Customer analysis," "Competitive landscape," "Options," "Key findings," "Recommendation," "Next steps" describe what each page is *about*, not what it *found*. None would survive a titles-only read-through.

## 2. What the argument owner must supply

- **One governing thought** — state whether A and B are alternatives, a sequence, or a combined ask, so the board is asked one question.
- **Three to five key-line statements, each with its own number and source**, e.g.:
  - Spa demand: survey n=212, August 2026, spa top-requested; leisure 64% / business 36% of room nights (Quayside booking system, 2025).
  - Competitive gap: 18% RevPAR uplift — sourced to a named benchmark.
  - Financial case: EUR 2.6m EBITDA claim reconciled to the per-hotel table (either Point House gets a real estimate, or the headline number drops to ~EUR 1.9m+Point House-TBD).
  - Funding: EUR 0.4m EBITDA / EUR 11m revenue for Westbay + Dunmore, plus what the sale actually raises (a valuation or multiple — not given, only EBITDA).
  - A call on Option C (cost it or drop it), and on whether dated rooms / business travel recovery / staff turnover belong in *this* decision or are separate workstreams.
- **A decision request**: what exactly the board approves (Option A's EUR 7.5m budget? the Westbay/Dunmore sale? a sequence of both?), who owns execution, and by what date.

## 3. Two headings rewritten as action titles (conditional — pending the sourcing above)

- **"Competitive landscape" →** *"Spa-equipped competitors have posted an 18% RevPAR uplift since 2023 — a benchmark Quayside has not yet verified against its own data"* (conditional on sourcing the 18% figure).
- **"Customer analysis" →** *"Spa is the top-requested amenity among leisure guests, who already make up 64% of Quayside's room nights"* (conditional on backing "spa guests spend more" with an actual number).

## 4. Where the request conflicts with the standard

- **20 slides exceeds the 8–15 main-page board-deck standard.** Fix: once the argument is cut to 3–5 key-line statements, the main deck is naturally ~8–10 pages (title, executive summary, 3–5 section pages, financial summary, risks/next steps). The per-hotel spa table, the Westbay/Dunmore P&L, survey methodology and competitor list move to an appendix — which can run as long as you like without inflating the board narrative, so the combined pack can still land near 20 pages if that's wanted.
- **"Keep my section headings" conflicts with the action-title requirement** (a board slide title must state the finding, not the topic). Fix: keep your seven sections as the deck's structure and order — but each section's slide title becomes the finding for that section (as shown in part 3), with your original heading kept as a small section/tracker label rather than the slide title.

## Fastest path to tomorrow morning

The blocking items are #1 (pick the CEO/CFO relationship), #3 (fix or flag the EUR 2.6m vs EUR 1.9m gap), and #4 (name an owner and date for the ask). Those three alone would let me turn this into a real deck same day — the rest (sourcing the 18%, costing Option C, confirming spa spend) can go into the deck as flagged assumptions with ranges rather than blocking it.

