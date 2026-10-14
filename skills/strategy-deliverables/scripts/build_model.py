#!/usr/bin/env python3
"""Build a transparent driver model from an inputs CSV and a model spec.

Reads:
  inputs.csv  columns: driver, value, unit, source, low, high
              (optional extra columns such as owner, date, note are kept)
  spec.json   periods, line items as formulas over drivers and earlier rows,
              key outputs, checks, scenarios and the break-even target

Writes to --out (default: ./model):
  calc.csv         every line item by period (base case)
  outputs.csv      key outputs for base, down and up scenarios
  checks.csv       each check with its result
  sensitivity.csv  one-way low/high per driver, tornado rank, break-even
  README.md        what the model answers, inputs, formulas, results, flags
  model.xlsx       only if openpyxl is installed: Inputs (marked input cells,
                   scenario switch), Calc (live formulas), Outputs, Checks

Formulas are parsed, never executed: allowed are numbers, driver names,
names of earlier line items, t (period index, 0 for the first period),
the operators + - * / ** and the functions min(), max(), prev(row)
(value of a row in the previous period, 0 in the first period) and
pick(i, a, b, ...) (the i-th argument counting from 0, the last one
when i is beyond the end).

Standard library only. Exit code 1 when a check fails or the spec is invalid.

Example:
  python3 build_model.py --inputs assets/model-example/inputs.csv \\
      --spec assets/model-example/spec.json --out model
"""

import argparse
import ast
import csv
import json
import math
import sys
from pathlib import Path

FUNCS = {"min", "max", "prev", "pick"}
TOL = 1e-9


class ModelError(Exception):
    pass


# ---------------------------------------------------------------- loading

def num(text, field, driver):
    text = (text or "").strip().replace(",", "")
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        raise ModelError("driver '{}': {} '{}' is not a number".format(driver, field, text))


def load_inputs(path):
    drivers = {}
    order = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        need = {"driver", "value", "unit", "source", "low", "high"}
        missing = need - set(reader.fieldnames or [])
        if missing:
            raise ModelError("inputs CSV lacks columns: " + ", ".join(sorted(missing)))
        for row in reader:
            name = (row.get("driver") or "").strip()
            if not name or name.startswith("#"):
                continue
            if not name.isidentifier():
                raise ModelError("driver name '{}' must be letters, digits, underscore".format(name))
            if name in drivers:
                raise ModelError("driver '{}' defined twice".format(name))
            value = num(row["value"], "value", name)
            if value is None:
                raise ModelError("driver '{}' has no value".format(name))
            drivers[name] = {
                "value": value,
                "unit": (row.get("unit") or "").strip(),
                "source": (row.get("source") or "").strip(),
                "low": num(row.get("low"), "low", name),
                "high": num(row.get("high"), "high", name),
            }
            order.append(name)
    if not drivers:
        raise ModelError("inputs CSV has no drivers")
    return drivers, order


def validate_expr(expr, label, drivers, earlier, all_rows):
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise ModelError("{}: cannot parse '{}' ({})".format(label, expr, exc.msg))
    constants = []

    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.BinOp):
            if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
                raise ModelError("{}: operator not allowed in '{}'".format(label, expr))
            walk(node.left)
            walk(node.right)
            return
        if isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.USub, ast.UAdd)):
                raise ModelError("{}: operator not allowed in '{}'".format(label, expr))
            walk(node.operand)
            return
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ModelError("{}: only numeric constants allowed".format(label))
            if node.value not in (0, 1):
                constants.append(node.value)
            return
        if isinstance(node, ast.Name):
            if node.id == "t" or node.id in drivers or node.id in earlier:
                return
            if node.id in all_rows:
                raise ModelError("{}: '{}' is defined later; reorder rows or use prev()".format(label, node.id))
            raise ModelError("{}: unknown name '{}'".format(label, node.id))
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in FUNCS or node.keywords:
                raise ModelError("{}: only min, max, prev, pick may be called".format(label))
            fn = node.func.id
            if fn == "prev":
                if len(node.args) != 1 or not isinstance(node.args[0], ast.Name) or node.args[0].id not in all_rows:
                    raise ModelError("{}: prev() takes one line-item name".format(label))
                return
            if fn == "pick" and len(node.args) < 2:
                raise ModelError("{}: pick() needs an index and at least one value".format(label))
            if fn in ("min", "max") and len(node.args) < 2:
                raise ModelError("{}: {}() needs at least two arguments".format(label, fn))
            for arg in node.args:
                walk(arg)
            return
        raise ModelError("{}: element '{}' not allowed in '{}'".format(label, type(node).__name__, expr))

    walk(tree)
    return tree.body, constants


