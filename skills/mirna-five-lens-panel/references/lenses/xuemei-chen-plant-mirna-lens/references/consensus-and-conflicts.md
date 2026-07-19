# Consensus, Status, and Conflicts — Xuemei Chen Lens

```yaml
expert_id: xuemei-chen
evidence_cutoff: 2026-07-17
phase: N2
principle: expert_framework_status_is_not_scientific_truth_status
tension_count: 6
```

本文件把“某个判断程序是否反映 Chen 公开研究框架”与“具体科学主张是否得到独立支持”分开。共同作者团队结果不等于 Xuemei Chen 对每个表述的个人背书；`expert_position` 不等于 `field_consensus`；新问题上的判断均为模型化推断。

## Knowledge-status map

### `field_consensus`

1. **HEN1-dependent terminal methylation 是植物 small-RNA 端保护的重要步骤。** Chen 团队的遗传、化学和生化结果与独立 HEN1 kinetic work 会合；但 enzyme activity、substrate geometry、protective consequence 与 in-vivo flux 仍是不同命题。  
   - Sources: `src-doi-10-1126-science-1107130`, `src-doi-10-1093-nar-gkj474`, `src-doi-10-1016-j-cub-2005-07-029`, `src-doi-10-1261-rna-2281410`  
   - Claims: `claim-chen-a-hen1-terminal-methylation`, `claim-chen-a-hen1-duplex-specificity`, `claim-chen-a-methylation-protects-ends`, `claim-chen-c-003`
2. **植物 miRNA action 可包含 cleavage 与 translational repression。** miR172/AP2 是直接锚点，独立遗传与 reconstituted AGO1-RISC 工作支持 translation inhibition 的存在；相对贡献仍依 target/context。  
   - Sources: `src-doi-10-1126-science-1088060`, `src-doi-10-1126-science-1159151`, `src-doi-10-1016-j-molcel-2013-10-033`  
   - Claims: `claim-chen-a-mir172-ap2-translational-repression`, `claim-chen-c-002`, `claim-chen-c-007`
3. **端代谢不是单一线性反应。** HESO1/URT1 genetics 显示 redundancy、synergy 和 trimming exposure；独立 URT1 structure 只支持 catalytic component，不提供完整 in-vivo flux。  
   - Sources: `src-doi-10-1016-j-cub-2012-02-052`, `src-doi-10-1371-journal-pgen-1005091`, `src-doi-10-1016-j-bbrc-2020-01-124`  
   - Claims: `claim-chen-a-heso1-unmethylated-substrates`, `claim-chen-c-004`, `claim-chen-c-008`
4. **存在正式 correction 时必须随原结果传播。** SDN 2008 的定量/figure-level 复用必须同时检查 2018 erratum；correction 是版本审计，不是独立复制。  
   - Sources: `src-doi-10-1126-science-1163728`, `src-doi-10-1126-science-aav2481`  
   - Claim: `claim-chen-a-sdn-turnover`

### `expert_position`

1. **以 lifecycle stage 定位 altered miRNA abundance。** Transcription、precursor processing/stability、methylation、loading、action 和 turnover 分开；整合检查表是从团队研究与作者综述提炼的 Lens。  
   - Sources: `src-doi-10-1073-pnas-2208415119`, `src-doi-10-1038-s41467-022-28872-x`, `src-doi-10-1105-tpc-113-113159`  
   - Claims: `claim-chen-a-stage-separated-diagnosis`, `claim-chen-b01`, `claim-chen-b11`
2. **RNA entity resolution 先于机制。** MIR locus、pri/pre、duplex、mature arm/isomiR 和 AGO-loaded product 不可混称。  
   - Sources: `src-doi-10-1038-s41477-019-0562-1`, `src-doi-10-1093-nar-gkj474`, `src-doi-10-1038-s41467-022-28872-x`  
   - Claims: `claim-chen-b02`, `claim-chen-b05`, `claim-chen-b07`
