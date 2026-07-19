# Scientific Reasoning Models — Michael J. Axtell Lens

```yaml
expert_id: michael-j-axtell
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
phase: N2
model_count: 5
```

本文件提炼的是公开研究中可复现的判断程序，不是 Michael J. Axtell 本人的代理，也不代表其当前个人意见。多作者论文只作为团队结果或共同标准使用；在新问题上的应用一律属于基于模型的推断。项目 I0–I3 与 F0–F4 是项目级操作量表，不是来源论文术语。

## Model M1

```yaml
model_id: AXT-M1
name: 生物发生优先的三层证据闸门
definition: >
  先以位点和前体的加工证据判定植物 MIRNA 身份，再独立评估靶标直接性，
  最后评估表型因果；后层证据不得反向补足前层，前层通过也不得自动升级后层。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    2008/2018 注释标准明确把精确 miRNA/miRNA* 加工置于身份核心；
    Axtell 团队的 degradome、定量 reporter 和 RDR 注释清理又把身份、直接靶向与功能层分开操作。
trigger_conditions:
  - 新植物 miRNA、同源 miRNA 或数据库条目的身份主张
  - 论文从靶标预测、PARE/degradome、reporter 或表达反相关推导功能
  - 同一论证同时混用 MIRNA 身份、靶标和表型证据
step_by_step_application:
  - 解析 family、MIR locus、precursor、mature 5p/3p、具体序列和 assembly
  - 仅用结构、精确加工、miRNA/miRNA*、重复与位点模式评定身份 I0-I3
  - 身份不足时停止使用“已确认 miRNA”，且不允许用预测靶标反向证明身份
  - 另以 prediction、PARE/degradome、reporter、AGO/生化证据评定靶标直接性 F0-F3
  - 只有靶位点遗传学、rescue 或等价干预才可把完整表型因果提升到 F4
  - 分栏报告三层结论、缺口和每层可推翻当前判断的证据
scientific_status:
  framework_status: expert_position
  framework_relation: explicit_and_strongly_consistent
  claim_directness: direct_framework_plus_direct_method_results
  independent_support: plant_database_reannotation_supports_identity_gate_but_target_and_phenotype_steps_are_not_independently_replicated_as_one_model
  scope_match: plant_miRNA_annotation_and_targeting
known_examples:
  - context: 2008/2018 植物 miRNA 注释标准
    application: 精确 duplex 加工与生物学重复先于靶标或保守性论据
  - context: Arabidopsis degradome 与 Nicotiana benthamiana 定量 reporter
    application: 切割和位点依赖抑制强于预测，但不等于完整表型因果
  - context: Arabidopsis rdr1/rdr2/rdr6 注释清理
    application: 遗传依赖用于质疑身份，低信息位点仍保留为 ambiguous
failure_conditions:
  - 缺少正确 assembly、前体序列或足够的独立 sRNA-seq libraries 时，身份只能为未决
  - 异源瞬时 reporter 不能替代原生组织和长期遗传因果
  - degradome 阴性受组织、丰度与捕获偏差限制，不能单独排除靶向
transfer_limits:
  - 不把植物近完全互补/切割逻辑机械迁移到动物
  - 不把动物 seed 或 Drosha-DGCR8 规则迁移为植物身份标准
  - 数据库收录、family 名称或相同成熟序列不跨物种自动建立 locus 身份
source_ids:
  - src-doi-10-1105-tpc-108-064311
  - src-doi-10-1105-tpc-17-00851
  - src-doi-10-1111-tpj-13919
  - src-doi-10-1016-j-cub-2008-04-042
  - src-doi-10-1105-tpc-113-120972
claim_ids:
  - claim-axtell-a-identity-before-function
  - claim-axtell-b01
  - claim-axtell-b04
  - claim-axtell-b05
  - claim-axtell-a-target-evidence-ladder
  - claim-axtell-talk-discovery-classification-function
```

## Model M2

