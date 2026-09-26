# 部署与配置指南（Setup & Configuration）

本仓库（`stanford-cs-learning-packs`）的**环境配置**与**内容审计修复**记录。

- 环境配置：让 omp 发挥全部能力的推荐设置 + 一键脚本。
- 内容修复：针对 6 条 GitHub issue 的审计修复（v2.4）。

---

## 一、推荐开启的配置项清单

| 分类 | 配置项 | 默认值 | 推荐值 | 核心价值 |
|---|---|---|---|---|
| 代码自愈 | `edit.autoRepair.enabled` | false | true | 大范围重构或行号微移时自动计算 AST 差异修复补丁，避免报 `Patch failed` 中断 |
| 语义搜索 | `astGrep.enabled` | false | true | 启用语法树级别代码搜索（`xd://ast_grep`），比普通文本正则更精准 |
| 工程规范 | `lsp.formatOnWrite` | false | true | 代码写入/修改后自动调用对应语言 LSP 格式化，保持代码整洁 |
| 多任务协作 | `task.enableLsp` | false | true | 允许后台并行子代理获取代码编译与诊断信息，防止交错代码 |
| 长期记忆 | `memory.backend` | off | mnemopi | 启用本地持久化事实与经验存储，跨 Session 沉淀用户习惯与项目约定 |
| 自动学习 | `autolearn.enabled` | false | true | 任务排查或踩坑成功后自动提炼经验沉淀为知识或固化为新技能 |
| 省流防爆 | `compaction.idleEnabled` | false | true | 连续长会话空闲时自动压缩超长工具输出，大幅降低 Token 消耗 |
| 安全回滚 | `checkpoint.enabled` | false | true | 开启临时快照检查点（`xd://checkpoint` / `xd://rewind`），大改前后可无损回滚 |
| 浏览器联动 | `browser.relay` | false | true | 支持接管本地真实 Chrome 浏览器会话，免重复登录，支持复杂网页操作 |
| 生态兼容 | `skills.enableClaudeUser` | false | true | 自动兼容读取 `~/.claude/skills` 下已有 Claude Code 全局技能 |
| 性能感知 | `display.showTokenUsage` | false | true | 底部实时展示每轮 Token 消耗 |
| 性能感知 | `display.showTurnTime` | false | true | 底部实时展示单轮耗时，直观排查慢调用 |

### Bash / macOS / Linux 一键应用

```bash
# 1. 核心生产力与代码质量
omp config set edit.autoRepair.enabled true
omp config set astGrep.enabled true
omp config set lsp.formatOnWrite true
omp config set task.enableLsp true

# 2. 记忆与自动学习
omp config set memory.backend mnemopi
omp config set autolearn.enabled true

# 3. 上下文与安全回滚
omp config set compaction.idleEnabled true
omp config set checkpoint.enabled true

# 4. 浏览器接管与生态兼容
omp config set browser.relay true
omp config set skills.enableClaudeUser true

# 5. 终端监控与可视化
omp config set display.showTokenUsage true
omp config set display.showTurnTime true
```

### Windows (CMD / PowerShell)

```powershell
omp config set edit.autoRepair.enabled true; `
omp config set astGrep.enabled true; `
omp config set lsp.formatOnWrite true; `
omp config set task.enableLsp true; `
omp config set memory.backend mnemopi; `
omp config set autolearn.enabled true; `
omp config set compaction.idleEnabled true; `
omp config set checkpoint.enabled true; `
omp config set browser.relay true; `
omp config set skills.enableClaudeUser true; `
omp config set display.showTokenUsage true; `
omp config set display.showTurnTime true
```

### 说明

`memory.backend` 推荐 `mnemopi`（而非 `local`）：它是当前实际在用的持久后端，记忆系统依赖它；降级成 `local` 可能破坏跨会话记忆。其余项均为上述一键脚本覆盖。

---

## 二、内容审计修复记录（对应 6 条 issue）

所有修复已随 **Release v2.4** 落地，`tools/verify_pack.py` 对 11 个包全 PASS。Release：`https://github.com/guohongbin-git/stanford-cs-learning-packs/releases/tag/v2.4`

| # | 类型 | 修复内容 |
|---|---|---|
| #1 | 审计 | README「讲次/talk」列与 `course_ir.json` 任何字段都不匹配 → 重列为可核验的「绑定讲次(派生)/talk」，加「讲次数字说明」；SEE 课（cs106a/b/107/229）讲次为主题派生标题，置 `official:false`，逐字官方讲次名保留 `official:true` |
| #2 | 审计② | 官方讲次多为改写非逐字 → SEE 课全部置 `official:false`；删除编造讲次（CS229 Self-Supervised/Societal Impact、CS221 CSP）；9/11 包测验复制 → 8 个包各写 9 道与周对齐、正确答案不重复的小测 |
| #3 | 审计③ | relations 合成链成环 → 打破全部合成关系环（移除 93 条成环边，11 包 0 环）；status 三态失效 → 阐明 status 三态语义（TEACHING_RECONSTRUCTION 诚实默认，SOURCE_CONFIRMED 仅逐字官方，HYPOTHESIS 未核实）；program 级 SOURCE_CONFIRMED 滥用 → evidence_status 修正（searched_not_found→VERIFIED_ABSENT，157 门） |
| #4 | fix(schema) | CS336 `failure_conditions` 类型不一致 → 由 str 统一为 `list[str]`（90 条）；跨课同名概念定义漂移 → Kernel 拆分：CS230 `Convolutional Kernel` / CS336 `GPU Kernel`，CS229 `Kernel Trick` 独立，跨包引用同步更新 |
| #5 | fix(content) | CS106A 全周小测重复占位符 → 8 包补 9 道不重复小测；CS229 Agent 契约缩水 → 补全 9 周 Agent 契约（goal/inputs/actions/evidence/risks）；CS25 seminar schema 说明 |
| #6 | feat(路线图) | 路线图部分落地：`verify_pack.py` 新增 [6] 小测跨周去重 + [7] failure_conditions 类型检查（P0）；MCP 服务化 / AI 交互抽屉为后续 P1/P2 |

### 校验

```bash
python3 tools/verify_pack.py docs/courses/<code>
```

6 项检查：manifest 完整性、HTML 自包含 + 内嵌 JSON 逐字段一致、schema、周<->概念双向一致、关系可解析、模板骨架命中数；v2.4 新增小测跨周去重与 failure_conditions 类型检查。

---

## 三、给使用者 / 贡献者的两个入口

1. **人**：打开 Pages 站点 → 点课程代码 → 直接是交互式课程（周导航、概念抽屉、双视图、小测进度），纯静态、无外链依赖。
2. **Agent**：读根 `AGENTS.md`（全局宪法）→ 读某课 `AGENTS.md`（版本边界）→ `course_ir.json` → `concepts.json`；或直接 ref `https://guohongbin-git.github.io/stanford-cs-learning-packs/courses/cs336/concepts.json`。