3. **空间 claim 要有 stage-matched readout。** ER、TREX-2/NPC、RBV 和 microtubule/AGO1-loading 研究共同支持 step × compartment 审查。  
   - Sources: `src-doi-10-1016-j-cell-2013-04-005`, `src-doi-10-1038-s41477-020-0726-z`, `src-doi-10-1016-j-devcel-2022-03-015`  
   - Claims: `claim-chen-a-er-translation-cleavage-separation`, `claim-chen-b08`, `claim-chen-b09`
4. **Total abundance 与 AGO loading 分离。** Loading claim 需要 AGO-associated readout 及 input/protein/recovery controls。  
   - Source: `src-doi-10-1038-s41467-022-28872-x`  
   - Claims: `claim-chen-a-rbv-coupled-checkpoints`, `claim-chen-b07`
5. **Mobility 分阶段。** Source production、source-cell loading、movement、recipient loading、target effect 与 phenotype 逐段报告。  
   - Sources: `src-doi-10-15252-embj-2018100754`, `src-doi-10-15252-embj-2020107455`, `src-doi-10-1016-j-devcel-2022-03-015`  
   - Claims: `claim-chen-a-mobility-loading-context`, `claim-chen-c-009`, `claim-chen-c-010`

### `contested` or context-dependent

1. **Cleavage、RNA decay 与 translational repression 的相对贡献。** 多种作用模式真实存在，但 target、site、tissue、stage、protein/RNA assay 与 AGO context 决定可见比例。不得形成普遍排序。  
   - Claims: `claim-chen-c-002`, `claim-chen-c-007`
2. **D-body abundance 是否定量决定 locus-specific processing flux。** SERRATE phase separation 支持 assembly/processing connection；visible body 仍不能替代 nascent、precursor/intermediate 与 rate measurements。  
   - Sources: `src-doi-10-1073-pnas-0802493105`, `src-doi-10-1038-s41556-020-00606-5`  
   - Claim: `claim-chen-c-005`
3. **Tail 是 cause、consequence 还是 competing branch。** HESO1/URT1 与 trimming 使单一 endpoint 有多种解释；需要 enzyme-combination mutants、AGO fraction 与 rate-resolved design。  
   - Claims: `claim-chen-c-004`, `claim-chen-c-008`
4. **AGO loading 与 mobility 的关系。** Source-cell cytoplasmic loading 可在测试的 root/miR165/166 情境与 movement 竞争；其他 family、tissue、长距离运输或 species 需重建证据链。  
   - Claims: `claim-chen-b09`, `claim-chen-c-009`, `claim-chen-c-010`

### `historical`

1. **2002 DCL1/HEN1 genetics 是路径入口。** 它建立 genetic requirement 与 developmental connection，但未用现代分辨率定位全部 lifecycle steps。  
   - Source: `src-doi-10-1016-s0960-9822-02-01017-5`  
   - Claims: `claim-chen-a-dcl1-hen1-genetic-entry`, `claim-chen-c-001`
2. **2004 miR172/AP2 是 protein-level action 的早期锚点。** 后续独立研究将 translational repression 扩展到其他实验体系，但不把原例升级成 universal prevalence。  
   - Sources: `src-doi-10-1126-science-1088060`, `src-doi-10-1126-science-1159151`, `src-doi-10-1016-j-molcel-2013-10-033`  
   - Claims: `claim-chen-b03`, `claim-chen-c-002`
3. **终端保护图景被扩展而非推翻。** 2005 HEN1 protection 后由 SDN、HESO1/URT1、AGO context 和 trimming 细化成分支网络。  
   - Claim: `claim-chen-c-011`
4. **公开研究轨迹由 genetics 扩展至 spatial loading/movement。** 官方 Q&A 只支持历史轨迹，不能充当机制验证或当前个人观点。  
   - Source: `src-url-ucr-qa-xuemei-chen-2020`  
   - Claim: `claim-chen-a-genetics-to-rna-trajectory`

### `superseded` operational shortcuts

以下做法被当前证据框架取代，不是对个人观点的归因：

1. **把 mature-miRNA endpoint 直接命名为 transcription 或 processing defect**，由 lifecycle-stage localization 取代。  
   - Claims: `claim-chen-b01`, `claim-chen-b11`