```yaml
model_id: AXT-M2
name: 多参数位点画像与正交三角验证
definition: >
  把产生小 RNA 的 locus 作为判断单元，同时审查大小分布、链偏向、重复性、
  发卡与 duplex 几何、加工精度、相位、遗传依赖和 mapping 不确定性；
  单一漂亮特征或软件标签不能裁决类别。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    该组合由 Axtell 的 ShortStack 独著方法具体化，并在苔藓全基因组注释、
    Arabidopsis RDR 遗传学、多重比对方法和 47 植物统一资源中反复出现。
trigger_conditions:
  - 候选 small-RNA locus 需要在 MIRNA、siRNA、PHAS、其他 hairpin 或 unclassified 间分类
  - 结论依赖单一 hairpin、单一 dominant read、单个 software score 或单次建库
  - 重复区域、旁系同源位点或 multi-mapping reads 影响成熟序列和位点丰度
step_by_step_application:
  - 固定 species、assembly、library、alignment 和软件版本
  - 生成 locus evidence vector：size、strand、repeat、hairpin、duplex、precision、phasing、abundance
  - 逐项标记直接观测、计算推断、缺失和冲突，不先压缩为一个总分
  - 用类定义相关的正交证据交叉：生物学重复、RDR/DCL/AGO 依赖、trigger 或阳性对照
  - 对 multi-mappers 报告放置策略、高 multiplicity cutoff 与 assembly collapse 风险
  - 只在向量整体与预期生物发生一致时赋予类别；否则转入 provisional/unclassified
scientific_status:
  framework_status: expert_position
  framework_relation: explicit_method_plus_recurrent_team_application
  claim_directness: direct_computational_and_genetic_results
  independent_support: partial_external_support_with_tool_specific_critique
  scope_match: reference_genome_based_small_rna_locus_annotation
known_examples:
  - context: ShortStack 在植物和动物参考基因组数据中的位点级注释
    application: 同时暴露大小、链、重复、发卡、MIRNA 与 phasing 特征
  - context: Physcomitrium patens 与 Arabidopsis rdr1/rdr2/rdr6 分析
    application: 以遗传背景和全位点读段模式区分 MIRNA 与 siRNA/未分类位点
  - context: Arabidopsis、水稻和玉米 multi-mapper 研究
    application: 用模拟与生物 truth sets 比较局部加权、随机放置和丢弃策略
failure_conditions:
  - assembly 错误、重复坍缩或缺少邻近 unique reads 时，位点归属可能无法解决
  - tissue/stage/library 覆盖不足时，miRNA* 或特定类别特征可能不可见
  - 多参数并非多数投票；若关键身份特征缺失，其他弱特征不能数量补偿
transfer_limits:
  - 具体参数和阈值必须按谱系、建库和软件版本验证
  - ShortStack 或任一替代工具的标签都不是实验验证
  - 跨物种比较必须分别绑定 assembly 和 locus，不能只对齐 family 名称
source_ids:
  - src-doi-10-1261-rna-035279-112
  - src-doi-10-1105-tpc-15-00228
  - src-doi-10-1111-tpj-13919
  - src-axtell-27175019
  - src-axtell-32179590
  - src-pmid-31253093
claim_ids:
  - claim-axtell-a-multiparameter-locus-profile
  - claim-axtell-b08
  - claim-axtell-b09
  - claim-axtell-b13
  - claim-axtell-c-003
  - claim-axtell-c-004
```

## Model M3

```yaml
model_id: AXT-M3
name: 背景类驱动的假阳性预算
definition: >
  在候选类别稀少而混淆背景极大时，先估计背景位点按机会通过算法或局部规则的可能性，
  再用可重复的类定义模式、遗传依赖、trigger 与阳性对照设置升级闸门。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    2018 miRNA 标准明确以大量内源 siRNA 的 base rate 解释严格门槛；
    24-nt PHAS 审计则将同一逻辑应用于多个算法、Arabidopsis 和四个额外真双子叶物种。
trigger_conditions:
  - 新颖、低丰度、23-24 nt 植物 miRNA 主张
  - 24-nt-dominated PHAS locus 或任何来自超大背景类别的稀有正类
  - 多个算法同时通过但缺乏稳定生物学模式
step_by_step_application:
  - 明确正类定义和主要背景类，例如 MIRNA 对 hc-siRNA 或 PHAS 对偶然 in-register 24-nt loci
  - 估计候选搜索空间、背景丰度和多重检验/多算法造成的机会命中
  - 冻结算法版本、阈值、assembly 和 biological replicate 单位
  - 检查定义性模式是否在相同 register/duplex geometry 上跨生物学重复复现
  - 检查 class-compatible trigger、RDR/DCL 依赖、genomic context 和阳性/硬阴性对照
  - 只有正交证据共同通过才升级；算法输出本身只标 hypothesis
scientific_status:
  framework_status: expert_position
  framework_relation: explicit_criteria_plus_strongly_consistent_critique
  claim_directness: direct_framework_and_direct_multispecies_computational_genetic_audit
  independent_support: independent_reannotation_supports_false_positive_concern_but_exact_thresholds_remain_method_dependent
  scope_match: plant_miRNA_and_phasiRNA_annotation_under_large_backgrounds
known_examples:
  - context: 大数据时代的植物 miRNA 注释修订
    application: 要求独立生物学 libraries，并对 23-24 nt 候选施加极强证据门槛
  - context: Arabidopsis 24-nt PHAS 候选与四个额外真双子叶物种
    application: 算法通过但 dominant register、trigger 和 pathway genetics 不一致；TAS2 作阳性对照
  - context: PmiREN 对 88 种植物的统一重注释
    application: 独立数据库工作显示大量历史条目需要纠正或移除，但数据库结果仍需 locus review
failure_conditions:
  - 不能因高假阳性风险把所有年轻或非经典候选先验拒绝
  - 新机制若不符合已知依赖，必须给出预声明的替代生物发生模型与能反驳它的实验
  - 不同工具共享作者、规则或代码谱系时，其一致性不是独立验证
transfer_limits:
  - 24-nt Arabidopsis 结论不否定其他类群中已知的 24-nt reproductive phasiRNA systems
  - PmiREN 或动物 miRBase 重注释的百分比不得外推到未分析物种
  - base-rate 逻辑可迁移，具体数值阈值不可无验证迁移
source_ids:
  - src-doi-10-1105-tpc-17-00851
  - src-axtell-31245701
  - src-doi-10-1111-tpj-13919
  - src-doi-10.1093-nar-gkz894
  - src-pmid-41183249
claim_ids:
  - claim-axtell-b02
  - claim-axtell-b03
  - claim-axtell-b06
  - claim-axtell-b07
  - claim-axtell-c-006
  - claim-axtell-c-012
```

