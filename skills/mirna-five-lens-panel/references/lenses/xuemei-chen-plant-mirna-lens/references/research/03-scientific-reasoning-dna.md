# Xuemei Chen — Scientific Reasoning DNA（N1 Agent B）

## Scope and attribution

本底稿只提炼公开论文中可复现的研究程序，不把共同作者论文的全部表述归为 Xuemei Chen 的个人意见。`explicit` 表示来源直接陈述或实施该判断，`strongly_consistent` 表示至少两个不同研究情境重复出现，`agent_inference` 表示本 Agent 的跨论文归纳。来源均以完整姓名并结合植物 RNA 主题、机构/共同作者或通讯作者信息核验；未使用 `Chen X` 单独检索结果。

## RDNA-1：按 miRNA 生命周期逐步定位缺陷

- **候选程序**：先区分 MIR transcription、pri-miRNA stability/processing、pre-miRNA end formation、duplex methylation、AGO loading、subcellular localization/movement、target action 与 turnover，再解释总 miRNA 或表型变化。
- **关系标签**：`strongly_consistent`；作者综述对 transcription/loading/3' modification 的分层为 `explicit` [src-doi-10-4161-rna-36243]。
- **复现情境 1**：AAR2 研究用正常 MIR promoter activity 与加速的 pri-miRNA decay，把缺陷定位到转录后、成熟 miRNA 积累前 [src-doi-10-1073-pnas-2208415119; claim-chen-b11]。
- **复现情境 2**：RBV 研究同时测总 miRNA 和 AGO1-associated miRNA，分离生物发生与装载 [src-doi-10-1038-s41467-022-28872-x; claim-chen-b07]。
- **复现情境 3**：miR165/166 研究将 source-cell loading、movement、recipient action 分开测量 [src-doi-10-1016-j-devcel-2022-03-015; claim-chen-b09]。
- **迁移价值**：面对“miRNA 降低”时，生成阶段特异的替代解释和最小判别实验。
- **failure/transfer limits**：不能因某一中间体未变就排除所有上游效应；不同 assay 的组织、时间点与动态范围必须匹配。该程序可迁移到其他植物，但具体因子和阶段位置不能直接外推。

## RDNA-2：保持 pri/pre/mature/AGO-loaded 实体分辨率

- **候选程序**：明确检测的是 MIR locus、pri-miRNA、pre-miRNA、miRNA/miRNA-star duplex、成熟 arm、isomiR/end variant 还是 AGO-loaded mature product。
- **关系标签**：`strongly_consistent`。
- **复现情境 1**：HEN1 重组蛋白研究将 21–24 nt duplex 定为生化底物，并定位末端 2'-O-methylation [src-doi-10-1093-nar-gkj474; claim-chen-b05]。
- **复现情境 2**：pre-miRNA 3' RACE sequencing 直接针对前体末端异质性，而非用成熟 read 反推前体 [src-doi-10-1038-s41477-019-0562-1; claim-chen-b02]。
- **复现情境 3**：RBV 论文区分 total mature miRNA 与 AGO1-IP fraction [src-doi-10-1038-s41467-022-28872-x; claim-chen-b07]。
- **failure/transfer limits**：pre-miRNA 定义与不同 MIR hairpin 的 processing direction 有关；同名 miRNA family 不能代替具体 locus/arm/sequence。2019 来源在本轮只有摘要，不能推断摘要未写明的 locus-level 细节。

## RDNA-3：遗传—生化—RNA 测量三角，而非表型单证据

- **候选程序**：遗传扰动/救援建立必要性或顺序，生化/interaction/localization assay 指向机制，RNA-species-resolved measurement 确认受影响步骤；表型作为下游一致性而非机制充分证据。
- **关系标签**：`agent_inference`（跨研究归纳），单篇研究内的具体组合为 `explicit`。
- **复现情境 1**：HEN1 工作组合 hen1 genetics、beta-elimination/mass analysis 与体外 methyltransferase assay [src-doi-10-1126-science-1107130; src-doi-10-1093-nar-gkj474; claim-chen-b04]。
- **复现情境 2**：HESO1 工作组合 suppressor genetics、terminal nucleotidyl transferase biochemistry 与 small-RNA end profiles [src-doi-10-1016-j-cub-2012-02-052; claim-chen-b04]。
- **复现情境 3**：TREX-2/NPC 工作组合 mutants、protein/localization assays、processing/loading/export readouts [src-doi-10-1038-s41477-020-0726-z; claim-chen-b08]。
- **failure/transfer limits**：这是 Agent 提炼，不是命名的 Chen 框架；严谨三角验证也并非该实验室独有。不同问题可能无需三类证据齐全，但缺失轴必须明确降低主张强度。

## RDNA-4：用 suppressor/epistasis 拆解 mutant pleiotropy 与竞争效应

