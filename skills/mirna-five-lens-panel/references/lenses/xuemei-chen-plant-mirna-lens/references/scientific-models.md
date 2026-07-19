# Scientific Reasoning Models — Xuemei Chen Lens

```yaml
expert_id: xuemei-chen
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
phase: N2
model_count: 5
```

本文件把 Xuemei Chen 公开研究中反复出现的实验判断程序转成可执行 Lens。它不是 Xuemei Chen 本人，不代表其当前个人意见；共同作者论文只作为团队结果使用。`expert_position`、`field_consensus`、`team_result` 和 `agent_inference` 必须分开。项目 I0–I3 与 F0–F4 是内部操作量表，不是来源论文的原始术语。

## Model M1

```yaml
model_id: CHEN-M1
name: 生命周期阶段定位与 RNA 实体分层
definition: >
  先固定所测 RNA 实体，再把变化定位到 MIR transcription、pri/pre-miRNA
  processing 或 stability、duplex methylation、AGO loading、target action 与 turnover；
  相邻阶段的证据不能互相代替。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    Chen 参与或领导的 AAR2、RBV、HEN1、TREX-2/NPC 与 movement 研究在不同问题中
    反复用阶段匹配的中间体和 readout 排除相邻解释；作者综述和公开报告又明确提供
    stage-and-spatial framing。完整检查表是 Agent 综合，不是专家原话。
trigger_conditions:
  - 论文以成熟 miRNA 总量或发育表型给出单一“biogenesis defect”
  - pri-miRNA、pre-miRNA、duplex、mature arm/isomiR 或 AGO-loaded product 被混称
  - 同一因子被声称同时影响 processing、loading、action 或 turnover
step_by_step_application:
  - 固定 species、tissue、stage、genotype、treatment，并解析 family、MIR locus、precursor、mature 5p/3p、isomiR、sequence 和 assembly
  - 对每个 assay 标记其直接测到的实体：promoter/pri、pre/end、duplex、total mature、AGO-loaded mature 或 target output
  - 将观察值放入 lifecycle 节点，并至少列出两个相邻节点的替代解释
  - 为相邻解释选择判别 readout，例如 promoter 对 pri-miRNA decay、total 对 AGO1-IP、end chemistry 对 abundance
  - 只在实体、组织、时间点和动态范围匹配时连接节点
  - 分节点报告 supported、partially_supported、unsupported 或 conflicting；缺节点不得由下游表型补齐
stop_or_downgrade_conditions:
  - 缺少具体 RNA 实体或 species/tissue/genotype 时停止机制定位并写入 missing_context
  - 只有总 small-RNA abundance、单一 endpoint 或 pleiotropic phenotype 时降级为阶段未决
  - 一个中间体未变但 assay sensitivity 或时间点不匹配时，不得据此排除全部上游效应
scientific_status:
  framework_status: mixed_team_results_and_agent_inference
  framework_relation: strongly_consistent_across_public_program
  directness: direct_component_results_plus_contextual_reviews
  independent_support: component_steps_supported_but_integrated_checklist_not_independently_tested_as_one_model
species_and_system_boundary:
  - 主要证据来自 Arabidopsis thaliana；作物迁移必须重新核对 MIR locus、paralog、AGO family、tissue/stage 与 assay
  - 该模型不能替代新植物 miRNA 的 I0-I3 身份注释；身份问题应调用 Evidence Auditor 或注释专门 Lens
  - 不得把动物 Drosha-DGCR8 或 seed-only 规则默认迁移到植物
source_ids:
  - src-doi-10-1073-pnas-2208415119
  - src-doi-10-1038-s41467-022-28872-x
  - src-doi-10-1038-s41477-019-0562-1
  - src-doi-10-1093-nar-gkj474
  - src-doi-10-1105-tpc-113-113159
claim_ids:
  - claim-chen-a-stage-separated-diagnosis
  - claim-chen-b01
  - claim-chen-b02
  - claim-chen-b07
  - claim-chen-b11
  - claim-chen-b12
```

## Model M2

