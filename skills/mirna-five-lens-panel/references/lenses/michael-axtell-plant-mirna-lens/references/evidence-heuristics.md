# Evidence Heuristics — Michael J. Axtell Lens

```yaml
expert_id: michael-j-axtell
evidence_cutoff: 2026-07-17
heuristic_count: 8
anti_pattern_count: 8
honest_boundary_count: 8
```

这些启发式是执行性检查，不是 Axtell 的逐字表述。`expert_position` 表示与公开标准/方法明确一致；`field_consensus` 表示有独立来源支持；`agent_inference` 表示从多个公开研究情境综合得到。

## Evidence Heuristics

### AXT-H1 — 发卡与表达不完成身份判定

**IF** 植物候选 small RNA 只有预测发卡、单个 dominant read、处理后表达变化或数据库记录，  
**THEN** 将其保持在 I1/I2 或 `provisional`，并检查精确 miRNA/miRNA* duplex、全位点 read geometry 与至少两个 biological libraries，  
**BECAUSE** 植物内源 siRNA 背景巨大，局部发卡和表面精度可偶然出现，  
**UNLESS** 已有 species/assembly-matched 的直接加工证据满足当前植物标准。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`, `src-doi-10.1093-nar-gkz894`
- `claim_ids`: `claim-axtell-b01`, `claim-axtell-b02`, `claim-axtell-c-006`

### AXT-H2 — 通路依赖主要用于排除，不是单测定证明

**IF** 候选在 `rdr1/rdr2/rdr6` 或其他 pathway mutant 中改变，  
**THEN** 用该结果检验其是否与声称的 precursor class 相容，并与发卡、精度和位点模式联合解释，  
**BECAUSE** RDR 依赖可暴露 siRNA 混淆，而 RDR independence 本身不证明 MIRNA，  
**UNLESS** 另有完整、独立的类定义生物发生证据。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1111-tpj-13919`, `src-axtell-31245701`
- `claim_ids`: `claim-axtell-b04`, `claim-axtell-b05`, `claim-axtell-b07`

### AXT-H3 — 算法一致性先审计假独立

**IF** 两个或更多软件给出相同 MIRNA/PHAS 标签，  
**THEN** 比较其作者网络、实现标准、输入 assembly、版本、参数和训练/benchmark 证据，再回到 locus-level features，  
**BECAUSE** 不同软件名可能共享规则或作者，且多算法可共同命中巨大背景类，  
**UNLESS** 一致性来自真正独立的方法谱系并得到正交生物学验证。

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-axtell-31245701`, `src-pmid-31253093`, `src-pmid-41183249`
- `claim_ids`: `claim-axtell-b06`, `claim-axtell-c-004`, `claim-axtell-c-012`

### AXT-H4 — 24-nt PHAS 需要稳定 register、trigger 与遗传背景

**IF** 真双子叶候选为 24-nt-dominated PHAS locus，  
**THEN** 检查同一 dominant phase register 的跨 library 复现、class-compatible trigger、RDR/DCL 依赖、genomic context 和阳性对照，  
**BECAUSE** 丰富的 24-nt hc-siRNA loci 可按机会通过 phasing scores，  
**UNLESS** 提出预声明且可反驳的非经典 pathway model，并以独立机制证据支持。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-axtell-31245701`
- `claim_ids`: `claim-axtell-b06`, `claim-axtell-b07`
- `transfer_limit`: 不否定其他类群中真实的 24-nt reproductive phasiRNA systems。

### AXT-H5 — 保守性只校准先验

**IF** 论证使用跨物种成熟序列相似、family 名称或靶标保守性，  
**THEN** 分开报告 family history、locus homology/synteny、species-specific processing、arm/sequence identity 和 function，  
**BECAUSE** 深保守关系与快速 locus birth/death 可同时存在，  
**UNLESS** 每一层都有相应的 species/assembly-matched 直接证据。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1105-tpc-105-032185`, `src-doi-10-1105-tpc-110-073882`, `src-doi-10-1105-tpc-17-00851`
- `claim_ids`: `claim-axtell-a-conservation-calibrates-prior`, `claim-axtell-c-001`, `claim-axtell-talk-evolution-separates-homology-levels`

### AXT-H6 — 缺 star 或低覆盖时保留证据缺口类别

**IF** 候选满足多数结构/表达条件但没有精确 miRNA*，或 counts/replicate variance 无法裁决，  
**THEN** 使用 `nearMIRNA`、`ambiguous`、`unclassified` 或等价 provisional 状态，并列出升级数据，  
**BECAUSE** 缺失可能来自真实非典型生物发生，也可能来自 tissue/stage/library/assembly 盲区，  
**UNLESS** 已有充分证据明确支持或排除该类别。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1111-tpj-13919`, `src-axtell-32179590`
- `claim_ids`: `claim-axtell-b05`, `claim-axtell-b13`

### AXT-H7 — 方法只升级其直接回答的 claim

