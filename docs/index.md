# Stanford CS 人机共学课程包

> 把 Stanford 公开计算机课程，做成**人和 Agent 共用**的学习包：可交互 HTML（人读）+ 结构化 IR / 概念库（Agent 读）+ AGENTS.md（使用规则）。

## 课程包一览（11 门，全部通过多轮独立核验）

| 课程 | 标题 | 方向 | 教学周 | 概念 | 证据绑定 |
|---|---|---|---|---|---|
| [CS106A](courses/cs106a/) | Programming Methodology（SEE Java 版） | 编程基础 | 9 | 43 | 26 讲 / 0 talk |
| [CS106B](courses/cs106b/) | Programming Abstractions（SEE C++ 版） | 编程基础 | 9 | 28 | 20 讲 / 0 talk |
| [CS107](courses/cs107/) | Programming Paradigms（SEE 版） | 系统基础 | 9 | 30 | 18 讲 / 0 talk |
| [CS109](courses/cs109/) | Probability for Computer Scientists（Autumn 2022） | 概率与统计 | 9 | 35 | 20 讲 / 0 talk |
| [CS221](courses/cs221/) | Artificial Intelligence（Autumn 2021） | AI 基础 | 9 | 32 | 16 讲 / 0 talk |
| [CS224N](courses/cs224n/) | NLP with Deep Learning（Winter 2021） | 自然语言处理 | 9 | 34 | 18 讲 / 0 talk |
| [CS224W](courses/cs224w/) | Machine Learning with Graphs（Autumn 2021） | 图机器学习 | 9 | 28 | 19 讲 / 0 talk |
| [CS229](courses/cs229/) | Machine Learning（Spring 2022） | 机器学习 | 9 | 61 | 14 讲 / 0 talk |
| [CS230](courses/cs230/) | Deep Learning（Autumn 2025） | 深度学习 | 9 | 60 | 9 讲 / 0 talk |
| [CS336](courses/cs336/) | Language Modeling from Scratch（Spring 2025） | 大模型工程 | 9 | 90 | 17 讲 / 0 talk |
| [CS25](courses/cs25/) | Transformers United（seminar） | 前沿研讨 | 主题聚类 | 59 | 54 讲 / 54 talk |

**打开方式**：点击课程代码，或在仓库 `docs/courses/<code>/` 下直接打开 HTML（Pages 会自动打开 index.html）。

## 学习路径

```
编程基础   CS106A → CS106B → CS107
数学与 AI  CS109 → CS221 / CS229 / CS224N / CS224W
深度学习   CS230
大模型     CS336
前沿研讨   CS25
```

## 每个包包含什么

| 文件 | 用途 | 读者 |
|---|---|---|
| `*_interactive_*.html` | 单文件交互课程：周导航、概念点击抽屉、Human/Agent 双视图、小测与进度 | 人 |
| `course_ir.json` | 课程结构：周次、学习目标、失败模式、小测、Agent 契约、讲次证据 | Agent |
| `concepts.json` | canonical 概念库：定义 / 为何重要 / 失效条件 / 例子 / 关系 / 周次 | 人 + Agent |
| `AGENTS.md` | 该包的使用规则：版本边界、证据语义、能力判定、升级条件 | Agent |
| `README.md` | 包说明与逐轮修复日志（Repair log） | 人 |
| `package_manifest.json` | 全文件 bytes + sha256 | 机器 |

## 证据与诚实边界

- 每个包都标注了**素材绑定**：`active_recent`（2023 年后的官方公开播放列表）或 `archive_official`（官方历史最佳版本）。
- 讲座/talk 条目区分 `official: true`（逐字取自官方页面）与 `official: false`（主题派生标签）。
- 概念状态统一为 `TEACHING_RECONSTRUCTION`：教学重构，**不是** Stanford 逐字讲义，也不代表官方立场。
- 完整 QA（逐页截图、contact sheet、渲染报告）随 Release 中的 zip 提供。

## 校验自己的副本

```bash
python3 tools/verify_pack.py docs/courses/cs336
```
会检查：manifest 的 bytes/sha256、HTML 内嵌 JSON 与独立文件是否逐字段一致、概念字段完整性、周↔概念双向一致、关系目标可解析、模板句骨架命中数。

## 目录结构

```
.
├── README.md          仓库说明
├── AGENTS.md          全局学习宪法（所有课程包共同遵守）
├── NOTICE.md          素材来源与免责声明
├── program/           课程总目录与依赖图（168 门 CS 课程，含素材状态分层）
├── docs/              GitHub Pages 站点
│   ├── index.md       本页
│   └── courses/       11 个课程包
└── tools/verify_pack.py
```
