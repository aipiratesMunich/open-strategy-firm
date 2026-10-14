#!/usr/bin/env python3
"""Create pr-02-model.xlsx with planted defects (fictional data). Needs openpyxl."""

from pathlib import Path

import openpyxl

wb = openpyxl.Workbook()
inp = wb.active
inp.title = "Inputs"
rows = [
    ("Driver", "Value", "Unit", "Source"),
    ("Orders 2026", 9000, "orders", "Brightwell sales data 2026"),
    ("Order growth p.a.", 0.12, "%", "Management estimate"),
    ("Average order value", 210, "EUR", "Brightwell sales data 2026"),
    ("Contribution margin", 0.32, "%", "Catering P&L 2026"),
    ("Kitchen investment", 1200000, "EUR", "Supplier quote"),
    ("Discount rate", 0.09, "%", "Group finance"),
]
for r in rows:
    inp.append(r)

calc = wb.create_sheet("Calc")
years = [2026, 2027, 2028, 2029, 2030, 2031]
calc.append(["Line"] + years)
calc["A3"] = "Orders"
calc["B3"] = "=Inputs!B2"
calc["A4"] = "Average order value"
calc["A5"] = "Revenue"
calc["A6"] = "Contribution"
calc["A12"] = "Investment"
calc["A13"] = "Net cash flow"
cols = "BCDEFG"
for i, col in enumerate(cols):
    if i > 0:
        prev = cols[i - 1]
        calc["{}3".format(col)] = "={}3*(1+Inputs!$B$3)".format(prev)
    calc["{}4".format(col)] = "=Inputs!$B$4"
    if i == 0:
        calc["B5"] = "=B3*B4"
    elif i == 1:
        calc["C5"] = "=C3*C4"
    else:
        # D1: hard-coded growth instead of input-driven orders
        calc["{}5".format(col)] = "={}5*1.18".format(cols[i - 1])
    calc["{}6".format(col)] = "={}5*Inputs!$B$5".format(col)
    # D6: investment entered positive, then subtracted below
    calc["{}12".format(col)] = "=Inputs!$B$6" if i == 1 else 0
    calc["{}13".format(col)] = "={}6+{}12".format(col, col)

out = wb.create_sheet("Outputs")
out["A1"] = "Revenue 2031"
out["B1"] = "=Calc!G5"
out["A2"] = "NPV 2027-2031"
out["B2"] = "=NPV(Inputs!B7,Calc!C13:G13)"

old = wb.create_sheet("Old")
old["A1"] = "Revenue (v1, lower case)"
old["B1"] = "=Calc!B5*1.05"
old.sheet_state = "hidden"

wb.save(Path(__file__).with_name("pr-02-model.xlsx"))
print("wrote pr-02-model.xlsx")
