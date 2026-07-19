# 科学限制与结论上限

## 身份和非背书

五个 Lens 都是公开研究框架的结构化提炼，不是科学家本人，不代表其当前意见，也未获得相关专家背书。多作者论文不能自动转化为某一作者对 Skill 全部表述的个人认可。

## 当前状态

原项目权威状态为 `partial_release_candidate`：

- Axtell：93/A，0 硬失败，`validated`；
- Chen：96/A，0 硬失败，`validated`；
- Meyers：95/A，0 硬失败，`validated`；
- Carrington：98/A，0 硬失败，`validated`；
- Jin：92/A，0 硬失败，但两轮修复后仍有 JIN-A03、JIN-A04、JIN-A06、JIN-S01 四个原始案例完整性回退，因此为 `needs_review`。

GitHub 候选包只把 Jin 作为 `supervised_preview` 执行，并增加强制状态、实体层级、运输方向、RNA 类别、逐边证据链、停止点和证据截止护栏。这不会把 Jin 改判为 `validated`。

## 常见观察的结论上限

| 观察 | 允许的结论上限 |
|---|---|
| 预测发卡 | 候选结构，不足以确认 miRNA |
| 数据库收录 | 存在记录，不证明高可信身份、直接靶标或功能 |
| 靶标预测 | 可检验假说，不是直接调控 |
| PARE/degradome 峰 | 支持特定位点切割，不是完整表型因果 |
| 表达反相关 | 相关线索，不能替代直接分子证据 |
| 受体样本出现外源 reads | 最多支持 donor-matching signal，仍需排除污染、外附和比对歧义 |
| 胞外囊泡富集 | 不等于囊泡内封装、完整摄取、AGO 进入或功能 |
| 五个 Lens 一致 | 分析框架一致，不是五个独立实验室的证据 |

## 物种与方法迁移

- 动物 seed 规则不能直接当作植物规则。
- Drosha–DGCR8 不能写成植物 miRNA 默认机制。
- 同名 miRNA 不能自动视为跨物种正交。
- family、MIR gene family、locus、precursor、mature、arm、isomiR、sequence、database record 和 assembly 必须区分。
- miRNA、phasiRNA、tasiRNA 和 hc-siRNA 不能混称。
- 从一个物种、组织、基因型、菌株、阶段、处理、assembly 或 assay 迁移到另一个体系时需要重新验证。

## 引用和时间

证据截止为 2026-07-17。之后的新论文、correction、erratum、retraction 和数据库版本需要重新检索。摘要来源只能支持摘要明确表达的有限结论；无法合法获得全文时不能猜测实验细节。

证据卡和 Skill 输出不能替代阅读原始论文、方法、图表、补充材料和更正文件。
