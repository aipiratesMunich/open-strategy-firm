# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States argument not ready for a deck and names D1 as main reason | yes | "this draft isn't ready for a deck yet... No single answer: CEO recommends Option A, CFO recommends Option B" and "Building 20 slides on top of this would just dress up the disagreement, not resolve it." |
| Finds at least four of D2-D6, including D3 and D4 with both numbers | yes | Found D2 (topic-label headings), D3 ("RevPAR uplift of 18%... not attributed"), D4 ("EUR 1.9m" vs "EUR 2.6m"), D5 ("7 items, not 3–5"), D6 ("Missing decision request") — all five found. |
| Lists what synthesis owner must supply: governing thought, 3-5 key-line statements with numbers, sources, decision request | yes | "One governing thought... 3–5 key-line statements, each with its own number and source... The decision request: what the board is being asked to approve, the budget, the owner, and the date." |
| Shows fixed titles for at least two sections, full-sentence, marked conditional or using only input numbers | yes | "'Competitive landscape' → 'Three competitors have added spas since 2023, reporting an 18% RevPAR uplift' — conditional" and "'Options' → 'Option A is costed at EUR 7.5m...' — conditional" |
| Pushes back on 20 slides citing board deck 8-15 pages | yes | "20 slides vs. 8–15: board decks run 8–15 main pages under this standard. Twenty slides on an argument that doesn't yet have a single recommendation would mean padding, not substance." |
| Must not produce a full 20-slide deck spec with topic headings as slide titles | yes | No deck spec was produced; response instead delivered a readiness note. |
| Must not choose between Option A/B, invent Point House figure, invent source for 18%, or invent a decision owner | yes | "pick one recommendation" left to user; Point House flagged as "not yet estimated"; 18% flagged as "not yet confirmed"; decision request flagged as missing, no owner invented. |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

I read `db-02-input.md` closely before building anything — and per the strategy-deliverables standard, this draft isn't ready for a deck yet. All four stop conditions are triggered:

- **No single answer**: CEO recommends Option A, CFO recommends Option B, "Both are attractive."
- **More than five key-line points**: "Key findings" lists 7, and they're topic labels, not findings with numbers.
- **Key numbers without sources**: several.
- **A total that doesn't tie**: Option A's hotel table sums to less than its headline figure.

Building 20 slides on top of this would just dress up the disagreement, not resolve it. Here's the readiness note instead.

## 1. Defects

**No governing thought / no single answer**
- "Recommendation" presents two competing options and declines to choose: *"The CEO recommends Option A. The CFO recommends Option B first. Both are attractive."* A board deck needs one recommendation, not two unreconciled ones.

**Topic-label headings, not findings**
- Market overview, Customer analysis, Competitive landscape, Options, Key findings — these are section topics, not statements of what was found. None of them is a sentence with a number that proves anything on its own.

**"Key findings" has 7 items, not 3–5, and most carry no number**
1. "The market is changing." — no number.
2. "Guests want spas." — no number (the number lives elsewhere, in Customer analysis).
3. "Competitors are investing." — has a number (18% RevPAR uplift) but see sourcing issue below.
4. "Two hotels are weak." — has a number (EUR 0.4m EBITDA / EUR 11m revenue, sourced to Quayside P&L 2025) — this is the one properly evidenced finding.
5. "Rooms are dated in some hotels." — no number, and the associated option (C) is "not costed."
6. "Business travel has not fully recovered." — no number, no source.
7. "Staff turnover is high (32%)." — has a number, no source, and no stated link to Options A/B/C.

**Key numbers without a source**
- "Spa guests spend more." — no figure at all.
- "Competitors with spas see a RevPAR uplift of 18%." — whose data? Not attributed (industry report? competitor filings? internal estimate?).
- Staff turnover "32%" — no source given.
- Guest survey is sourced (n=212, August 2026) — that one's fine.

**Total that does not tie**
- The Option A table: Harbour View 0.8 + Cliffside 0.6 + Saltings 0.5 = **EUR 1.9m** named across three hotels.
- The text claims the full programme "adds **EUR 2.6m** EBITDA a year" across four hotels.
- Point House is listed as "not yet estimated" — so EUR 0.7m of the EUR 2.6m headline (27% of it) is currently unaccounted for. The deck cannot state EUR 2.6m until Point House has a number or the headline is restated as "EUR 1.9m confirmed, Point House pending."

**Missing decision request**
- "Next steps" says only "Align management, then decide." No specific ask, no budget confirmed (Option A costs EUR 7.5m; Option B's funding math depends on a sale price for Westbay/Dunmore that is never given — only their EBITDA and revenue), no owner, no date.

**Option C is a dangling comparator**
- "Refurbish rooms in all hotels. Not costed." It's tied to finding 5 (dated rooms) but can't be ranked against A or B without a cost, so it currently just sits there unresolved.

## 2. What the argument owner needs to supply

- **One governing thought**: a single recommendation (A, B, a combination, or a sequenced "B then A") — not "both are attractive."
- **3–5 key-line statements**, each with its own number and source, e.g.:
  - Point House spa EBITDA estimate (to close the EUR 1.9m → EUR 2.6m gap)
  - Source for the 18% competitor RevPAR uplift
  - A figure for "spa guests spend more" (e.g., ADR or spend-per-stay delta, sourced)
  - Westbay/Dunmore expected sale proceeds, to show whether Option B actually funds Option A
  - A decision on whether staff turnover (32%) and business-travel recovery belong in this argument at all, or are a separate workstream
- **The decision request**: what the board is being asked to approve, the budget, the owner, and the date.

## 3. Two headings rewritten as action titles (numbers from the input only, marked conditional)

- **"Competitive landscape" →** *"Three competitors have added spas since 2023, reporting an 18% RevPAR uplift"* — **conditional**: source for the 18% figure not yet confirmed; cannot go on a board page unsourced.
- **"Options" →** *"Option A is costed at EUR 7.5m; EUR 1.9m of its claimed EUR 2.6m EBITDA is confirmed by named hotels"* — **conditional**: pending Point House estimate; headline number changes once that lands.

## 4. Conflict with the deck standard

- **20 slides vs. 8–15**: board decks run 8–15 main pages under this standard. Twenty slides on an argument that doesn't yet have a single recommendation would mean padding, not substance.
- **"Keep my section headings"**: the current headings (Market overview, Customer analysis, …) are topic labels, which the standard replaces with action titles — one finding-with-a-number per page title. If you want the originals kept verbatim as slide titles, that conflicts with the standard directly; the usual fix is to keep them as the section/tracker labels (visible in the deck's running section marker) while the actual slide titles become action sentences built from each section's numbers.

**Proposed fix:** close the gaps in section 2 above (especially Point House and the decision request), pick one recommendation, and I'll build an 8–15 page board deck with your section names retained as tracker labels and action titles on each page. Want me to draft the specific questions to send to the CEO/CFO to get those numbers, or do you have them already?


## Files in work dir after run

- db-02-input.md
