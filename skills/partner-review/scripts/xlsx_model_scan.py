#!/usr/bin/env python3
"""Scan an .xlsx model for common integrity red flags.

Reports, per sheet:
- formulas that contain hard-coded numbers (other than 0 and 1),
- hidden and very hidden sheets,
- links to external workbooks,
- counts of formulas and typed-in numeric constants.

It reads the file structure only; it does not recalculate. Standard library only.

Usage:
    python3 xlsx_model_scan.py model.xlsx
    python3 xlsx_model_scan.py model.xlsx --limit 50   # max findings listed per sheet
"""

import posixpath
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
STRING = re.compile(r'"[^"]*"')
SHEET_PREFIX = re.compile(r"('[^']+'|[A-Za-z0-9_.]+)!")
NUMBER = re.compile(r"(?<![A-Za-z0-9$_.:])(\d+(?:\.\d+)?%?)(?![\d.]*[A-Za-z_(:])")
TRIVIAL = {"0", "1", "0.0", "1.0"}


def literals(formula):
    cleaned = SHEET_PREFIX.sub("", STRING.sub('""', formula))
    return [n for n in NUMBER.findall(cleaned) if n not in TRIVIAL]


def sheets(z):
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    targets = {r.get("Id"): r.get("Target") for r in rels.findall("rel:Relationship", NS)}
    out = []
    for s in wb.findall("m:sheets/m:sheet", NS):
        target = targets.get(s.get("{%s}id" % NS["r"]), "")
        path = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join("xl", target))
        out.append((s.get("name"), s.get("state", "visible"), path))
    return out


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 25
    total_flags = 0
    with zipfile.ZipFile(argv[0]) as z:
        externals = [n for n in z.namelist() if n.startswith("xl/externalLinks/") and n.endswith(".xml")]
        print("# Model scan: {}\n".format(argv[0]))
        print("External workbook links: {}".format(len(externals) or "none"))
        for name, state, path in sheets(z):
            root = ET.fromstring(z.read(path))
            formulas, constants, flagged = 0, 0, []
            for c in root.iter("{%s}c" % NS["m"]):
                f = c.find("m:f", NS)
                v = c.find("m:v", NS)
                if f is not None and f.text:
                    formulas += 1
                    nums = literals(f.text)
                    if nums:
                        flagged.append((c.get("r"), f.text, nums))
                elif v is not None and c.get("t") in (None, "n"):
                    constants += 1
            total_flags += len(flagged)
            print("\n## Sheet '{}' ({})".format(name, state))
            if state != "visible":
                print("RED FLAG: sheet is {}".format(state))
            print("formulas: {}, typed numeric constants: {}, formulas with hard-coded numbers: {}".format(
                formulas, constants, len(flagged)))
            for ref, text, nums in flagged[:limit]:
                print("  {:<8} ={}   <- {}".format(ref, text, ", ".join(nums)))
            if len(flagged) > limit:
                print("  ... {} more".format(len(flagged) - limit))
    print("\nTotal formulas with hard-coded numbers: {}".format(total_flags))
    print("Note: constants on an input sheet are expected; constants on calculation sheets are not.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
