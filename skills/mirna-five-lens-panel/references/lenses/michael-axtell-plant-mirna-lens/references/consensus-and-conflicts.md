# Consensus, Status, and Conflicts — Michael J. Axtell Lens

```yaml
expert_id: michael-j-axtell
evidence_cutoff: 2026-07-17
phase: N2
principle: expert_framework_status_is_not_scientific_truth_status
```

本文件把“该框架是否具有 Axtell 研究特征”与“科学事实是否已获独立支持”分开。`expert_position` 不等于 `field_consensus`；`agent_inference` 不得改写为专家原话。

## Knowledge-status map

### `field_consensus`

1. **数据库收录不等于实验确认。** miRBase 自身质量工作、动物独立重注释和植物 PmiREN 重注释均支持对 locus、arm、endpoint、assembly 与 evidence tier 重新审计。动物百分比不得数值外推到植物。  
   - Sources: `src-pmid-22303321`, `src-pmid-30423142`, `src-doi-10.1093-nar-gkz894`  
   - Claims: `claim-axtell-c-005`, `claim-axtell-c-006`
2. **靶标预测、切割证据和表型因果是不同层级。** Degradome/PARE 与 reporter 强于预测，但不能各自完成完整表型因果链。  
   - Sources: `src-doi-10-1016-j-cub-2008-04-042`, `src-doi-10-1105-tpc-113-120972`  
   - Claim: `claim-axtell-a-target-evidence-ladder`
3. **正式 correction 必须随相关结果传播。** 2024 notice 修正 2023 Cuscuta promoter 论文图 3A/3D 的回归方程；通知称 lines、r²、underlying data 与 conclusions 不变。Correction 不是独立复制。  
   - Source: `src-doi-10.1093-plcell-koad305`  
   - Claim: `claim-axtell-c-009`

### `expert_position`

1. **生物发生优先的身份闸门。** 植物 MIRNA 先由 precise miRNA/miRNA* processing 与 locus evidence 评定，target/conservation/database 不能代替。  
   - Sources: `src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`  
   - Claims: `claim-axtell-a-identity-before-function`, `claim-axtell-b01`
2. **大背景类下优先最小化假阳性。** 新注释要求 biological replication，23–24 nt 候选需要极强证据；算法输出只生成 hypothesis。  
   - Sources: `src-doi-10-1105-tpc-17-00851`, `src-axtell-31245701`  
   - Claims: `claim-axtell-b02`, `claim-axtell-b03`, `claim-axtell-b06`, `claim-axtell-b07`
3. **多参数 locus evidence vector。** Size、strand、repeat、hairpin、precision、phasing、dependency 与 mapping 共同解释，工具标签不自动成立。  
   - Sources: `src-doi-10-1261-rna-035279-112`, `src-doi-10-1111-tpj-13919`, `src-axtell-27175019`  
   - Claims: `claim-axtell-a-multiparameter-locus-profile`, `claim-axtell-b08`, `claim-axtell-b09`
4. **保留 provisional/unclassified。** Homology-only、低信息、缺 star 或与已知类别不合时，不强制赋名。  
   - Sources: `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1111-tpj-13919`, `src-axtell-32179590`  
   - Claims: `claim-axtell-b03`, `claim-axtell-b05`, `claim-axtell-b13`
5. **Trans-species 结论分阶段。** Detection、movement、recipient effector use、direct target 与 phenotype 分开报告。  
   - Sources: `src-doi-10-1038-nature25027`, `src-doi-10-1016-j-pbi-2019-03-014`, `src-pmid-42417192`  
   - Claims: `claim-axtell-a-transspecies-chain`, `claim-axtell-talk-transspecies-uncertainty-ladder`, `claim-axtell-c-011`

### `contested`

1. **ShortStack 与替代工具的性能排序。** miRkwood 在其特定 benchmark 中报告较优表现；这证明工具性能有条件，不证明其在所有物种、版本和参数上普遍优越。  
   - Sources: `src-doi-10-1261-rna-035279-112`, `src-pmid-31253093`  
   - Claims: `claim-axtell-c-003`, `claim-axtell-c-004`
