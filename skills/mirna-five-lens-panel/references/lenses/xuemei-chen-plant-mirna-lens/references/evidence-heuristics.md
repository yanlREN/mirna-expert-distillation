# Evidence Heuristics — Xuemei Chen Lens

```yaml
expert_id: xuemei-chen
evidence_cutoff: 2026-07-17
heuristic_count: 8
anti_pattern_or_boundary_count: 9
```

这些条目是可执行检查，不是 Xuemei Chen 的逐字表述。`team_result` 指共同作者团队的公开结果；`expert_position` 指跨 Chen 研究重复的公开框架；`field_consensus` 只在独立证据匹配时使用；`agent_inference` 是本项目综合，不能改写为个人意见。

## Evidence Heuristics

### CHEN-H1 — 先固定 RNA 实体，再定位机制

**IF** 文章只写“miRNA 增加/降低”或混用 MIR locus、pri/pre-miRNA、duplex、mature arm/isomiR 与 AGO-loaded product，  
**THEN** 先声明 species、tissue、stage、genotype、entity 与 assay 直接测量对象，再把变化放入 lifecycle 节点，  
**BECAUSE** promoter、pri-miRNA decay、pre-miRNA end、total mature 与 AGO1-IP 回答不同阶段，  
**UNLESS** 结论被明确限制为不含机制定位的描述性 abundance observation。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1038-s41477-019-0562-1`, `src-doi-10-1073-pnas-2208415119`, `src-doi-10-1038-s41467-022-28872-x`
- `claim_ids`: `claim-chen-b01`, `claim-chen-b02`, `claim-chen-b07`, `claim-chen-b11`

### CHEN-H2 — Total abundance 不等于 AGO loading

**IF** 论文声称 loading、RISC availability 或 activity，  
**THEN** 要求 total-input 与 AGO-associated fraction、AGO protein abundance、IP recovery 和匹配 controls，  
**BECAUSE** total mature-miRNA 变化与 loading efficiency 是可分离变量，  
**UNLESS** 作者只声称 total abundance，而不声称 loading 或 effector use。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1038-s41467-022-28872-x`, `src-doi-10-15252-embj-2018100754`
- `claim_ids`: `claim-chen-a-rbv-coupled-checkpoints`, `claim-chen-b07`, `claim-chen-c-009`

### CHEN-H3 — 定位必须配 stage-matched perturbation/readout

**IF** 结论依赖 D-body、nuclear pore、ER、polysome、cell type 或其他 compartment，  
**THEN** 把 colocalization/enrichment 视为假设，并检查 compartment-specific perturbation 与 processing、loading、translation、export 或 movement readout，  
**BECAUSE** visible body、physical proximity 或 bulk fraction enrichment 不等于 catalytic flux，  
**UNLESS** claim 本身只描述位置而不声称功能机制。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1016-j-cell-2013-04-005`, `src-doi-10-1038-s41477-020-0726-z`, `src-doi-10-1038-s41556-020-00606-5`
- `claim_ids`: `claim-chen-a-er-translation-cleavage-separation`, `claim-chen-b08`, `claim-chen-c-005`

### CHEN-H4 — 用 RNA + protein 成对读数判定 action mode

**IF** 文章声称 cleavage、mRNA decay 或 translational repression，  
**THEN** 在 target/tissue/stage 匹配的体系中同时检查 target RNA、protein、target-site dependence 与必要 controls，  
**BECAUSE** RNA-only assay 会漏掉直接 translation effects，而 protein change 也可能是间接效应，  
**UNLESS** 结论明确限制为经直接测得的单一分子 readout。

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-doi-10-1126-science-1088060`, `src-doi-10-1126-science-1159151`, `src-doi-10-1016-j-molcel-2013-10-033`
- `claim_ids`: `claim-chen-a-mir172-ap2-translational-repression`, `claim-chen-c-002`, `claim-chen-c-007`

### CHEN-H5 — Suppressor/epistasis 先检验 bypass、dosage 与 allele

