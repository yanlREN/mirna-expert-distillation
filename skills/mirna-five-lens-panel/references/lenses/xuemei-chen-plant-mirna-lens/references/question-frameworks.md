# Paper Interrogation Frameworks — Xuemei Chen Lens

```yaml
expert_id: xuemei-chen
evidence_cutoff: 2026-07-17
dimension_count: 6
purpose: generate_evidence_revealing_questions_not_personal_imitation_or_preanswers
```

## Input contract

```yaml
article:
  title:
  abstract_or_text:
  organism:
  species:
  genome_assembly:
  tissue:
  developmental_stage:
  genotype:
  treatment:
  section:
  figures_or_tables_available:
user_focus:
entities_if_stated:
  mirna_family:
  mir_locus:
  precursor:
  mature_arm:
  mature_sequence:
  isomir_or_end_state:
  target_gene:
```

缺失字段写入 `missing_context`，不得猜测。先提取文章的明确主张及其 anchor，再选择最相关的 2–4 个模型。纯文章提问模式只生成问题和依据，不预先回答。该 Lens 不提供 Chen 特有的新 miRNA 注释模型；若文章主张新 miRNA 身份，必须调用 Evidence Auditor 或植物注释专门 Lens，并保持 I0–I3 与功能证据分开。

## Dimension Q1 — RNA 实体与生命周期阶段

```yaml
dimension_id: CHEN-Q1
name: rna_entity_and_lifecycle_localization
lens_model_ids: [CHEN-M1]
primary_risk: endpoint_abundance_to_mechanism_jump
```

### 先识别

- 所测对象是 MIR gene family、特定 locus、pri/pre-miRNA、duplex、mature 5p/3p、isomiR、具体序列还是 AGO-loaded product？
- 观察值位于 transcription、processing/stability、methylation、loading、action 或 turnover 的哪一步？
- Assay 的 tissue、time point、genotype 与动态范围是否足以比较相邻阶段？

### 高价值问题模板

1. “miRNA abundance” 对应哪个具体实体和 assay；family、locus、arm、sequence 与 assembly 是否始终一致？
2. Promoter activity、pri-miRNA abundance/decay、pre-miRNA ends、duplex、total mature 与 AGO1-IP 中哪些被直接测量？
3. 哪两个相邻 lifecycle explanations 同样能解释 endpoint，文章用什么 stage-matched readout 区分？
4. 一个中间体未变时，时间点、检测灵敏度或 tissue mismatch 是否足以造成假阴性？
5. 若声称新 miRNA，是否把身份 I0–I3 与 target/function F0–F4 分开，并调用了注释专门审计？

### 预期证据

MIR promoter/nascent RNA, pri-miRNA decay, precursor/end assays, duplex/methylation assays, total small-RNA measurements, AGO1-IP/loading, matched species/tissue/stage/genotype.

### 依据

- `claim_ids`: `claim-chen-a-stage-separated-diagnosis`, `claim-chen-b01`, `claim-chen-b02`, `claim-chen-b07`, `claim-chen-b11`
- `source_ids`: `src-doi-10-1073-pnas-2208415119`, `src-doi-10-1038-s41477-019-0562-1`, `src-doi-10-1038-s41467-022-28872-x`

## Dimension Q2 — 遗传、机制与替代解释

```yaml
dimension_id: CHEN-Q2
name: orthogonal_mechanism_and_alternative_explanations
lens_model_ids: [CHEN-M2, CHEN-M1]
primary_risk: pleiotropic_genetics_to_direct_mechanism
```

### 先识别

- Genetic evidence 回答 requirement、order、dosage、bypass、suppression 还是 direct interaction？
- 生化/定位 assay 与被声称的 RNA stage 是否匹配？
- Rescue、suppressor 或 epistasis 是否限定 allele、tissue、stage 与 dosage？

### 高价值问题模板

1. 除作者首选机制外，哪两个替代解释也能解释 phenotype 与 mature-miRNA endpoint？
2. Suppressor 是恢复原 pathway、旁路补偿、改变 dosage，还是减少竞争 substrate；各预测由什么 RNA readout 区分？
3. Partial allele 的 epistasis 是否被无依据外推到 null、其他组织或 enzyme 过量情境？
4. Genetics、biochemistry/localization 与 RNA-species readout 是否在同一阶段会合；缺失轴如何降低 claim strength？
5. Phenotype rescue 是否只证明 downstream consistency，还是有 stage-matched molecular restoration？

### 预期证据

Allele-defined genetics, complementation/rescue, suppressor mapping, epistasis, purified-enzyme or interaction/localization assay, RNA-entity-resolved readout, matched controls.

### 依据

- `claim_ids`: `claim-chen-a-substrate-pool-competition`, `claim-chen-a-heso1-unmethylated-substrates`, `claim-chen-b06`, `claim-chen-b08`, `claim-chen-b12`
- `source_ids`: `src-doi-10-1093-nar-gkq348`, `src-doi-10-1016-j-cub-2012-02-052`, `src-doi-10-1038-s41477-020-0726-z`

