#!/usr/bin/env zsh
set -euo pipefail

target="${1:-codex}"

case "$target" in
  codex)
    skills_dir="$HOME/.codex/skills"
    app_name="Codex"
    ;;
  claude-code|claude)
    skills_dir="$HOME/.claude/skills"
    app_name="Claude Code"
    ;;
  *)
    echo "Usage: install.sh [codex|claude-code]" >&2
    exit 2
    ;;
esac

repo_dir="$(mktemp -d)/hardware-agency-agents"
git clone --depth 1 https://github.com/Seahan1/hardware-agency-agents.git "$repo_dir"
cd "$repo_dir"

find hardware-agency-agents-cn hardware-agency-agents-en hardware-design-review-validation -name '*.md' -type f | while IFS= read -r file; do
  name="${file%.md}"
  name="${name//\//__}"
  name="${name// /-}"
  name="${name//:/-}"
  dir="$skills_dir/hardware-agency-agents__$name"
  mkdir -p "$dir"
  cp "$file" "$dir/SKILL.md"
done

echo "Installed hardware-agency-agents skills for $app_name. Restart $app_name to pick them up."
