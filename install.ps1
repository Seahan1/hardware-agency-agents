<#
.SYNOPSIS
    Installs hardware-agency-agents skills for Codex, Claude Code, or Antigravity on Windows.

.PARAMETER Target
    Target application: "codex", "claude-code", or "antigravity". Defaults to "codex".

.PARAMETER Language
    Language filter: "all", "en", or "cn". Defaults to "all".

.EXAMPLE
    .\install.ps1 -Target codex -Language en
    .\install.ps1 -Target claude-code -Language cn
    irm https://raw.githubusercontent.com/Seahan1/hardware-agency-agents/main/install.ps1 | iex
#>

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet("codex", "claude-code", "claude", "antigravity", "agy")]
    [string]$Target = "codex",

    [Parameter(Position = 1)]
    [ValidateSet("all", "en", "cn", "zh", "zh-cn")]
    [string]$Language = "all"
)

$ErrorActionPreference = "Stop"

switch ($Target) {
    "codex" {
        $skillsDir = Join-Path $HOME ".codex\skills"
        $appName = "Codex"
    }
    { $_ -in "claude-code", "claude" } {
        $skillsDir = Join-Path $HOME ".claude\skills"
        $appName = "Claude Code"
    }
    { $_ -in "antigravity", "agy" } {
        $skillsDir = Join-Path $HOME ".gemini\antigravity-cli\skills"
        $appName = "Antigravity"
    }
}

# Determine source repository directory
$isLocalRepo = (Test-Path "skills") -and (Test-Path "skills.zh-CN")
$tempRepoDir = $null

if ($isLocalRepo) {
    $repoDir = (Get-Item .).FullName
} else {
    $tempRepoDir = Join-Path ([IO.Path]::GetTempPath()) ("hardware-agency-agents-" + [guid]::NewGuid())
    Write-Host "Cloning repository..."
    git clone --depth 1 "https://github.com/Seahan1/hardware-agency-agents.git" $tempRepoDir
    $repoDir = $tempRepoDir
}

try {
    $installedCount = 0

    if ($Language -eq "en" -or $Language -eq "all") {
        $enSource = Join-Path $repoDir "skills"
        if (Test-Path $enSource) {
            $enProjectDir = Join-Path $skillsDir "Hardware Development Agents"
            New-Item -ItemType Directory -Force -Path $enProjectDir | Out-Null

            Get-ChildItem -Path $enSource -Directory | ForEach-Object {
                $catDest = Join-Path $enProjectDir $_.Name
                New-Item -ItemType Directory -Force -Path $catDest | Out-Null
                Copy-Item -Path (Join-Path $_.FullName "*") -Destination $catDest -Recurse -Force
            }
            $installedCount += (Get-ChildItem -Path $enProjectDir -Recurse -Filter "SKILL.md" -File).Count
        }
    }

    if ($Language -in @("cn", "zh", "zh-cn", "all")) {
        $cnSource = Join-Path $repoDir "skills.zh-CN"
        if (Test-Path $cnSource) {
            $cnProjectDir = Join-Path $skillsDir "硬件开发代理"
            New-Item -ItemType Directory -Force -Path $cnProjectDir | Out-Null

            Get-ChildItem -Path $cnSource -Directory | ForEach-Object {
                $catDest = Join-Path $cnProjectDir $_.Name
                New-Item -ItemType Directory -Force -Path $catDest | Out-Null
                Copy-Item -Path (Join-Path $_.FullName "*") -Destination $catDest -Recurse -Force
            }
            $installedCount += (Get-ChildItem -Path $cnProjectDir -Recurse -Filter "SKILL.md" -File).Count
        }
    }

    Write-Host ""
    Write-Host "Successfully installed $installedCount hardware-agency-agents skills ($Language) for $appName."
    Write-Host "Skills directory: $skillsDir"
    Write-Host "Restart $appName to load them."
}
finally {
    if ($tempRepoDir -and (Test-Path $tempRepoDir)) {
        Remove-Item -Path $tempRepoDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
