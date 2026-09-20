# Contributing

[中文](CONTRIBUTING_ZH.md) | [English](CONTRIBUTING.md)

## 范围

本公开候选固定为五个功能性专家视角。普通贡献不得添加、替换或合并视角，也不得把专家视角5的 `supervised_preview` 改成 `validated`。人名只用于文献归属，不作为模拟发言角色。

## 可接受的贡献

- 修复失效链接或书目元数据错误；
- 增加 correction、erratum、retraction 或独立反方证据；
- 修复 miRNA family/locus/arm/species/assembly 混淆；
- 改善 WorkBuddy 安装兼容性和无障碍说明；
- 添加能暴露过度推断的评测案例；
- 修复引用闭包、JSONL 结构或校验和问题。

## 科学变更要求

任何改变结论上限的 PR 都应提供：

1. 原始论文、方法标准或官方数据库文档链接；
2. DOI、PMID、PMCID 或稳定 URL；
3. 物种、组织、处理、基因型、菌株、assembly 和 assay 范围；
4. 证据直接性、独立性和限制；
5. 受影响的 claim/source ID；
6. 对应回归测试。

预测不能写成验证，表达相关不能写成因果，PARE/degradome 不能写成完整表型因果，数据库收录不能写成实验确认。

## 禁止贡献

- 论文 PDF、未经授权全文或大段受版权保护引文；
- 原始测序数据、模型权重、本地 LLM 或训练环境；
- 专家私人通信、未公开观点或人物冒充；
- 无来源的 DOI/PMID/ORCID/accession；
- 通过删除测试或降低标准让组件“通过”。
