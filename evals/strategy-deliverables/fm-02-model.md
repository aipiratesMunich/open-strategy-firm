# Halvorsen Instruments: calibration lab business case v5 (spreadsheet export)

*Fictional company. All figures invented for evaluation. Export of the workbook: values and the formula of each cell.*

## Sheet: Inputs

| Cell | Driver | Value | Unit | Source |
|---|---|---|---|---|
| B2 | Calibrations in 2027 | 6,000 | calibrations | 2026 order book plus signed framework contracts |
| B3 | Calibration volume growth | 4% | per year | Sales plan 2027-2031 |
| B4 | Price per calibration | 260 | EUR | 2026 price list |
| B5 | Variable cost per calibration | 120 | EUR | Technician time and consumables, 2026 actuals |
| B6 | Lab fixed cost | 0.35 | EUR m per year | Lease and supervisor |
| B7 | Investment (lab, reference standards) | 2.4 | EUR m | Supplier quote |
| B8 | Discount rate | 8% | per year | Group finance |
| B9 | EUR per EUR m | 1,000,000 | | unit conversion |

## Sheet: Calc

Columns: B = start 2027 (t = 0), C = 2027, D = 2028, E = 2029, F = 2030, G = 2031.

| Row | Line item | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 3 | Calibrations | | `=Inputs!B2` | `=C3*1.07` | `=D3*1.07` | `=E3*1.07` | `=F3*1.07` |
| 4 | Contribution per calibration (EUR) | | `=Inputs!B4-Inputs!B5` | `=Inputs!B4-Inputs!B5` | `=Inputs!B4-Inputs!B5` | `=Inputs!B4-Inputs!B5` | `=Inputs!B4-Inputs!B5` |
| 5 | Contribution (EUR m) | | `=C3*C4/Inputs!B9` | `=D3*D4/Inputs!B9` | `=E3*E4/Inputs!B9` | `=F3*F4/Inputs!B9` | `=G3*G4/Inputs!B9` |
| 6 | Fixed cost (EUR m) | | `=-Inputs!B6` | `=-Inputs!B6` | `=-Inputs!B6` | `=-Inputs!B6` | `=-Inputs!B6` |
| 7 | Adjustment (agreed with CFO) (EUR m) | | 0.75 | 0.75 | 0.75 | 0.75 | 0.75 |
| 8 | Investment (EUR m) | `=-Inputs!B7` | | | | | |
| 9 | Net cash flow (EUR m) | `=B8` | `=SUM(C5:C8)` | `=SUM(D5:D8)` | `=SUM(E5:E8)` | `=SUM(F5:F8)` | `=SUM(G5:G8)` |

## Sheet: Outputs

| Cell | Output | Formula | Value shown |
|---|---|---|---|
| B2 | NPV 2027-2031 (EUR m) | `=Calc!B9+NPV(Inputs!B8,Calc!C9:G9)` | 3.02 |
| B3 | Calibrations 2031 | `=Calc!G3` | 7,865 |
