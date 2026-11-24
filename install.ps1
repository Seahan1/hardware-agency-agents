param(
    [ValidateSet("codex", "claude-code", "claude")]
    [string]$Target = "codex"
)

$ErrorActionPreference = "Stop"

if ($Target -eq "codex") {
    $appName = "Codex"
    $defaultSkillsDir = Join-Path $HOME ".codex/skills"
} else {
    $appName = "Claude Code"
    $defaultSkillsDir = Join-Path $HOME ".claude/skills"
}

$skillsDir = if ($env:HARDWARE_AGENCY_SKILLS_DIR) { $env:HARDWARE_AGENCY_SKILLS_DIR } else { $defaultSkillsDir }
$repoUrl = if ($env:HARDWARE_AGENCY_REPOSITORY) { $env:HARDWARE_AGENCY_REPOSITORY } else { "https://github.com/Seahan1/hardware-agency-agents.git" }
$repoRef = if ($env:HARDWARE_AGENCY_REF) { $env:HARDWARE_AGENCY_REF } else { "main" }
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
$repoDir = Join-Path $tempRoot "hardware-agency-agents"

try {
    New-Item -ItemType Directory -Path $tempRoot | Out-Null
    git clone --branch $repoRef --depth 1 $repoUrl $repoDir
    if ($LASTEXITCODE -ne 0) {
        throw "Git clone failed."
    }

    $skillRoots = @("hardware-agency-agents-cn", "hardware-agency-agents-en", "hardware-design-review-validation")
    foreach ($skillRoot in $skillRoots) {
        Get-ChildItem -LiteralPath (Join-Path $repoDir $skillRoot) -Filter "*.md" -File -Recurse | ForEach-Object {
            $relativePath = $_.FullName.Substring($repoDir.Length + 1)
            $name = $relativePath.Substring(0, $relativePath.Length - 3).Replace("\", "__").Replace("/", "__").Replace(" ", "-").Replace(":", "-")
            $destination = Join-Path $skillsDir ("hardware-agency-agents__" + $name)
            New-Item -ItemType Directory -Path $destination -Force | Out-Null
            Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $destination "SKILL.md") -Force
        }
    }
    Write-Host "Installed hardware-agency-agents skills for $appName. Restart $appName to pick them up."
} finally {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
}
