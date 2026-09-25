# hardware-agency-agents

[English](./README.md) | [简体中文](./README.zh-CN.md)

![License](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-55-blue)
![Domains](https://img.shields.io/badge/domains-8-orange)
![Language](https://img.shields.io/badge/language-bilingual-purple)

Are you already used to AI giving hardware advice with great confidence while clearly not understanding hardware at all?

If you are tired of suggestions like "just make the ground trace wider" or "place the capacitor anywhere first and tune it later", this repository is built for you.

`hardware-agency-agents` is an open-source library of hardware engineering skills organized by real engineering roles. Each skill document focuses on a specific role boundary, technical constraints, workflows, communication style, and expected deliverables, so hardware tasks can be approached with more rigorous engineering judgment instead of generic assistant-style advice.

This repository is inspired by the organizational clarity of strong skill libraries, and it now maintains synchronized Chinese and English skill documents around the actual files in this repository, with a focus on board-level constraints and production-oriented design thinking.

## 📚 Table of Contents

- [Quick Start](#-quick-start)
- [Public Notes](#-public-notes)
- [Overview](#-overview)
- [How To Use](#-how-to-use)
- [Repository Structure](#-repository-structure)
- [Skill Index](#-skill-index)
- [How To Choose A Skill](#-how-to-choose-a-skill)
- [What Makes This Repository Different](#-what-makes-this-repository-different)
- [License](#-license)
- [Contributing](#-contributing)
- [GitHub Checks](#-github-checks)

## ⚡ Quick Start

1. Install the skills for your agent:

   **Linux / macOS (Bash / Zsh):**

   ```bash
   # Codex
   curl -fsSL https://raw.githubusercontent.com/Seahan1/hardware-agency-agents/main/install.sh | bash -s -- codex

   # Claude Code
   curl -fsSL https://raw.githubusercontent.com/Seahan1/hardware-agency-agents/main/install.sh | bash -s -- claude-code
   ```

   **Windows (PowerShell):**

   ```powershell
   # Codex
   irm https://raw.githubusercontent.com/Seahan1/hardware-agency-agents/main/install.ps1 | iex

   # Claude Code
   & ([scriptblock]::Create((irm https://raw.githubusercontent.com/Seahan1/hardware-agency-agents/main/install.ps1))) claude-code
   ```

2. Pick the closest skill for your task from the index below.
3. Read that skill as the primary engineering role.
4. Add one or two adjacent skills when the task crosses domains.
5. Use the skill content to frame review comments, design constraints, debug hypotheses, and validation plans.

Suggested starting points:

- Board implementation: `PCB Hardware Engineer`
- STM32 boards: `STM32 Hardware Engineer`
- Power design: `Power Hardware Engineer`
- EMC and corrective action: `EMC Hardware Engineer`
- Validation closure: `Hardware Validation Engineer`
- Hardware design review: choose the matching review skill from `skills/ or skills.zh-CN/` before board release, EVT/DVT issue closure, or production introduction

## 📢 Public Notes

- This repository is a collection of hardware skill documents, not an official built-in library for any single agent platform
- The content is intended for role selection, design discussion, review guidance, and engineering analysis, not as an automatic guarantee of project correctness
- Users should still validate all conclusions against datasheets, standards, measurements, and project-specific constraints
- This repository is not officially affiliated with ST, TI, NXP, ADI, Altium, KiCad, or other vendors and platforms mentioned in hardware workflows

## 📦 Overview

- 47 hardware role skills plus 8 hardware design review skills in English and Chinese (55 unique skills, 110 files total)
- 8 engineering domains
- Coverage across PCB implementation, embedded hardware, power, EMC/compliance, validation, SoC/FPGA platforms, and communication interfaces
- Suitable for schematic review, PCB constraint analysis, hardware design review, debug work, validation planning, and production-readiness discussions

## 🧭 How To Use

You can treat each `.md` file in this repository as a reusable specialist role template:

1. When the task boundary is clear, choose the most relevant skill as the primary role.
2. When the problem crosses domains, choose one primary skill and add one or two closely related supporting skills.
3. When the task is in review, validation, debug, or production handoff stages, prefer skills that emphasize constraints, verification, and deliverables instead of pure functional discussion.

Typical examples:

- STM32 control board schematic review: start with `STM32 Hardware Engineer`, optionally add `PCB Hardware Engineer` and `EMC Hardware Engineer`
- Buck converter stability and thermal analysis: start with `Power Hardware Engineer`
- High-speed board layout and impedance constraints: start with `High-Speed PCB Engineer` or `SI/PI Engineer`
- EVT/DVT validation closure: start with `Hardware Validation Engineer` or `EVT/DVT Engineer`
- Hardware design review before board release or production introduction: start with the matching skill in `skills/ or skills.zh-CN/`

## 🗂️ Repository Structure

```text
hardware-agency-agents/
├── skills/                     # English skills in standard format (55 skills)
│   ├── pcb-hardware-engineer/
│   │   └── SKILL.md
│   ├── emc-hardware-engineer/
│   │   └── SKILL.md
│   └── ...
└── skills.zh-CN/               # Chinese skills in standard format (55 skills)
    ├── PCB硬件工程师/
    │   └── SKILL.md
    ├── EMC硬件工程师/
    │   └── SKILL.md
    └── ...
```

Notes:

- `README.md` is the default English landing page
- `README.zh-CN.md` is the matching Simplified Chinese page
- `skills` stores all English skills in standard Codex / Claude Code / Antigravity CLI format (`skills/<name>/SKILL.md`)
- `skills.zh-CN` stores all Chinese skills in standard format (`skills.zh-CN/<name>/SKILL.md`)

## 🧰 Skill Index

### PCB and Board-Level Implementation (9)

| Skill | Focus |
| --- | --- |
| [DFA Engineer](./skills/PCB%20and%20Board-Level%20Implementation/dfa-engineer/SKILL.md) | Design for assembly, soldering risk, component spacing, orientation, and reworkability |
| [DFM Engineer](./skills/PCB%20and%20Board-Level%20Implementation/dfm-engineer/SKILL.md) | Design for manufacturability, process limits, panelization, via process, and fabrication data review |
| [PCB Layout Engineer](./skills/PCB%20and%20Board-Level%20Implementation/pcb-layout-engineer/SKILL.md) | Layout and routing quality, stackup planning, constraints, impedance, vias, and return paths |
| [PCB Footprint Library Engineer](./skills/PCB%20and%20Board-Level%20Implementation/pcb-footprint-library-engineer/SKILL.md) | Footprint library quality, pad rules, 3D models, and naming standards |
| [PCB Hardware Engineer](./skills/PCB%20and%20Board-Level%20Implementation/pcb-hardware-engineer/SKILL.md) | End-to-end board implementation from schematic to manufacturable PCB with SI, PI, EMC, DFM, and outputs |
| [SI/PI Engineer](./skills/PCB%20and%20Board-Level%20Implementation/si-pi-engineer/SKILL.md) | Signal integrity and power integrity modeling, simulation, diagnosis, and correction |
| [RF Hardware Engineer](./skills/PCB%20and%20Board-Level%20Implementation/rf-hardware-engineer/SKILL.md) | RF front-end implementation, impedance matching, antenna coordination, and RF debug |
| [Hardware Process Engineer](./skills/PCB%20and%20Board-Level%20Implementation/hardware-process-engineer/SKILL.md) | SMT/DIP process, manufacturing introduction, and process coordination |
| [High-Speed PCB Engineer](./skills/PCB%20and%20Board-Level%20Implementation/high-speed-pcb-engineer/SKILL.md) | High-speed board constraints, differential routing, length matching, impedance, and crosstalk control |

### Reliability, EMC, and Compliance (8)

| Skill | Focus |
| --- | --- |
| [EMC Hardware Engineer](./skills/Reliability%20EMC%20and%20Safety/emc-hardware-engineer/SKILL.md) | EMC design, diagnosis, and closure from board level to system level |
| [EMI Remediation Engineer](./skills/Reliability%20EMC%20and%20Safety/emi-remediation-engineer/SKILL.md) | EMI problem localization, interference source analysis, and corrective actions |
| [ESD Protection Engineer](./skills/Reliability%20EMC%20and%20Safety/esd-protection-engineer/SKILL.md) | ESD protection schemes, TVS selection, discharge paths, and interface protection |
| [Failure Analysis Engineer](./skills/Reliability%20EMC%20and%20Safety/failure-analysis-engineer/SKILL.md) | Failure reproduction, root cause analysis, component failure modes, and stress-related faults |
| [Safety Compliance Engineer](./skills/Reliability%20EMC%20and%20Safety/safety-compliance-engineer/SKILL.md) | Electrical safety design, insulation boundaries, risk assessment, and certification preparation |
| [Environmental Test Engineer](./skills/Reliability%20EMC%20and%20Safety/environmental-test-engineer/SKILL.md) | Temperature, vibration, drop, aging, and environmental stress testing |
| [Hardware Reliability Engineer](./skills/Reliability%20EMC%20and%20Safety/hardware-reliability-engineer/SKILL.md) | Derating, lifetime, thermal stress, environmental robustness, and MTBF-related methods |
| [Certification Engineer (CE FCC UL and More)](./skills/Reliability%20EMC%20and%20Safety/certification-engineer/SKILL.md) | Regulatory certification documents, lab coordination, and corrective support |

### Embedded Hardware (7)

| Skill | Focus |
| --- | --- |
| [MCU Hardware Engineer](./skills/Embedded%20Hardware/mcu-hardware-engineer/SKILL.md) | MCU minimum system, reset, clocks, download interface, and board debug |
| [Microcontroller Hardware Engineer](./skills/Embedded%20Hardware/microcontroller-hardware-engineer/SKILL.md) | Single-chip control hardware, buses, logic levels, pull-up/down handling, and protection |
| [Embedded Hardware Engineer](./skills/Embedded%20Hardware/embedded-hardware-engineer/SKILL.md) | Board-level embedded hardware with MCU/MPU peripherals, interfaces, power, and joint debug |
| [Embedded Systems Hardware Engineer](./skills/Embedded%20Hardware/embedded-systems-hardware-engineer/SKILL.md) | Complex embedded platforms, DDR, Flash, buses, timing, and system architecture |
| [Industrial Control Hardware Engineer](./skills/Embedded%20Hardware/industrial-control-hardware-engineer/SKILL.md) | Industrial anti-interference, isolation, surge, lightning, and wide-temperature design |
| [Control Board Hardware Engineer](./skills/Embedded%20Hardware/control-board-hardware-engineer/SKILL.md) | Controller main boards, functional boards, drive/protection design, and bring-up |
| [Automation Control Hardware Engineer](./skills/Embedded%20Hardware/automation-control-hardware-engineer/SKILL.md) | Automation control hardware, IO, relays, industrial buses, drives, and sensing |

### Digital / Analog / Mixed-Signal (7)

| Skill | Focus |
| --- | --- |
| [STM32 Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/stm32-hardware-engineer/SKILL.md) | STM32 minimum system, Boot, SWD, ADC reference, and peripheral board design |
| [Low-Power Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/low-power-hardware-engineer/SKILL.md) | Battery-powered low-power planning, sleep/wake design, and power budgeting |
| [Signal Chain Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/signal-chain-hardware-engineer/SKILL.md) | Sensor-to-processor signal conditioning, filtering, isolation, and error-chain analysis |
| [Digital Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/digital-hardware-engineer/SKILL.md) | Digital logic, timing constraints, interfaces, board implementation, and debug |
| [Mixed-Signal Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/mixed-signal-hardware-engineer/SKILL.md) | Mixed-signal partitioning, grounding, sampling synchronization, and interference control |
| [Analog Hardware Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/analog-hardware-engineer/SKILL.md) | Op-amp circuits, filtering, signal conditioning, noise, and stability analysis |
| [High-Speed Digital Circuit Engineer](./skills/Digital%20Analog%20and%20Mixed-Signal/high-speed-digital-circuit-engineer/SKILL.md) | High-speed interfaces, timing margin, reference planes, and board-level debug |

### Testing and Validation (6)

| Skill | Focus |
| --- | --- |
| [EVT/DVT Engineer](./skills/Testing%20and%20Validation/evt-dvt-engineer/SKILL.md) | Engineering sample validation, risk identification, and maturity judgment |
| [Lab Test Engineer](./skills/Testing%20and%20Validation/lab-test-engineer/SKILL.md) | Lab instruments, execution discipline, data capture, and repeatability |
| [Board-Level Debug Engineer](./skills/Testing%20and%20Validation/board-level-debug-engineer/SKILL.md) | Power-up, clocks, reset, interfaces, and fault localization |
| [Hardware Test Engineer](./skills/Testing%20and%20Validation/hardware-test-engineer/SKILL.md) | Functional, performance, boundary, and stability testing |
| [Hardware Validation Engineer](./skills/Testing%20and%20Validation/hardware-validation-engineer/SKILL.md) | Validation planning, defect closure, and EVT/DVT/PVT gate decisions |
| [Automated Test Hardware Engineer](./skills/Testing%20and%20Validation/automated-test-hardware-engineer/SKILL.md) | Test fixtures, interface control, production test links, and automation platforms |

### Power and Power Electronics (5)

| Skill | Focus |
| --- | --- |
| [BMS Hardware Engineer](./skills/Power%20and%20Power%20Electronics/bms-hardware-engineer/SKILL.md) | Cell sensing, balancing, protection, high-voltage safety, and isolated communication |
| [Energy Storage Hardware Engineer](./skills/Power%20and%20Power%20Electronics/energy-storage-hardware-engineer/SKILL.md) | Energy storage modules, power conversion, protection, and thermal management |
| [Power Electronics Engineer](./skills/Power%20and%20Power%20Electronics/power-electronics-engineer/SKILL.md) | Mid/high-power conversion, gate drive, magnetics, thermal design, and loss analysis |
| [Motor Drive Hardware Engineer](./skills/Power%20and%20Power%20Electronics/motor-drive-hardware-engineer/SKILL.md) | Half-bridge/full-bridge topology, current sensing, protection, and motor-drive control boards |
| [Power Hardware Engineer](./skills/Power%20and%20Power%20Electronics/power-hardware-engineer/SKILL.md) | AC/DC, DC/DC, LDO, power trees, compensation, thermal design, and protection strategies |

### Platform and Low-Level Board Coordination (4)

| Skill | Focus |
| --- | --- |
| [CPLD Engineer](./skills/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/cpld-engineer/SKILL.md) | Basic programmable logic, interface conversion, IO levels, timing, and configuration |
| [FPGA Hardware Engineer](./skills/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/fpga-hardware-engineer/SKILL.md) | FPGA power rails, clocks, configuration, multi-voltage domains, and high-speed IO |
| [SoC Hardware Platform Engineer](./skills/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/soc-hardware-platform-engineer/SKILL.md) | SoC/MPU platforms, DDR, power sequencing, PMIC coordination, and boot configuration |
| [Chip Applications Engineer (Hardware-Focused FAE AE)](./skills/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/chip-applications-engineer/SKILL.md) | Application support, reference design adaptation, and customer-facing hardware analysis |

### Communication and Interfaces (1)

| Skill | Focus |
| --- | --- |
| [Communications Hardware Engineer](./skills/Communication%20and%20Interfaces/communications-hardware-engineer/SKILL.md) | Communication boards, high-speed interfaces, link debug, transmission lines, and EMC-aware design |


### Hardware Design Review and Validation (16)

#### English Review Skills (8)

| Skill | Focus |
| --- | --- |
| [PCB and Board-Level Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/pcb-and-board-level-design-review-engineer/SKILL.md) | Board implementation review for schematics, PCB layout, stackup, impedance, manufacturing data, and test points |
| [Reliability EMC and Safety Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/reliability-emc-and-safety-design-review-engineer/SKILL.md) | Risk review for derating, temperature rise, ESD, surge, EMC, safety distances, and certification data |
| [Embedded Hardware Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/embedded-hardware-design-review-engineer/SKILL.md) | Review for MCU/MPU minimum systems, reset and clock circuits, boot configuration, interfaces, and debug access |
| [Digital Analog and Mixed-Signal Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/digital-analog-and-mixed-signal-design-review-engineer/SKILL.md) | Review for high-speed digital, analog chains, ADC/DAC, references, noise, and crosstalk |
| [Testing and Validation Review Engineer](./skills/Hardware%20Design%20Review%20Validation/testing-and-validation-review-engineer/SKILL.md) | Review for EVT, DVT, PVT, test coverage, sample size, data records, and issue closure |
| [Power and Power Electronics Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/power-and-power-electronics-design-review-engineer/SKILL.md) | Review for power trees, power stages, loops, ripple, transients, protection, thermal behavior, and EMI |
| [Chip Platform and Board Co-Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/chip-platform-and-board-co-design-review-engineer/SKILL.md) | Review for SoC, FPGA, DDR, PMIC, boot chains, and reference-design adaptation |
| [Communications and Interface Design Review Engineer](./skills/Hardware%20Design%20Review%20Validation/communications-and-interface-design-review-engineer/SKILL.md) | Review for Ethernet, USB, CAN, RS485, LVDS, connectors, cables, and interface protection |

#### Chinese Review Skills (8)

| Skill | Focus |
| --- | --- |
| [PCB与板级实现评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/PCB%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向原理图、PCB、叠层、阻抗、制造资料和测试点的板级实现评审 |
| [可靠性EMC安规评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E5%8F%AF%E9%9D%A0%E6%80%A7EMC%E5%AE%89%E8%A7%84%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向降额、温升、ESD、浪涌、EMC、安规距离和认证资料的风险评审 |
| [嵌入式硬件评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向 MCU/MPU 最小系统、复位时钟、启动配置、接口和调试入口的评审 |
| [数字模拟混合信号评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E6%95%B0%E5%AD%97%E6%A8%A1%E6%8B%9F%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向高速数字、模拟链路、ADC/DAC、参考源、噪声和串扰的评审 |
| [测试与验证评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向 EVT、DVT、PVT、测试覆盖、样本量、数据记录和问题闭环的评审 |
| [电源与功率电子评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向电源树、功率级、环路、纹波、瞬态、保护、热和 EMI 的评审 |
| [芯片平台与板级协同评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E8%8A%AF%E7%89%87%E5%B9%B3%E5%8F%B0%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%8D%8F%E5%90%8C%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向 SoC、FPGA、DDR、PMIC、启动链路和参考设计落地的评审 |
| [通信与接口评审工程师](./skills.zh-CN/%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E8%AF%84%E5%AE%A1%E4%B8%8E%E9%AA%8C%E8%AF%81/%E9%80%9A%E4%BF%A1%E4%B8%8E%E6%8E%A5%E5%8F%A3%E8%AF%84%E5%AE%A1%E5%B7%A5%E7%A8%8B%E5%B8%88/SKILL.md) | Chinese-language hardware design review skill: 面向以太网、USB、CAN、RS485、LVDS、连接器、线缆和接口保护的评审 |

## 🎯 How To Choose A Skill

If your task is mainly about the following areas, start here:

- Schematic-to-board implementation: `PCB Hardware Engineer`, `PCB Layout Engineer`, `High-Speed PCB Engineer`
- Control boards and embedded platforms: `MCU Hardware Engineer`, `STM32 Hardware Engineer`, `Embedded Systems Hardware Engineer`
- Precision analog and signal-chain work: `Analog Hardware Engineer`, `Signal Chain Hardware Engineer`, `Mixed-Signal Hardware Engineer`
- Power, storage, and drives: `Power Hardware Engineer`, `Power Electronics Engineer`, `Motor Drive Hardware Engineer`, `BMS Hardware Engineer`
- Compliance, reliability, and corrective work: `EMC Hardware Engineer`, `Safety Compliance Engineer`, `Hardware Reliability Engineer`, `Certification Engineer (CE FCC UL and More)`
- Debug and validation closure: `Board-Level Debug Engineer`, `Hardware Test Engineer`, `Hardware Validation Engineer`, `EVT/DVT Engineer`
- Board-release, design-review, EVT/DVT issue-closure, and production-introduction reviews: use the matching `Hardware Design Review and Validation` skill

## ✨ What Makes This Repository Different

- It is organized by real hardware roles rather than by abstract knowledge topics
- It emphasizes engineering rules, constraints, verification logic, and deliverables instead of glossary-style descriptions
- It covers a full lifecycle from design and review to debug, validation, and production handoff
- It can be used both as an agent role library and as an internal capability map for hardware teams

## ⚖️ License

This repository is released under the [MIT License](./LICENSE). You may copy, modify, distribute, and use it commercially, as long as the original copyright and license notice are preserved.

## 🤝 Contributing

If you want to add skills, expand domains, refine role boundaries, or improve repository structure, read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

Before submitting changes, keep these standards in mind:

- Skill names should be clear and role boundaries should be explicit
- Frontmatter should include at least `name` and `description`
- Content should emphasize constraints, workflows, deliverables, and application scope
- Do not submit internal company materials, customer-sensitive content, or copyrighted assets you do not own

## ✅ GitHub Checks

GitHub Actions is configured to validate this repository on pull requests and manual runs:

- skill frontmatter completeness
- duplicate `name` values
- whether local skill links in `README.md` and `README.zh-CN.md` point to real files

These workflows are only for repository quality checks. They do not automatically install skills into any local agent directory.
## 🚀 Possible Next Steps

If you continue expanding this repository, these are strong next improvements:

- add a consistent naming and tagging system across domains
- add cross-skill composition suggestions such as `STM32 + EMC + Validation`
- keep the English and Chinese indexes synchronized
- clarify primary vs secondary roles where skill boundaries overlap