## Model M4

```yaml
model_id: AXT-M4
name: 证据缺口类别与实体分辨的演化审计
definition: >
  在证据不完整或跨物种比较时，不把不确定性压成二元结论；
  分开 family、MIR gene family、locus、precursor、mature arm、sequence 和 assembly，
  并用 provisional、nearMIRNA、ambiguous 或 unclassified 保存缺口。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: medium_high
  rationale: >
    Axtell 研究同时展示深保守 family/target 与 Arabidopsis 属内快速 locus turnover；
    2018 标准、RDR 清理和 47 植物资源都拒绝用同名、同源或低信息强行命名。
trigger_conditions:
  - 仅以 family 名称、成熟序列相似或数据库同名声称跨物种正交
  - 缺少 miRNA*、低 read counts、replicate variance 或未覆盖关键 tissue/stage
  - 比较研究把“未检出”写成位点不存在或功能丢失
step_by_step_application:
  - 为每个主张声明实体层级与 assembly：family、locus、precursor、arm、sequence、coordinate
  - 将 sequence similarity、synteny/locus homology、species-specific processing、target conservation 和 function 分开评级
  - 用保守性校准古老关系的先验，但不把保守性当身份的必要或充分条件
  - 对 homology-only、缺 star、低信息或类别不合的条目赋予明确 provisional 状态
  - 列出缺口来自生物学缺失还是采样、assembly、mapping 或数据库版本限制
  - 指定能够升级或否决类别的下一项数据，不把 provisional 当固定生物类别
scientific_status:
  framework_status: mixed_expert_position_and_agent_inference
  framework_relation: explicit_categories_plus_strongly_consistent_entity_hygiene
  claim_directness: direct_comparative_and_resource_results
  independent_support: independent_plant_and_database_reannotation_supports_version_and_identity_caution
  scope_match: plant_miRNA_evolution_cross_species_annotation_and_low_information_loci
known_examples:
  - context: 2005 陆生植物深保守关系与 2010 Arabidopsis 属内位点出生消亡
    application: family 历史、locus 同源和候选身份被分开
  - context: Arabidopsis RDR 分析
    application: 118 个低信息条目保留 ambiguous，38 个非发卡 RDR-independent loci 保留 unclassified
  - context: 47 植物统一资源
    application: 缺少精确 miRNA* 的候选保留 nearMIRNA，而不静默升级
failure_conditions:
  - provisional 标签不能成为无限期规避验证的终点
  - family-level 保守不能支持特定位点、臂、序列或表型主张
  - 未检出只能约束已采样 tissue/stage/genotype/library 和当前 assembly
transfer_limits:
  - 动物数据库端点/arm 审计支持“需复核”的逻辑，但其误注释比例不可迁移到植物
  - 绿藻 precursor 异质性只提示需要 lineage-matched validation，不能事后豁免所有陆生植物标准
  - 同一 miRNA 名称不自动等于跨物种 orthology
source_ids:
  - src-doi-10-1105-tpc-105-032185
  - src-doi-10-1105-tpc-110-073882
  - src-doi-10-1105-tpc-17-00851
  - src-doi-10-1111-tpj-13919
  - src-axtell-32179590
  - src-pmid-30423142
  - src-doi-10.1093-nar-gkz894
claim_ids:
  - claim-axtell-a-conservation-calibrates-prior
  - claim-axtell-c-001
  - claim-axtell-c-008
  - claim-axtell-b05
  - claim-axtell-b13
  - claim-axtell-c-005
  - claim-axtell-a-entity-resolution
  - claim-axtell-talk-evolution-separates-homology-levels
```