- **候选程序**：对于广泛发育异常的小 RNA mutant，不把表型直接归因于单一 miRNA；利用 suppressor 与 epistasis 寻找 pathway order、substrate competition 或旁路。
- **关系标签**：`explicit`。
- **复现情境 1**：hen1-2 suppressor screen 发现 Pol IV pathway second-site mutations，并通过 miRNA methylation 恢复支持 siRNA/miRNA 对 HEN1 的竞争 [src-doi-10-1093-nar-gkq348; claim-chen-b06]。
- **复现情境 2**：HESO1 suppressor strategy 将未甲基化 small-RNA uridylation 与 terminal nucleotidyl transferase 活性连接 [src-doi-10-1016-j-cub-2012-02-052; claim-chen-b04]。
- **复现情境 3**：AAR2/HYL1 genetic dependence 用于约束 pri-miRNA stability 解释，同时保留 AAR2 作为 splicing factor 的 pleiotropy [src-doi-10-1073-pnas-2208415119; claim-chen-b11]。
- **failure/transfer limits**：suppressor 可能是 bypass 或剂量补偿，不自动证明直接相互作用；partial allele 的 epistasis 不能直接外推 null allele 或其他组织。

## RDNA-5：定位证据必须与机制匹配

- **候选程序**：colocalization/compartment association 只提供候选位置；要声称 processing、loading、export 或 movement，必须有相应 genetic perturbation 与 stage-matched molecular readout。
- **关系标签**：`strongly_consistent`。
- **复现情境 1**：TREX-2/NPC 研究将 localization/interaction 与 processing、AGO1 loading、export 读数配对 [src-doi-10-1038-s41477-020-0726-z; claim-chen-b08]。
- **复现情境 2**：RBV 工作将 cellular localization/interaction 与 total/AGO1-IP small RNA 配对 [src-doi-10-1038-s41467-022-28872-x; claim-chen-b07]。
- **复现情境 3**：microtubule/KTN1 工作用 cell-type perturbation、AGO1 loading 与 movement readouts 约束 source-cell 机制 [src-doi-10-1016-j-devcel-2022-03-015; claim-chen-b09]。
- **failure/transfer limits**：过表达标签可能改变定位；空间共现不等于直接作用。source/recipient cell 的边界在移动研究中不可省略。

## RDNA-6：direct target、mode of action 与 phenotype causality 分轴

- **候选程序**：分别问 target site 是否直接、mRNA/protein 哪一层受影响、target perturbation 是否足以解释 phenotype。
- **关系标签**：`explicit`（miR172/AP2 案例），跨问题规则为 `strongly_consistent`。
- **复现情境 1**：miR172/APETALA2 研究用 target-site/transgene、RNA 与 protein 层读数支持 translational repression，再连接 floral phenotype [src-doi-10-1126-science-1088060; claim-chen-b03]。
- **复现情境 2**：miR165/166 movement 研究分别测 movement、AGO1 loading、target response 与组织表型，避免把其中一轴代替全部因果链 [src-doi-10-1016-j-devcel-2022-03-015; claim-chen-b09]。
- **failure/transfer limits**：miR172 结论不能外推为植物 miRNA 普遍以 translational repression 为主；PARE/cleavage、AGO loading、表达反相关均不能单独证明完整表型因果。

## RDNA-7：把稳定性和尾化解释置于 AGO/底物情境

- **候选程序**：对 truncation/tailing 先问 methylation status、AGO association、substrate stage 和 species/context，再解释 turnover。
- **关系标签**：`explicit`。
- **复现情境 1**：hen1 研究把 loss of methylation 与 3' uridylation/trimming 联系 [src-doi-10-1016-j-cub-2005-07-029; claim-chen-b04]。
- **复现情境 2**：跨 Arabidopsis/rice end profiling 显示 modification profile 随 miRNA 和 AGO1 context 变化 [src-doi-10-1105-tpc-113-114603; claim-chen-b10]。
- **复现情境 3**：AGO1-associated HESO1 活性研究区分 free/AGO-bound small-RNA context [src-doi-10-1073-pnas-1405083111; claim-chen-b10]。
- **failure/transfer limits**：tail read 不等于降解速率；跨物种 conservation 只支持模式层类比，不能把同名 miRNA 当正交或假设频率相同。

## Cross-framework decision order

1. 锁定 organism、tissue、stage、genotype、treatment 与具体 miRNA entity。
2. 明确观察值处于 lifecycle 哪一层，列出至少两个相邻阶段的替代解释。
3. 选择与阶段匹配的 RNA measurement；涉及 loading/movement 时加入 AGO1-IP 或 cell-type/spatial readout。
4. 用 genetics/rescue/epistasis 定位必要性，用 biochemistry/interaction 定位直接机制。
5. direct target、mode of action 与 phenotype causality 分别评级。
6. 若只有表型、总 small-RNA abundance 或 colocalization，保持低直接性并提出最小补充实验。

## Honest boundaries

- 这些程序主要来自 Arabidopsis；作物迁移须重新验证组织、MIR locus、AGO family 与加工路线。
- 不采用动物 Drosha–DGCR8 或 seed-only 规则解释植物机制。
- Chen 共同作者身份不等于个人对论文每句话的背书；`claim-chen-b12` 明确是 Agent 推断。
- AAR2 正式 correction（DOI 10.1073/pnas.2219264119；PMID 36534814；PMCID PMC9907120）影响 Fig. 1/Fig. S3 legends 及 Figs. 6/S2/S6；本底稿使用的 promoter/decay 结论映射到 Figs. 3/4，不依赖受影响图件。任何受影响 panel 复用必须使用线上已更正版本，correction 不计独立支持。
- 本维度不提供独立实验室复现判定；该任务属于 Agent C。
