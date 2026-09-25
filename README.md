# Stanford CS Learning Packs — Human + Agent Shared Knowledge

[English](#english) · [中文](#中文)

## 中文

把 Stanford 公开计算机课程（视频 + 官方课程页）做成**人和 Agent 共用**的学习包。

每个包同时提供两种投影：

- **Human View**：单文件交互 HTML（周导航 / 概念抽屉 / 小测 / 进度）
- **Agent View**：`course_ir.json` + `concepts.json`，同一套概念身份、同一套关系
- **规则**：`AGENTS.md` 规定 Agent 该怎么用这套资料（版本边界、证据语义、能力判定、升级条件）

### 在线使用（GitHub Pages）

打开 <https://guohongbin-git.github.io/stanford-cs-learning-packs/> 选择课程。

### 已交付（11 门，均通过多轮独立核验）

| 课程 | 方向 | 素材绑定 | 概念 | 讲次/talk |
|---|---|---|---|---|
| CS106A Programming Methodology | 编程基础（SEE Java 版） | archive_official | 43 | 26 |
| CS106B Programming Abstractions | 编程基础（SEE C++ 版） | archive_official | 28 | 20 |
| CS107 Programming Paradigms | 系统基础（SEE 版） | archive_official | 30 | 18 |
| CS109 Probability for CS | 概率与统计 | Autumn 2022 | 35 | 20 |
| CS221 Artificial Intelligence | AI 基础 | Autumn 2021 | 32 | 16 |
| CS224N NLP with Deep Learning | 自然语言处理 | Winter 2021 | 34 | 18 |
| CS224W Machine Learning with Graphs | 图机器学习 | Autumn 2021 | 28 | 19 |
| CS229 Machine Learning | 机器学习 | Spring 2022 | 61 | 14 |
| CS230 Deep Learning | 深度学习 | Autumn 2025 | 60 | 9 |
| CS336 Language Modeling from Scratch | 大模型工程 | Spring 2025 | 90 | 17 |
| CS25 Transformers United | 前沿研讨 | 2023+ 届次 | 59 | 54 talks |

### 课程总目录

`program/program_ir.json` 是 168 门 Stanford CS 课程的程序级目录与依赖图，含素材状态分层：

- `active_recent`（3）：2023 年后的官方公开播放列表
- `archive_official`（8）：官方历史最佳公开版本
- `searched_not_found`（8）：已专项检索确认无公开录像（CS103/111/146/147/148/154/155/161）
- `pending_verification`（149）：尚未做素材检索

### 证据与免责

- 概念状态统一 `TEACHING_RECONSTRUCTION`：**教学重构，不是 Stanford 逐字讲义**，也不代表校方立场。
- 讲座/talk 条目区分 `official: true`（逐字取自官方页面）与 `official: false`（主题派生标签）。
- 与 Stanford 官方无隶属关系。原始课程版权归 Stanford 及其讲者。

### 校验

```bash
python3 tools/verify_pack.py docs/courses/cs336
```

### 目录

```
docs/      GitHub Pages 站点（courses/<code>/ 为各课程包）
program/   课程总目录 IR
tools/     校验脚本
```

---

## English

Public Stanford CS courses turned into **shared human/agent learning packs**: a self-contained interactive HTML for humans, structured `course_ir.json` + `concepts.json` for agents, and an `AGENTS.md` contract describing how agents may use the material.

- **Online use**: <https://guohongbin-git.github.io/stanford-cs-learning-packs/>
- **Delivered**: 11 course packs (CS106A/B/107, CS109, CS221, CS224N/W, CS229, CS230, CS336, CS25)
- **Program catalog**: `program/program_ir.json` — 168 Stanford CS courses with a dependency DAG and material-status tiers
- **Evidence policy**: every concept is `TEACHING_RECONSTRUCTION`; lecture/talk entries distinguish verbatim `official: true` titles from derived `official: false` labels; no Stanford affiliation
- **Verify**: `python3 tools/verify_pack.py docs/courses/cs336`