# db-01: Board deck from a finished synthesis

## Prompt

> Turn the Fernhill synthesis into the board pre-read deck for 10 December.

Input file: `db-01-synthesis.md`

*Fictional company. All figures invented for evaluation.*

## What this case tests

The happy path: a finished argument with one governing thought, four key-line points, numbers with sources and a decision request. The skill should produce a spec in its format with SCQA, an executive summary first, one message per slide, action titles, charts chosen from the message, a source on every chart, the remaining gap shown, and a titles-only read-through.

## Reference values

- 58.0 + 3.1 + 2.4 + 1.2 = 64.7; remaining gap to EUR 66.0m = EUR 1.3m.
- Premium price: EUR 4 x 25,000 x 12 = EUR 1.2m before churn.
- Off-peak: 10,800 x EUR 24 x 12 = about EUR 3.1m.

## Pass criteria

- Must: uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch in the synthesis to its owner.
- Must: writes `06-deck.md` (or prints it) in the skill's spec format with frontmatter, an SCQA opening in four sentences and the key line above the first slide.
- Must: page 2 (after the title page) is the executive summary: governing thought as title, one point per key-line statement with its number, the remaining EUR 1.3m gap, what would change the answer, and the decision request with EUR 1.9m, owner (COO), start date.
- Must: every main-page title is a full-sentence finding with a number or comparison; no title is a topic label ("Utilisation", "Market overview", "Next steps").
- Must: 8 to 15 main pages, sections following the key line (not project phases), new-city analysis included as a finding (not hidden).
- Must: utilisation by time band shown as a bar chart (or equivalent) with the 10 am to 4 pm band highlighted; the revenue bridge shown as a waterfall from 58.0 to 64.7 with the 66.0 target as a reference and the 1.3 gap visible.
- Must: every chart has a header (measure, unit, period) and a source line taken from the synthesis.
- Must: numbers tie across executive summary, section pages and bridge (no rounding drift, e.g. not 6.5 or 6.8 for the sum).
- Must: a titles-only read-through is listed, and it tells the story in order.
- Must: if Python is available, runs `render_deck.py` and reports its warnings; otherwise says the spec is delivered unrendered.
- Must not: add new analysis, new numbers, competitor facts or sources not in the synthesis.
- Must not: put agenda, method or background pages before the executive summary.
