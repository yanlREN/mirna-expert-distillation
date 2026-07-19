# Paper Interrogation Frameworks — Michael J. Axtell Lens

```yaml
expert_id: michael-j-axtell
evidence_cutoff: 2026-07-17
dimension_count: 6
purpose: generate evidence-revealing questions, not imitate a person or pre-answer the paper
```

## Input contract

```yaml
article:
  title:
  abstract_or_text:
  organism:
  species:
  genome_assembly:
  section:
  figures_or_tables_available:
user_focus:
entities_if_stated:
  mirna_family:
  mir_locus:
  precursor:
  mature_arm:
  mature_sequence:
  target_gene:
```

缺失字段写入 `missing_context`，不得猜测。先提取文章明确主张及其 anchor，再从下列维度选择最相关的 2–4 个模型；纯文章提问模式只生成问题和依据，不预先回答。

## Dimension Q1 — 实体与身份闸门

```yaml
dimension_id: AXT-Q1
name: entity_and_biogenesis_identity
lens_model_ids: [AXT-M1, AXT-M2]
primary_risk: mirna_identity_inflation
```

### 先识别

- 文章说的是 miRNA family、MIR gene family、特定 locus、precursor、5p/3p product、isomiR、具体序列，还是数据库记录？
- coordinate 是否绑定 species 与 assembly？
- 身份证据来自 hairpin prediction、单一 library、miRNA/miRNA* duplex、加工精度、遗传依赖还是数据库？

### 高价值问题模板

1. 该结论对应哪个具体 MIR locus、precursor、mature arm 与序列；这些对象是否在全文和图表中保持一致？
2. 全位点 read distribution 是否显示精确 duplex 加工，还是只展示了最有利的局部 read/hairpin？
3. 新注释是否在至少两个 biological libraries 中复现；technical/read multiplicity 是否被误当作生物学重复？
4. 哪些数据直接排除了 hc-siRNA、phasiRNA、其他 hairpin RNA、tRF/rRNA fragment 或随机降解？
5. 23–24 nt 候选为何足以克服巨大 24-nt siRNA 背景的假阳性风险？

### 预期证据

`genome-mapped small_rna_seq`, precursor folding, miRNA/miRNA* duplex geometry, biological replication, locus-wide size/strand/repeat patterns, pathway genetics where relevant.

### 依据

- `claim_ids`: `claim-axtell-b01`, `claim-axtell-b02`, `claim-axtell-a-multiparameter-locus-profile`, `claim-axtell-a-entity-resolution`
- `source_ids`: `src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1261-rna-035279-112`

## Dimension Q2 — 算法、背景类与复现

```yaml
dimension_id: AXT-Q2
name: algorithm_background_and_reproducibility
lens_model_ids: [AXT-M2, AXT-M3]
primary_risk: computational_false_positive
```

### 先识别

- 正类有多稀少，主要混淆背景类有多大？
- 多个工具是否真正独立，还是共享标准、作者、代码或输入偏差？
- PHAS/precision 的定义性 pattern 是否在同一 register/位置跨 libraries 复现？

### 高价值问题模板

1. 在全部搜索空间中有多少背景 loci 可能按机会通过同一阈值；是否控制多重筛选与 cherry-picking？
2. 软件版本、参数、reference assembly、multi-mapper policy 和未合并 biological libraries 是否可复现？
3. 所谓“多个算法一致”是否来自独立假设，还是共享实现标准或合作网络？
4. 若主张 24-nt PHAS，dominant phase register 是否稳定，trigger 与 RDR/DCL 依赖是否匹配，并有何阳性/硬阴性对照？
5. 当工具冲突时，作者是否展示 per-locus evidence fields，而不是只比较总分或标签？

### 预期证据

Frozen tool versions, parameter files, per-locus feature tables, biological replicate register/precision, genetic dependencies, trigger evidence, positive/hard-negative controls, multimapper audit.

### 依据

- `claim_ids`: `claim-axtell-b06`, `claim-axtell-b07`, `claim-axtell-b09`, `claim-axtell-c-004`, `claim-axtell-c-012`
- `source_ids`: `src-axtell-31245701`, `src-axtell-27175019`, `src-pmid-31253093`, `src-pmid-41183249`

