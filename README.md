# hardware-agency-agents

[English](./README.md) | [简体中文](./README.zh-CN.md)

![License](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-47-blue)
![Domains](https://img.shields.io/badge/domains-8-orange)
![Language](https://img.shields.io/badge/language-bilingual-purple)

Are you already used to AI giving hardware advice with great confidence while clearly not understanding hardware at all?

If you are tired of suggestions like "just make the ground trace wider" or "place the capacitor anywhere first and tune it later", this repository is built for you.

`hardware-agency-agents` is an open-source library of hardware engineering skills organized by real engineering roles. Each skill document focuses on a specific role boundary, technical constraints, workflows, communication style, and expected deliverables, so hardware tasks can be approached with more rigorous engineering judgment instead of generic assistant-style advice.

This repository is inspired by the organizational clarity of strong skill libraries, and it now maintains synchronized Chinese and English skill documents around the actual files in this repository, with a focus on board-level constraints and production-oriented design thinking.

## 📚 Table of Contents

- [Why This Repo Exists](#-why-this-repo-exists)
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

## 🧠 Why This Repo Exists

Most AI systems can talk about electronics, but that does not mean they can reason like a real hardware engineer.

This repository exists to narrow that gap:

- turn generic AI assistance into role-based hardware reasoning
- make constraints, failure mechanisms, verification logic, and deliverables explicit
- reduce low-quality advice that ignores physics, manufacturability, EMC, safety, and production reality
- provide reusable specialist roles for real board-level engineering workflows

## ⚡ Quick Start

1. Pick the closest skill for your task from the index below.
2. Read that skill as the primary engineering role.
3. Add one or two adjacent skills when the task crosses domains.
4. Use the skill content to frame review comments, design constraints, debug hypotheses, and validation plans.

Suggested starting points:

- Board implementation: `PCB Hardware Engineer`
- STM32 boards: `STM32 Hardware Engineer`
- Power design: `Power Hardware Engineer`
- EMC and corrective action: `EMC Hardware Engineer`
- Validation closure: `Hardware Validation Engineer`

## 📢 Public Notes

- This repository is a collection of hardware skill documents, not an official built-in library for any single agent platform
- The content is intended for role selection, design discussion, review guidance, and engineering analysis, not as an automatic guarantee of project correctness
- Users should still validate all conclusions against datasheets, standards, measurements, and project-specific constraints
- This repository is not officially affiliated with ST, TI, NXP, ADI, Altium, KiCad, or other vendors and platforms mentioned in hardware workflows

## 📦 Overview

- 47 hardware role skills with English and Chinese versions
- 8 engineering domains
- Coverage across PCB implementation, embedded hardware, power, EMC/compliance, validation, SoC/FPGA platforms, and communication interfaces
- Suitable for schematic review, PCB constraint analysis, debug work, validation planning, and production-readiness discussions

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

## 🗂️ Repository Structure

```text
hardware-agency-agents/
├── hardware-agency-agents-en/
│   ├── PCB and Board-Level Implementation/
│   ├── Reliability EMC and Safety/
│   ├── Embedded Hardware/
│   ├── Digital Analog and Mixed-Signal/
│   ├── Testing and Validation/
│   ├── Power and Power Electronics/
│   ├── Chip Platforms and Low-Level Board Co-Design/
│   └── Communication and Interfaces/
└── hardware-agency-agents-cn/
    ├── PCB 与板级实现方向/
    ├── 可靠性 EMC 安规方向/
    ├── 嵌入式硬件方向/
    ├── 数字 : 模拟 : 混合信号方向/
    ├── 测试与验证方向/
    ├── 电源与功率电子方向/
    ├── 芯片平台与底层板级协同方向/
    └── 通信与接口方向/
```

Notes:

- `README.md` is the default English landing page
- `README.zh-CN.md` is the matching Simplified Chinese page
- `hardware-agency-agents-en` stores the English skill set
- `hardware-agency-agents-cn` stores the Chinese skill set

## 🧰 Skill Index

### PCB and Board-Level Implementation (9)

| Skill | Focus |
| --- | --- |
| [DFA Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/DFA%20Engineer.md) | Design for assembly, soldering risk, component spacing, orientation, and reworkability |
| [DFM Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/DFM%20Engineer.md) | Design for manufacturability, process limits, panelization, via process, and fabrication data review |
| [PCB Layout Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/PCB%20Layout%20Engineer.md) | Layout and routing quality, stackup planning, constraints, impedance, vias, and return paths |
| [PCB Footprint Library Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/PCB%20Footprint%20Library%20Engineer.md) | Footprint library quality, pad rules, 3D models, and naming standards |
| [PCB Hardware Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/PCB%20Hardware%20Engineer.md) | End-to-end board implementation from schematic to manufacturable PCB with SI, PI, EMC, DFM, and outputs |
| [SI/PI Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/SI-PI%20Engineer.md) | Signal integrity and power integrity modeling, simulation, diagnosis, and correction |
| [RF Hardware Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/RF%20Hardware%20Engineer.md) | RF front-end implementation, impedance matching, antenna coordination, and RF debug |
| [Hardware Process Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/Hardware%20Process%20Engineer.md) | SMT/DIP process, manufacturing introduction, and process coordination |
| [High-Speed PCB Engineer](./hardware-agency-agents-en/PCB%20and%20Board-Level%20Implementation/High-Speed%20PCB%20Engineer.md) | High-speed board constraints, differential routing, length matching, impedance, and crosstalk control |

### Reliability, EMC, and Compliance (8)

| Skill | Focus |
| --- | --- |
| [EMC Hardware Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/EMC%20Hardware%20Engineer.md) | EMC design, diagnosis, and closure from board level to system level |
| [EMI Remediation Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/EMI%20Remediation%20Engineer.md) | EMI problem localization, interference source analysis, and corrective actions |
| [ESD Protection Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/ESD%20Protection%20Engineer.md) | ESD protection schemes, TVS selection, discharge paths, and interface protection |
| [Failure Analysis Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/Failure%20Analysis%20Engineer.md) | Failure reproduction, root cause analysis, component failure modes, and stress-related faults |
| [Safety Compliance Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/Safety%20Compliance%20Engineer.md) | Electrical safety design, insulation boundaries, risk assessment, and certification preparation |
| [Environmental Test Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/Environmental%20Test%20Engineer.md) | Temperature, vibration, drop, aging, and environmental stress testing |
| [Hardware Reliability Engineer](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/Hardware%20Reliability%20Engineer.md) | Derating, lifetime, thermal stress, environmental robustness, and MTBF-related methods |
| [Certification Engineer (CE FCC UL and More)](./hardware-agency-agents-en/Reliability%20EMC%20and%20Safety/Certification%20Engineer%20-%20CE%20FCC%20UL%20and%20More.md) | Regulatory certification documents, lab coordination, and corrective support |

### Embedded Hardware (7)

| Skill | Focus |
| --- | --- |
| [MCU Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/MCU%20Hardware%20Engineer.md) | MCU minimum system, reset, clocks, download interface, and board debug |
| [Microcontroller Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Microcontroller%20Hardware%20Engineer.md) | Single-chip control hardware, buses, logic levels, pull-up/down handling, and protection |
| [Embedded Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Embedded%20Hardware%20Engineer.md) | Board-level embedded hardware with MCU/MPU peripherals, interfaces, power, and joint debug |
| [Embedded Systems Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Embedded%20Systems%20Hardware%20Engineer.md) | Complex embedded platforms, DDR, Flash, buses, timing, and system architecture |
| [Industrial Control Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Industrial%20Control%20Hardware%20Engineer.md) | Industrial anti-interference, isolation, surge, lightning, and wide-temperature design |
| [Control Board Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Control%20Board%20Hardware%20Engineer.md) | Controller main boards, functional boards, drive/protection design, and bring-up |
| [Automation Control Hardware Engineer](./hardware-agency-agents-en/Embedded%20Hardware/Automation%20Control%20Hardware%20Engineer.md) | Automation control hardware, IO, relays, industrial buses, drives, and sensing |

### Digital / Analog / Mixed-Signal (7)

| Skill | Focus |
| --- | --- |
| [STM32 Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/STM32%20Hardware%20Engineer.md) | STM32 minimum system, Boot, SWD, ADC reference, and peripheral board design |
| [Low-Power Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/Low-Power%20Hardware%20Engineer.md) | Battery-powered low-power planning, sleep/wake design, and power budgeting |
| [Signal Chain Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/Signal%20Chain%20Hardware%20Engineer.md) | Sensor-to-processor signal conditioning, filtering, isolation, and error-chain analysis |
| [Digital Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/Digital%20Hardware%20Engineer.md) | Digital logic, timing constraints, interfaces, board implementation, and debug |
| [Mixed-Signal Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/Mixed-Signal%20Hardware%20Engineer.md) | Mixed-signal partitioning, grounding, sampling synchronization, and interference control |
| [Analog Hardware Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/Analog%20Hardware%20Engineer.md) | Op-amp circuits, filtering, signal conditioning, noise, and stability analysis |
| [High-Speed Digital Circuit Engineer](./hardware-agency-agents-en/Digital%20Analog%20and%20Mixed-Signal/High-Speed%20Digital%20Circuit%20Engineer.md) | High-speed interfaces, timing margin, reference planes, and board-level debug |

### Testing and Validation (6)

| Skill | Focus |
| --- | --- |
| [EVT/DVT Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/EVT-DVT%20Engineer.md) | Engineering sample validation, risk identification, and maturity judgment |
| [Lab Test Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/Lab%20Test%20Engineer.md) | Lab instruments, execution discipline, data capture, and repeatability |
| [Board-Level Debug Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/Board-Level%20Debug%20Engineer.md) | Power-up, clocks, reset, interfaces, and fault localization |
| [Hardware Test Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/Hardware%20Test%20Engineer.md) | Functional, performance, boundary, and stability testing |
| [Hardware Validation Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/Hardware%20Validation%20Engineer.md) | Validation planning, defect closure, and EVT/DVT/PVT gate decisions |
| [Automated Test Hardware Engineer](./hardware-agency-agents-en/Testing%20and%20Validation/Automated%20Test%20Hardware%20Engineer.md) | Test fixtures, interface control, production test links, and automation platforms |

### Power and Power Electronics (5)

| Skill | Focus |
| --- | --- |
| [BMS Hardware Engineer](./hardware-agency-agents-en/Power%20and%20Power%20Electronics/BMS%20Hardware%20Engineer.md) | Cell sensing, balancing, protection, high-voltage safety, and isolated communication |
| [Energy Storage Hardware Engineer](./hardware-agency-agents-en/Power%20and%20Power%20Electronics/Energy%20Storage%20Hardware%20Engineer.md) | Energy storage modules, power conversion, protection, and thermal management |
| [Power Electronics Engineer](./hardware-agency-agents-en/Power%20and%20Power%20Electronics/Power%20Electronics%20Engineer.md) | Mid/high-power conversion, gate drive, magnetics, thermal design, and loss analysis |
| [Motor Drive Hardware Engineer](./hardware-agency-agents-en/Power%20and%20Power%20Electronics/Motor%20Drive%20Hardware%20Engineer.md) | Half-bridge/full-bridge topology, current sensing, protection, and motor-drive control boards |
| [Power Hardware Engineer](./hardware-agency-agents-en/Power%20and%20Power%20Electronics/Power%20Hardware%20Engineer.md) | AC/DC, DC/DC, LDO, power trees, compensation, thermal design, and protection strategies |

### Platform and Low-Level Board Coordination (4)

| Skill | Focus |
| --- | --- |
| [CPLD Engineer](./hardware-agency-agents-en/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/CPLD%20Engineer.md) | Basic programmable logic, interface conversion, IO levels, timing, and configuration |
| [FPGA Hardware Engineer](./hardware-agency-agents-en/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/FPGA%20Hardware%20Engineer.md) | FPGA power rails, clocks, configuration, multi-voltage domains, and high-speed IO |
| [SoC Hardware Platform Engineer](./hardware-agency-agents-en/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/SoC%20Hardware%20Platform%20Engineer.md) | SoC/MPU platforms, DDR, power sequencing, PMIC coordination, and boot configuration |
| [Chip Applications Engineer (Hardware-Focused FAE AE)](./hardware-agency-agents-en/Chip%20Platforms%20and%20Low-Level%20Board%20Co-Design/Chip%20Applications%20Engineer%20-%20Hardware%20Focused%20FAE%20AE.md) | Application support, reference design adaptation, and customer-facing hardware analysis |

### Communication and Interfaces (1)

| Skill | Focus |
| --- | --- |
| [Communications Hardware Engineer](./hardware-agency-agents-en/Communication%20and%20Interfaces/Communications%20Hardware%20Engineer.md) | Communication boards, high-speed interfaces, link debug, transmission lines, and EMC-aware design |

## 🎯 How To Choose A Skill

If your task is mainly about the following areas, start here:

- Schematic-to-board implementation: `PCB Hardware Engineer`, `PCB Layout Engineer`, `High-Speed PCB Engineer`
- Control boards and embedded platforms: `MCU Hardware Engineer`, `STM32 Hardware Engineer`, `Embedded Systems Hardware Engineer`
- Precision analog and signal-chain work: `Analog Hardware Engineer`, `Signal Chain Hardware Engineer`, `Mixed-Signal Hardware Engineer`
- Power, storage, and drives: `Power Hardware Engineer`, `Power Electronics Engineer`, `Motor Drive Hardware Engineer`, `BMS Hardware Engineer`
- Compliance, reliability, and corrective work: `EMC Hardware Engineer`, `Safety Compliance Engineer`, `Hardware Reliability Engineer`, `Certification Engineer (CE FCC UL and More)`
- Debug and validation closure: `Board-Level Debug Engineer`, `Hardware Test Engineer`, `Hardware Validation Engineer`, `EVT/DVT Engineer`

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
