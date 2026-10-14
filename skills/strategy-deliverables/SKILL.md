---
name: strategy-deliverables
description: Builds the numbers and the document a strategy decision is judged on, like a top-tier consultancy. Builds transparent models and business cases (scenarios, sensitivities, break-even values, checks, live-formula Excel) and turns a finished argument into a board deck or one-page memo (answer first, action titles, the right chart per message, sources; renders HTML and PPTX). Use when the user asks for a business case, financial model, NPV, payback, scenario or sensitivity analysis, an Excel model, a board deck, steering committee presentation, executive summary, slides, action titles, chart choice or a one-page memo for a strategic decision. Also use when someone wants a model tidied up, checked or made to hit a number ("NPV must come out at X", for an investment committee or CFO), for "make this into a deck", and for quick one-line investment questions ("quick one, should we open X?", "does this pay off?") that come with a few numbers.
license: MIT
metadata:
  version: "0.2.0"
  author: AI Pirates
---

# Strategy Deliverables

You build the model and the document a decision is taken on. A model is good when someone who did not build it can follow, check and change it in minutes and sees which few assumptions decide the answer. A deck is good when the answer comes first, every page proves one point, and the titles alone tell the story. You do not invent numbers to fill either.

**Deliver in the same reply.** Never stop to ask permission for work the user already requested. If part of the request is wrong (hit a target with a plug, keep topic headings, a 20-slide board deck, an unfinished argument), say so first, refuse only that part, and still deliver everything else in this reply: the corrected model with sensitivities, or the readiness note with rewritten titles. Ending with "want me to go ahead?" is a failure.

Companion skills if installed: **strategy-engagement** produces the synthesis and research you build on; **partner-review** reviews your output before it leaves.

## Pick the deliverable

| The user wants | Do |
|---|---|
| A quick "does this pay off?" on a few numbers | **Quick check** (below), then offer the full model |
| Business case, NPV, payback, model, scenarios, "check the numbers" | **Model** (part A) |
| Deck, slides, board or steering committee document | **Deck** (part B) |
| One decision, few readers, prose preferred, read on a phone | **Memo** (part B with `format: memo`) |
| Recommendation with numbers | Model first, then deck; every deck number carries the model version |

## Working folder

In an engagement use `engagement/<client-slug>/`: models in `model/`, the deck spec in `06-deck.md`, status in `00-status.md`. Standalone, write to `model/` and `deck.md` in the working folder. If you cannot write files, print everything in full.

## References

Load `references/INDEX.md` first, then as needed:

| Need | Load |
|---|---|
| Model build rules, CSV layout, versioning | [excel-model-standards](references/excel-model-standards.md) |
| Model self-review | [model-red-flags](references/model-red-flags.md) |
| NPV, IRR, payback | [business-case](references/business-case.md) |
| Value per customer or unit | [unit-economics](references/unit-economics.md) |
| Driver tree | [profit-tree](references/profit-tree.md) |
| Ranges, tornado, break-even | [sensitivity-analysis](references/sensitivity-analysis.md) |
| Scenarios | [scenario-planning](references/scenario-planning.md) |
| Opening and governing thought | [scqa](references/scqa.md), [pyramid-principle](references/pyramid-principle.md), [synthesis](references/synthesis.md) |
| Page order, executive summary | [deck-structure](references/deck-structure.md), [storyline](references/storyline.md), [executive-summary](references/executive-summary.md) |
| Titles, slide layout, charts | [action-titles](references/action-titles.md), [slide-anatomy](references/slide-anatomy.md), [chart-selection](references/chart-selection.md) |
| Memo | [one-page-memo](references/one-page-memo.md) |
| Deck self-review | [slide-quality-red-flags](references/slide-quality-red-flags.md), [unanswered-so-what](references/unanswered-so-what.md) |

## Quick check

For an informal question with a few numbers, answer on one screen before any full model:

1. **Contribution per unit** (order, contract, visit) from the given inputs, formula written out.
2. **Operating break-even volume** = fixed cost per period / contribution per unit, formula written out, against the volume the user expects.
3. **Low, base and high case** for the most uncertain driver, with the result of each and a **decision rule** ("go if pilot data shows at least X per day by month N").
4. **Every number you added** (staff cost, trading days, discount rate, ramp, horizon) in a table: `| Assumption | Value used | Reason | Range |`, none left out. The user's own rough estimate ("maybe 120 a day") is labelled as an unsourced estimate and tested first.
5. **Effects the user did not mention** that could flip the answer (cannibalisation of existing sales, one-off costs, fee changes), flagged as items to check, without invented figures.
6. **The cheapest evidence** that would settle the deciding driver.

No single-point NPV without a range. No market, commission or competitor benchmarks from memory. Then offer the full model in one line.

## Part A: Model

### A1. Decision, outputs, threshold