def load_spec(path, drivers):
    spec = json.loads(Path(path).read_text(encoding="utf-8"))
    periods = [str(p) for p in spec.get("periods", [])]
    if not periods:
        raise ModelError("spec needs a non-empty 'periods' list")
    rows = spec.get("rows", [])
    names = [r.get("name", "") for r in rows]
    all_rows = set(names)
    if len(all_rows) != len(names):
        raise ModelError("duplicate line-item names in spec")
    clash = all_rows & set(drivers)
    if clash or "t" in all_rows or "t" in drivers:
        raise ModelError("names used both as driver and line item (or 't'): " + ", ".join(sorted(clash | ({"t"} & (all_rows | set(drivers))))))
    warnings = []
    earlier = set()
    for r in rows:
        if not str(r.get("name", "")).isidentifier():
            raise ModelError("line item name '{}' is not a valid identifier".format(r.get("name")))
        r["ast"], consts = validate_expr(r["expr"], "row " + r["name"], drivers, earlier, all_rows)
        if consts:
            warnings.append("row {}: hard-coded number(s) {} in formula; move to inputs".format(r["name"], consts))
        earlier.add(r["name"])
    for c in spec.get("checks", []):
        c["ast"], _ = validate_expr(c["expr"], "check " + c["name"], drivers, all_rows, all_rows)
        if c.get("rule", ">=0") not in (">=0", "<=0", "==0"):
            raise ModelError("check {}: rule must be >=0, <=0 or ==0".format(c["name"]))
    for o in spec.get("outputs", []):
        if o.get("row") not in all_rows:
            raise ModelError("output {}: unknown row '{}'".format(o.get("name"), o.get("row")))
        if o.get("fn") not in ("value", "sum", "irr", "payback"):
            raise ModelError("output {}: fn must be value, sum, irr or payback".format(o.get("name")))
        if o["fn"] == "value" and str(o.get("period")) not in periods:
            raise ModelError("output {}: period '{}' not in periods".format(o.get("name"), o.get("period")))
    for scen, overrides in spec.get("scenarios", {}).items():
        for d in overrides:
            if d not in drivers:
                raise ModelError("scenario {}: unknown driver '{}'".format(scen, d))
    return spec, periods, warnings


# ---------------------------------------------------------------- evaluation

def evaluate(node, env, prev_vals, label):
    if isinstance(node, ast.BinOp):
        a = evaluate(node.left, env, prev_vals, label)
        b = evaluate(node.right, env, prev_vals, label)
        op = type(node.op)
        if op is ast.Add:
            return a + b
        if op is ast.Sub:
            return a - b
        if op is ast.Mult:
            return a * b
        if op is ast.Div:
            if b == 0:
                raise ModelError("{}: division by zero".format(label))
            return a / b
        try:
            return float(a) ** b
        except (OverflowError, ZeroDivisionError) as exc:
            raise ModelError("{}: {}".format(label, exc))
    if isinstance(node, ast.UnaryOp):
        v = evaluate(node.operand, env, prev_vals, label)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.Constant):
        return float(node.value)
    if isinstance(node, ast.Name):
        return env[node.id]
    fn = node.func.id
    if fn == "prev":
        return prev_vals.get(node.args[0].id, 0.0)
    args = [evaluate(a, env, prev_vals, label) for a in node.args]
    if fn == "min":
        return min(args)
    if fn == "max":
        return max(args)
    idx = int(round(args[0]))
    values = args[1:]
    return values[max(0, min(idx, len(values) - 1))]


