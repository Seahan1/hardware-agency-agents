from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
SKILL_DIR_NAMES = {
    "PCB 与板级实现方向",
    "可靠性 EMC 安规方向",
    "嵌入式硬件方向",
    "数字 : 模拟 : 混合信号方向",
    "测试与验证方向",
    "电源与功率电子方向",
    "芯片平台与底层板级协同方向",
    "通信与接口方向",
}


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
        for path in ROOT.glob("*/*.md")
        if path.parent.name in SKILL_DIR_NAMES
    )
    if not skill_files:
        fail("No skill markdown files found under first-level directories")

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


def validate_readme(skill_files: list[Path]) -> None:
    if not README.exists():
        fail("README.md is missing")

    text = README.read_text(encoding="utf-8")
    links = re.findall(r"\]\((\.\/[^)]+\.md)\)", text)
    expected = {path.relative_to(ROOT).as_posix() for path in skill_files}
    found_local_skills = set()

    for link in links:
        relative = unquote(link[2:])
        target = (ROOT / relative).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f"README.md contains a link outside the repository: {link}")
        if not target.exists():
            fail(f"README.md points to a missing file: {link}")
        path_in_repo = target.relative_to(ROOT).as_posix()
        if path_in_repo in expected:
            found_local_skills.add(path_in_repo)

    missing = sorted(expected - found_local_skills)
    if missing:
        fail(
            "README.md is missing links for these skill files: "
            + ", ".join(missing)
        )


def main() -> None:
    skill_files = validate_skills()
    validate_readme(skill_files)
    print(f"Validated {len(skill_files)} skill files and README links successfully.")


if __name__ == "__main__":
    main()
