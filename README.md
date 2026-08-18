# Reverse AI Product Architecture Skill

一套面向生成式 AI 产品和多 Agent 工作台的“证据优先”逆向分析 Skill。

它从页面截图、聊天记录、画布、资产卡、任务状态、模型选项和错误提示出发，逐层还原：

- 用户从输入需求到最终结果的真实旅程
- 实际出现的 Agent、触发条件、I/O 契约和下游交接
- 可观察的工具调用与运行结果
- 项目全局上下文、资产引用和状态流
- 模型接入与路由边界
- As-Is 产品架构、To-Be 建议架构和关键风险
- 单个 Agent 的功能等价 System Prompt
- 可追溯的 HTML 产品架构报告

这套方法最初从一次 AI 视频创作产品的完整页面拆解中抽象而来。仓库只发布通用方法、模板和校验工具，不包含用户账号信息、原始私有对话、Cookie、Token 或未经授权的产品截图。

## 为什么需要它

AI 产品的界面经常同时展示聊天、Agent、工具计划、画布资产、异步任务和最终预览。只读聊天文字很容易得出错误结论：

- Agent 说“已完成”，不代表资产真的完成。
- 工具返回成功，不代表项目状态写入成功。
- 画布有资产，不代表资产库、历史版本或下游引用已经同步。
- 页面出现一个模型，不代表系统具备完整动态路由。
- 常见工程做法不等于产品当前真实后端。

这个 Skill 用四级证据标签把事实、推断、建议和未知严格分开：

- 【已确认】：页面、官方资料或可复核结果直接支持
- 【合理推断】：由多条页面事实推导，但后台不可见
- 【建议设计】：为稳定性、恢复能力或治理提出的方案
- 【未知】：当前证据不足

## 能完成什么

### 1. 用户旅程

从最早一条用户消息开始，检查按钮、表单、确认卡、画布、资产、任务、错误、预览和剪辑入口，输出正常、修改/纠偏、失败/中断三类路径。

### 2. Agent I/O 契约

只记录真实出现的 Agent，逐一整理六类输入、五类输出、可观察判断、功能性工具、全局上下文读写、完成条件和异常边界。

### 3. 功能等价 System Prompt

在完成证据追溯、状态机和工具契约后，为单个 Agent 编写可直接使用的功能等价 Prompt；它复现页面行为，但不冒充产品官方原文，也不声称读取隐藏思维链。

### 4. 产品全景架构

把用户交互流、Agent 控制流、工具调用流、上下文流和媒体资产流合并到九层产品架构，并补充数据实体、ER 图、端到端时序、模型路由、As-Is/To-Be 和风险优先级。

### 5. HTML 可视化报告

用泳道、节点链、分层图、状态图、风险矩阵和证据追溯表生成可交付页面，而不是把整页做成同一种数据卡片。

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
        │   ├── deliverable-specs.md
        │   └── architecture-schema.md
        ├── scripts/
        │   ├── inventory_screenshots.py
        │   └── validate_analysis.py
        └── assets/
            └── report-template.html
```

## 安装

### 方法一：克隆后复制到 Codex Skills 目录

```bash
git clone https://github.com/HurmitLI/reverse-ai-product-architecture-skill.git
cd reverse-ai-product-architecture-skill
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
cp -R skills/reverse-ai-product-architecture "$CODEX_SKILLS_DIR/"
```

重新打开 Codex 任务后即可使用。

### 方法二：开发时使用符号链接

```bash
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
ln -s "$(pwd)/skills/reverse-ai-product-architecture" "$CODEX_SKILLS_DIR/reverse-ai-product-architecture"
```

## 使用方式

显式调用：

```text
使用 $reverse-ai-product-architecture，查看这个截图文件夹，先梳理用户旅程，再识别 Agent 和工具，最后输出 HTML 产品架构报告。
```

只拆用户旅程：

```text
使用 $reverse-ai-product-architecture，从最早一条消息开始，基于页面事实还原正常、修改和失败/中断路径。所有节点标截图证据编号。
```

只拆一个 Agent：

```text
使用 $reverse-ai-product-architecture，只分析“分镜师”，先完成输入、输出、工具、状态机和规则追溯，再编写功能等价 System Prompt。
```

做完整架构：

```text
使用 $reverse-ai-product-architecture，基于已有用户旅程、Agent 契约和页面截图，输出 Agent、工具、全局上下文、模型、资产、状态、计费与安全的产品全景架构 HTML。
```

## 推荐输入

- 按时间顺序命名的页面截图
- 聊天、画布、任务、资产库、历史版本和错误状态
- 模型、分辨率、时长、余额或计费页面
- 已完成的用户旅程或 Agent 契约
- 产品官方帮助或官方文档链接（可选）

截图可以放在多级文件夹中。先生成证据清单：

```bash
python3 skills/reverse-ai-product-architecture/scripts/inventory_screenshots.py \
  /path/to/screenshots \
  --output /path/to/evidence-manifest.csv
```

输出 CSV 包含证据编号、相对路径、文件名和可识别的图片尺寸。

## 推荐交付顺序

1. 查看范围与证据缺口
2. 用户旅程证据表与三泳道图
3. Agent 清单与 I/O 契约卡
4. 工具总表与全局上下文字段表
5. 数据生产者—消费者关系
6. 单 Agent 功能等价 System Prompt（按需）
7. 端到端五流与九层产品架构
8. 全局上下文、知识、模型路由和数据实体
9. ER 图、时序图与产品全景主图
10. As-Is、To-Be、风险和证据追溯
11. 仍然无法确认的问题

## HTML 报告模板

`assets/report-template.html` 提供：

- 四级证据配色
- 五流泳道
- 分层架构组件
- 证据追溯表
- As-Is / To-Be / 风险区
- 桌面和移动端布局

模板使用语义占位符，例如 `{{PRODUCT_NAME}}`、`{{TRACE_ROWS}}`。可以复制后替换，也可以只复用视觉语言。

## 校验

### 校验 Skill 结构

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skills/reverse-ai-product-architecture
```

### 校验 HTML 报告

```bash
python3 skills/reverse-ai-product-architecture/scripts/validate_analysis.py \
  /path/to/product-architecture.html
```

校验器会检查：

- 是否为完整 HTML
- 是否存在重复 ID
- 四级证据标签是否齐全
- 关键章节关键词是否出现
- 是否存在 S/E 证据编号
- 是否出现高风险越界表述

## 安全与发布边界

- 浏览器默认只读，不主动触发生成、重试、购买、发布、删除或覆盖。
- 不读取或输出 Cookie、Token、密码、鉴权头和个人敏感信息。
- 不把公开“思考完成/规划完成”写成隐藏思维链。
- 不把口头计划直接当成工具成功。
- 不把字段模板、数据库类别或云服务写成当前产品事实。
- 未经授权，不把原始截图、对话和私有资产提交到公共仓库。

## 适用边界

特别适合：

- AI 视频、图片、音频和内容创作产品
- 多 Agent 工作台
- 聊天驱动的异步任务产品
- 带画布、资产库、版本和确认门的生成式 AI 应用

不适合直接用作：

- 未经授权的接口破解或凭证逆向
- 隐藏思维链提取
- 仅凭行业经验猜测真实后端
- 绕过产品权限、安全或计费机制
