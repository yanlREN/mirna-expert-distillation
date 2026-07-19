# miRNA Five-Lens Scientific Panel for WorkBuddy

一个面向 miRNA、植物 small RNA、RNA silencing 与跨界 RNA 问题的五视角科研分析 Skill。它会让同一问题依次经过 Axtell、Chen、Meyers、Carrington 和 Jin 五套公开研究框架，并保留各自关注点、证据边界、分歧与后续问题。

> **发布状态：GitHub 公开候选 / prerelease。** 四个 Lens 已通过本项目发布门禁；Jin Lens 仅为 `supervised_preview`，尚未通过正式发布门禁。这个状态必须在使用界面、输出和二次分发中保留。

## 它能做什么

- 分析科学问题、论文摘要、结果段、图注或研究设想；
- 分别列出五个 Lens 最先检查的前提、证据能支持到哪里和缺失对照；
- 区分 miRNA 身份、直接靶标证据与表型因果；
- 区分 family、MIR gene family、locus、precursor、mature、5p/3p、isomiR、sequence 与数据库记录；
- 对跨界 RNA 按 origin → release/carrier → stability → intact uptake → effector access → direct target action → phenotype 逐边审查；
- 最后汇总共同点、互补关注、必须保留的分歧和最能改变结论的证据。

它不会训练模型，不包含模型权重，不下载原始测序数据，也不会冒充任何专家本人。

## 五个 Lens 的状态

| Lens | 主要关注 | 状态 |
|---|---|---|
| Axtell | miRNA 身份、注释严格性、miRNA/siRNA 分类与实体层级 | `validated` |
| Chen | 植物 miRNA 生物发生、加工、甲基化、AGO 装载与生命周期 | `validated` |
| Meyers | small-RNA 组学、PARE/degradome、PHAS/phasiRNA 与可重复性 | `validated` |
| Carrington | DCL/RDR/AGO、tasiRNA、病毒抑制子与 RNA silencing 通路 | `validated` |
| Jin | 植物–病原跨界 RNA、载体/摄取、受体作用路径与因果链 | `supervised_preview` |

`supervised_preview` 不等于“第五位已验证专家”。Jin 在独立 N5 回归中仍有 4 个完整性回退案例，因此面板强制显示状态、证据截止日期和逐边停止点。

## 仓库结构

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── RELEASE-MANIFEST.yaml
├── CHECKSUMS.sha256
├── docs/
├── skills/
│   └── mirna-five-lens-panel/       # 自包含 WorkBuddy Skill
├── dist/
│   └── mirna-five-lens-panel-workbuddy.zip
└── third-party-licenses/
    └── NUWA-MIT.txt
```

面板已内嵌五个 Lens。普通用户只需安装 `mirna-five-lens-panel`，不要再同时启用五个独立副本。

## 快速安装到 WorkBuddy

### 方法一：界面上传（推荐）

1. 从 GitHub Release 下载 `mirna-five-lens-panel-workbuddy.zip`。
2. 核对 `CHECKSUMS.sha256`。
3. 打开 WorkBuddy，进入“技能”→“已安装”→“添加技能”→“上传技能”。
4. 选择下载的 ZIP，等待导入完成。
5. 新建任务，首次使用建议选择 **Ask / 问一问** 模式。
6. 在输入区选择 `mirna-five-lens-panel`，然后提问。

WorkBuddy 官方说明支持通过“上传技能”导入本地技能包，并建议安装第三方 Skill 前检查来源、权限与脚本内容：

- [WorkBuddy 技能管理](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
- [WorkBuddy 新建任务与选择技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

### 方法二：手动复制

将 `skills/mirna-five-lens-panel` 整个目录复制到用户级 Skills 目录：

```text
Windows: C:\Users\<你的用户名>\.workbuddy\skills\mirna-five-lens-panel
macOS/Linux: ~/.workbuddy/skills/mirna-five-lens-panel
```

随后完全退出并重新打开 WorkBuddy。如果你的 WorkBuddy 版本使用不同位置，以其界面显示的本地技能目录为准。

完整步骤与故障排除见 [docs/INSTALL-WORKBUDDY.md](docs/INSTALL-WORKBUDDY.md)。

## 最小使用示例

```text
请用五视角科学面板分析下面的问题：

