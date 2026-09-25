# Contributing

[English](./CONTRIBUTING.md) | [简体中文](./CONTRIBUTING.zh-CN.md)

感谢你为这个硬件 skill 仓库补充内容。这个仓库的目标不是堆积术语，而是沉淀可复用、边界清晰、适合真实工程协作的角色化 skill。

## 提交前先确认

- 你新增的内容对应一个真实且可独立承担任务的硬件岗位或子角色
- 该 skill 与现有 skill 没有明显重复，只是命名不同
- 文档强调工程约束、工作流程、交付物和适用场景，而不是泛化介绍
- 不包含公司内部规范、客户资料、保密设计、受版权限制的截图或大段复制内容

## Skill 文件要求

每个 skill 均遵循 Codex / Claude Code / Antigravity CLI 标准格式，存放在独立目录下，文件统一命名为 `SKILL.md`：

- 英文版 skill：`skills/<skill-name>/SKILL.md`
- 中文版 skill：`skills.zh-CN/<skill-name>/SKILL.md`

`SKILL.md` 文件开头必须包含 YAML frontmatter，至少包括：

```yaml
---
name: example-hardware-engineer
description: 示例领域与任务协同 skill。用于典型任务、典型对象、常见问题、关键约束和交付物输出。
color: teal
---
```

要求如下：

- `name`：必须唯一，使用全小写连字符命名（如 `pcb-hardware-engineer`），与所在目录名完全一致
- `description`：必须完整说明职责边界、技术重点和典型应用场景（用于 Agent 激活判断）
- `color`：可选但建议保留，与现有风格一致即可

## Description 写作规范

每个 skill 的 `description` 建议统一采用 Agent 更容易触发的写法：

```text
[角色领域] skill。用于 [任务类型]、[典型对象]、[常见问题]、[关键约束] 和 [交付物]。
```

建议同时满足以下要求：

- 包含明确的领域词、任务词、对象词、问题词和输出词
- 优先写用户会搜索的对象、故障现象、评审动作和输出结果

## 内容要求

- 以“工程判断框架”写作，而不是教科书式知识罗列
- 强调输入条件、边界、失效机制、验证要求和交付结果
- 避免空泛表达，如“需要注意稳定性”“注意 EMI 问题”
- 尽量写成可执行的规则、流程和沟通方式
- 不要使用占位文本、未完成标题或省略号式残缺内容

## 方向分组
 
新增 skill 时，建议同步提交英文版与中文版（分别置于 `skills/<name>/SKILL.md` 与 `skills.zh-CN/<name>/SKILL.md`），归属于以下 8 个专业方向或硬件设计评审方向：

- `PCB 与板级实现方向` (`PCB and Board-Level Implementation`)
- `可靠性 EMC 安规方向` (`Reliability EMC and Safety`)
- `嵌入式硬件方向` (`Embedded Hardware`)
- `数字-模拟-混合信号方向` (`Digital Analog and Mixed-Signal`)
- `测试与验证方向` (`Testing and Validation`)
- `电源与功率电子方向` (`Power and Power Electronics`)
- `芯片平台与底层板级协同方向` (`Chip Platforms and Low-Level Board Co-Design`)
- `通信与接口方向` (`Communication and Interfaces`)
- `硬件设计评审与验证方向` (`Hardware Design Review and Validation`)

如果你认为必须新增一个新方向，请在 PR 描述中说明：

- 为什么现有目录不适合
- 新方向与已有方向的边界差异
- 预期后续还会容纳哪些 skill

## README 更新要求

如果你新增、删除或重命名了 skill，请同步更新 `README.md` 中的：

- 统计数量
- 对应方向的小节计数
- Skill Index 链接
- 必要时的选型建议

## Pull Request 建议

一个 PR 最好只做一类事情：

- 新增一个或一组相关 skill
- 修正文案和边界定义
- 调整目录结构
- 修复元数据或链接问题

这样更方便评审和回滚。
