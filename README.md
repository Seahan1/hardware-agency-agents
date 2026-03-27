# hardware-agency-agents

[English](./README.md) | [简体中文](./README.zh-CN.md)

![License](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-47-blue)
![Domains](https://img.shields.io/badge/domains-8-orange)
![Language](https://img.shields.io/badge/language-bilingual-purple)

Are you already used to AI giving hardware advice with great confidence while clearly not understanding hardware at all?

If you are tired of suggestions like "just make the ground trace wider" or "place the capacitor anywhere first and tune it later", this repository is built for you.

`hardware-agency-agents` is an open-source library of hardware engineering skills organized by real engineering roles. Each skill document focuses on a specific role boundary, technical constraints, workflows, communication style, and expected deliverables, so hardware tasks can be approached with more rigorous engineering judgment instead of generic assistant-style advice.

This repository is inspired by the organizational clarity of strong skill libraries, but all content here is written around the actual files in this repository, with a focus on Chinese hardware engineering practice, board-level constraints, and production-oriented design thinking.

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

- Board implementation: `PCB硬件工程师`
- STM32 boards: `STM32硬件工程师`
- Power design: `电源硬件工程师`
- EMC and corrective action: `EMC硬件工程师`
- Validation closure: `硬件验证工程师`

## 📢 Public Notes

- This repository is a collection of hardware skill documents, not an official built-in library for any single agent platform
- The content is intended for role selection, design discussion, review guidance, and engineering analysis, not as an automatic guarantee of project correctness
- Users should still validate all conclusions against datasheets, standards, measurements, and project-specific constraints
- This repository is not officially affiliated with ST, TI, NXP, ADI, Altium, KiCad, or other vendors and platforms mentioned in hardware workflows

## 📦 Overview

- 47 hardware-related skills
- 8 engineering domains
- Coverage across PCB implementation, embedded hardware, power, EMC/compliance, validation, SoC/FPGA platforms, and communication interfaces
- Suitable for schematic review, PCB constraint analysis, debug work, validation planning, and production-readiness discussions

## 🧭 How To Use

You can treat each `.md` file in this repository as a reusable specialist role template:

1. When the task boundary is clear, choose the most relevant skill as the primary role.
2. When the problem crosses domains, choose one primary skill and add one or two closely related supporting skills.
3. When the task is in review, validation, debug, or production handoff stages, prefer skills that emphasize constraints, verification, and deliverables instead of pure functional discussion.

Typical examples:

- STM32 control board schematic review: start with `STM32硬件工程师`, optionally add `PCB硬件工程师` and `EMC硬件工程师`
- Buck converter stability and thermal analysis: start with `电源硬件工程师`
- High-speed board layout and impedance constraints: start with `高速PCB工程师` or `SI/PI工程师`
- EVT/DVT validation closure: start with `硬件验证工程师` or `EVT/DVT工程师`

## 🗂️ Repository Structure

```text
hardware-agency-agents/
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

- Each `.md` file under the domain folders is a skill document
- The repository root currently also contains a mirrored `PCB硬件工程师.md` file

## 🧰 Skill Index

### PCB and Board-Level Implementation (9)

| Skill | Focus |
| --- | --- |
| [DFA工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/DFA%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Design for assembly, soldering risk, component spacing, orientation, and reworkability |
| [DFM工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/DFM%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Design for manufacturability, process limits, panelization, via process, and fabrication data review |
| [PCB Layout工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/PCB%20Layout%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Layout and routing quality, stackup planning, constraints, impedance, vias, and return paths |
| [PCB封装库工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/PCB%E5%B0%81%E8%A3%85%E5%BA%93%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Footprint library quality, pad rules, 3D models, and naming standards |
| [PCB硬件工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/PCB%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | End-to-end board implementation from schematic to manufacturable PCB with SI, PI, EMC, DFM, and outputs |
| [SI/PI工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/SIPI%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Signal integrity and power integrity modeling, simulation, diagnosis, and correction |
| [射频硬件工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/%E5%B0%84%E9%A2%91%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | RF front-end implementation, impedance matching, antenna coordination, and RF debug |
| [硬件工艺工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/%E7%A1%AC%E4%BB%B6%E5%B7%A5%E8%89%BA%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | SMT/DIP process, manufacturing introduction, and process coordination |
| [高速PCB工程师](./PCB%20%E4%B8%8E%E6%9D%BF%E7%BA%A7%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%90%91/%E9%AB%98%E9%80%9FPCB%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | High-speed board constraints, differential routing, length matching, impedance, and crosstalk control |

### Reliability, EMC, and Compliance (8)

| Skill | Focus |
| --- | --- |
| [EMC硬件工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/EMC%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | EMC design, diagnosis, and closure from board level to system level |
| [EMI整改工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/EMI%E6%95%B4%E6%94%B9%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | EMI problem localization, interference source analysis, and corrective actions |
| [ESD防护工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/ESD%E9%98%B2%E6%8A%A4%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | ESD protection schemes, TVS selection, discharge paths, and interface protection |
| [失效分析工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/%E5%A4%B1%E6%95%88%E5%88%86%E6%9E%90%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Failure reproduction, root cause analysis, component failure modes, and stress-related faults |
| [安规工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/%E5%AE%89%E8%A7%84%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Electrical safety design, insulation boundaries, risk assessment, and certification preparation |
| [环境测试工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/%E7%8E%AF%E5%A2%83%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Temperature, vibration, drop, aging, and environmental stress testing |
| [硬件可靠性工程师](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/%E7%A1%AC%E4%BB%B6%E5%8F%AF%E9%9D%A0%E6%80%A7%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Derating, lifetime, thermal stress, environmental robustness, and MTBF-related methods |
| [认证工程师（CE/FCC/UL等）](./%E5%8F%AF%E9%9D%A0%E6%80%A7%20EMC%20%E5%AE%89%E8%A7%84%E6%96%B9%E5%90%91/%E8%AE%A4%E8%AF%81%E5%B7%A5%E7%A8%8B%E5%B8%88%EF%BC%88CE_FCC_UL%E7%AD%89%EF%BC%89.md) | Regulatory certification documents, lab coordination, and corrective support |

### Embedded Hardware (7)

| Skill | Focus |
| --- | --- |
| [MCU硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/MCU%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | MCU minimum system, reset, clocks, download interface, and board debug |
| [单片机硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E5%8D%95%E7%89%87%E6%9C%BA%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Single-chip control hardware, buses, logic levels, pull-up/down handling, and protection |
| [嵌入式硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Board-level embedded hardware with MCU/MPU peripherals, interfaces, power, and joint debug |
| [嵌入式系统硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%B3%BB%E7%BB%9F%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Complex embedded platforms, DDR, Flash, buses, timing, and system architecture |
| [工控硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E5%B7%A5%E6%8E%A7%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Industrial anti-interference, isolation, surge, lightning, and wide-temperature design |
| [控制板硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E6%8E%A7%E5%88%B6%E6%9D%BF%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Controller main boards, functional boards, drive/protection design, and bring-up |
| [自动化控制硬件工程师](./%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%A1%AC%E4%BB%B6%E6%96%B9%E5%90%91/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%8E%A7%E5%88%B6%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Automation control hardware, IO, relays, industrial buses, drives, and sensing |

### Digital / Analog / Mixed-Signal (7)

| Skill | Focus |
| --- | --- |
| [STM32硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/STM32%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | STM32 minimum system, Boot, SWD, ADC reference, and peripheral board design |
| [低功耗硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E4%BD%8E%E5%8A%9F%E8%80%97%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Battery-powered low-power planning, sleep/wake design, and power budgeting |
| [信号链硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E4%BF%A1%E5%8F%B7%E9%93%BE%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Sensor-to-processor signal conditioning, filtering, isolation, and error-chain analysis |
| [数字硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E6%95%B0%E5%AD%97%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Digital logic, timing constraints, interfaces, board implementation, and debug |
| [数模混合硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E6%95%B0%E6%A8%A1%E6%B7%B7%E5%90%88%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Mixed-signal partitioning, grounding, sampling synchronization, and interference control |
| [模拟硬件工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E6%A8%A1%E6%8B%9F%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Op-amp circuits, filtering, signal conditioning, noise, and stability analysis |
| [高速数字电路工程师](./%E6%95%B0%E5%AD%97%20:%20%E6%A8%A1%E6%8B%9F%20:%20%E6%B7%B7%E5%90%88%E4%BF%A1%E5%8F%B7%E6%96%B9%E5%90%91/%E9%AB%98%E9%80%9F%E6%95%B0%E5%AD%97%E7%94%B5%E8%B7%AF%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | High-speed interfaces, timing margin, reference planes, and board-level debug |

### Testing and Validation (6)

| Skill | Focus |
| --- | --- |
| [EVT/DVT工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/EVT_DVT%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Engineering sample validation, risk identification, and maturity judgment |
| [实验室测试工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/%E5%AE%9E%E9%AA%8C%E5%AE%A4%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Lab instruments, execution discipline, data capture, and repeatability |
| [板级调试工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/%E6%9D%BF%E7%BA%A7%E8%B0%83%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Power-up, clocks, reset, interfaces, and fault localization |
| [硬件测试工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/%E7%A1%AC%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Functional, performance, boundary, and stability testing |
| [硬件验证工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/%E7%A1%AC%E4%BB%B6%E9%AA%8C%E8%AF%81%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Validation planning, defect closure, and EVT/DVT/PVT gate decisions |
| [自动化测试硬件工程师](./%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%AA%8C%E8%AF%81%E6%96%B9%E5%90%91/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Test fixtures, interface control, production test links, and automation platforms |

### Power and Power Electronics (5)

| Skill | Focus |
| --- | --- |
| [BMS硬件工程师](./%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E6%96%B9%E5%90%91/BMS%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Cell sensing, balancing, protection, high-voltage safety, and isolated communication |
| [储能硬件工程师](./%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E6%96%B9%E5%90%91/%E5%82%A8%E8%83%BD%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Energy storage modules, power conversion, protection, and thermal management |
| [功率电子工程师](./%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E6%96%B9%E5%90%91/%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Mid/high-power conversion, gate drive, magnetics, thermal design, and loss analysis |
| [电机驱动硬件工程师](./%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E6%96%B9%E5%90%91/%E7%94%B5%E6%9C%BA%E9%A9%B1%E5%8A%A8%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Half-bridge/full-bridge topology, current sensing, protection, and motor-drive control boards |
| [电源硬件工程师](./%E7%94%B5%E6%BA%90%E4%B8%8E%E5%8A%9F%E7%8E%87%E7%94%B5%E5%AD%90%E6%96%B9%E5%90%91/%E7%94%B5%E6%BA%90%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | AC/DC, DC/DC, LDO, power trees, compensation, thermal design, and protection strategies |

### Platform and Low-Level Board Coordination (4)

| Skill | Focus |
| --- | --- |
| [CPLD工程师](./%E8%8A%AF%E7%89%87%E5%B9%B3%E5%8F%B0%E4%B8%8E%E5%BA%95%E5%B1%82%E6%9D%BF%E7%BA%A7%E5%8D%8F%E5%90%8C%E6%96%B9%E5%90%91/CPLD%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Basic programmable logic, interface conversion, IO levels, timing, and configuration |
| [FPGA硬件工程师](./%E8%8A%AF%E7%89%87%E5%B9%B3%E5%8F%B0%E4%B8%8E%E5%BA%95%E5%B1%82%E6%9D%BF%E7%BA%A7%E5%8D%8F%E5%90%8C%E6%96%B9%E5%90%91/FPGA%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | FPGA power rails, clocks, configuration, multi-voltage domains, and high-speed IO |
| [SoC硬件平台工程师](./%E8%8A%AF%E7%89%87%E5%B9%B3%E5%8F%B0%E4%B8%8E%E5%BA%95%E5%B1%82%E6%9D%BF%E7%BA%A7%E5%8D%8F%E5%90%8C%E6%96%B9%E5%90%91/SoC%E7%A1%AC%E4%BB%B6%E5%B9%B3%E5%8F%B0%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | SoC/MPU platforms, DDR, power sequencing, PMIC coordination, and boot configuration |
| [芯片应用工程师（FAE/AE偏硬件）](./%E8%8A%AF%E7%89%87%E5%B9%B3%E5%8F%B0%E4%B8%8E%E5%BA%95%E5%B1%82%E6%9D%BF%E7%BA%A7%E5%8D%8F%E5%90%8C%E6%96%B9%E5%90%91/%E8%8A%AF%E7%89%87%E5%BA%94%E7%94%A8%E5%B7%A5%E7%A8%8B%E5%B8%88%EF%BC%88FAE_AE%E5%81%8F%E7%A1%AC%E4%BB%B6%EF%BC%89.md) | Application support, reference design adaptation, and customer-facing hardware analysis |

### Communication and Interfaces (1)

| Skill | Focus |
| --- | --- |
| [通信硬件工程师](./%E9%80%9A%E4%BF%A1%E4%B8%8E%E6%8E%A5%E5%8F%A3%E6%96%B9%E5%90%91/%E9%80%9A%E4%BF%A1%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88.md) | Communication boards, high-speed interfaces, link debug, transmission lines, and EMC-aware design |

## 🎯 How To Choose A Skill

If your task is mainly about the following areas, start here:

- Schematic-to-board implementation: `PCB硬件工程师`, `PCB Layout工程师`, `高速PCB工程师`
- Control boards and embedded platforms: `MCU硬件工程师`, `STM32硬件工程师`, `嵌入式系统硬件工程师`
- Precision analog and signal-chain work: `模拟硬件工程师`, `信号链硬件工程师`, `数模混合硬件工程师`
- Power, storage, and drives: `电源硬件工程师`, `功率电子工程师`, `电机驱动硬件工程师`, `BMS硬件工程师`
- Compliance, reliability, and corrective work: `EMC硬件工程师`, `安规工程师`, `硬件可靠性工程师`, `认证工程师（CE/FCC/UL等）`
- Debug and validation closure: `板级调试工程师`, `硬件测试工程师`, `硬件验证工程师`, `EVT/DVT工程师`

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
- whether local skill links in `README.md` point to real files

These workflows are only for repository quality checks. They do not automatically install skills into any local agent directory.
## 🚀 Possible Next Steps

If you continue expanding this repository, these are strong next improvements:

- add a consistent naming and tagging system across domains
- add cross-skill composition suggestions such as `STM32 + EMC + Validation`
- add English aliases or search-oriented indexes
- clarify primary vs secondary roles where skill boundaries overlap
