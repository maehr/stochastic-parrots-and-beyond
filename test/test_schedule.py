"""Tests for data/schedule.yml, the single source of the course day timetable."""

from __future__ import annotations

import importlib.util

import pytest
from conftest import REPO_ROOT

SCRIPT = REPO_ROOT / "scripts" / "build_schedule.py"


def _load_builder():
    spec = importlib.util.spec_from_file_location("build_schedule", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = _load_builder()
build, duration, load, minutes = (
    builder.build,
    builder.duration,
    builder.load,
    builder.minutes,
)


@pytest.fixture(scope="module")
def slots() -> list[dict]:
    return load()


def test_generated_files_are_current():
    stale = [
        str(path.relative_to(REPO_ROOT))
        for path, text in build().items()
        if not path.exists() or path.read_text(encoding="utf-8") != text
    ]
    assert not stale, f"Out of date: {stale}. Run npm run schedule:build."


def test_slots_are_contiguous(slots):
    for prev, slot in zip(slots, slots[1:], strict=False):
        assert prev["end"] == slot["start"], slot["activity"]
        assert duration(slot) > 0, slot["activity"]


def test_schedule_fits_each_confirmed_edition(slots, editions_data):
    for eid, edition in editions_data["editions"].items():
        if edition["start"] is None or edition["end"] is None:
            continue
        assert minutes(slots[0]["start"]) >= minutes(edition["start"]), eid
        assert minutes(slots[-1]["end"]) <= minutes(edition["end"]), eid


def test_every_slot_except_breaks_has_a_lead(slots):
    for slot in slots:
        if slot["format"] == "Break":
            assert not slot.get("lead"), slot["activity"]
        else:
            assert slot.get("lead"), f"{slot['activity']} has no lead"


def test_links_resolve(slots):
    for slot in slots:
        link = slot.get("link")
        if link:
            path = REPO_ROOT / link.lstrip("/").split("#", 1)[0]
            assert path.exists(), f"{slot['activity']} links to missing {link}"


def test_four_lens_slots_of_fifteen_minutes(slots):
    lens_slots = [
        s for s in slots if (s.get("link") or "").startswith("/contents/lenses/")
    ]
    assert len(lens_slots) == 4
    assert all(duration(s) == 15 for s in lens_slots)