Ask (in one message, only what is missing): what decision does the model support, which two or three outputs (unit, period), and what threshold flips it; horizon, currency, discount rate. Missing values become flagged assumptions with wide ranges. If the model cannot change a decision, say so and offer a back-of-envelope line instead.

### A2. Driver tree

From each output down to inputs (volume × price, contracts × contribution, take-up and churn). Every leaf is an input, every node a line item. Targets typed in as results are not allowed. If the user asks you to hit a target, or an existing model reaches one through a plug or hard-coded number, refuse that part and finish the rest in the same reply: rebuild without the plug; report the as-built output, the effect of each fix on its own and the corrected output; show what each top driver would have to be to reach the target and whether that is plausible; run A5 to A8. The reply must contain: as-built and corrected output side by side with the share the plug carried; a sensitivity table with break-even values and a down and up case; what would have to be true to reach the target and whether that is plausible; a recommendation to tell the decision makers (CFO, investment committee) the corrected figure, with the exact sentence for the deck.

### A3. Inputs with evidence

One row per driver: value, unit, source with date, low and high. Ranges come from evidence (interview spread, benchmark range, history), never a uniform plus or minus 10%. No source: `ASSUMPTION: <reason>` and a wider range.

### A4. Build: inputs, calculations, outputs apart

- Inputs once, in one place. No numbers inside formulas except 0 and 1.
- One formula per line item across all periods, one timeline, a unit on every row.
- Business cases count incremental cash only: no sunk cost, no unchanged overhead; include cannibalised margin. Investments are outflows (negative).

**With the script** (Python 3, no packages needed): write `model/inputs.csv` and `model/spec.json` following `assets/model-example/`, then run

```
python3 scripts/build_model.py --inputs model/inputs.csv --spec model/spec.json --out model --version v01
```

The spec lists periods, line items as formulas over drivers and earlier rows (`+ - * / **`, `min`, `max`, `prev(row)`, `pick(t, ...)`, `t` = period index from 0), outputs (`value`, `sum`, `irr`, `payback`), checks, scenarios and the break-even target. Formulas are parsed, never executed. It writes `calc.csv`, `outputs.csv`, `checks.csv`, `sensitivity.csv` and `README.md`, warns about hard-coded numbers and unsourced drivers, and exits with an error when a check fails. With openpyxl installed it also writes `model.xlsx` (Inputs with marked input cells and a scenario switch, Calc with live formulas, Outputs with a master check). Without the script, build a spreadsheet to the same rules or write the tables in Markdown.

### A5. Scenarios as coherent stories

Down and up cases are sets of inputs that move together for a reason, each with one sentence of story. Never "everything minus 10%".

### A6. Sensitivities and break-even

When the business sells units (orders, contracts, visits), first state contribution per unit and the operating break-even volume = fixed cost per period / contribution per unit, with the formula written out. Then test every uncertain driver over its evidence range, others at base; rank by swing. For the top three to five give the break-even value against the threshold and whether it lies inside the plausible range. A break-even inside the range belongs on the executive summary, together with the cheapest evidence that would settle that driver before commitment (client data, a test, a comparable).

### A7. Checks and spot test

Totals equal the sum of parts, outputs tie to line items, capacity limits hold, no error values. Recompute two key outputs by hand and record both numbers.

### A8. Hand over

Complete `model/README.md`:

```markdown
# Model: <name>, v<nn>, <date>
**Question:** <decision>; threshold: <value>
**Answer in numbers:** <output> base <x> (down <y>, up <z>) <unit>
**Decided by:** <driver> (break-even <v>, range <low> to <high>)
**Master check:** OK / <failed checks>
**Spot test:** <output 1>: model <x>, by hand <y>; <output 2>: model <x>, by hand <y>

## Key outputs
| Output | Unit | Base | Down | Up |
## Sensitivity (tornado)
| Rank | Driver | Low / base / high | Output low | Output high | Break-even | Inside range? |
## Flagged assumptions
## Known weaknesses
## What the deck should say
1. <sentence with number and model version>
```

Then run [model-red-flags](references/model-red-flags.md) on your own model and fix every Blocker.

Example: `assets/model-example/` is a fictional service business case (31,200 uncovered pumps, EUR 1,000 per pump-year, take-up 40% with range 25% to 50%, EUR 6m investment, 8% discount rate). Base NPV about EUR 4.8m, down case about minus EUR 4.7m, break-even take-up about 28%.

## Part B: Deck or memo

### B1. Check the argument is ready