```yaml
model_id: CHEN-M2
name: 遗传—机制—RNA 三角与替代解释排除
definition: >
  用遗传扰动、rescue、suppressor 或 epistasis 定位必要性和顺序，用生化、interaction
  或定位 assay 约束直接机制，再用 RNA-species-resolved readout 确认受影响阶段；
  phenotype 只作下游一致性，不能单独完成机制证明。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: medium_high
  rationale: >
    HEN1、HESO1、hen1-2 substrate competition、TREX-2/NPC 与 RBV 研究在不同问题中
    重复组合 genetics、biochemistry/localization 与 RNA readout。三角协议为 Agent 综合，
    具体团队结果具有直接证据，但严谨三角验证并非该实验室独有。
trigger_conditions:
  - pleiotropic small-RNA mutant 被直接赋予单一步骤机制
  - suppressor 或 epistasis 被写成 direct interaction
  - biochemical activity、colocalization 或 rescue 中任一单项被用来完成整条因果链
step_by_step_application:
  - 写出至少两个可竞争的机制解释及各自可证伪 prediction
  - 判断遗传证据回答的是 requirement、order、dosage、bypass 还是 suppression
  - 选择与候选步骤匹配的 biochemical、interaction 或 localization assay
  - 同步测量该步骤直接涉及的 RNA entity，而不是只测 mature total
  - 检查 rescue/epistasis 是否来自匹配 allele、tissue、stage 与 dosage
  - 仅在不同证据轴会合时给强机制结论；缺一轴时明确降级，不机械要求每篇论文凑齐三类 assay
stop_or_downgrade_conditions:
  - suppressor 可能是 bypass 或剂量补偿且无 stage-matched readout 时，停止 direct-mechanism 结论
  - partial allele 的结果不得外推 null、所有组织或 enzyme-saturating 情境
  - 只有 phenotype rescue 或 physical interaction 时，机制最多为 partially_supported
scientific_status:
  framework_status: agent_inference_from_recurrent_team_results
  framework_relation: strongly_consistent
  directness: mixed_direct_genetics_biochemistry_and_rna_measurements
  independent_support: rigorous_design_logic_is_broadly_shared_but_specific_chains_are_context_bounded
species_and_system_boundary:
  - 主要适用于 Arabidopsis pathway genetics；其他植物需验证 ortholog/paralog、allele 与 tissue equivalence
  - HEN1 substrate-pool competition 只在 limiting-capacity/allele-matched 情境触发，不是所有 abundance 变化的默认解释
source_ids:
  - src-doi-10-1126-science-1107130
  - src-doi-10-1093-nar-gkj474
  - src-doi-10-1016-j-cub-2012-02-052
  - src-doi-10-1093-nar-gkq348
  - src-doi-10-1038-s41477-020-0726-z
  - src-doi-10-1038-s41467-022-28872-x
claim_ids:
  - claim-chen-a-hen1-terminal-methylation
  - claim-chen-a-hen1-duplex-specificity
  - claim-chen-a-heso1-unmethylated-substrates
  - claim-chen-a-substrate-pool-competition
  - claim-chen-b04
  - claim-chen-b05
  - claim-chen-b06
  - claim-chen-b08
  - claim-chen-b12
```

## Model M3

```yaml
model_id: CHEN-M3
name: Step × Compartment 空间证据矩阵
definition: >
  对每个 lifecycle step 同时追问“发生了什么”和“在哪里发生”；定位、共现或 bulk abundance
  只产生空间假设，必须由 compartment-specific perturbation 与 stage-matched readout 连接到
  processing、loading、action、movement 或 export。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    ER-associated translational repression、TREX-2/NPC、RBV、single-cell loading、HASTY 与
    microtubule-limited AGO1 loading 在不同体系中反复把 pathway step 与 compartment/cell type 配对；
    官方报告只支持 where/how 的公开范围，机制仍来自论文。
trigger_conditions:
  - 结论涉及 D-body、nuclear pore、ER、polysome、AGO compartment、source/recipient cell 或 movement
  - 文章用 colocalization、body abundance、bulk RNA 或 recipient reads 声称空间机制
  - total abundance 与 AGO loading、cell autonomy 或 mobility 被混为同一变量
step_by_step_application:
  - 定义 compartment、source cell、recipient cell 与所测 RNA/protein entity
  - 区分 presence、enrichment、interaction、flux、loading、movement、target engagement 和 phenotype
  - 为声称的 step 配对空间扰动与 readout，例如 fractionation/polysome、AGO1-IP、cell-type rescue、grafting 或 movement reporter
  - 对 loading/movement 依次检查 source production、source-cell loading、movement、recipient loading、target effect 与 phenotype
  - 审查标签过表达、fraction purity、input/protein/recovery 与组织混合控制
  - 逐格报告证据；任何空格保持 missing，不由相邻格自动补足
stop_or_downgrade_conditions:
  - 只有 colocalization、visible body 或 compartment enrichment 时，停止 catalytic/flux 结论
  - 只有 recipient reads 时，停止 movement、recipient loading 与功能结论
  - AGO association 没有 input、AGO protein 与 recovery controls 时，loading 结论降级
scientific_status:
  framework_status: mixed_expert_position_field_support_and_agent_operationalization
  framework_relation: explicit_public_scope_plus_strongly_consistent_team_results
  directness: direct_spatial_genetic_and_biochemical_results
  independent_support: independent_spatial_loading_and_hasty_work_supports_gates_but_not_every_specific_mechanism
species_and_system_boundary:
  - ER、TREX-2/NPC、RBV 与 microtubule mechanisms 不得跨 tissue 或 species 自动互换
  - microtubule-limited cytoplasmic AGO1 loading 仅限测试的 Arabidopsis miR165/166/root context
  - HASTY 不能写成动物 Exportin-5 机制在植物中的简单复制
source_ids:
  - src-doi-10-1016-j-cell-2013-04-005
  - src-doi-10-1038-s41477-020-0726-z
  - src-doi-10-1038-s41467-022-28872-x
  - src-doi-10-15252-embj-2018100754
  - src-doi-10-15252-embj-2020107455
  - src-doi-10-1016-j-devcel-2022-03-015
  - src-url-hkust-ias-lecture-2017
claim_ids:
  - claim-chen-a-er-translation-cleavage-separation
  - claim-chen-a-where-how-public-framing
  - claim-chen-a-rbv-coupled-checkpoints
  - claim-chen-a-mobility-loading-context
  - claim-chen-b07
  - claim-chen-b08
  - claim-chen-b09
  - claim-chen-c-009
  - claim-chen-c-010
```

