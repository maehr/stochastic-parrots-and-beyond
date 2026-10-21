#!/usr/bin/env python3
"""Build the Word reference document for the handouts.

The default reference document of Pandoc draws no table borders. The Word
versions of the worksheets need visible cells, so that a participant can type
into them on a laptop. This script copies the default reference document and
adds cell borders and a minimum row height to its default table style.

``contents/handouts/_metadata.yml`` points ``reference-doc`` to the result.
Run the script again after a Quarto update, then run ``npm run handouts:build``.

Usage:
    uv run python scripts/build_reference_docx.py
    uv run python scripts/build_reference_docx.py --landscape
"""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET = REPO_ROOT / "contents" / "handouts" / "_reference.docx"
LANDSCAPE_TARGET = TARGET.with_name("_reference-landscape.docx")

SIDES = ("top", "left", "bottom", "right", "insideH", "insideV")
BORDERS = (
    "<w:tblBorders>"
    + "".join(
        f'<w:{side} w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        for side in SIDES
    )
    + "</w:tblBorders>"
)
# 510 twips is 9 mm. Rows grow when the text needs more space.
ROW_HEIGHT = '<w:trPr><w:trHeight w:val="510" w:hRule="atLeast"/></w:trPr>'

# The schema fixes the order of the elements: tblBorders follows tblInd, and
# trPr follows tblPr.
TABLE_STYLE = re.compile(
    r'(<w:style w:type="table" w:default="1" w:styleId="Table">.*?'
    r"<w:tblInd [^>]*/>)(.*?</w:tblPr>)",
    flags=re.S,
)


def patch(styles: str) -> str:
    patched, count = TABLE_STYLE.subn(
        lambda m: m.group(1) + BORDERS + m.group(2) + ROW_HEIGHT, styles, count=1
    )
    if count != 1:
        raise SystemExit("The default table style of Pandoc has changed.")
    return patched


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--landscape",
        action="store_true",
        help="Create an A4 landscape variant of the existing reference document.",
    )
    args = parser.parse_args()
    if args.landscape:
        # Preserve the shared styles. Change page geometry for wide worksheets.
        with (
            zipfile.ZipFile(TARGET) as source,
            zipfile.ZipFile(LANDSCAPE_TARGET, "w", zipfile.ZIP_DEFLATED) as target,
        ):
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "word/document.xml":
                    document = data.decode("utf-8")
                    geometry = (
                        '<w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>'
                        '<w:pgMar w:top="850" w:right="907" w:bottom="850" '
                        'w:left="907" w:header="425" w:footer="425" w:gutter="0"/>'
                    )
                    document = re.sub(r"<w:pgSz\b[^>]*/>", "", document)
                    document = re.sub(r"<w:pgMar\b[^>]*/>", "", document)
                    document, count = re.subn(
                        r"</w:sectPr>", geometry + "</w:sectPr>", document
                    )
                    if count != 1:
                        raise SystemExit("Expected one reference document section.")
                    data = document.encode("utf-8")
                target.writestr(item, data)
        print(LANDSCAPE_TARGET.relative_to(REPO_ROOT))
        return 0
    with tempfile.TemporaryDirectory() as tmp:
        default = Path(tmp) / "reference.docx"
        subprocess.run(
            [
                "quarto",
                "pandoc",
                "-o",
                str(default),
                "--print-default-data-file",
                "reference.docx",
            ],
            check=True,
        )
        with (
            zipfile.ZipFile(default) as source,
            zipfile.ZipFile(TARGET, "w", zipfile.ZIP_DEFLATED) as target,
        ):
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "word/styles.xml":
                    data = patch(data.decode("utf-8")).encode("utf-8")
                target.writestr(item, data)
    print(TARGET.relative_to(REPO_ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