[粘贴问题、摘要、结果或图注]

请分别给出 Axtell、Chen、Meyers、Carrington 和 Jin 五个 Lens 的：
1. 适用性；
2. 最关注的问题；
3. 当前证据能支持到哪里；
4. 证据缺口；
5. 最值得追问的 2–4 个问题。

最后列出共同点、互补关注、必须保留的分歧和最能改变结论的下一步证据。
不要用多数投票决定科学结论；Jin 必须标记为 supervised_preview。
```

更多模板见 [docs/USAGE.md](docs/USAGE.md)。

## 科学与身份边界

- 输出是 Agent 对公开研究框架的应用，不是专家本人发言，也不代表专家当前意见或背书。
- 多位 Lens 一致不是多个独立实验室的证据，不能通过投票决定科学事实。
- 数据库收录、预测发卡、靶标预测、PARE 峰或表达反相关都各有明确结论上限。
- 新问题上的判断默认是 `agent_inference`；只有来源实际支持时才能写成 `documented_framework`。
- 证据截止为 **2026-07-17**；涉及之后的新论文、文章更正或撤稿时应重新核验原始来源。
- 该工具不能替代原论文阅读、统计复核、实验验证、临床判断或领域同行评审。

详见 [docs/SCIENTIFIC-LIMITATIONS.md](docs/SCIENTIFIC-LIMITATIONS.md)。

## 安全说明

本候选包不包含可执行脚本、二进制程序、账户凭据、网络连接器或自动写文件逻辑；其内容为 Markdown、YAML 和 JSONL 形式的指令、元数据、结构化证据摘要及合法链接。用户输入如何被模型服务处理仍取决于 WorkBuddy 的模型、权限和隐私设置。

安装第三方 Skill 前请自行检查包内容和 SHA-256。不要把未公开数据、患者资料、密码、机构凭据或受限全文直接粘贴给未知模型服务。详见 [SECURITY.md](SECURITY.md)。

## 验证状态

- 面板和五个内嵌 Lens 均通过 Skill 结构检查；
- JSONL 可解析，引用文件闭包完整；
- 包内没有 PDF、原始测序数据、模型权重、缓存或凭据；
- ZIP 内容和 SHA-256 在生成时重新核验；
- 原项目权威状态仍是 `partial_release_candidate`，本仓库是独立的 GitHub 公开候选，不把 Jin 改判为 validated。

详细结果见 [docs/VALIDATION.md](docs/VALIDATION.md)。

## 上传 GitHub 前

1. 完整上传本目录内容，不要只上传 `SKILL.md`。
2. 首次 GitHub Release 标为 **Pre-release**，不要标为 production-ready。
3. 将 `dist/mirna-five-lens-panel-workbuddy.zip` 与 `CHECKSUMS.sha256` 一起作为 Release assets。
4. 保留 `LICENSE`、`NOTICE.md`、`RELEASE-MANIFEST.yaml` 和 Jin 的 `supervised_preview` 标记。
5. 不要加入论文 PDF、缓存、原始测序数据、模型文件或访问凭据。

本项目不会自动创建 GitHub 仓库或推送远程。发布步骤见 [docs/GITHUB-PUBLISHING.md](docs/GITHUB-PUBLISHING.md)。

## 许可证与来源

本候选包的原创指令、文档和结构化代码材料按 [MIT License](LICENSE) 提供。Nuwa 上游方法框架的 MIT 许可证保存在 [third-party-licenses/NUWA-MIT.txt](third-party-licenses/NUWA-MIT.txt)。论文、数据库和第三方网页仍归各自权利人所有；本仓库不重新分发论文全文。

完整归属与非背书声明见 [NOTICE.md](NOTICE.md)。