**IF** 论文报告 complementarity、表达反相关、PARE/degradome、AGO association 或 transient reporter，  
**THEN** 分别标为 prediction、间接关联、切割/加工、effector association 或位点依赖抑制，并单独评定 phenotype causality，  
**BECAUSE** 每种方法解决的是不同层级，切割和 reporter 都不能独自证明完整表型因果，  
**UNLESS** 有靶位点遗传学、rescue 或等价因果干预。

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-doi-10-1016-j-cub-2008-04-042`, `src-axtell-19850910`, `src-doi-10-1105-tpc-113-120972`
- `claim_ids`: `claim-axtell-a-target-evidence-ladder`, `claim-axtell-b10`, `claim-axtell-b11`, `claim-axtell-b12`

### AXT-H8 — 受体样本中的 reads 不等于跨物种功能

**IF** donor-like small-RNA reads 出现在 host、界面或另一物种样本中，  
**THEN** 依次检查 source locus、组织混合/污染、movement、recipient AGO loading、direct target effect 和 phenotype，  
**BECAUSE** presence、移动、效应器利用、靶向和因果是不同证据步骤，  
**UNLESS** 每一步都在匹配的体系中有直接证据；未证步骤必须标为 missing。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1038-nature25027`, `src-doi-10-7554-elife-49750`, `src-doi-10-1093-plcell-koad076`, `src-pmid-42417192`
- `claim_ids`: `claim-axtell-a-transspecies-chain`, `claim-axtell-talk-transspecies-uncertainty-ladder`, `claim-axtell-c-011`

## Anti-patterns

### AXT-AP1 — 用功能反向证明身份

从预测靶标、PARE peak、表达反相关或表型倒推“因此是 miRNA”。这违反身份与功能分层；应先完成 locus/precursor 加工审查。关联：`AXT-M1`；`claim-axtell-a-identity-before-function`。

### AXT-AP2 — 把数据库名当成实验验证

以 miRBase/PmiREN 收录、high-confidence 标签或稳定 family 名称替代当前 assembly、coordinate、arm 和 library 证据。独立重注释明确显示数据库条目可被纠正、降级或删除。来源：`src-pmid-30423142`, `src-doi-10.1093-nar-gkz894`；claims：`claim-axtell-c-005`, `claim-axtell-c-006`。

### AXT-AP3 — 单一漂亮特征裁决全位点

只展示最像发卡的一段、最高丰度 read 或一个好看的 precision score，而忽略全位点大小、链、重复、相位和遗传依赖。关联：`AXT-M2`；`claim-axtell-a-multiparameter-locus-profile`。

### AXT-AP4 — 把 software concordance 当独立复制

用 ShortStack、miRScore 或其他共享标准/作者的软件一致性充当两个独立实验室。应按假设、作者与实现谱系审计。来源：`src-pmid-41183249`；claim：`claim-axtell-c-012`。

### AXT-AP5 — 强迫低信息位点进入熟悉类别

缺 star、低 counts、replicate variance 或类别矛盾时仍二元接受/拒绝，而不保留 `nearMIRNA`、`ambiguous` 或 `unclassified`。来源：`src-doi-10-1111-tpj-13919`, `src-axtell-32179590`；claims：`claim-axtell-b05`, `claim-axtell-b13`。

### AXT-AP6 — 同名即正交、未检出即丢失

把 family 名称或成熟序列相似写成 locus orthology，或把某 library 未检测到写成物种中不存在。应分别检查 synteny、assembly、组织/阶段和 species-specific processing。关联：`AXT-M4`；`claim-axtell-a-entity-resolution`。

### AXT-AP7 — 把切割或 reporter 升格为完整表型机制

PARE/degradome 证明匹配切割事件、瞬时 reporter 证明 assay 中的位点依赖抑制；二者都不是 target-site genetics/rescue。来源：`src-doi-10-1016-j-cub-2008-04-042`, `src-doi-10-1105-tpc-113-120972`；claim：`claim-axtell-a-target-evidence-ladder`。

### AXT-AP8 — 从跨物种 reads 跳到运输、靶向和表型

未排除界面混样或污染，也未证明 recipient effector loading，就把 reads presence 写成跨物种调控。Cuscuta 的特定证据链不能泛化为膳食 RNA 或所有跨界体系。关联：`AXT-M5`；`claim-axtell-a-transspecies-chain`。

## Honest Boundaries

1. **公开资料边界。** 本 Lens 只反映截至 2026-07-17 的公开语料；不能恢复私人直觉、未发表判断或截止日后的观点。
2. **归因边界。** 多作者标准和团队论文不等于 Axtell 对每个表述的个人背书；2008 标准保守标为 `coauthor`。
3. **报告材料边界。** 三场学术报告只有官方题目/公告，无录像、slides、transcript 或 Q&A；不能重建现场回答、措辞或类比。
4. **全文边界。** 三项来源只使用摘要支持高层范围；未用摘要推断未读正文的实验细节。
5. **软件边界。** ShortStack、miRScore、miRkwood、PmiREN 或任一数据库/工具均非 oracle；性能依赖数据集、版本、参数、assembly 和 benchmark。
6. **谱系边界。** 严格标准与 lineage sensitivity 存在张力；绿藻或动物材料只能支持迁移警示，不能直接给陆生植物设置数值阈值。
7. **当前结果边界。** 2026 Cuscuta AGO-loading 结果为 Axtell 团队近期研究，尚不能在本语料中算作独立实验室复制。
8. **应用边界。** 本 Lens 不能替代原始论文、locus-level 数据检查、实验设计审查或临床判断，也不保证专家本人同意任何新问题输出。

## Runtime evidence labels

对每个关键主张同时输出：

```yaml
status: supported|partially_supported|unsupported|conflicting
knowledge_status: field_consensus|expert_position|contested|historical|superseded|hypothesis|agent_inference
directness: direct|indirect|computational|contextual
independent_support: strong|limited|none|not_applicable
scope_match: matched|partial|mismatched|unknown
source_ids: []
claim_ids: []
```
