# Stanford CS 课程总目录（Program IR v0.5）

`program_ir.json` 是程序级课程目录与依赖图，用于决定哪些课可以做成学习包、按什么顺序做。

## 字段

| 字段 | 说明 |
|---|---|
| `courses[]` | 168 门 Stanford CS 课程：code / title / level / track / evidence_url / material_status / target_offering / public_materials / prerequisites |
| `dependency_dag` | 依赖边（prerequisite → dependent，标注 official / inferred）、环、孤岛、推荐拓扑序 |
| `statistics` | 分层计数与生成队列 |

## 素材状态分层

| 状态 | 数量 | 含义 |
|---|---|---|
| `active_recent` | 3 | 确认有 2023 年及以后的官方公开播放列表 → 可生成 |
| `archive_official` | 8 | 官方历史最佳公开版本（标注真实 offering 年份）→ 可生成 |
| `searched_not_found` | 8 | 已专项检索（SEE / 课程存档 / 官方频道）确认无公开录像 → 出队 |
| `pending_verification` | 149 | 尚未做素材检索 |

## 已生成学习包（11 门）

见仓库 `docs/courses/`；对应关系：`active_recent` 3 门 + `archive_official` 8 门全部完成。
