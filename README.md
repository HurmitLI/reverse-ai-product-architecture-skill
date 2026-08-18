# Reverse AI Product Architecture Skill

一套适用于所有 AI 产品品类的“证据优先”产品拆解 Skill。

如果只拆解生图、生视频、AI 音频、数字人或多模态创作工作台，可使用更聚焦的 [AIGC 产品拆解 Skill](https://github.com/HurmitLI/reverse-aigc-product-architecture-skill)。两个 Skill 名称不同，可以同时安装。

它不局限于 OiiOii、LibTV 等生图/视频产品，也适用于：

- 蚂蚁阿福这类医疗与健康 AI
- AI 搜索、问答和 RAG 产品
- AI 助手、Copilot 和个人助理
- 智能客服、销售和运营 AI
- 编程与开发者 AI 工具
- 企业 AI、知识助手和 SaaS Copilot
- 推荐、排序和决策型 AI
- Agent 平台与自动化产品
- 图片、视频、音频和多模态 AIGC

Skill 从页面、截图、操作记录、对话、结果、错误和官方资料出发，逐层还原：

- 用户、场景、痛点、替代方案与价值主张
- 用户旅程、反馈、失败、恢复和人工接管
- AI 能力的输入、输出、自主程度和责任边界
- Agent、工作流、工具调用和下游交接
- 模型、路由、参数、限制、成本与降级
- 上下文、记忆、知识库、RAG 和数据关系
- 评测、内容安全、隐私、权限与高风险治理
- 套餐、额度、用量、计费、运营和指标
- As-Is、To-Be、关键风险和产品机会点
- 单 Agent 的功能等价 System Prompt
- 可追溯的 HTML 产品全景架构

## 核心原则

### 1. Agent 必须拆，但不能编

Agent 是核心分析维度，但不预设产品一定有多个 Agent。

- 页面明确出现 Agent：拆触发、I/O、工具、上下文、状态、交接和完成条件。
- 只看到功能阶段：记录为“能力组件”，确切 Agent 形态标为推断或未知。
- 没有 Agent 证据：分析单 Agent、隐式编排或普通服务的可能性，但不自行命名。

### 2. AI 结果成功不等于用户任务完成

必须区分：

1. 模型或工具调用成功
2. 业务任务状态完成
3. 用户目标真实达成

例如，Agent 说“已完成”只证明它说过；仍要检查业务对象、页面状态、外部动作、引用和最终结果。

### 3. 四级证据不能混淆

- 【已确认】：页面、官方资料或可复核结果直接支持
- 【合理推断】：多条行为事实支持，但内部实现不可见
- 【建议设计】：针对已观察问题提出的改进
- 【未知】：当前证据不足

### 4. 不把常见 AI 架构当成事实

不默认存在：

- 多 Agent
- RAG 或向量库
- 长期记忆
- 动态模型路由
- 自动评测
- 安全审核链
- 任务队列或特定云服务

只有页面或官方资料支持时才能确认。

## 能完成什么

### 用户旅程

从最早一条输入开始，检查页面反馈、AI 处理、用户选择、数据变化、失败和人工接管，输出主流程、修改/追问、失败/中断和权限/安全分支。

### AI 能力契约

逐项记录用户问题、输入、上下文/知识、输出、自主级别、验证方式、失败降级、成本/延迟和责任边界。

### Agent I/O 契约

只记录证据支持的 Agent 或能力组件，整理六类输入、可观察判断、工具权限、五类输出、上下文读写、完成条件、异常和下游交接。

### 模型、工具、上下文与知识

检查模型能力与限制、工具副作用、当前/会话/任务/长期上下文、用户私有知识、公共知识、RAG 引用和权限隔离。

### 评测、安全与治理

检查事实、引用、业务完成、用户反馈、内容安全、提示注入、越权工具、隐私、人工复核和申诉。医疗等高风险产品额外突出专业责任和紧急升级路径。

### 产品全景架构

合并用户流、Agent 流、工具/模型流、上下文/知识流、结果/数据流和评测安全流，输出十层架构、数据实体、ER 图、时序图、As-Is/To-Be 和风险优先级。

## 产品类型路由

每次分析都执行 AI 通用核心，再根据证据选择最多三个扩展：

| 产品类型 | 重点维度 |
|---|---|
| 医疗与健康 AI | 健康数据、证据、风险、人工复核、专业责任、隐私 |
| 搜索 / 问答 / RAG | 检索范围、引用、时效、权限、冲突、无答案 |
| 助手 / Copilot | 上下文、建议与执行边界、确认、撤销、记忆、集成 |
| 客服 / 运营 AI | 意图、知识、工单、转人工、质检、SLA |
| 编程 / 开发者 AI | 仓库上下文、工具权限、补丁、测试、回滚、安全 |
| 企业 AI / SaaS | 组织、RBAC、连接器、租户隔离、审计、企业计费 |
| 推荐 / 决策 AI | 候选、排序、解释、反馈、实验、公平、业务约束 |
| Agent 平台 / 自动化 | 编排、工具、状态机、人审、幂等、补偿、追踪 |
| 多模态 / AIGC | Prompt、素材、模型、生成资产、一致性、版权、成本 |

详细检查项见 `references/product-type-routing.md`。

## 目录结构

```text
.
├── README.md
└── skills/
    └── reverse-ai-product-architecture/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── evidence-protocol.md
        │   ├── product-type-routing.md
        │   ├── deliverable-specs.md
        │   └── architecture-schema.md
        ├── scripts/
        │   ├── inventory_screenshots.py
        │   └── validate_analysis.py
        └── assets/
            └── report-template.html
```

## 安装

```bash
git clone https://github.com/HurmitLI/reverse-ai-product-architecture-skill.git
cd reverse-ai-product-architecture-skill
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
cp -R skills/reverse-ai-product-architecture "$CODEX_SKILLS_DIR/"
```

开发时也可以使用符号链接：

```bash
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
ln -s "$(pwd)/skills/reverse-ai-product-architecture" "$CODEX_SKILLS_DIR/reverse-ai-product-architecture"
```

## 使用示例

### 医疗 AI

```text
使用 $reverse-ai-product-architecture，基于蚂蚁阿福的页面截图，拆解用户旅程、AI 能力边界、Agent、知识来源、人工责任、安全与医疗数据架构。
```

### AI 搜索 / RAG

```text
使用 $reverse-ai-product-architecture，分析这个 AI 搜索产品的检索范围、引用机制、Agent/工具、上下文、无答案处理、评测与产品架构。
```

### AI 编程工具

```text
使用 $reverse-ai-product-architecture，拆解它如何读取仓库、规划任务、调用终端和编辑工具、验证代码、处理权限、失败和回滚。
```

### Agent 平台

```text
使用 $reverse-ai-product-architecture，从最早一条任务开始，识别真实 Agent、I/O 契约、工具、状态机、全局上下文、模型和下游交接。
```

### AIGC

```text
使用 $reverse-ai-product-architecture，拆解这个 AI 视频产品从需求、剧本、素材、分镜到成片的用户流、Agent 流、工具/模型流和资产流。
```

### 单 Agent 功能等价 Prompt

```text
使用 $reverse-ai-product-architecture，只分析目标 Agent。先完成证据范围、I/O、工具、上下文、状态机和规则追溯，再写功能等价 System Prompt。
```

## 推荐输入

- 按时间顺序命名的页面截图
- 用户与 AI 的完整对话
- 搜索引用、知识来源和上传资料
- Agent、工具、任务、运行历史和错误状态
- 模型、参数、额度、套餐和计费页面
- 业务结果、反馈、转人工、审核和安全提示
- 官方帮助、隐私说明或开发文档（可选）

生成截图证据清单：

```bash
python3 skills/reverse-ai-product-architecture/scripts/inventory_screenshots.py \
  /path/to/screenshots \
  --output /path/to/evidence-manifest.csv
```

## 推荐交付顺序

1. 执行摘要
2. 证据来源与缺口
3. 用户、场景、价值和风险等级
4. 用户旅程与 AI 能力契约
5. 功能域与信息架构
6. Agent 清单与 I/O 契约
7. 模型、工具、上下文、记忆和知识
8. 状态机、数据实体和外部集成
9. 评测、安全、隐私与人工治理
10. 商业化与运营
11. 产品全景架构、As-Is/To-Be、风险和机会点
12. 证据追溯与未知问题

## HTML 模板

`assets/report-template.html` 提供四级证据配色、端到端六流、AI 产品分层架构、证据追溯和 As-Is/To-Be/风险区域。模板可直接替换语义占位符，也可以只复用视觉语言。

## 示例报告

- [通义听悟产品拆解](examples/通义听悟产品拆解.html)：基于通义听悟 Web 页面与阿里云官方资料，展示用户旅程、AI 能力契约、工作流、上下文与数据、商业化、风险以及 As-Is/To-Be 架构。

## 校验

校验 Skill：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skills/reverse-ai-product-architecture
```

校验 HTML 报告：

```bash
python3 skills/reverse-ai-product-architecture/scripts/validate_analysis.py \
  /path/to/product-architecture.html
```

校验器检查完整 HTML、重复 ID、四级证据标签、关键章节、S/E 证据编号和高风险越界表述。

## 安全与发布边界

- 浏览器默认只读，不主动触发高成本生成、支付、发布、删除或高风险业务操作。
- 不读取或输出 Cookie、Token、密码、鉴权头、医疗隐私和个人敏感信息。
- 不把公开“思考完成/规划完成”写成隐藏思维链。
- 不把口头计划直接当成工具成功。
- 不把常见 AI 架构、模型供应商、向量库或云服务写成产品事实。
- 未经授权，不把原始截图、对话和私有数据提交到公共仓库。