## Dimension Q3 — Step × Compartment 与 loading/movement

```yaml
dimension_id: CHEN-Q3
name: spatial_step_loading_and_movement
lens_model_ids: [CHEN-M3, CHEN-M1]
primary_risk: localization_or_recipient_reads_to_function
```

### 先识别

- Claim 是位置、interaction、flux、loading、movement、target engagement 还是 phenotype？
- Source/recipient cell、nucleus/cytoplasm、ER/polysome、D-body/nuclear pore 是否明确定义？
- Bulk、fraction、AGO-IP、cell-type 或 movement assay 的 controls 是否充分？

### 高价值问题模板

1. Colocalization、body abundance 或 compartment enrichment 如何由 perturbation 与 stage-matched readout 连接到 processing/loading/action？
2. Fraction purity、tag overexpression、AGO protein abundance、input 与 IP recovery 如何控制？
3. 数据证明的是 recipient presence 还是 source-to-recipient movement；如何排除 tissue mixing、contamination 或另一 source？
4. Source production、source-cell AGO loading、movement、recipient loading、direct target effect 与 phenotype 中哪些是直接支持、哪些缺失？
5. Microtubule/KTN1 或 HASTY 机制是否被限制在测试的 family、root cell types 与 Arabidopsis，而非泛化？
6. D-body 或 nuclear-pore claim 是否有 locus-specific precursor/intermediate/flux evidence，而非可见结构替代速率？

### 预期证据

Fractionation/polysome controls, imaging plus perturbation, AGO1-IP/loading, source-restricted expression, cell-type rescue, grafting/directional movement, recipient target readout, phenotype rescue.

### 依据

- `claim_ids`: `claim-chen-a-er-translation-cleavage-separation`, `claim-chen-b07`, `claim-chen-b08`, `claim-chen-b09`, `claim-chen-c-005`, `claim-chen-c-009`, `claim-chen-c-010`
- `source_ids`: `src-doi-10-1016-j-cell-2013-04-005`, `src-doi-10-1038-s41477-020-0726-z`, `src-doi-10-15252-embj-2018100754`, `src-doi-10-15252-embj-2020107455`, `src-doi-10-1016-j-devcel-2022-03-015`

## Dimension Q4 — Direct target、action mode 与 phenotype

```yaml
dimension_id: CHEN-Q4
name: target_action_and_phenotype_axes
lens_model_ids: [CHEN-M4]
primary_risk: molecular_association_to_full_causality
```

### 先识别

- Evidence 是 prediction、anticorrelation、AGO association、matched cleavage、reporter、endogenous target-site genetics 还是 rescue？
- Target RNA 与 protein 是否都测量，且来自匹配 tissue/stage/genotype？
- Phenotype 是否由 target-site-specific intervention 连接？

### 高价值问题模板

1. Direct target claim 依赖什么位点匹配证据；prediction、PARE/degradome、AGO association 和 reporter 被如何分级？
2. Target-site-disrupted control 是否只改变拟议 miRNA interaction，并保持蛋白功能和其他 regulatory elements？
3. RNA 与 protein readouts 是否同时测量；它们支持 cleavage、RNA decay、translation repression 还是混合模式？
4. PARE/degradome 或 RNA 阴性是否受组织、丰度、时间点与捕获偏差限制？
5. 哪项 endogenous target-site genetics、rescue 或等价干预将分子作用连接到完整 phenotype；若没有，措辞是否降级？
6. 作者是否把 miR172/AP2 或单个 assay 的作用模式无依据推广到其他 target/species？

### 预期证据

Matched cleavage/5′-end evidence, site-mutant reporter, target RNA and protein, endogenous target-site edit, rescue/epistasis, tissue/stage/genotype matching.

### 依据

- `claim_ids`: `claim-chen-a-mir172-ap2-translational-repression`, `claim-chen-a-er-translation-cleavage-separation`, `claim-chen-b03`, `claim-chen-c-002`, `claim-chen-c-007`
- `source_ids`: `src-doi-10-1126-science-1088060`, `src-doi-10-1126-science-1159151`, `src-doi-10-1016-j-molcel-2013-10-033`, `src-doi-10-1016-j-cell-2013-04-005`

## Dimension Q5 — HEN1、端状态与 turnover network

```yaml
dimension_id: CHEN-Q5
name: terminal_chemistry_and_turnover_network
lens_model_ids: [CHEN-M5, CHEN-M2]
primary_risk: end_state_to_unique_enzyme_or_decay_rate
```

### 先识别

- RNA stage 是 pre-miRNA end、duplex、free mature 还是 AGO-bound mature？
- Methylation、tailing、trimming 与 abundance 是 endpoint 还是 rate-resolved measurement？
- Enzyme/genotype、allele、AGO fraction 与 substrate architecture 是否匹配？

### 高价值问题模板