**IF** second-site suppressor 或 epistasis 被用来指派 pathway order 或直接机制，  
**THEN** 比较 bypass、剂量补偿、substrate competition 与 direct restoration，并核对 partial/null allele、tissue 和 stage，  
**BECAUSE** phenotypic suppression 不自动等于直接相互作用或完整 biochemical restoration，  
**UNLESS** stage-matched biochemical/RNA readout 与遗传结果共同会合。

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1093-nar-gkq348`, `src-doi-10-1016-j-cub-2012-02-052`
- `claim_ids`: `claim-chen-a-substrate-pool-competition`, `claim-chen-a-heso1-unmethylated-substrates`, `claim-chen-b06`

### CHEN-H6 — HEN1 四个命题分别验证

**IF** 文章声称 HEN1 mechanism，  
**THEN** 分开 enzyme requirement、terminal chemical position、duplex geometry/size preference 与 in-vivo protection，  
**BECAUSE** genetics、mass/chemical analysis、purified substrate panel 与 hen1 end phenotype 支持不同命题，  
**UNLESS** 论文明确只回答其中一个命题并限制措辞。

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-doi-10-1126-science-1107130`, `src-doi-10-1093-nar-gkj474`, `src-doi-10-1016-j-cub-2005-07-029`, `src-doi-10-1261-rna-2281410`
- `claim_ids`: `claim-chen-a-hen1-terminal-methylation`, `claim-chen-a-hen1-duplex-specificity`, `claim-chen-a-methylation-protects-ends`, `claim-chen-c-003`

### CHEN-H7 — Tail/isomiR snapshot 不是 decay rate

**IF** 观察到 uridylation、truncation、isomiR shift 或 steady-state abundance change，  
**THEN** 联合检查 methylation、AGO association、substrate stage、genotype、HESO1/URT1/SDN 分支，并把 rate 保持为未决，  
**BECAUSE** 分支、冗余和 trimming 可产生相似端状态，snapshot 不提供 flux，  
**UNLESS** 有 kinetic、pulse-chase、metabolic labeling 或等价的 rate-resolved evidence。

- `knowledge_status`: `expert_position`
- `independent_support`: field evidence refines the branching network but does not establish every substrate-specific rate
- `source_ids`: `src-doi-10-1105-tpc-113-114603`, `src-doi-10-1073-pnas-1405083111`, `src-doi-10-1371-journal-pgen-1005091`, `src-doi-10-1016-j-bbrc-2020-01-124`
- `claim_ids`: `claim-chen-b10`, `claim-chen-c-004`, `claim-chen-c-008`

### CHEN-H8 — Movement 按门链逐段核验

**IF** miRNA 在另一 cell/tissue 中被检测到并声称 mobility 或非细胞自主功能，  
**THEN** 依次检查 source production、source-cell loading、movement、recipient loading、direct target effect 和 phenotype，  
**BECAUSE** recipient presence、transport、effector use、targeting 与 causality 是不同命题，  
**UNLESS** claim 明确只限于检测且不包含 transport 或 function。

- `knowledge_status`: `expert_position`
- `independent_support`: independent spatial and HASTY studies support the gate logic, not the same microtubule mechanism
- `source_ids`: `src-doi-10-15252-embj-2018100754`, `src-doi-10-15252-embj-2020107455`, `src-doi-10-1016-j-devcel-2022-03-015`
- `claim_ids`: `claim-chen-a-mobility-loading-context`, `claim-chen-b09`, `claim-chen-c-009`, `claim-chen-c-010`

## Anti-patterns and Boundary Rules

### CHEN-AP1 — 用终点 abundance 代替阶段定位

从 mature total 或发育表型直接写成 transcription、processing 或 turnover defect。应使用 `CHEN-M1`，把相邻阶段和对应实体逐一排除。关联 claims：`claim-chen-a-stage-separated-diagnosis`, `claim-chen-b01`。

### CHEN-AP2 — 混合 family、locus、precursor、arm、isomiR 与序列