2. **固定严格阈值与谱系敏感性。** 严格、可重复的 processing criteria 降低植物 siRNA 背景假阳性；独立 miRA 工作提示绿藻/异质 precursor 可能需要 lineage-aware 参数。正确响应是预声明 benchmark，不是事后豁免。  
   - Sources: `src-doi-10-1105-tpc-17-00851`, `src-pmid-26542525`  
   - Claims: `claim-axtell-c-002`, `claim-axtell-c-007`

### `historical`

1. **2005 深保守关系是早期发现轴。** 后续框架把保守性定位为先验/历史证据，而非新 locus 身份的必要或充分条件。  
   - Sources: `src-doi-10-1105-tpc-105-032185`, `src-doi-10-1105-tpc-17-00851`  
   - Claims: `claim-axtell-c-001`, `claim-axtell-a-conservation-calibrates-prior`
2. **2008→2018 标准收紧。** 2018 修订针对大规模 sRNA-seq 下的 questionable annotations，强化 biological replication 与 false-positive minimization。  
   - Sources: `src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`  
   - Claim: `claim-axtell-c-002`
3. **2018–2026 研究范围扩展。** 公开记录从 annotation/evolution 并行扩展到 Cuscuta trans-species targeting、promoter 与 AGO-loading 问题；这是方向时间线，不是每个环节均成领域共识。  
   - Claims: `claim-axtell-talk-expansion-with-boundary`, `claim-axtell-c-011`

### `superseded`

以下是被当前框架取代的操作做法，不是对某位作者私人观点的归因：

1. **以 predicted hairpin、conservation、target prediction 或数据库条目作为植物 MIRNA 身份充分条件**，已被 processing- and replication-centered criteria 取代。  
   - Claims: `claim-axtell-b01`, `claim-axtell-b02`
2. **把 homology-only 第二物种记录直接写成已确认 MIRNA locus**，已被 provisional status 取代。  
   - Claim: `claim-axtell-b03`
3. **把一个软件 pass/fail 或多个共享假设的软件一致性当生物学验证**，已被 per-locus evidence 与 independence audit 取代。  
   - Claims: `claim-axtell-c-003`, `claim-axtell-c-012`

### `hypothesis`

1. **非经典或谱系特异 miRNA 生物发生。** 可以作为候选解释，但必须在看到结果前声明其 precursor、processing 与 pathway predictions，并用 lineage-matched positives/hard negatives 验证。  
   - Source: `src-pmid-26542525`  
   - Claim: `claim-axtell-c-007`
2. **某个算法发现的 24-nt PHAS locus。** 在 stable register、trigger 和 genetics 未通过前只属 hypothesis，不是类别事实。  
   - Source: `src-axtell-31245701`  
   - Claims: `claim-axtell-b06`, `claim-axtell-b07`
3. **跨物种 RNA 整条因果链。** 每个尚未直接支持的环节保持 hypothesis；不能由相邻环节自动填充。  
   - Claims: `claim-axtell-a-transspecies-chain`, `claim-axtell-talk-transspecies-uncertainty-ladder`

### `agent_inference`

1. **Discovery → classification → function 的审阅顺序**来自报告题目与论文三角综合，不是讲座逐字内容。  
   - Claim: `claim-axtell-talk-discovery-classification-function`
2. **Family/locus/precursor/arm/sequence/assembly 的强制实体解析**是从注释标准提炼的操作规则，不是专家原话。  
   - Claim: `claim-axtell-a-entity-resolution`
3. **异常应修订分类而不是被隐藏**是对 RDR 与苔藓研究决策的综合。  
   - Claim: `claim-axtell-a-exceptions-revise-classification`
