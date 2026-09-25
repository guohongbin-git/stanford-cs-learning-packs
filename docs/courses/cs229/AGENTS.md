# CS229 Machine Learning Agent Contract

## 1. Purpose
本文件定义 CS229 Spring 2022 archive_official 课程包的使用边界。
该包用于辅助理解机器学习概念、课程结构和复习路径。
它不是 Stanford 官方课程替代品，也不是考试或作业答案库。

## 2. Version Boundary
本包绑定 Stanford Online Machine Learning I Spring 2022 录制版本。
该版本属于 archive_official，而不是最新学期课程。
CS229 核心理论多年稳定，但 lecture 顺序、assignment 结构和课程材料可能随学期变化。

## 3. Read Order
建议先读取 course_ir.json 理解九周教学组织。
再读取 concepts.json 建立数学概念关系。
最后通过 HTML Human View 和 Agent View 进行学习检查。

## 4. Evidence Semantics
课程包中的内容来自公开课程主题重构。
Generative model、discriminative model、SVM、EM 等概念解释需要保持机器学习领域原始含义。
Agent 必须区分课程事实、教学解释和推导说明。

## 5. Agent Use Contract
Agent 可以帮助解释 CS229 概念关系。
Agent 可以根据课程结构生成复习问题。
Agent 不得声称代表课程教师，也不得补写不存在的讲义内容或论文结论。

## 6. 适用范围
本包适用于机器学习基础学习。
覆盖监督学习、生成模型、核方法、学习理论、无监督学习和强化学习入门。
适合课程预习、复习和知识导航。

## 7. 禁用场景
本包不能替代官方 problem set、考试材料或课程论坛讨论。
HTML 中的 quiz 用于学习检测，不等同于 Stanford 官方作业。
用户仍应完成官方练习以验证推导和编程能力。

## 8. Concept Usage
概念节点需要结合数学假设和应用场景理解。
例如 generative 与 discriminative 方法不能只按模型名称区分。
Agent 应说明模型适用条件、限制和典型失败原因。

## 9. 双视图
Human View 面向学习者展示课程主题和概念解释。
Agent View 提供结构化 canonical JSON。
两个视图共享同一数据源，避免解释和结构不一致。

## 10. Capability Rule
Agent 可以辅助概念检索、关系分析和学习规划。
涉及线性代数、概率论和优化推导时，应明确数学基础要求。
Agent 不应替代完整数学证明过程。

## 11. Skill Formation
CS229 学习需要具备线性代数、概率论、统计学习和优化基础。
学习者应理解模型假设，而不是只记忆算法名称。
课程目标是形成机器学习建模和实验分析能力。

## 12. Escalation
当问题涉及最新研究、论文实验结果或课程变更时，应转向原始来源。
Agent 不应根据课程包推测未提供的信息。
对于论文结论，必须引用真实论文或官方材料。

## 13. Update Rule
任何课程版本变化需要更新 version 和 target_offering。
新的 lecture、assignment 或 syllabus 变化不能覆盖旧版本证据。
archive_official 记录必须保留真实年份语义。

## 14. Maintenance Contract
维护者需要保证 JSON、HTML 和 manifest 哈希一致。
修改概念、课程结构或代理规则后必须重新执行 QA。
发布前需要检查唯一性、schema 和文件完整性。
