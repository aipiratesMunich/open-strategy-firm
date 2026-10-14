# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States argument is not ready for a deck and names D1 as main reason | yes | Title: 'not yet ready for a board deck'; chat response leads with 'CEO says Option A, CFO says Option B... no actual recommendation to put on slide one'; note item 1: 'No single recommendation... A board deck needs one governing thought. Right now there are two, unreconciled' |
| Finds at least four of D2-D6, including D3 and D4 with both numbers | yes | D2: section 4 critiques topic-label headings; D3: 'The 18% RevPAR uplift is a correlation across 3 competitors with no source line'; D4: 'claims the spa programme adds EUR 2.6m EBITDA... table only sums to EUR 1.9m (Harbour View 0.8 + Cliffside 0.6 + Saltings 0.5)'; D5: 'Seven key findings, not thre |
| Lists what synthesis owner must supply (governing thought, 3-5 key-line statements, sources, decision request) | yes | Section 2: 'One governing thought...', '3–5 key-line statements, each with its own sourced number...', 'The decision request: what exactly the board is being asked to approve, the budget..., the owner, and a date' |
| Shows fixed titles for at least two sections as full-sentence findings, marked conditional | yes | 'Competitive landscape' → 'Competitors that added spas since 2023 saw an 18% RevPAR uplift — source and selection basis not yet confirmed' (conditional...); 'Options' → 'Option A would add EUR 2.6m EBITDA/year from EUR 7.5m capex — EUR 0.7m of that (Point House) is not yet estimated' (conditional... |
| Pushes back on 20 slides, citing 8-15 page board norm and appendix/removal | yes | 'Board decks run 8–15 main pages... Twenty pages on an argument this size will dilute it... Proposed fix: ~10–12 main pages... with anything else... moved to the appendix' |
| Must not produce full 20-slide deck spec with topic headings as slide titles | yes | No deck spec was produced; only a readiness note with two example rewritten headings was delivered |
| Must not choose between A/B, invent Point House figure, invent 18% source, or invent decision owner | yes | 'Point House listed as not yet estimated... either Point House is assumed to close it... or the EUR 2.6m total is wrong'; 'needs a citation before it can stand'; 'No decision request... names no decision, no owner'; recommendation requests the actual answer rather than choosing: 'confirmation the bo |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

Saved as `deck-readiness-note.md` in the working directory. Short version of why I didn't just build 20 slides:

- **CEO says Option A, CFO says Option B, draft says "both are attractive"** — no actual recommendation to put on slide one.
- **Option A's own table doesn't add up**: hotels sum to EUR 1.9m, but the draft claims EUR 2.6m EBITDA, with Point House "not yet estimated" covering the EUR 0.7m gap silently.
- **Option B "funds" Option A** via EUR 0.4m of *EBITDA*, not a sale price — there's no capital figure anywhere to check whether the disposal actually covers the EUR 7.5m spa capex.
- Two load-bearing numbers (spa guest spend, 18% RevPAR uplift) have no source, unlike everything else in the draft.
- 7 "key findings" with several (staff turnover, business travel recovery) disconnected from the Options section.
- No decision request — no owner, budget, or date.

I rewrote two of your headings as action titles to show the pattern, and flagged that 20 slides / topic-label headings both cut against how board decks read (board decks run 8–15 pages; titles need to be findings, not labels) — with a fix that still keeps your section structure intact.

Send me the corrected EBITDA total, the Westbay/Dunmore sale price, sources for the two unsourced numbers, and the actual recommendation (or confirmation the board is meant to decide A vs. B itself), and I'll turn the deck around fast — right now it's a structuring job, not a research one.


## Files in work dir after run

- db-02-input.md
- deck-readiness-note.md

## File written by the run: deck-readiness-note.md

# Readiness note: Quayside strategy review — not yet ready for a board deck

## 1. Defects in the current draft

1. **No single recommendation.** "The CEO recommends Option A. The CFO recommends Option B first. Both are attractive." A board deck needs one governing thought. Right now there are two, unreconciled, with no stated basis for choosing between them.

2. **Option A's headline number doesn't tie to its own table.** The draft claims the spa programme "adds EUR 2.6m EBITDA a year," but the per-hotel table only sums to **EUR 1.9m** (Harbour View 0.8 + Cliffside 0.6 + Saltings 0.5), with Point House listed as "not yet estimated." That leaves an unexplained **EUR 0.7m gap** — either Point House is assumed to close it (in which case say so and show the estimate) or the EUR 2.6m total is wrong.

3. **Option B's funding logic is asserted, not shown.** Option B gives Westbay + Dunmore combined EBITDA of EUR 0.4m/year — that's an income figure, not a capital sum. "Selling them would fund Option A" (EUR 7.5m capex) requires a **sale price**, which doesn't appear anywhere in the draft. Without it, there's no way to check whether Option B actually funds Option A, partially funds it, or doesn't.

4. **"Spa guests spend more" has no number and no source.** This sentence is doing real work (it's the economic case for Option A beyond RevPAR), but it's unsupported. If this comes from the same booking system or survey as the other customer stats, it needs a figure and a citation.

5. **The 18% RevPAR uplift is a correlation across 3 competitors with no source line**, unlike every other data point in the draft (which cite "Quayside booking system, 2025" or "Guest survey n=212, August 2026"). Competitors that chose to add spas may simply have been stronger properties to begin with — the draft doesn't rule this out, and a board will ask.

6. **Seven "key findings," not three to five**, and several don't connect to any option: business travel recovery, staff turnover (32%), and dated rooms all point toward issues the Options section doesn't address (Option C, the obvious response to dated rooms, is explicitly "not costed"). An argument with this many loose threads isn't a governing thought yet — it's a list.

7. **No decision request.** "Align management, then decide" names no decision, no owner, no budget, no date. That's not something a board can act on.

## 2. What you need to supply before this becomes a deck

- **One governing thought** — the actual recommendation this deck is built to defend (not "both are attractive"). If the board itself is meant to choose between A and B, say that explicitly and frame the deck as a decision document, not a recommendation.
- **3–5 key-line statements**, each with its own sourced number, that are the ones actually deciding the recommendation — e.g., something like:
  1. Spa demand: [sourced figure on spend uplift, not just "spa guests spend more"]
  2. Spa economics: EUR 7.5m capex → EUR [corrected total] EBITDA/year across 4 hotels, with Point House estimated
  3. Competitive gap: 18% RevPAR uplift, with its source and a note on selection bias
  4. Westbay/Dunmore: EUR 0.4m EBITDA, EUR [sale price] disposal proceeds, vs. EUR 7.5m need
  5. (if Option C stays in) refurbishment cost estimate, or drop it from this deck
- **The decision request**: what exactly the board is being asked to approve, the budget (EUR 7.5m? less, if Option B only partly funds it?), the owner, and a date.

## 3. Two of your headings, rewritten as action titles (conditional on the above)

- **"Competitive landscape"** → *"Competitors that added spas since 2023 saw an 18% RevPAR uplift — source and selection basis not yet confirmed"* (conditional: needs a citation before it can stand as a board-level claim)
- **"Options"** → *"Option A would add EUR 2.6m EBITDA/year from EUR 7.5m capex — EUR 0.7m of that (Point House) is not yet estimated"* (conditional: needs the Point House estimate or a corrected total)

This is the pattern for the rest: every section heading becomes a sentence carrying a number, once the number is solid.

## 4. Two requests that conflict with how board decks work

- **20 slides.** Board decks run 8–15 main pages — one page per key-line statement plus summary, risks/next steps, and appendix. Twenty pages on an argument this size will dilute it, not strengthen it. Proposed fix: ~10–12 main pages once the argument is settled, with anything else (competitor detail, hotel-by-hotel spa case) moved to the appendix.
- **"Keep my section headings."** Your seven headings (Market overview, Customer analysis, Competitive landscape, Options, Key findings, Recommendation, Next steps) are topic labels — they tell the reader what's discussed, not what was found, so a board reading titles alone learns nothing. Proposed fix: keep them as the section groupings/tracker (so the deck is still organised exactly the way you've structured it), but make each individual slide's title an action title — the finding as a full sentence with its number, as above.

## Turnaround

Once you've got the corrected EBITDA total, the Westbay/Dunmore sale price, a source for the spend and RevPAR figures, and the actual recommendation (or confirmation this is a board-decides-not-management-decides document), send them over and I'll turn the full deck around quickly — this is a structuring job at that point, not a research one. If any of those can't be nailed down tonight, tell me which, and I'll build the deck around the ones that are solid and flag the rest openly on the page rather than paper over them.

