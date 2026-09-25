from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
README_EN = ROOT / "README.md"
README_CN = ROOT / "README.zh-CN.md"

SKILL_DIRECTORIES = [
    ROOT / "skills",
    ROOT / "skills.zh-CN",
]


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
    skill_files: list[Path] = []
    seen_en_names: dict[str, Path] = {}
    seen_cn_names: dict[str, Path] = {}

    for sdir in SKILL_DIRECTORIES:
        if not sdir.exists():
            fail(f"Required directory does not exist: {sdir.relative_to(ROOT)}")

        is_cn = "zh-CN" in sdir.name
        seen = seen_cn_names if is_cn else seen_en_names
        lang = "Chinese" if is_cn else "English"

        for category_dir in sorted(sdir.iterdir()):
            if not category_dir.is_dir():
                continue
            for skill_dir in sorted(category_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.is_file():
                    fail(f"Missing required SKILL.md in {skill_dir.relative_to(ROOT)}")

                skill_files.append(skill_md)
                text = skill_md.read_text(encoding="utf-8")
                meta = parse_frontmatter(text, skill_md)

                for field in ("name", "description"):
                    if not meta.get(field):
                        fail(f"{skill_md.relative_to(ROOT)} is missing required field: {field}")

                name = meta["name"]
                if is_cn:
                    norm_name = re.sub(r"[/_]", "", name)
                    norm_dir = re.sub(r"[/_]", "", skill_dir.name)
                    if norm_name != norm_dir:
                        fail(
                            f"{skill_md.relative_to(ROOT)} frontmatter name '{name}' does not "
                            f"match directory name '{skill_dir.name}'"
                        )
                else:
                    expected_name = skill_dir.name
                    if name != expected_name:
                        fail(
                            f"{skill_md.relative_to(ROOT)} frontmatter name '{name}' does not "
                            f"match directory name '{expected_name}'"
                        )

                    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
                        fail(
                            f"{skill_md.relative_to(ROOT)} name '{name}' must be lowercase and hyphenated"
                        )

                if name in seen:
                    other = seen[name].relative_to(ROOT)
                    fail(
                        f"Duplicate {lang} skill name '{name}' found in "
                        f"{other} and {skill_md.relative_to(ROOT)}"
                    )
                seen[name] = skill_md

    print(f"Validated {len(seen_en_names)} English skills and {len(seen_cn_names)} Chinese skills (total {len(skill_files)} files).")
    return skill_files


def validate_readme_file(readme_path: Path, expected_skills: set[str], doc_name: str) -> None:
    if not readme_path.exists():
        fail(f"{doc_name} is missing")

    text = readme_path.read_text(encoding="utf-8")
    links = re.findall(r"\]\((\.\/[^)]+\.md)\)", text)
    found_skills = set()

    for link in links:
        relative = unquote(link[2:])
        target = (ROOT / relative).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f"{doc_name} contains a link outside the repository: {link}")
        if not target.exists():
            fail(f"{doc_name} points to a missing file: {link}")
        path_in_repo = target.relative_to(ROOT).as_posix()
        if path_in_repo in expected_skills:
            found_skills.add(path_in_repo)

    missing = sorted(expected_skills - found_skills)
    if missing:
        fail(
            f"{doc_name} is missing links for these skill files:\n  "
            + "\n  ".join(missing)
        )
    print(f"{doc_name}: All {len(expected_skills)} expected skill links verified successfully.")


def main() -> None:
    skill_files = validate_skills()

    # Expected in README.md: English skills + Chinese review skills
    # (README.md lists all 55 English skills, and links the 8 Chinese review skills in its review table)
    expected_en = {
        p.relative_to(ROOT).as_posix()
        for p in skill_files
        if p.relative_to(ROOT).as_posix().startswith("skills/")
        or (
            p.relative_to(ROOT).as_posix().startswith("skills.zh-CN/")
            and "硬件设计评审与验证" in p.as_posix()
        )
    }
    validate_readme_file(README_EN, expected_en, "README.md")

    # Expected in README.zh-CN.md: Chinese skills + English review skills
    # (README.zh-CN.md lists all 55 Chinese skills, and links the 8 English review skills in its review table)
    expected_cn = {
        p.relative_to(ROOT).as_posix()
        for p in skill_files
        if p.relative_to(ROOT).as_posix().startswith("skills.zh-CN/")
        or (
            p.relative_to(ROOT).as_posix().startswith("skills/")
            and "Hardware Design Review Validation" in p.as_posix()
        )
    }
    validate_readme_file(README_CN, expected_cn, "README.zh-CN.md")


if __name__ == "__main__":
    main()