## Dimension Q3 — 靶标直接性与表型因果

```yaml
dimension_id: AXT-Q3
name: target_directness_and_phenotype_causality
lens_model_ids: [AXT-M1]
primary_risk: prediction_to_causality_jump
```

### 先识别

- claim 是预测互补、表达关联、切割、AGO association、site-dependent repression，还是 organismal phenotype？
- RNA 与 protein readout 是否都测量？靶位点对照是否只改变拟议 interaction？

### 高价值问题模板

1. 预测靶标是否有位置匹配的 PARE/degradome/5′-end、reporter 或其他直接证据？
2. degradome peak 是否能与一般 decay 或 precursor processing 区分；匹配的组织、处理和基因型是什么？
3. reporter 的 target-site-disrupted control 是否保持编码蛋白不变，并同时检测 RNA 与 protein level？
4. transient Nicotiana assay 的剂量、组织和异源 context 与原生体系有何差异？
5. 哪项 target-site genetics、rescue 或等价干预把直接靶向连接到完整表型；若没有，作者是否限制了措辞？

### 预期证据

PARE/degradome or 5′ RACE, matched site-mutant reporter, RNA/protein measurements, endogenous target-site genetics, rescue/epistasis, matched tissue/stage/genotype.

### 依据

- `claim_ids`: `claim-axtell-a-target-evidence-ladder`, `claim-axtell-b10`, `claim-axtell-b11`, `claim-axtell-b12`
- `source_ids`: `src-doi-10-1016-j-cub-2008-04-042`, `src-axtell-19850910`, `src-doi-10-1105-tpc-113-120972`

## Dimension Q4 — 演化、同源与缺失边界

```yaml
dimension_id: AXT-Q4
name: evolution_homology_and_absence
lens_model_ids: [AXT-M4]
primary_risk: same_name_equals_orthology
```

### 先识别

- 保守的是 mature sequence、precursor structure、syntenic locus、target site 还是 phenotype？
- “缺失”基于何种 tissue/stage/library depth 与 assembly quality？
- 数据库版本与命名是否掩盖 locus/arm 改变？

### 高价值问题模板

1. 跨物种同名是否有 locus synteny/origin 证据，还是仅成熟序列相似？
2. 各物种是否分别满足 species-specific processing criteria，还是由 homology 投射注释？
3. family-level antiquity 如何与特定 locus 的 birth/death、arm 和 sequence 证据区分？
4. 未检出是否可能由组织、发育阶段、建库深度、mapping 或 assembly 缺陷解释？
5. 结论依赖哪个数据库版本；坐标、mature/star placement 或 confidence 是否经原始 reads 复核？

### 预期证据

Species-specific sRNA-seq, assemblies and coordinates, synteny/locus origin, precursor processing, target-site conservation, explicit sampling matrix, database version history.

### 依据

- `claim_ids`: `claim-axtell-a-conservation-calibrates-prior`, `claim-axtell-c-001`, `claim-axtell-c-005`, `claim-axtell-c-008`, `claim-axtell-talk-evolution-separates-homology-levels`
- `source_ids`: `src-doi-10-1105-tpc-105-032185`, `src-doi-10-1105-tpc-110-073882`, `src-pmid-30423142`, `src-doi-10.1093-nar-gkz894`

## Dimension Q5 — 不确定类别、工具冲突与阈值张力

```yaml
dimension_id: AXT-Q5
name: uncertainty_bins_and_method_tensions
lens_model_ids: [AXT-M3, AXT-M4]
primary_risk: forced_binary_classification
```

### 先识别

- 缺 star、低 counts、variance 或工具冲突是否被隐藏？
- lineage-specific 参数是在看到候选前验证，还是事后放宽？
- `nearMIRNA`/ambiguous/unclassified 是否被误写成生物学类别？

### 高价值问题模板

1. 哪些候选因缺失 miRNA*、replicate coverage 或相互矛盾的 feature 被保留为 provisional，而非强制接受/拒绝？
2. 若放宽 precursor/precision 阈值，是否在 lineage-matched positives 与 hard negatives 上预先验证？
3. 工具排名是否在相同 assembly、libraries、versions、defaults 与评价指标下完成？
4. 独立 support 是不同实验室和方法，还是同一合作网络的多款软件？
5. 什么新增实验会把当前 `nearMIRNA`/ambiguous/unclassified 升级、降级或维持？

