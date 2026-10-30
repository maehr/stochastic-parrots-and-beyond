"""Tests that keep the site consistent with the edition model and the files."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

import pytest
from conftest import REPO_ROOT, site_sources

# Edition facts belong in data/editions.yml. A page uses the `edition`
# shortcode instead of a hard-coded copy, so the facts cannot conflict.
HARD_CODED_FACTS = (
    "4 November 2026",
    "November 4, 2026",
    "2026-11-04",
    "Schönbeinstrasse",
    "room 306",
    "7 October 2026",
    "47E7M",
    "evasys.unibas.ch",
)

LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
EVALUATION = re.compile(r"\{\{<\s*edition\s+(\S+)\s+evaluation(?:_url)?\b")
SHORTCODE = re.compile(r"\{\{<\s*edition\b")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


@pytest.mark.parametrize("page", site_sources(), ids=rel)
def test_no_hard_coded_edition_facts(page: Path):
    text = page.read_text(encoding="utf-8")
    found = [fact for fact in HARD_CODED_FACTS if fact in text]
    assert not found, f"{rel(page)} hard-codes {found}. Use the edition shortcode."


@pytest.mark.parametrize("page", site_sources(), ids=rel)
def test_evaluation_link_only_on_its_edition_page(page: Path):
    for eid in EVALUATION.findall(page.read_text(encoding="utf-8")):
        assert rel(page) == f"contents/editions/{eid}.qmd", (
            f"{rel(page)} shows the evaluation link of {eid}. "
            "Only the page of that edition may show it."
        )


def test_slide_decks_are_independent_of_editions():
    for deck in sorted((REPO_ROOT / "contents" / "slides").glob("*.qmd")):
        text = deck.read_text(encoding="utf-8")
        assert not SHORTCODE.search(text), f"{rel(deck)} uses edition facts"


@pytest.mark.parametrize("page", site_sources(), ids=rel)
def test_local_links_resolve(page: Path):
    text = page.read_text(encoding="utf-8")
    # Ignore code blocks: they show link syntax as an example.
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    broken = []
    for target in LINK.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        path = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not path:
            continue
        # A part in _parts/ renders inside its deck, so its links resolve there.
        base = page.parent.parent if page.parent.name == "_parts" else page.parent
        resolved = REPO_ROOT / path.lstrip("/") if path.startswith("/") else base / path
        if not resolved.exists():
            broken.append(target)
    assert not broken, f"{rel(page)} links to missing files: {broken}"


LENSES = {
    "01-scale": "01-scale",
    "02-representation": "02-representation",
    "03-lifecycle-labor": "03-lifecycle-labor",
    "04-political-economy": "04-political-economy",
}

LESSON_ORDER = (
    "Question",
    "Core concepts",
    "Evidence and limits",
    "Case",
    "Activity",
    "Output",
    "Reading",
    "Slides",
)


@pytest.mark.parametrize("lens", sorted(LENSES))
def test_each_lens_has_a_lesson_a_deck_and_guiding_questions(lens: str):
    lesson = REPO_ROOT / "contents" / "lenses" / f"{lens}.qmd"
    deck = REPO_ROOT / "contents" / "slides" / f"{LENSES[lens]}.qmd"
    include = f"_guiding-questions-{lens[:2]}.qmd"
    questions = REPO_ROOT / "contents" / "lenses" / include
    assert lesson.exists(), rel(lesson)
    assert deck.exists(), rel(deck)
    text = lesson.read_text(encoding="utf-8")
    assert f"slides/{LENSES[lens]}.qmd" in text, f"{rel(lesson)} does not link its deck"
    assert include in text, f"{rel(lesson)} does not include its guiding questions"
    items = re.findall(r"^\d+\. ", questions.read_text(encoding="utf-8"), flags=re.M)
    assert len(items) == 4, f"{rel(questions)} must hold four guiding questions"


@pytest.mark.parametrize("lens", sorted(LENSES))
def test_lesson_sections_follow_the_fixed_order(lens: str):
    text = (REPO_ROOT / "contents" / "lenses" / f"{lens}.qmd").read_text(
        encoding="utf-8"
    )
    headings = [h.strip() for h in re.findall(r"^## (.+)$", text, flags=re.M)]
    positions = []
    for name in LESSON_ORDER:
        match = [i for i, h in enumerate(headings) if h.startswith(name)]
        assert match, f"{lens}: section '{name}' is missing"
        positions.append(match[0])
    assert positions == sorted(positions), (
        f"{lens}: sections are out of order: {headings}"
    )


def test_liberating_structures_pages_carry_cc_by_sa():
    pages = [
        REPO_ROOT / "contents" / "panarchy.qmd",
        REPO_ROOT / "contents" / "panarchy-facilitator.qmd",
        REPO_ROOT / "contents" / "slides" / "05-panarchy.qmd",
        REPO_ROOT / "contents" / "slides" / "06-day.qmd",
        *sorted((REPO_ROOT / "contents" / "handouts").glob("panarchy*.qmd")),
        *sorted((REPO_ROOT / "contents" / "handouts").glob("sheet-*.qmd")),
    ]
    for page in pages:
        assert page.exists(), rel(page)
        text = page.read_text(encoding="utf-8")
        assert re.search(r"^license:\s*['\"]?CC BY-SA", text, flags=re.M), (
            f"{rel(page)} adapts Liberating Structures and must carry CC BY-SA 4.0"
        )
        assert "Liberating Structures" in text, f"{rel(page)} lacks the attribution"


@pytest.mark.parametrize("page", site_sources(), ids=rel)
def test_fenced_divs_are_not_indented(page: Path):
    # Prettier indents a closing ":::" that follows a list item without a blank
    # line. Quarto then reads the fence as list text, and the div stays open.
    bad = [
        i + 1
        for i, line in enumerate(page.read_text(encoding="utf-8").splitlines())
        if re.match(r"^\s+:::\s*$", line)
    ]
    assert not bad, (
        f"{rel(page)}: indented ':::' on lines {bad}. Add a blank line before it."
    )


# Issue 12: the Research Use keeps one name all day. The Research Use Card
# defines it. Link targets and file names may still contain "research-use".
LINK_TARGET = re.compile(r"\]\([^)]*\)|\{[^}]*\}")


@pytest.mark.parametrize("page", site_sources(), ids=rel)
def test_research_use_keeps_its_name(page: Path):
    text = LINK_TARGET.sub("", page.read_text(encoding="utf-8"))
    found = re.findall(r"research-use|[Rr]esearch use card|use clinic", text)
    assert not found, f"{rel(page)} renames the Research Use: {found}"