def run(spec, periods, values):
    """Return {row: [value per period]} and check results for one set of driver values."""
    calc = {r["name"]: [] for r in spec["rows"]}
    prev_vals = {}
    check_vals = {c["name"]: [] for c in spec.get("checks", [])}
    for t, label in enumerate(periods):
        env = dict(values)
        env["t"] = float(t)
        current = {}
        for r in spec["rows"]:
            v = evaluate(r["ast"], env, prev_vals, "row {} in {}".format(r["name"], label))
            if isinstance(v, complex) or math.isnan(v) or math.isinf(v):
                raise ModelError("row {} in {}: result is not a finite number".format(r["name"], label))
            env[r["name"]] = v
            current[r["name"]] = v
            calc[r["name"]].append(v)
        for c in spec.get("checks", []):
            check_vals[c["name"]].append(evaluate(c["ast"], env, prev_vals, "check " + c["name"]))
        prev_vals = current
    return calc, check_vals


def irr(flows):
    def npv(rate):
        return sum(cf / (1 + rate) ** i for i, cf in enumerate(flows))
    lo, hi = -0.99, 10.0
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def outputs_for(spec, periods, calc):
    result = {}
    for o in spec.get("outputs", []):
        series = calc[o["row"]]
        fn = o["fn"]
        if fn == "value":
            result[o["name"]] = series[periods.index(str(o["period"]))]
        elif fn == "sum":
            result[o["name"]] = sum(series)
        elif fn == "irr":
            result[o["name"]] = irr(series)
        else:  # payback: first period where the (cumulative) row is >= 0
            hit = [p for p, v in zip(periods, series) if v >= -TOL]
            result[o["name"]] = hit[0] if hit else None
    return result


def output_value(spec, periods, values, name):
    calc, _ = run(spec, periods, values)
    return outputs_for(spec, periods, calc)[name]


def break_even(spec, periods, base_values, driver, out_name, target):
    def f(x):
        vals = dict(base_values)
        vals[driver] = x
        try:
            v = output_value(spec, periods, vals, out_name)
        except ModelError:
            return None
        return None if v is None else v - target

    base = base_values[driver]
    f0 = f(base)
    if f0 is None:
        return None
    if abs(f0) < TOL:
        return base
    span = max(abs(base) * 0.05, 1e-6)
    prev_pts = {1: (base, f0), -1: (base, f0)}
    for k in range(40):
        for sign in (1, -1):
            x = base + sign * span * (1.5 ** k)
            fx = f(x)
            px, pf = prev_pts[sign]
            if fx is not None and pf is not None and pf * fx <= 0:
                lo, hi, flo = (px, x, pf)
                for _ in range(100):
                    mid = (lo + hi) / 2
                    fm = f(mid)
                    if fm is None:
                        break
                    if flo * fm <= 0:
                        hi = mid
                    else:
                        lo, flo = mid, fm
                return (lo + hi) / 2
            prev_pts[sign] = (x, fx)
    return None


# ---------------------------------------------------------------- formatting

def fmt(v, digits=4):
    if v is None:
        return "none"
    if isinstance(v, str):
        return v
    if abs(v) >= 1000:
        return "{:,.0f}".format(v)
    return "{:.{}g}".format(v, digits)


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def plain(v):
    if v is None:
        return ""
    if isinstance(v, float):
        v = round(v, 10)
        return repr(v if v != 0 else 0.0)
    return v


def is_assumption(source):
    return source == "" or source.lower().startswith("assumption")


# ---------------------------------------------------------------- xlsx

def col(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def to_excel(node, ctx):
    """Translate a validated AST to an Excel formula fragment."""
    if isinstance(node, ast.BinOp):
        ops = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.Pow: "^"}
        return "({}{}{})".format(to_excel(node.left, ctx), ops[type(node.op)], to_excel(node.right, ctx))
    if isinstance(node, ast.UnaryOp):
        return "({}{})".format("-" if isinstance(node.op, ast.USub) else "+", to_excel(node.operand, ctx))
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.Name):
        if node.id == "t":
            return "{}$1".format(ctx["col"])
        if node.id in ctx["driver_cell"]:
            return ctx["driver_cell"][node.id]
        return "{}{}".format(ctx["col"], ctx["row_of"][node.id])
    fn = node.func.id
    if fn == "prev":
        if ctx["pcol"] is None:
            return "0"
        return "{}{}".format(ctx["pcol"], ctx["row_of"][node.args[0].id])
    args = [to_excel(a, ctx) for a in node.args]
    if fn in ("min", "max"):
        return "{}({})".format(fn.upper(), ",".join(args))
    n = len(args) - 1
    return "CHOOSE(MAX(1,MIN({}+1,{})),{})".format(args[0], n, ",".join(args[1:]))


