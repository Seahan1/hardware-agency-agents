from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOTS = (
    ROOT / "hardware-agency-agents-cn",
    ROOT / "hardware-agency-agents-en",
    ROOT / "hardware-design-review-validation",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} is missing YAML frontmatter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail(f"{path.relative_to(ROOT)} has malformed frontmatter")

    raw = parts[1]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_skills() -> list[Path]:
    skill_files = sorted(
        path
        for skill_root in SKILL_ROOTS
        for path in skill_root.rglob("*.md")
    )
    if not skill_files:
        fail("No skill markdown files found under the configured skill roots")

    seen_names: dict[str, Path] = {}
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text, path)
        for field in ("name", "description"):
            if not meta.get(field):
                fail(f"{path.relative_to(ROOT)} is missing required field: {field}")
        name = meta["name"]
        if name in seen_names:
            other = seen_names[name].relative_to(ROOT)
            fail(
                f"Duplicate skill name '{name}' found in "
                f"{other} and {path.relative_to(ROOT)}"
            )
        seen_names[name] = path
    return skill_files


def validate_readme(readme: Path, skill_files: list[Path]) -> None:
    if not readme.exists():
        fail(f"{readme.name} is missing")

    text = readme.read_text(encoding="utf-8")
    links = re.findall(r"\]\((\.\/[^)]+\.md)\)", text)
    expected = {path.relative_to(ROOT).as_posix() for path in skill_files}
    found_local_skills = set()
    seen_local_skills = set()

    for link in links:
        relative = unquote(link[2:])
        target = (ROOT / relative).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f"{readme.name} contains a link outside the repository: {link}")
        if not target.exists():
            fail(f"{readme.name} points to a missing file: {link}")
        path_in_repo = target.relative_to(ROOT).as_posix()
        if path_in_repo in expected:
            if path_in_repo in seen_local_skills:
                fail(f"{readme.name} links to the same skill more than once: {link}")
            seen_local_skills.add(path_in_repo)
            found_local_skills.add(path_in_repo)

    missing = sorted(expected - found_local_skills)
    if missing:
        fail(
            f"{readme.name} is missing links for these skill files: "
            + ", ".join(missing)
        )


def main() -> None:
    skill_files = validate_skills()
    english_files = [
        path
        for path in skill_files
        if path.is_relative_to(ROOT / "hardware-agency-agents-en")
        or path.is_relative_to(ROOT / "hardware-design-review-validation" / "en")
    ]
    chinese_files = [
        path
        for path in skill_files
        if path.is_relative_to(ROOT / "hardware-agency-agents-cn")
        or path.is_relative_to(ROOT / "hardware-design-review-validation" / "cn")
    ]
    validate_readme(ROOT / "README.md", english_files)
    validate_readme(ROOT / "README.zh-CN.md", chinese_files)
    print(f"Validated {len(skill_files)} skill files and both README indexes successfully.")


if __name__ == "__main__":
    main()