### 预期证据

Predeclared thresholds, lineage-matched benchmark, per-locus disagreements, replicate uncertainty, hard negatives, independent-lab evidence, explicit upgrade/downgrade rule.

### 依据

- `claim_ids`: `claim-axtell-b05`, `claim-axtell-b13`, `claim-axtell-c-003`, `claim-axtell-c-004`, `claim-axtell-c-007`
- `source_ids`: `src-doi-10-1111-tpj-13919`, `src-axtell-32179590`, `src-pmid-26542525`, `src-pmid-31253093`

## Dimension Q6 — Trans-species 链条与界面伪影

```yaml
dimension_id: AXT-Q6
name: transspecies_chain_and_interface_artifacts
lens_model_ids: [AXT-M5, AXT-M1]
primary_risk: detection_to_cross_species_function_jump
```

### 先识别

- donor identity、source assignment、movement、recipient loading、direct target 与 phenotype 各有哪些独立证据？
- 界面取样能否排除组织混合、污染与相同序列多来源？
- Cuscuta 特异 promoter/AGO 现象是否被无依据泛化？

### 高价值问题模板

1. donor locus 与 precursor 如何确认，受体样本中的 reads 如何唯一归属于 donor？
2. 取样、洗涤、空间定位、遗传或方向性设计如何排除界面组织混合和污染？
3. 数据证明的是 presence 还是 movement；两者之间缺少哪一步？
4. 是否直接检测 recipient AGO/effector loading；donor self-AGO avoidance 与 recipient loading 是否被区分？
5. 宿主靶标有何 matched cleavage/reporter/genetic evidence，且是否来自正确组织、阶段和互作条件？
6. 若声称表型，哪项靶位点干预或 rescue 证明该跨物种 RNA 是因果而非伴随？
7. 结论是否被限制在 Cuscuta-host 体系，还是无依据外推到膳食 RNA、其他植物或 cross-kingdom 情形？

### 预期证据

Donor locus/precursor evidence, interface/spatial controls, directional movement evidence, recipient AGO loading, matched target cleavage/reporter, target-site genetics/rescue, taxon-specific boundary.

### 依据

- `claim_ids`: `claim-axtell-a-transspecies-chain`, `claim-axtell-talk-transspecies-uncertainty-ladder`, `claim-axtell-c-011`
- `source_ids`: `src-doi-10-1038-nature25027`, `src-doi-10-7554-elife-49750`, `src-doi-10-1093-plcell-koad076`, `src-pmid-42417192`

## Question ranking

按以下顺序排序，不按“看起来高级”排序：

1. 会改变核心身份或因果结论的问题；
2. 能区分两个可行替代解释的问题；
3. 暴露 species/assembly/entity mismatch 的问题；
4. 暴露 evidence directness 或 independence 误标的问题；
5. 指向一个可执行关键实验的问题；
6. 仅改善表述而不改变判断的问题。

## Output schema

```json
{
  "question_id": "AXT-Q?-NN",
  "question": "",
  "lens_model_ids": [],
  "question_type": "identity|method|directness|causality|alternative_explanation|scope|evolution|conflict|next_experiment",
  "article_anchor": "",
  "why_it_matters": "",
  "answerable_from_article": true,
  "external_evidence_needed": false,
  "risk_flags": [],
  "expected_evidence_type": [],
  "source_ids": [],
  "claim_ids": []
}
```

## Quality stop rules

- 不把文章未提供的信息写成问题前提。
- 不询问专家私人意见，也不写“Axtell 会怎么说”。
- 不把通用“有没有对照/重复”当高价值问题；必须指出 Axtell Lens 相关的具体对照、背景类、位点特征或升级门槛。
- 若当前语料不能支持某一事实性前提，写 `current corpus insufficient`。
- correction `src-doi-10.1093-plcell-koad305` 必须随 2023 promoter 论文回归方程的任何复用一并检查。