2. **把 HEN1 protection 写成“mature miRNA 不再 turnover”**，由 SDN/HESO1/URT1/AGO-context network 取代。  
   - Claims: `claim-chen-a-sdn-turnover`, `claim-chen-b10`, `claim-chen-c-008`
3. **把 plant miRNA action 简化为 cleavage-only 或 translation-only**，由 target-specific paired RNA/protein readouts 取代。  
   - Claims: `claim-chen-c-002`, `claim-chen-c-007`
4. **把 localization、AGO association 或 recipient reads 当作完整 spatial mechanism**，由 step × compartment 与 mobility gates 取代。  
   - Claims: `claim-chen-b08`, `claim-chen-c-009`

### `hypothesis`

1. 某个未测试因素影响 lifecycle 的具体节点：在实体和相邻-stage readouts 补齐前保持 hypothesis。
2. 某个 U-tail 由唯一 enzyme 产生或是 rate-limiting decay step：在 enzyme-combination 与 rate-resolved evidence 前保持 hypothesis。
3. 某个 miRNA 由 source cell 移动并在 recipient 中造成表型：每个未直接支持的 gate 均保持 hypothesis。
4. 可见 D-body 对每个 MIR locus 的 processing flux 都是必要且定量的：需 locus-specific rate/perturbation evidence。

### `agent_inference`

1. **Stage-separated diagnostic** 是作者综述、公开 where/how scope 与多项团队研究的综合，不是命名的个人框架。  
   - Claim: `claim-chen-a-stage-separated-diagnosis`
2. **Genetics–mechanism–RNA triangulation** 是跨 HEN1、HESO1、TREX-2/NPC、RBV 与 movement 研究提炼的决策协议。  
   - Claim: `claim-chen-b12`
3. **从 genetic requirement 到 branched turnover 与 spatial gates 的时间线** 是项目综合，不代表当前私人判断。  
   - Claim: `claim-chen-c-011`
4. **Family/locus/precursor/arm/isomiR/sequence/assembly 强制分层** 是项目级实体卫生与本 corpus 方法的结合；不能据此宣称存在 Chen 特有 de novo miRNA annotation standard。

## Methodological Tensions

### Tension T1 — Cleavage vs translational repression

```yaml
position_a: plant miRNA-target complementarity can support cleavage or RNA decay
position_b: direct genetic and biochemical evidence also supports translational repression
status: resolved_as_target_and_context_dependent_coexistence
resolution_rule: pair target-site evidence with matched RNA and protein readouts, then separately rate phenotype causality
must_not_do: infer a universal dominant mode from miR172/AP2 or from RNA-only assays
source_ids:
  - src-doi-10-1126-science-1088060
  - src-doi-10-1126-science-1159151
  - src-doi-10-1016-j-molcel-2013-10-033
claim_ids:
  - claim-chen-c-002
  - claim-chen-c-007
```

### Tension T2 — Terminal protection vs ongoing turnover

```yaml
position_a: HEN1 methylation protects small-RNA 3-prime ends from uridylation and trimming
position_b: mature miRNAs still undergo SDN-mediated and context-dependent turnover
status: refined_not_contradicted
resolution_rule: separate methylation state, AGO context, substrate stage, nuclease/tailase genotype and flux
must_not_do: translate protection into absolute stability
source_ids:
  - src-doi-10-1016-j-cub-2005-07-029
  - src-doi-10-1126-science-1163728
  - src-doi-10-1073-pnas-1405083111
claim_ids:
  - claim-chen-a-methylation-protects-ends
  - claim-chen-a-sdn-turnover
  - claim-chen-b10
```

### Tension T3 — Linear tailing model vs branched network

```yaml
position_a: an observed U-tail may implicate HESO1 or URT1 activity
position_b: redundancy, sequentiality and trimming can yield the same endpoint pattern
status: context_dependent_branched_network
resolution_rule: use enzyme-combination genotypes, AGO/free fractions and rate-resolved measurements
must_not_do: assign a unique enzyme or degradation rate from one steady-state end profile
source_ids:
  - src-doi-10-1016-j-cub-2012-02-052
  - src-doi-10-1371-journal-pgen-1005091
  - src-doi-10-1016-j-bbrc-2020-01-124
claim_ids:
  - claim-chen-c-004
  - claim-chen-c-008
```

