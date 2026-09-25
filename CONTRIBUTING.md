# Contributing Guide

[English](./CONTRIBUTING.md) | [简体中文](./CONTRIBUTING.zh-CN.md)

Thank you for contributing to `hardware-agency-agents`. The goal of this repository is not to pile up abstract terminology, but to build a reusable, well-bounded library of role-based skills tailored for real engineering collaboration.

## Pre-Submission Checklist

- Your added content corresponds to a real hardware engineering role or specialized sub-role capable of taking ownership of tasks.
- The skill does not duplicate an existing skill under a different name.
- The document emphasizes engineering constraints, workflows, deliverables, and practical application boundaries, rather than generic textbook descriptions.
- The submission contains no company-confidential designs, customer IP, proprietary documents, or copyright-infringing materials.

## Skill File Requirements

Each skill is maintained in standard Codex / Claude Code / Antigravity CLI format as a dedicated directory containing a `SKILL.md` file:

- English skills: `skills/<Category>/<skill-slug>/SKILL.md`
- Chinese skills: `skills.zh-CN/<Category>/<Chinese_Name>/SKILL.md`

The beginning of every `SKILL.md` must include valid YAML frontmatter containing at least:

```yaml
---
name: example-hardware-engineer
description: Role and collaboration skill for [domain]. Used for [typical tasks], [target objects], [common failure modes], [critical constraints], and [deliverables].
color: teal
---
```

Requirements:

- `name`: Must be unique, lowercase, and hyphenated (e.g. `pcb-hardware-engineer`), exactly matching the skill's directory name.
- `description`: Must clearly state role boundaries, core technical focus, and primary use cases.
- `color`: Optional but recommended for visual consistency.

## Description Guidelines

Each skill's `description` should follow a standardized structure optimized for agent triggering:

```text
[Role/Domain] skill. Used for [task types], [target objects], [common problems/failures], [critical constraints], and [deliverables].
```

Key guidelines:

- Include explicit domain terms, task keywords, hardware targets, failure modes, and deliverables.
- Prioritize terms users search for: component types, symptoms, review actions, and engineering outputs.

## Content Quality Standards

- Frame guidance as an **engineering decision framework**, not a textbook catalog.
- Emphasize input requirements, boundary conditions, failure mechanisms, verification gates, and deliverables.
- Avoid vague hand-waving statements such as "ensure stability" or "pay attention to EMI issues".
- Write executable rules, deterministic workflows, and structured communication protocols.
- Avoid placeholder text, unfinished sections, or trailing ellipsis.

## Domain Grouping
 
When adding a skill, maintain synchronized English and Chinese versions (`skills/<Category>/<skill-slug>/SKILL.md` and `skills.zh-CN/<Category>/<Chinese_Name>/SKILL.md`) categorized across the engineering domains:

- `PCB and Board-Level Implementation` (`PCB 与板级实现方向`)
- `Reliability EMC and Safety` (`可靠性 EMC 安规方向`)
- `Embedded Hardware` (`嵌入式硬件方向`)
- `Digital Analog and Mixed-Signal` (`数字与模拟混合信号方向`)
- `Testing and Validation` (`测试与验证方向`)
- `Power and Power Electronics` (`电源与功率电子方向`)
- `Chip Platforms and Low-Level Board Co-Design` (`芯片平台与底层板级协同方向`)
- `Communication and Interfaces` (`通信与接口方向`)
- `Hardware Design Review Validation` (`硬件设计评审与验证`)

If you believe a new domain directory is necessary, please explain in your PR:

- Why the existing domains are insufficient.
- The boundary differences between the proposed domain and existing domains.
- What future skills will be housed under the new domain.

## Documentation & README Updates

If you add, delete, or rename a skill, please update the corresponding entries in `README.md` and `README.zh-CN.md`:

- Overall skill statistics and badge counts.
- Domain section counts.
- Skill Index table links.
- Selection recommendations where applicable.

## Pull Request Guidelines

Keep each PR focused on a single logical change:

- Adding a new skill or a cohesive set of related skills.
- Refining role boundaries or rule text.
- Adjusting directory layout.
- Fixing metadata or documentation links.

This makes reviews faster and rollbacks safer.