## Model M4

```yaml
model_id: CHEN-M4
name: Direct Target → Action Mode → Phenotype Causality 分轴
definition: >
  把靶位点直接性、cleavage/mRNA decay/translation repression 的作用模式和完整表型因果
  分别评级；任何一个轴通过都不能自动升级另外两个轴。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    sole-author miR172/AP2 研究以 target-site、RNA/protein 与 floral phenotype 分层；
    ER action 与 movement 研究在其他情境继续分开 cleavage、translation、loading、target response
    和 phenotype，且有独立遗传与生化工作支持翻译抑制这一作用模式。
trigger_conditions:
  - 论文从 prediction、complementarity、PARE/degradome、AGO association 或表达反相关推出功能
  - “miRNA regulates target” 未说明 cleavage、RNA decay、translation 或其组合
  - 分子效应被直接写成 organismal phenotype mechanism
step_by_step_application:
  - 明确特定 miRNA entity、target site、tissue、stage、genotype 与 treatment
  - 独立评级 direct target evidence：prediction、association、matched cleavage、site-dependent reporter 或 endogenous target-site genetics
  - 配对测量 target RNA 与 protein，并记录 cleavage、RNA decay 和 translation readouts
  - 检查 target-site-disrupted control 是否只改变拟议 interaction，且 assay context 是否原生匹配
  - 将 phenotype causality 单列；只有 target-site genetics、rescue 或等价因果干预才可升至 F4
  - 输出各轴结论、冲突和能区分作用模式的下一项实验
stop_or_downgrade_conditions:
  - RNA-only assay 不足以排除 translation effect；protein-only effect 也可能间接
  - PARE/degradome、AGO association 或 reporter 各自不能单独证明完整表型因果
  - miR172/AP2 不得作为所有植物 miRNA 以 translational repression 为主的依据
scientific_status:
  framework_status: expert_position_with_independent_field_support
  framework_relation: explicit_anchor_plus_strongly_consistent_program
  directness: direct_genetic_rna_protein_and_biochemical_results
  independent_support: independent_genetic_and_reconstituted_translation_systems_support_dual_modes
species_and_system_boundary:
  - 证据主要为 Arabidopsis target/tissue-specific systems；作用模式比例不可跨 target、tissue 或 species 数值外推
  - 不把植物近完全互补或 cleavage 逻辑机械迁移动物，也不把 animal seed-only 规则迁移植物
source_ids:
  - src-doi-10-1126-science-1088060
  - src-doi-10-1126-science-1159151
  - src-doi-10-1016-j-molcel-2013-10-033
  - src-doi-10-1016-j-cell-2013-04-005
  - src-doi-10-1016-j-devcel-2022-03-015
claim_ids:
  - claim-chen-a-mir172-ap2-translational-repression
  - claim-chen-a-er-translation-cleavage-separation
  - claim-chen-b03
  - claim-chen-c-002
  - claim-chen-c-007
  - claim-chen-b09
```

## Model M5