以同一 miRNA 名称无区分地指代 MIR gene family、具体 locus、precursor、mature 5p/3p、end variant、database record 或 coordinate。跨物种同名不自动正交；缺 assembly/sequence 时写 `missing_context`。关联：`CHEN-M1`; `claim-chen-b02`。

### CHEN-AP3 — 把共定位或可见结构写成机制

以 D-body、nuclear-pore、ER 或 AGO colocalization 直接证明 processing flux、loading、export 或 movement。必须加入 perturbation 与 stage-matched readout。来源：`src-doi-10-1038-s41477-020-0726-z`, `src-doi-10-1038-s41556-020-00606-5`；claims：`claim-chen-b08`, `claim-chen-c-005`。

### CHEN-AP4 — 压缩 target、action 与 phenotype 三轴

把 prediction、表达反相关、AGO association、PARE/degradome 或 reporter 中任一项升级为 direct target 加完整 phenotype causality。应按 `CHEN-M4` 分栏；只有 target-site genetics/rescue 或等价干预才能升到 F4。关联：`claim-chen-b03`, `claim-chen-b09`。

### CHEN-AP5 — 把 miR172/AP2 普遍化为 translation-first 规则

miR172/AP2 与独立证据证明 translational repression 是真实作用模式，不证明所有植物 target 以 translation 为主。每个 target 必须重新匹配 RNA、protein、site、tissue 与 stage。来源：`src-doi-10-1126-science-1088060`, `src-doi-10-1126-science-1159151`, `src-doi-10-1016-j-molcel-2013-10-033`。

### CHEN-AP6 — 从一个 tail 指定唯一 enzyme 或 decay rate

把 U-tail、truncation 或 isomiR distribution 直接归给 HESO1/URT1/SDN 中的唯一一个，或写成降解速率。分支、冗余、AGO context 和 substrate stage 必须保留。关联：`CHEN-M5`; `claim-chen-c-004`, `claim-chen-c-008`。

### CHEN-AP7 — 从 recipient reads 跳到 movement 和功能

未排除 source/recipient contamination、tissue mixing，未测 recipient loading 和 target effect，就写成 mobile miRNA phenotype。必须逐段应用 `CHEN-H8`；微管机制仅限测试的 Arabidopsis root/miR165/166 context。

### CHEN-BR1 — Arabidopsis transfer gate

本 corpus 高度偏向 *Arabidopsis thaliana*。迁移到作物或其他植物时必须重新核对 MIR locus、paralog、mature arm/sequence、tissue/stage、AGO family、allele 与 assay；标记 `conserved|analogous|lineage_specific|uncertain|unsupported_transfer`。禁止把动物 Drosha–DGCR8、seed-only 或 Exportin-5 机制默认写入植物，也不得把 HASTY 简化为动物模型复制。

### CHEN-BR2 — Correction/erratum gate

任何定量、figure-level 或方法细节复用都先核对 correction、retraction 与 expression of concern。`src-doi-10-1126-science-1163728` 必须携带 `src-doi-10-1126-science-aav2481`；correction 内容在 corpus 不足时停止细节复用。`src-doi-10-1073-pnas-2208415119` 必须携带 `src-doi-10-1073-pnas-2219264119`：correction 影响 Fig. 1/Fig. S3 legends 及 Figs. 6/S2/S6；promoter/decay 使用限于未受影响的 Figs. 3/4。Correction 不是独立复制。

## Runtime evidence labels

```yaml
status: supported|partially_supported|unsupported|conflicting
knowledge_status: field_consensus|expert_position|contested|historical|superseded|hypothesis|agent_inference
attribution: team_result|sole_author_result|public_scope|field_evidence|agent_inference
directness: direct|indirect|computational|contextual
independent_support: strong|limited|none|not_applicable
scope_match: matched|partial|mismatched|unknown
transfer_type: conserved|analogous|lineage_specific|uncertain|unsupported_transfer
source_ids: []
claim_ids: []
```
