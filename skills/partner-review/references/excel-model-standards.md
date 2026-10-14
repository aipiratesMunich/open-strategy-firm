# Excel Model Standards

## What it is

The build rules for any numbers model behind a recommendation: business case, market sizing, pricing effect, scenario model. The goal is a model that a person who did not build it can follow, check and change in minutes. The same structure applies when no spreadsheet tool is available and the model is built as CSV files plus a short script.

## When NOT to use

- **A back-of-envelope estimate** with three or four inputs. Write it as a calculation line in the document, with each assumption stated (market sizing). A full model structure adds nothing.
- **Pure data analysis** (cleaning an export, a pivot of sales by region). Use an analysis notebook or table; keep raw data and steps reproducible, but the input-calculation-output layout is overkill.
- **Integrated three-statement or debt models** for financing or valuation. These standards are the floor; such models also need balance-sheet and cash-flow integrity rules beyond this note. Flag the need for a specialist.

## Standard

**Structure**
- **Inputs, calculations and outputs are separate**: separate sheets, or clearly separated blocks in a small model. Inputs appear once; everything else refers to them.
- **No hard-coded numbers in formulas.** Constants like 12 months or 1,000 go to inputs with a label.
- **One direction of flow**: inputs feed calculations, calculations feed outputs. No circular references unless documented and switchable.
- **One formula per row.** Each row is one line item with one formula copied across all periods. No exceptions hidden in single cells.
- **One timeline** in the same columns on every calculation sheet, with period labels and a flag for actuals versus forecast.
- **Units on every row** (EUR m, pumps, %), one unit convention per model.
- **Short formulas.** Split long nested formulas into helper rows that can be read.

**Transparency**
- **Colour code by cell role**, with a legend on the cover: inputs in one colour (commonly blue font or a pale fill), formulas black, links to other sheets in a third colour. Never colour by taste.
- **Every input has** a source or reason, date, owner, and a low and high value.
- **No hidden rows, sheets or external links** that change results.

**Integrity**
- **Check block**: totals equal the sum of parts, segments sum to the total, outputs tie to calculation rows, no error values. One master check cell shows OK or the number of failed checks.
- **Sensitivity block**: the three to five most uncertain drivers, each tested low and high, with the effect on the key output and the break-even value of each ([Sensitivity Analysis](sensitivity-analysis.md)).
- **Scenarios** as coherent sets of inputs selected by one switch (scenario planning).

**Versioning**
- File name carries version and date: `<client>_<model>_v<nn>_<yyyy-mm-dd>`.
- A change log on the cover: version, date, author, what changed, effect on key outputs.
- Deck and executive summary state which model version their numbers come from.

These rules follow the published FAST Standard and the ICAEW Financial Modelling Code in substance; both go further on layout detail.

**CSV fallback (no spreadsheet tool)**

When the strategy-deliverables skill cannot write a spreadsheet, it uses the same separation as plain files and a Python standard-library script:

| File | Role | Columns |
|---|---|---|
| `inputs.csv` | All assumptions, one row each | `name, value, low, high, unit, source, owner, date, note` |
| `timeline.csv` | Periods | `period, label, is_actual` |
| `calc.py` | Reads inputs and timeline, computes one line item per function, writes outputs; no numbers in code except 0 and 1 | n/a |
| `calc.csv` | Every line item by period | `line_item, unit, <period 1>, <period 2>, ...` |
| `outputs.csv` | Key outputs for the deck | `output, unit, value, period, model_version` |
| `checks.csv` | Each check and its result | `check, expected, actual, status` |
| `sensitivity.csv` | Driver tests | `driver, low, base, high, output_low, output_base, output_high, break_even` |
| `CHANGELOG.md` | Versions | version, date, what changed, effect on outputs |

The script fails loudly when any check fails. Same rules apply: one formula per line item, inputs only in `inputs.csv`.

## Step by step

1. Write down the question the model answers and the two or three outputs it must produce.
2. Draw the driver tree from output to inputs (unit economics, [Business Case](business-case.md)).
3. Set up the timeline and the input sheet; enter each input with source, range, owner.
4. Build calculations one line item per row, in the order of the driver tree.
5. Build the output sheet with only what the deck needs.
6. Add the check block and make the master check visible on the cover.
7. Add the sensitivity block and scenario switch.
8. Recompute two key outputs by hand. Fix any difference before going further.
9. Version the file, write the change log, and record the version in the deck.
10. Hand it to a second person for review against [Model Red Flags](model-red-flags.md). Authors find few of their own errors.

## Common mistakes

- **Typed-in numbers inside formulas.** Struck because nobody can see or change the assumption, and the sensitivity misses it.
- **Target typed in as a result.** Revenue for 2030 entered as EUR 200m instead of built from volume and price. The model then proves what it assumes.
- **Different formula in one cell of a row.** A manual override in 2029 that nobody remembers. Struck because it silently breaks every copy across.
- **Colour as decoration.** Blue headers and green totals that mean nothing, so the reader cannot tell inputs from formulas.
- **No checks.** Segments that do not add to the total go unnoticed until the client finds them.
- **Version chaos.** "final_v3_new.xlsx" and a deck built from the version before. Struck as a tie-out blocker.
- **Sensitivity on everything by plus or minus 10%.** Hides which driver matters. Test the uncertain ones over their real range.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps service business case, CSV fallback.

`inputs.csv` (extract):

| name | value | low | high | unit | source |
|---|---|---|---|---|---|
| uncovered_pumps | 31200 | | | pumps | ERP export Dec 2025: 52% of 60,000 |
| price_per_pump | 1000 | | | EUR/year | 12 interviews, stated willingness to pay |
| take_up_2030 | 0.40 | 0.25 | 0.50 | share | interviews plus comparable offers |
| investment | 6.0 | | | EUR m | service plan estimate |

`calc.csv` (extract), take-up ramp held in inputs as 10%, 25%, 35%, 40%:

| line_item | unit | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| take_up | share | 0.10 | 0.25 | 0.35 | 0.40 |
| contracts | pumps | 3,120 | 7,800 | 10,920 | 12,480 |
| service_revenue | EUR m | 3.1 | 7.8 | 10.9 | 12.5 |

`checks.csv`: contracts not above uncovered_pumps (OK); service_revenue equals contracts times price divided by one million (OK).

`sensitivity.csv`: take-up 25% gives EUR 7.8m in 2030, 50% gives EUR 15.6m.

Weak version: one sheet, "=31200*0.4*1000" typed into the 2030 cell, no range, file named "service_final.xlsx".

## Output template

```markdown
# Model: <name>, v<nn>, <date>

**Question answered:** <question>
**Key outputs:** <output 1, unit>; <output 2, unit>
**Format:** spreadsheet / CSV fallback

## Inputs
| name | value | low | high | unit | source | owner | date |
|---|---|---|---|---|---|---|---|

## Line items (calculation order)
| line_item | unit | formula in words | depends on |
|---|---|---|---|

## Checks
| check | expected | actual | status |
|---|---|---|---|

## Sensitivity
| driver | low | base | high | output at low | output at base | output at high | break-even |
|---|---|---|---|---|---|---|---|

## Change log
| version | date | author | change | effect on key outputs |
|---|---|---|---|---|
```

## Related

- [Model Red Flags](model-red-flags.md), [Sensitivity Analysis](sensitivity-analysis.md), scenario planning, [Business Case](business-case.md), unit economics, [Weak Evidence](weak-evidence.md)