## Model M5

```yaml
model_id: AXT-M5
name: 分阶段的 trans-species miRNA 证据链
definition: >
  跨物种小 RNA 主张必须逐段建立 donor identity、source/interface assignment、movement、
  recipient effector loading、direct target effect 和 phenotype causality；任何上游检测都不能自动推出下游步骤。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high_within_cuscuta_program
  rationale: >
    Axtell 团队的 Cuscuta 研究从界面表达与宿主靶向，扩展到靶位点补偿变化、
    U6-like promoter 和选择性 AGO loading；各论文分别回答链条中的不同问题。
trigger_conditions:
  - 跨物种、跨界或寄生植物来源小 RNA 的移动与功能主张
  - 在受体样本中检测到 donor-like reads 并据此声称调控或表型
  - 将 promoter、进化相容、AGO loading、切割和表型压成单一机制结论
step_by_step_application:
  - 先以 donor locus、precursor、mature sequence 和加工证据确认 RNA 身份
  - 证明 source assignment 与 interface enrichment，并排查组织混合、污染和 mapping 歧义
  - 将 movement 与“受体样本中存在”分开，要求方向性或空间/遗传证据
  - 检查 recipient AGO/effector loading；donor 自身 AGO 回避与 recipient loading 分开陈述
  - 以 matched PARE/5-prime end、reporter 或等价方法验证受体直接靶标
  - 只有遗传/rescue 或等价干预才连接到 phenotype causality
  - 对每一段报告 supported、missing 或 conflicting，不允许整链一票通过
scientific_status:
  framework_status: expert_position_with_agent_operationalization
  framework_relation: strongly_consistent_across_team_program
  claim_directness: mixed_direct_small_rna_target_promoter_and_loading_results_plus_contextual_evolution
  independent_support: limited_for_the_integrated_chain_and_recent_2026_result
  scope_match: cuscuta_host_plant_interfaces
known_examples:
  - context: 2018 Cuscuta campestris-host interface study
    application: parasite miRNA 表达、宿主转录本切割和宿主 assays 支持链条部分环节
  - context: 2019 补偿性靶位点序列变化与 2023 U6-like promoter
    application: 分别支持演化相容与 donor locus transcription，不替代 movement/phenotype 证据
  - context: 2026 Cuscuta AGO loading study
    application: 选择性避免 self AGO loading 是独立步骤，不能自动升级为所有受体中的功能结论
failure_conditions:
  - 界面组织混合、污染或相同序列多来源未排除时，source 和 movement 均未建立
  - comparative co-variation 不能替代直接移动或表型实验
  - 当前整合模型主要来自一个寄生植物研究程序，近期环节缺乏独立实验室复制
transfer_limits:
  - 不推广到膳食 RNA、所有 plant-plant 或一般 cross-kingdom RNA
  - Cuscuta 特有 promoter 与 self-AGO avoidance 不得假定为其他谱系通则
  - 检测、移动、loading、targeting 和 phenotype 的证据门槛必须在新体系逐段重建
source_ids:
  - src-doi-10-1038-nature25027
  - src-doi-10-7554-elife-49750
  - src-doi-10-1093-plcell-koad076
  - src-doi-10.1093-plcell-koad305
  - src-doi-10-1016-j-pbi-2019-03-014
  - src-pmid-42417192
claim_ids:
  - claim-axtell-a-transspecies-chain
  - claim-axtell-talk-transspecies-uncertainty-ladder
  - claim-axtell-c-009
  - claim-axtell-c-011
```

## Cross-model usage rule

- 新候选植物 miRNA：先用 `AXT-M1`，再用 `AXT-M2`；若来自大规模算法筛选或 23–24 nt 背景，再加 `AXT-M3`。
- 跨物种同名、保守性或未检出：使用 `AXT-M4`，不得用 family 证据替代 locus 证据。
- trans-species RNA：强制使用 `AXT-M5`，同时回到 `AXT-M1` 分开身份、靶标与表型。
- 任何模型都不允许因专家知名度、合作网络内工具一致或数据库收录而升级科学事实。
