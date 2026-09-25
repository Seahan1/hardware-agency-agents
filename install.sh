#!/usr/bin/env bash
set -euo pipefail

target="${1:-codex}"
lang="${2:-all}"

case "$target" in
  codex)
    skills_dir="$HOME/.codex/skills"
    app_name="Codex"
    ;;
  claude-code|claude)
    skills_dir="$HOME/.claude/skills"
    app_name="Claude Code"
    ;;
  antigravity|agy)
    skills_dir="$HOME/.gemini/antigravity-cli/skills"
    app_name="Antigravity"
    ;;
  *)
    echo "Usage: install.sh [codex|claude-code|antigravity] [all|en|cn]" >&2
    exit 2
    ;;
esac

# Check if running inside repository, otherwise clone to temp
if [ -d "skills" ] && [ -d "skills.zh-CN" ]; then
  repo_dir="$(pwd)"
else
  temp_dir="$(mktemp -d)"
  repo_dir="$temp_dir/hardware-agency-agents"
  git clone --depth 1 https://github.com/Seahan1/hardware-agency-agents.git "$repo_dir"
fi

cd "$repo_dir"

search_dirs=()
case "$lang" in
  en)
    search_dirs=("skills")
    ;;
  cn|zh|zh-cn)
    search_dirs=("skills.zh-CN")
    ;;
  all)
    search_dirs=("skills" "skills.zh-CN")
    ;;
  *)
    echo "Invalid language: $lang. Must be 'all', 'en', or 'cn'." >&2
    exit 2
    ;;
esac

mkdir -p "$skills_dir"
count=0

if [ "$lang" = "en" ] || [ "$lang" = "all" ]; then
  en_project_dir="$skills_dir/Hardware Development Agents"
  mkdir -p "$en_project_dir"
  for cat_dir in "skills"/*; do
    if [ -d "$cat_dir" ]; then
      cat_name="$(basename "$cat_dir")"
      dest_cat="$en_project_dir/$cat_name"
      mkdir -p "$dest_cat"
      cp -R "$cat_dir"/* "$dest_cat/"
    fi
  done
  en_count=$(find "$en_project_dir" -name "SKILL.md" -type f | wc -l | tr -d ' ')
  count=$((count + en_count))
fi

if [ "$lang" = "cn" ] || [ "$lang" = "zh" ] || [ "$lang" = "zh-cn" ] || [ "$lang" = "all" ]; then
  cn_project_dir="$skills_dir/硬件开发代理"
  mkdir -p "$cn_project_dir"
  for cat_dir in "skills.zh-CN"/*; do
    if [ -d "$cat_dir" ]; then
      cat_name="$(basename "$cat_dir")"
      dest_cat="$cn_project_dir/$cat_name"
      mkdir -p "$dest_cat"
      cp -R "$cat_dir"/* "$dest_cat/"
    fi
  done
  cn_count=$(find "$cn_project_dir" -name "SKILL.md" -type f | wc -l | tr -d ' ')
  count=$((count + cn_count))
fi

echo "Installed $count hardware-agency-agents skills ($lang) for $app_name."
echo "Skills directory: $skills_dir"
echo "Restart $app_name to load them."