def write_xlsx(path, spec, periods, drivers, order, scen_values, results, sens, be_info):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill

    blue = Font(color="0000CC")
    bold = Font(bold=True)
    fill = PatternFill("solid", fgColor="FFF2CC")
    wb = Workbook()

    ws = wb.active
    ws.title = "Inputs"
    scen_names = ["base"] + [s for s in ("down", "up") if s in spec.get("scenarios", {})]
    ws["A1"] = "Scenario switch (1 = base" + "".join(", {} = {}".format(i + 2, s) for i, s in enumerate(scen_names[1:])) + ")"
    ws["A1"].font = bold
    ws["B1"] = 1
    ws["B1"].font = blue
    ws["B1"].fill = fill
    ws["A2"] = "Legend: blue on yellow = input cell; black = formula. Live value follows the switch."
    header = ["Driver", "Unit", "Live value", "Base"] + [s.capitalize() for s in scen_names[1:]] + ["Low", "High", "Source"]
    for j, h in enumerate(header):
        ws.cell(row=4, column=j + 1, value=h).font = bold
    driver_cell = {}
    for i, name in enumerate(order):
        r = 5 + i
        d = drivers[name]
        ws.cell(row=r, column=1, value=name)
        ws.cell(row=r, column=2, value=d["unit"])
        cells = []
        for k, s in enumerate(scen_names):
            c = ws.cell(row=r, column=4 + k, value=scen_values[s][name])
            c.font, c.fill = blue, fill
            cells.append("{}{}".format(col(3 + k), r))
        ws.cell(row=r, column=3, value="=CHOOSE($B$1,{})".format(",".join(cells)))
        base_col = 4 + len(scen_names)
        for k, key in enumerate(("low", "high")):
            if d[key] is not None:
                c = ws.cell(row=r, column=base_col + k, value=d[key])
                c.font, c.fill = blue, fill
        ws.cell(row=r, column=base_col + 2, value=d["source"] or "ASSUMPTION, no source")
        driver_cell[name] = "Inputs!$C${}".format(r)

    wc = wb.create_sheet("Calc")
    wc["A1"] = "period index t"
    wc["A2"] = "Line item"
    wc["B2"] = "Unit"
    wc["C2"] = "Formula (spec)"
    for c in ("A2", "B2", "C2"):
        wc[c].font = bold
    first = 3
    for j, p in enumerate(periods):
        wc.cell(row=1, column=4 + j, value=j)
        wc.cell(row=2, column=4 + j, value=p).font = bold
    row_of = {}
    for i, r in enumerate(spec["rows"]):
        row_of[r["name"]] = first + i
    checks = spec.get("checks", [])
    check_row0 = first + len(spec["rows"]) + 1
    for c_i, c in enumerate(checks):
        row_of["__check_" + c["name"]] = check_row0 + c_i
    items = [(r["name"], r.get("unit", ""), r["expr"], r["ast"], row_of[r["name"]]) for r in spec["rows"]]
    items += [("check: " + c["name"], "must be " + c.get("rule", ">=0"), c["expr"], c["ast"], row_of["__check_" + c["name"]]) for c in checks]
    for label, unit, expr, tree, rr in items:
        wc.cell(row=rr, column=1, value=label)
        wc.cell(row=rr, column=2, value=unit)
        wc.cell(row=rr, column=3, value=expr)
        for j in range(len(periods)):
            ctx = {"col": col(3 + j), "pcol": col(2 + j) if j else None, "row_of": row_of, "driver_cell": driver_cell}
            wc.cell(row=rr, column=4 + j, value="=" + to_excel(tree, ctx))
    last = col(3 + len(periods) - 1)
    status_col = 4 + len(periods)
    status_cells = []
    if checks:
        wc.cell(row=check_row0 - 1, column=1, value="Checks").font = bold
        wc.cell(row=check_row0 - 1, column=status_col, value="Status").font = bold
    for c in checks:
        rr = row_of["__check_" + c["name"]]
        rng = "D{0}:{1}{0}".format(rr, last)
        rule = c.get("rule", ">=0")
        cond = {">=0": "MIN({})>=-1E-9", "<=0": "MAX({})<=1E-9", "==0": "AND(MIN({0})>=-1E-6,MAX({0})<=1E-6)"}[rule].format(rng)
        wc.cell(row=rr, column=status_col, value='=IF({},"OK","FAIL")'.format(cond))
        status_cells.append("Calc!{}{}".format(col(status_col - 1), rr))

    wo = wb.create_sheet("Outputs")
    wo["A1"] = "Master check (failed checks, 0 = OK)"
    wo["A1"].font = bold
    wo["B1"] = '=COUNTIF({},"FAIL")'.format(",".join(status_cells)) if status_cells else 0
    if len(status_cells) > 1:
        wo["B1"] = "=" + "+".join('COUNTIF({},"FAIL")'.format(s) for s in status_cells)
    wo["A3"], wo["B3"], wo["C3"] = "Output (live, current scenario)", "Value", "Unit"
    for c in ("A3", "B3", "C3"):
        wo[c].font = bold
    for i, o in enumerate(spec.get("outputs", [])):
        rr = row_of[o["row"]]
        rng = "Calc!$D${0}:${1}${0}".format(rr, last)
        if o["fn"] == "value":
            f = "=Calc!{}{}".format(col(3 + periods.index(str(o["period"]))), rr)
        elif o["fn"] == "sum":
            f = "=SUM({})".format(rng)
        elif o["fn"] == "irr":
            f = '=IFERROR(IRR({}),"none")'.format(rng)
        else:
            f = '=IFERROR(INDEX(Calc!$D$2:${0}$2,MATCH(TRUE,INDEX({1}>=0,0),0)),"none")'.format(last, rng)
        wo.cell(row=4 + i, column=1, value=o.get("label", o["name"]))
        wo.cell(row=4 + i, column=2, value=f)
        wo.cell(row=4 + i, column=3, value=o.get("unit", ""))
    r0 = 6 + len(spec.get("outputs", []))
    wo.cell(row=r0, column=1, value="Scenario results and sensitivity below are values written by build_model.py, not live formulas.").font = bold
    wo.cell(row=r0 + 1, column=1, value="Output")
    for k, s in enumerate(scen_names):
        wo.cell(row=r0 + 1, column=2 + k, value=s)
    for i, o in enumerate(spec.get("outputs", [])):
        wo.cell(row=r0 + 2 + i, column=1, value=o.get("label", o["name"]))
        for k, s in enumerate(scen_names):
            wo.cell(row=r0 + 2 + i, column=2 + k, value=results[s][o["name"]])

    wsn = wb.create_sheet("Sensitivity")
    wsn["A1"] = "One-way sensitivity on {} (values from build_model.py, not live). Break-even target: {}".format(be_info["output"], be_info["target"])
    hdr = ["rank", "driver", "unit", "low", "base", "high", "output_low", "output_base", "output_high", "swing", "break_even", "break_even_in_range"]
    for j, h in enumerate(hdr):
        wsn.cell(row=3, column=j + 1, value=h).font = bold
    for i, row in enumerate(sens):
        for j, v in enumerate(row):
            wsn.cell(row=4 + i, column=j + 1, value=v)
    for sheet in wb.worksheets:
        sheet.column_dimensions["A"].width = 34
        sheet.column_dimensions["C"].width = 16
    wc.column_dimensions["C"].width = 48
    wb.save(path)