1. HEN1 claim 回答的是 enzyme requirement、terminal chemical position、duplex geometry 还是 in-vivo protection；证据是否被越级复用？
2. 观察到的 U-tail/truncation 如何区分 HESO1、URT1、SDN、redundancy、sequentiality 与 trimming exposure？
3. End profile 来自 total、AGO-bound 还是 free fraction；methylation 和 genotype context 是什么？
4. Steady-state isomiR distribution 是否被误写为 degradation rate；有什么 kinetic/pulse-chase 或等价 flux evidence？
5. In-vitro substrate panel/structure 是否被无依据外推到 in-vivo access、localization 或 substrate prevalence？
6. 若复用 SDN 2008 的 figure 或数值，是否同时检查 `src-doi-10-1126-science-aav2481` 并限定 correction 未闭合的细节？

### 预期证据

Chemical end assay, purified-substrate panel, methylation-sensitive measurement, enzyme-combination genetics, total versus AGO fractions, end profiling, kinetic/pulse-chase design, correction-linked source audit.

### 依据

- `claim_ids`: `claim-chen-a-hen1-terminal-methylation`, `claim-chen-a-hen1-duplex-specificity`, `claim-chen-a-methylation-protects-ends`, `claim-chen-a-sdn-turnover`, `claim-chen-b10`, `claim-chen-c-004`, `claim-chen-c-008`
- `source_ids`: `src-doi-10-1126-science-1107130`, `src-doi-10-1093-nar-gkj474`, `src-doi-10-1016-j-cub-2005-07-029`, `src-doi-10-1126-science-1163728`, `src-doi-10-1126-science-aav2481`, `src-doi-10-1371-journal-pgen-1005091`

## Dimension Q6 — Transfer、correction 与不确定性

```yaml
dimension_id: CHEN-Q6
name: transfer_correction_and_uncertainty
lens_model_ids: [CHEN-M1, CHEN-M2, CHEN-M3, CHEN-M4, CHEN-M5]
primary_risk: arabidopsis_or_version_specific_result_generalized
```

### 先识别

- 结论从 Arabidopsis 迁移到哪个 crop、plant lineage 或 non-plant system？
- Family 名称是否遮蔽 locus、arm、sequence、paralog、AGO family 或 tissue difference？
- 原始来源是否有 correction、retraction、EoC、abstract-only 或 no-transcript 限制？

### 高价值问题模板

1. 哪一层被主张为 conserved：protein family、biochemical activity、MIR locus、mature sequence、action mode 还是 phenotype；证据是否逐层匹配？
2. 在新物种中是否重新核对 paralog、MIR locus/arm/sequence、tissue/stage、AGO family 与 assay，而非只用同名 family？
3. 是否导入动物 Drosha–DGCR8、seed-only 或 Exportin-5 逻辑解释植物；如是，直接的 plant evidence 是什么？
4. 关键来源的 correction/retraction/EoC 是否复核；原论文与 correction 是否被错误计为两项独立支持？
5. 结论来自开放全文、abstract-bounded record、review 还是 lecture page；措辞是否与直接性相匹配？
6. 哪些判断是 team result、public scope、field consensus 或 Agent inference；是否有任何团队结果被写成专家私人意见？

### 预期证据

Species-matched genetics/biochemistry, locus/sequence/assembly audit, paralog and AGO-family checks, independent-lab evidence, source-version/correction record, explicit attribution labels.

### 依据

- `claim_ids`: `claim-chen-a-hen1-duplex-specificity`, `claim-chen-a-sdn-turnover`, `claim-chen-a-where-how-public-framing`, `claim-chen-b11`, `claim-chen-c-009`, `claim-chen-c-011`
- `source_ids`: `src-doi-10-1093-nar-gkj474`, `src-doi-10-1126-science-1163728`, `src-doi-10-1126-science-aav2481`, `src-doi-10-15252-embj-2020107455`

## Question ranking

1. 会改变 lifecycle stage、direct target、action mode 或 phenotype-causality 结论的问题；
2. 能区分两个可行替代解释的问题；
3. 暴露 RNA-entity、species、tissue、stage、genotype 或 compartment mismatch 的问题；
4. 暴露 evidence directness、independence 或 correction 缺口的问题；
5. 指向一个可执行关键实验的问题；
6. 仅改善表述而不改变判断的问题。

## Output schema

```json
{
  "question_id": "CHEN-Q?-NN",
  "question": "",
  "lens_model_ids": [],
  "question_type": "entity|lifecycle|method|directness|action_mode|causality|spatial|turnover|transfer|correction|next_experiment",
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

- 不把文章未提供的信息写成问题前提；缺失即 `missing_context`。
- 不询问专家私人意见，不写“Chen 会怎么说”，也不从讲座页面构建个人语气。
- 不把通用“有没有对照/重复”当高价值问题；必须指出具体 RNA entity、lifecycle step、compartment、alternative 或升级门槛。
- 不构造 Chen 特有的 de novo miRNA annotation model；身份 claim 转交 Auditor/注释专门 Lens。
- 当前 corpus 不能支持的事实前提写 `current corpus insufficient`。
- SDN 2008 的定量/figure-level 复用必须携带 2018 erratum；AAR2 correction 必须携带原文传播，并按已核验的 Fig. 1/Fig. S3 legends 与 Figs. 6/S2/S6 范围限制图件复用。