4. **跨物种同名审计的完整层级**来自 evolution talk title 与比较论文综合；无 transcript 支持现场措辞。  
   - Claim: `claim-axtell-talk-evolution-separates-homology-levels`

## Methodological Tensions

### Tension T1 — Specificity vs lineage sensitivity

```yaml
position_a: strict precise-processing and replication rules reduce false positives in the enormous plant siRNA background
position_b: fixed precursor assumptions may lose heterogeneous or lineage-specific true positives
status: contested_context_dependent
resolution_rule: predeclare lineage-aware thresholds and validate on matched positives and hard negatives
must_not_do: relax criteria only after seeing a favored candidate
source_ids:
  - src-doi-10-1105-tpc-17-00851
  - src-pmid-26542525
claim_ids:
  - claim-axtell-c-002
  - claim-axtell-c-007
```

### Tension T2 — Harmonized tools vs locus-level judgment

```yaml
position_a: standardized pipelines make multi-species analyses reproducible and expose evidence fields
position_b: performance and labels depend on dataset, assembly, parameters, version and shared assumptions
status: contested_method_dependent
resolution_rule: freeze inputs and versions, compare per-locus errors, and add independent biological validation
must_not_do: treat any tool as an oracle or rank tools universally from one benchmark
source_ids:
  - src-doi-10-1261-rna-035279-112
  - src-pmid-31253093
  - src-pmid-41183249
claim_ids:
  - claim-axtell-c-003
  - claim-axtell-c-004
  - claim-axtell-c-012
```

### Tension T3 — Conservation as prior vs novelty as possibility

```yaml
position_a: deep conservation strengthens antiquity and conserved regulatory relationships
position_b: genuine young loci can lack conservation and old family names do not prove each locus
status: resolved_as_separate_claim_layers
resolution_rule: use conservation to calibrate prior, then require species-specific biogenesis for identity
must_not_do: reject novelty solely for nonconservation or accept orthology solely from a shared name
source_ids:
  - src-doi-10-1105-tpc-105-032185
  - src-doi-10-1105-tpc-110-073882
  - src-doi-10-1105-tpc-17-00851
claim_ids:
  - claim-axtell-a-conservation-calibrates-prior
  - claim-axtell-c-001
  - claim-axtell-c-008
```

### Tension T4 — Classification completeness vs honest unresolved bins

```yaml
position_a: comparative resources benefit from harmonized categories
position_b: low coverage, missing star reads and unexplained genetics make some loci genuinely unresolved
status: expert_position_with_operational_categories
resolution_rule: retain nearMIRNA, ambiguous or unclassified with explicit upgrade and rejection evidence
must_not_do: turn an evidence-gap category into a stable biological class
source_ids:
  - src-doi-10-1111-tpj-13919
  - src-axtell-32179590
claim_ids:
  - claim-axtell-b05
  - claim-axtell-b13
```

## Conflict-resolution procedure

遇到相反结论时依次执行：

1. 对齐 species、tissue、stage、genotype、treatment、assembly、library 与软件版本；
2. 对齐实体层级：family、locus、precursor、arm、sequence、target；
3. 比较 directness：prediction < association < cleavage/reporter < target-site genetics/rescue；
4. 审计 independence：同一实验室、共同作者和共享方法谱系不重复计数；
5. 区分结论冲突、范围差异、采样盲区和阈值差异；
6. 保留仍不可解的部分，并提出可区分解释的实验；
7. 不以论文新旧、期刊、引用量、专家名望或 Agent 多数投票决定胜负。

## Current unresolved limits

- ShortStack 与 miRkwood 的普遍性能排序未解决；现有比较只支持条件性判断。
- Strict criteria 的最佳 lineage-specific 数值参数未由本语料给出。
- 2026 Cuscuta self-AGO avoidance 结果缺少本语料内独立实验室复制。
- 三场报告没有 transcript/Q&A，不能形成直接的“响应风格”模型。
- 2023 promoter correction 已明确且结论据通知不变，但任何复用回归方程时仍须携带 correction。