# ---------------------------------------------------------------- main

def main(argv):
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        epilog=__doc__.split("\n\n", 1)[1],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--inputs", required=True, help="inputs CSV: driver, value, unit, source, low, high")
    ap.add_argument("--spec", required=True, help="model spec JSON")
    ap.add_argument("--out", default="model", help="output folder (default: model)")
    ap.add_argument("--version", default="v01", help="model version label for README (default: v01)")
    ap.add_argument("--no-xlsx", action="store_true", help="skip model.xlsx even if openpyxl is installed")
    args = ap.parse_args(argv)

    try:
        drivers, order = load_inputs(args.inputs)
        spec, periods, warnings = load_spec(args.spec, drivers)
        base_values = {k: d["value"] for k, d in drivers.items()}
        scen_values = {"base": base_values}
        for s, over in spec.get("scenarios", {}).items():
            v = dict(base_values)
            v.update({k: float(x) for k, x in over.items()})
            scen_values[s] = v
        calcs, checks_out, results = {}, {}, {}
        for s, vals in scen_values.items():
            calcs[s], checks_out[s] = run(spec, periods, vals)
            results[s] = outputs_for(spec, periods, calcs[s])

        be = spec.get("break_even", {})
        be_out = be.get("output") or (spec.get("outputs") or [{}])[0].get("name")
        be_target = float(be.get("target", 0))
        out_names = [o["name"] for o in spec.get("outputs", [])]
        if be_out not in out_names:
            raise ModelError("break_even.output '{}' is not a defined output".format(be_out))
        sens, no_range = [], []
        base_out = results["base"][be_out]
        if not isinstance(base_out, (int, float)) or base_out is None:
            raise ModelError("break_even.output must be numeric (value, sum or irr)")
        for name in order:
            d = drivers[name]
            if d["low"] is None or d["high"] is None:
                no_range.append(name)
                continue
            lo_v = dict(base_values, **{name: d["low"]})
            hi_v = dict(base_values, **{name: d["high"]})
            o_lo = output_value(spec, periods, lo_v, be_out)
            o_hi = output_value(spec, periods, hi_v, be_out)
            swing = abs((o_hi or 0) - (o_lo or 0))
            bev = break_even(spec, periods, base_values, name, be_out, be_target)
            inside = "" if bev is None else ("yes" if min(d["low"], d["high"]) <= bev <= max(d["low"], d["high"]) else "no")
            sens.append([name, d["unit"], d["low"], d["value"], d["high"], o_lo, base_out, o_hi, swing, bev, inside])
        sens.sort(key=lambda r: -r[8])
        sens = [[i + 1] + r for i, r in enumerate(sens)]
    except ModelError as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "calc.csv", ["line_item", "unit"] + periods,
              [[r["name"], r.get("unit", "")] + [plain(v) for v in calcs["base"][r["name"]]] for r in spec["rows"]])
    scen_names = list(scen_values)
    write_csv(out / "outputs.csv", ["output", "unit"] + scen_names + ["model_version"],
              [[o["name"], o.get("unit", "")] + [plain(results[s][o["name"]]) for s in scen_names] + [args.version]
               for o in spec.get("outputs", [])])

    check_rows, failed = [], []
    for c in spec.get("checks", []):
        rule = c.get("rule", ">=0")
        for s in scen_names:
            vals = checks_out[s][c["name"]]
            if rule == ">=0":
                ok, actual = min(vals) >= -TOL, min(vals)
            elif rule == "<=0":
                ok, actual = max(vals) <= TOL, max(vals)
            else:
                actual = max(abs(v) for v in vals)
                ok = actual <= 1e-6
            check_rows.append([c["name"], s, rule, plain(actual), "OK" if ok else "FAIL"])
            if not ok:
                failed.append("{} ({})".format(c["name"], s))
    write_csv(out / "checks.csv", ["check", "scenario", "expected", "actual", "status"], check_rows)
    write_csv(out / "sensitivity.csv",
              ["rank", "driver", "unit", "low", "base", "high", "output_low", "output_base", "output_high", "swing", "break_even", "break_even_in_range"],
              [[plain(v) for v in r] for r in sens])

    assumptions = [n for n in order if is_assumption(drivers[n]["source"])]
    lines = ["# Model: {}, {}".format(spec.get("title", "model"), args.version), ""]
    lines += ["**Question answered:** {}".format(spec.get("question", "NOT STATED, add 'question' to the spec")), ""]
    lines += ["**Master check:** {}".format("OK" if not failed else "FAILED: " + ", ".join(failed)), ""]
    lines += ["## Key outputs", "", "| Output | Unit | " + " | ".join(scen_names) + " |", "|---|---|" + "---|" * len(scen_names)]
    for o in spec.get("outputs", []):
        lines.append("| {} | {} | {} |".format(o.get("label", o["name"]), o.get("unit", ""), " | ".join(fmt(results[s][o["name"]]) for s in scen_names)))
    if spec.get("scenarios"):
        lines += ["", "Scenarios (coherent sets, drivers changed from base):"]
        for s, over in spec["scenarios"].items():
            story = spec.get("scenario_stories", {}).get(s, "")
            lines.append("- **{}**: {}{}".format(s, ", ".join("{} = {}".format(k, fmt(float(v))) for k, v in over.items()),
                                                  " ({})".format(story) if story else ""))
    lines += ["", "## Sensitivity on {} (one-way, others at base; break-even target {})".format(be_out, fmt(be_target)), "",
              "| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |",
              "|---|---|---|---|---|---|---|---|"]
    for r in sens:
        lines.append("| {} | {} | {} / {} / {} {} | {} | {} | {} | {} | {} |".format(
            r[0], r[1], fmt(r[3]), fmt(r[4]), fmt(r[5]), r[2], fmt(r[6]), fmt(r[8]), fmt(r[9]), fmt(r[10]), r[11] or "n/a"))
    if no_range:
        lines += ["", "Drivers without low/high range (not tested): " + ", ".join(no_range)]
    lines += ["", "## Inputs", "", "| Driver | Value | Unit | Low | High | Source |", "|---|---|---|---|---|---|"]
    for n in order:
        d = drivers[n]
        lines.append("| {} | {} | {} | {} | {} | {} |".format(n, fmt(d["value"]), d["unit"], fmt(d["low"]) if d["low"] is not None else "",
                                                             fmt(d["high"]) if d["high"] is not None else "", d["source"] or "**ASSUMPTION, no source**"))
    lines += ["", "## Line items (calculation order)", "", "| Line item | Unit | Formula |", "|---|---|---|"]
    for r in spec["rows"]:
        lines.append("| {} | {} | `{}` |".format(r["name"], r.get("unit", ""), r["expr"]))
    lines += ["", "## Checks", "", "| Check | Scenario | Expected | Actual | Status |", "|---|---|---|---|---|"]
    for c in check_rows:
        lines.append("| {} | {} | {} | {} | {} |".format(c[0], c[1], c[2], fmt(float(c[3])) if c[3] != "" else "", c[4]))
    lines += ["", "## Flags", ""]
    flags = ["Drivers flagged as assumptions (no source or source starts with 'assumption'): " + (", ".join(assumptions) or "none")]
    flags += warnings
    flags += ["No range for: " + ", ".join(no_range)] if no_range else []
    lines += ["- " + f for f in flags]
    lines += ["", "## Files", "",
              "- `calc.csv`: every line item by period, base case",
              "- `outputs.csv`: key outputs per scenario",
              "- `checks.csv`: check results per scenario",
              "- `sensitivity.csv`: tornado ranking and break-even values"]

    xlsx_msg = "model.xlsx skipped (--no-xlsx)"
    if not args.no_xlsx:
        try:
            import openpyxl  # noqa: F401
        except ImportError:
            xlsx_msg = "model.xlsx skipped: openpyxl not installed (pip install openpyxl); CSV files are complete"
        else:
            write_xlsx(out / "model.xlsx", spec, periods, drivers, order, scen_values, results,
                       [[plain(v) for v in r] for r in sens], {"output": be_out, "target": be_target})
            xlsx_msg = "model.xlsx written (Inputs with scenario switch, Calc with live formulas, Outputs, Sensitivity)"
            lines.append("- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)")
    (out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("wrote {}: calc.csv, outputs.csv, checks.csv, sensitivity.csv, README.md".format(out))
    print(xlsx_msg)
    for w in warnings:
        print("WARNING: " + w)
    if assumptions:
        print("FLAG: drivers without source: " + ", ".join(assumptions))
    for o in spec.get("outputs", []):
        print("  {:<28} {}".format(o["name"], " | ".join("{}={}".format(s, fmt(results[s][o["name"]])) for s in scen_names)))
    if sens:
        print("  top drivers on {}: {}".format(be_out, ", ".join("{} (break-even {})".format(r[1], fmt(r[10])) for r in sens[:3])))
    if failed:
        print("CHECK FAILED: " + ", ".join(failed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