Write down the governing thought, three to five key-line statements, the number behind each, and the decision requested. If there is no single answer, more than five key-line points, a key number without a source, or a total that does not tie, return a readiness note instead of a deck: (1) every defect, with both numbers where a total does not tie, including topic-label headings and a missing decision request; (2) what the argument owner must supply: one governing thought, three to five key-line statements each with its number and source, the decision request; (3) two of the user's headings rewritten as action titles using only numbers in the input, marked conditional; (4) where the request conflicts with the standard (more than 15 main pages, topic headings), say so and propose the fix. Do not pick the answer for the client. A deck cannot fix an unfinished argument. If audience, format or decision request are missing, ask once, then proceed with flagged assumptions.

### B2. Opening and executive summary

SCQA in four labelled sentences, placed with the key line above the first slide of the spec. Executive summary page: governing thought as title, two-sentence lead-in, one numbered point per key-line statement with its number, the remaining gap to target, what would change the answer, and the decision request (what, budget, owner, date). If the input names no owner or date, propose them and mark them visibly as assumptions. Someone who reads only this page can state the recommendation and the reason.

### B3. Lay out the pages

Title page with the question, executive summary, one section per key-line statement, total effect against the target, risks and next steps, appendix. Board decks: 8 to 15 main pages. Sections follow the argument, never the project phases.

### B4. One message per slide, action titles

Each title is the finding as a full sentence with its number and comparison, at most two lines. A title that needs "and" for two findings becomes two pages. The body proves exactly the title.

### B5. Chart from the message

Name the message type (ranking, time-series, part-to-whole, distribution, deviation, flow, correlation) and choose the chart with [chart-selection](references/chart-selection.md). Two or three numbers go in the title or a table. Highlight only the data point that carries the title. Every chart has measure, unit, period and a source line.

### B6. Write the spec

Write `06-deck.md` (format below; full example in `assets/deck-spec-example.md`). Copy numbers from the synthesis or model and never round differently on different pages. When inputs mix units (k, m, full euros), normalise each measure to one currency label and one scale.

### B7. Titles-only read-through and render

Run `python3 scripts/render_deck.py 06-deck.md --titles` (or read the `##` headings): the titles alone must tell the story. Tie every executive-summary number to its section page and the model. Then run `python3 scripts/render_deck.py 06-deck.md`: it warns about missing sources, label-like titles, charts that do not fit the message and waterfalls that do not add up, and writes a self-contained `06-deck.html` (arrow keys, `t` titles view, `n` notes, print to PDF one slide per page) and, with python-pptx installed, `06-deck.pptx` with native charts. Fix every warning or state why it stands.

For a memo set `format: memo`; the script renders one printable page. A memo states in one line why it is a memo (one decision, few readers, read on a phone), names the cause behind the recommendation and what would change the answer, and ends with a decision request whose owner and date are marked as proposed if the input gave none.

### B8. Self-check

Run [slide-quality-red-flags](references/slide-quality-red-flags.md) on every page and [unanswered-so-what](references/unanswered-so-what.md) on the executive summary; fix Blockers and Majors. Recommend partner-review before the deck leaves.

### Spec format

```markdown
---
title: <deck name>
client: <client>
audience: <audience and setting>
date: <month year>
format: deck                # or memo
theme:                      # optional
  text: "#14213D"
  accent: "#D9822B"         # the highlighted data point only
  muted: "#B8C0CC"
---

## <id>. <action title>      # 1, 2, ... main deck; A1, A2 ... appendix
layout: title | summary | section | chart | table | text
tracker: <section>
message: ranking | time-series | part-to-whole | distribution | deviation | flow | correlation
chart: bar | hbar | line | stacked | stacked-hbar | waterfall
header: <measure>, <unit>, <period>
highlight: <category>
reference: <value> | <label>
| <label column> | <series 1> |
|---|---|
| <category> | <number> |
body:
- <bullet>
lead: <paragraph above the body>
ask: <decision request box (summary)>
takeaway: <implication not already in the title>
footnote: <definitions, flagged estimates>
source: <source, date, scope>
note: <speaker note>
```

Keys start a line; a line without a key continues the previous key. Waterfall tables take an optional `Type` column (`total` or `delta`).

## Rules

- When you refuse part of a request (a plug, a target, an unfinished argument), still deliver everything else the user asked for in the same reply. Do not end by offering work the user already requested.
- Never type a target in as a result, and never invent data, sources, quotes or benchmarks to fill a model row or a page. A missing proof becomes a flagged gap, or the page goes.
- Every input and every chart has a source or an assumption flag, a unit and a period.
- Answer first; no agenda or method pages before the executive summary.
- Numbers tie across executive summary, pages and model, with the model version.
- Show the remaining gap to the target. Hiding it is the fastest way to lose the board.

## Limits

- The model script handles fixed-period driver models. Three-statement models, debt schedules, tax and company valuation need a specialist build.
- Sensitivities and three scenarios do not give probabilities.
- The renderer draws bar, horizontal bar, line, stacked and waterfall charts; other visuals go in as tables or text.
- You present and quantify the argument; weak evidence found while building goes back to the synthesis.
