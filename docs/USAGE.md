# 使用指南与提问模板

## 直接分析科学问题

```text
请用五视角科学面板分析下面的问题：

[问题]

请分别列出 Axtell、Chen、Meyers、Carrington、Jin 的适用性、主要关注、当前证据上限、证据缺口和 2–4 个能改变结论的问题。最后总结共同点、互补关注、必须保留的分歧和下一步证据。不要多数投票；Jin 标记为 supervised_preview。
```

## 审查论文摘要、结果或图注

```text
请用五视角面板审查下面文字。不要只总结，也不要假设作者结论成立。

[标题、摘要、结果或图注]

请让五个 Lens 分别指出：
- 最先检查的前提；
- 证据实际支持到哪一步；
- 可能混淆的 miRNA/小 RNA 实体；
- 因果链中缺失的一环；
- 最关键的缺失对照；
- 如果只能追问一个问题，会问什么。
```

## 只生成多视角问题清单

```text
针对下面的研究设想，请先不要给统一结论。请由五个 Lens 各提出 3 个互不重复、能够改变实验解释的问题，并说明为什么重要。Jin 必须显示 supervised_preview。

[研究设想]
```

## 审查候选植物 miRNA

```text
请审查这个植物 miRNA 候选。先区分 family、locus、precursor、mature、5p/3p、sequence、assembly 和数据库记录，再分别说明五个 Lens 会要求哪些身份、加工、靶标和表型证据。

[候选信息]
```

## 审查跨界 RNA 主张

```text
请用五视角面板审查下面的跨界 RNA 主张。必须区分植物到病原和病原到植物，区分 small RNA、dsRNA、mRNA、HIGS、SIGS 与自然交换，并按 origin、release/carrier、stability、intact uptake、effector access、direct target action、phenotype 逐边指出支持与缺口。

[主张或实验摘要]
```

## 如何理解输出

- `validated`：该 Lens 通过了本项目独立评测和发布门禁。
- `supervised_preview`：允许受监督试用，但没有通过正式发布门禁；当前仅 Jin 使用。
- `primary`：问题与该 Lens 的核心范围直接相关。
- `complementary`：能处理一个独立的辅助问题。
- `low`：相关性低；该 Lens 应说明边界，而不是凑观点。
- `documented_framework`：分析直接使用了已核验的公开框架。
- `agent_inference`：Agent 把框架应用到新问题，不代表专家本人观点。
- `contested`：公开证据存在冲突、范围限制或更正，不能抹平。

## 推荐提供的信息

为了得到更有用的答案，尽量提供：物种、组织或区室、发育/感染阶段、处理、基因型、菌株、genome assembly、RNA 类别、实体层级、方法、对照和声称的结论。

缺少这些信息时，面板应显式列为未知，而不是编造。
