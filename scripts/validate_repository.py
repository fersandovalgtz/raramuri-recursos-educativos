from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
REQUIRED = ["README.md", "CITATION.cff", "CHANGELOG.md", "GOVERNANCE.md", "VALIDATION_STATUS.md", "CULTURAL_SAFETY.md", "VARIATION_POLICY.md", "AUDIO_POLICY.md"]
FORBIDDEN_DIRS = {"raw-private", "private-data", "identifiable-data", "datos-identificables", "restricted-cultural-material"}


def fail(message: str) -> None:
    ERRORS.append(message)


for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"Missing required file: {rel}")

citation = ROOT / "CITATION.cff"
if citation.exists():
    text = citation.read_text(encoding="utf-8")
    for field in ("cff-version:", "title:", "authors:", "repository-code:"):
        if field not in text:
            fail(f"CITATION.cff missing field: {field}")

for path in ROOT.rglob("*"):
    if any(part in FORBIDDEN_DIRS for part in path.parts):
        fail(f"Sensitive/private directory must not be committed: {path.relative_to(ROOT)}")

link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
html_pattern = re.compile(r'(?:href|src)=["\']([^"\']+)["\']')
checked_links = 0
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    links = link_pattern.findall(text) + html_pattern.findall(text)
    for raw in links:
        raw = raw.strip().split()[0]
        if raw.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        if not target or target.startswith("/"):
            continue
        checked_links += 1
        if not (md.parent / target).resolve().exists():
            fail(f"Broken local link in {md.relative_to(ROOT)}: {raw}")

csv_count = 0
for csv_path in ROOT.rglob("*.csv"):
    csv_count += 1
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        fail(f"Empty CSV: {csv_path.relative_to(ROOT)}")
        continue
    width = len(rows[0])
    for line_no, row in enumerate(rows[1:], start=2):
        if len(row) != width:
            fail(f"CSV column mismatch: {csv_path.relative_to(ROOT)} line {line_no} ({len(row)} != {width})")

print(f"Validated {len(list(ROOT.rglob('*.md')))} Markdown files, {checked_links} local links and {csv_count} CSV files.")
if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print("Repository validation passed.")