```yaml
model_id: CHEN-M5
name: 终端保护置于 Branched Tailing/Trimming Network
definition: >
  先分开 HEN1 enzyme requirement、terminal chemistry、duplex substrate architecture 与 protective
  consequence，再按 methylation、AGO association、substrate stage、genotype、HESO1/URT1 与 trimming
  解释端状态；tail/isomiR snapshot 不是 degradation rate。
expert_characteristic_evidence:
  recurrence: strong
  generative_power: strong
  distinctiveness: high
  rationale: >
    Chen 团队的 HEN1 chemical/biochemical chain、HESO1 suppressor、AGO-context end profiling 与
    SDN work 跨多个情境复现，后续 HESO1/URT1 genetics 和独立 URT1/HEN1 studies 将早期线性保护
    图景扩展成分支网络。
trigger_conditions:
  - 论文以 tail、truncation、isomiR 或 abundance 推断单一 turnover enzyme
  - hen1、HESO1、URT1、SDN 或 AGO-associated end metabolism 被讨论
  - HEN1 机制混合 enzyme requirement、chemical position、substrate geometry 和 in-vivo protection
step_by_step_application:
  - 固定 RNA stage：pre-miRNA end、duplex、free mature 或 AGO-bound mature product
  - 记录 species、genotype、allele、methylation state、AGO fraction 与具体 3′ end species
  - 将 HEN1 催化、duplex architecture 与 loss-of-methylation phenotype 分开评级
  - 对 HESO1、URT1、SDN 与 trimming 列出 redundancy、sequentiality、competition 或未决分支
  - 把 steady-state tail/truncation profile 与 decay flux 分开；定速率需 kinetic、pulse-chase 或等价设计
  - 仅在 enzyme perturbation、substrate context 与 stage-matched end/flux readout 会合时指派机制
stop_or_downgrade_conditions:
  - 只有端点测序 snapshot 时，停止 degradation-rate 或唯一 enzyme 结论
  - in-vitro HEN1/URT1 substrate behavior 不得直接当作 in-vivo access、localization 或 flux
  - SDN 2008 的定量或 figure-level 复用必须同时检查 2018 formal erratum；缺 correction 内容时停止细节复用
scientific_status:
  framework_status: expert_position_refined_by_field_evidence
  framework_relation: explicit_team_program_plus_agent_network_synthesis
  directness: direct_genetic_chemical_biochemical_and_end_profile_results
  independent_support: independent_hen1_kinetics_and_urt1_structure_support_components_not_full_flux_network
species_and_system_boundary:
  - 主要为 Arabidopsis；Arabidopsis/rice pattern 只支持情境依赖，不证明同名 family 正交或相同 modification frequency
  - plant HEN1 substrate architecture 不自动迁移动物 HEN homologs
  - partial hen1 substrate competition 只在 allele/capacity 匹配时调用
source_ids:
  - src-doi-10-1126-science-1107130
  - src-doi-10-1093-nar-gkj474
  - src-doi-10-1016-j-cub-2005-07-029
  - src-doi-10-1126-science-1163728
  - src-doi-10-1126-science-aav2481
  - src-doi-10-1016-j-cub-2012-02-052
  - src-doi-10-1105-tpc-113-114603
  - src-doi-10-1073-pnas-1405083111
  - src-doi-10-1371-journal-pgen-1005091
  - src-doi-10-1016-j-bbrc-2020-01-124
claim_ids:
  - claim-chen-a-hen1-terminal-methylation
  - claim-chen-a-hen1-duplex-specificity
  - claim-chen-a-methylation-protects-ends
  - claim-chen-a-sdn-turnover
  - claim-chen-a-heso1-unmethylated-substrates
  - claim-chen-b04
  - claim-chen-b05
  - claim-chen-b10
  - claim-chen-c-003
  - claim-chen-c-004
  - claim-chen-c-008
```

## Cross-model usage rule

- 成熟 miRNA 或表型改变：先用 `CHEN-M1` 定位实体和阶段，再用 `CHEN-M2` 检查替代解释与证据会合。
- 涉及定位、D-body、核孔、ER、AGO loading 或 movement：强制加入 `CHEN-M3`；bulk abundance 不回答空间 claim。
- 涉及 target 或 phenotype：使用 `CHEN-M4`，分开 direct target、action mode 与 phenotype causality。
- 涉及 HEN1、tailing、trimming、SDN、HESO1/URT1 或 isomiR ends：使用 `CHEN-M5` 并执行 correction gate。
- 新 miRNA 身份注释不构造 Chen 特有模型；调用项目 Evidence Auditor 或植物注释专门 Lens，并保持 family/locus/precursor/arm/sequence/assembly 分层。
- 所有新问题输出均属模型化推断；专家名望、共同作者网络、数据库收录或多个 Agent 一致都不能升级科学事实。
