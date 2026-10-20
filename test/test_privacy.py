"""Privacy guard. The repository holds generic teaching resources only.

Participant names, contact details, attendance records, evaluation answers,
submissions, certificates, and signatures must never enter Git. These tests
fail when a tracked file looks like such data, or when a tracked file or the
history contains an e-mail address outside the allowlist.
"""

from __future__ import annotations

import re
import subprocess

import pytest
from conftest import REPO_ROOT, tracked_files

# Public role addresses and the maintainer contact. Add an address only for a
# public role, never for a participant. The GitHub noreply address of the
# maintainer appears in the co-author trailers of squash merges.
ALLOWED_EMAILS = {
    "14755525+maehr@users.noreply.github.com",
    "grace@unibas.ch",
    "moritz.maehr@gmail.com",
    "noreply@anthropic.com",
    "l.j.wagner@proton.me",
    "maehr@users.noreply.github.com",
}

EMAIL = re.compile(
    r"\b[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
)

FORBIDDEN_NAME = re.compile(
    r"attendance|anwesen|participant|teilnehm|roster|certificate|zertifikat|"
    r"signature|unterschrift|submission|abgabe|evaluation[-_ ]?(export|results)",
    re.IGNORECASE,
)
FORBIDDEN_SUFFIX = {".xlsx", ".xls", ".ods", ".csv", ".p12", ".pfx", ".pem", ".key"}

# Files that third parties wrote, and lock files. They hold no course data.
SKIP = {
    "package-lock.json",
    "uv.lock",
    "LICENSE-AGPL.md",
    "LICENSE-CCBY.md",
    "LICENSE-CCBYSA.md",
}

# Domains that appear in package or image metadata, not in personal addresses.
NOT_AN_ADDRESS = re.compile(r"@\d+x\.|\.(png|jpg|jpeg|svg|webp)$", re.IGNORECASE)

FILES = tracked_files()
needs_git = pytest.mark.skipif(FILES is None, reason="not a Git checkout")


def addresses(text: str) -> set[str]:
    return {m for m in EMAIL.findall(text) if not NOT_AN_ADDRESS.search(m)}


@needs_git
def test_no_participant_files_are_tracked():
    assert FILES is not None
    bad = [
        str(p.relative_to(REPO_ROOT))
        for p in FILES
        if FORBIDDEN_NAME.search(p.name) or p.suffix.lower() in FORBIDDEN_SUFFIX
    ]
    assert not bad, f"These tracked files look like participant data: {bad}"


@needs_git
def test_tracked_files_contain_only_allowed_addresses():
    assert FILES is not None
    found: dict[str, set[str]] = {}
    for path in FILES:
        if path.name in SKIP or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        extra = addresses(text) - ALLOWED_EMAILS
        if extra:
            found[str(path.relative_to(REPO_ROOT))] = extra
    assert not found, f"Unexpected e-mail addresses: {found}"


@needs_git
def test_history_contains_only_allowed_addresses():
    log = subprocess.run(
        ["git", "log", "-p", "--format=%B", "--", ".", *(f":!{s}" for s in SKIP)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    # Keep added lines and commit messages. Drop the "+" marker of a diff line.
    added = "\n".join(
        line[1:] if line.startswith("+") else line
        for line in log.splitlines()
        if not line.startswith("-")
    )
    extra = addresses(added) - ALLOWED_EMAILS
    assert not extra, f"The Git history contains unexpected e-mail addresses: {extra}"