### Tension T4 — Processing-body localization vs locus-specific flux

```yaml
position_a: SERRATE phase separation and D-body assembly can promote miRNA processing
position_b: visible localization and pleiotropic mutants do not quantify processing for every pri-miRNA
status: contested_scope_and_rate
resolution_rule: combine separation-specific perturbation with nascent transcription, precursor/intermediate and processing-rate measurements
must_not_do: use body number or colocalization as a proxy for direct catalytic flux
source_ids:
  - src-doi-10-1073-pnas-0802493105
  - src-doi-10-1038-s41556-020-00606-5
claim_ids:
  - claim-chen-c-005
```

### Tension T5 — AGO loading vs mobility

```yaml
position_a: AGO loading is required for effector activity
position_b: source-cell cytoplasmic AGO1 loading can compete with mobility in the tested miR165/166 root context
status: context_dependent_spatial_gate
resolution_rule: separately measure source production, source loading, movement, recipient loading, target effect and phenotype
must_not_do: generalize the microtubule mechanism to all miRNAs, tissues or long-distance transport
source_ids:
  - src-doi-10-15252-embj-2018100754
  - src-doi-10-15252-embj-2020107455
  - src-doi-10-1016-j-devcel-2022-03-015
claim_ids:
  - claim-chen-b09
  - claim-chen-c-009
  - claim-chen-c-010
```

### Tension T6 — Arabidopsis mechanistic depth vs cross-species transfer

```yaml
position_a: Arabidopsis genetics and biochemistry provide unusually deep stage-specific mechanisms
position_b: paralogs, MIR loci, tissues, AGO families and processing routes may differ in crops or other taxa
status: transfer_requires_revalidation
resolution_rule: label transfer as conserved, analogous, lineage_specific, uncertain or unsupported_transfer and require organism-matched evidence
must_not_do: infer orthology from a shared family name or import animal Drosha-DGCR8, seed-only or Exportin-5 logic into plants
source_ids:
  - src-doi-10-1093-nar-gkj474
  - src-doi-10-15252-embj-2020107455
claim_ids:
  - claim-chen-a-hen1-duplex-specificity
  - claim-chen-c-009
```

## Conflict-resolution procedure

1. 对齐 species、tissue、stage、genotype、treatment、time point、assembly 与 assay sensitivity；
2. 对齐实体：MIR gene family、locus、pri/pre、duplex、mature arm/isomiR、AGO-loaded product、target；
3. 对齐 lifecycle step 与 compartment；
4. 比较 directness，并将 target directness、action mode 与 phenotype causality 分轴；
5. 审计 independence：同一实验室、共同作者和共享方法 cluster 不重复计数；
6. 检查 correction/retraction/EoC；原论文与 formal erratum 作为版本链，不作两项独立证据；
7. 保留仍不可解的范围差异，并提出能区分解释的实验；
8. 不以论文新旧、期刊、引用量、专家名望或 Agent 多数投票决定胜负。

## Current unresolved limits

- Cleavage、RNA decay 与 translational repression 在新 target 中的相对贡献必须逐例测量。
- Visible D-body 对每个 MIR locus 的 quantitative processing flux 未由本 corpus 普遍建立。
- HESO1/URT1/SDN 在具体 AGO-bound/free substrate 上的 rate-limiting contribution 仍依体系。
- Microtubule-limited source-cell AGO1 loading 的广泛可迁移性未建立。
- 2018 SDN erratum 的具体 figure/quantitative 影响未在本 corpus 闭合；禁止细节复用。
- AAR2 correction 已闭合为版本链：影响 Fig. 1/Fig. S3 legends 及 Figs. 6/S2/S6；本 corpus 的 promoter/decay 结论映射到未受影响的 Figs. 3/4。Correction 不计独立支持。
- 官方讲座缺 transcript/Q&A；只能支持日期、范围和 where/how framing，不能构建个人语气或反驳风格。
