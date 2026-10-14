#!/usr/bin/env python3
"""Print the outline of a .pptx deck: slide number, title, then body text.

Use it for the titles-only read-through: do the titles alone tell the story?
Standard library only.

Usage:
    python3 pptx_outline.py deck.pptx            # titles and body text
    python3 pptx_outline.py deck.pptx --titles   # titles only
"""

import posixpath
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
TITLE_TYPES = {"title", "ctrTitle"}


def slide_paths(z):
    pres = ET.fromstring(z.read("ppt/presentation.xml"))
    rels = ET.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
    targets = {r.get("Id"): r.get("Target") for r in rels.findall("rel:Relationship", NS)}
    paths = []
    for sld in pres.findall("p:sldIdLst/p:sldId", NS):
        rid = sld.get("{%s}id" % NS["r"])
        target = targets.get(rid, "")
        paths.append(posixpath.normpath(posixpath.join("ppt", target)))
    return paths


def shape_text(shape):
    paras = []
    for p in shape.iter("{%s}p" % NS["a"]):
        text = "".join(t.text or "" for t in p.iter("{%s}t" % NS["a"])).strip()
        if text:
            paras.append(text)
    return paras


def read_slide(z, path):
    root = ET.fromstring(z.read(path))
    title, body = "", []
    for shape in root.iter("{%s}sp" % NS["p"]):
        ph = shape.find("p:nvSpPr/p:nvPr/p:ph", NS)
        paras = shape_text(shape)
        if ph is not None and ph.get("type") in TITLE_TYPES and not title:
            title = " ".join(paras)
        else:
            body.extend(paras)
    for frame in root.iter("{%s}graphicFrame" % NS["p"]):
        body.extend(shape_text(frame))
    return title, body


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    titles_only = "--titles" in argv
    with zipfile.ZipFile(argv[0]) as z:
        for i, path in enumerate(slide_paths(z), start=1):
            title, body = read_slide(z, path)
            print("{:>3}. {}".format(i, title or "[NO TITLE]"))
            if not titles_only:
                for line in body:
                    print("       {}".format(line))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
