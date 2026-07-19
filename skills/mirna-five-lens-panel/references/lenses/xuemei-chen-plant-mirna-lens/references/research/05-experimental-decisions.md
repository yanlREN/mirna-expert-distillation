# Xuemei Chen — Experimental Decision Cases（N1 Agent B）

以下 12 个案例只记录公开研究中可重建的决策结构。`chosen evidence` 表示论文采用的证据组合，不把共同作者团队的全部推理冒充为 Xuemei Chen 的个人判断。

## DEC-B01：miR172 对 APETALA2 的作用层级

- **problem**：花发育表型来自 APETALA2 transcript cleavage、translation repression，还是间接网络变化？
- **alternatives**：mRNA 降低；蛋白翻译受抑；非直接下游效应。
- **chosen evidence**：target-site/transgene genetics，APETALA2 RNA 与 protein 层的比较，花器官表型 [src-doi-10-1126-science-1088060; claim-chen-b03]。
- **decision**：在该 Arabidopsis 情境中支持 miR172 对 APETALA2 的 translational repression，并把分子作用与花表型连接但不混同。
- **why**：protein 与 transcript 的分层读数能判别单纯 mRNA loss 无法解释的作用模式。
- **limitation**：单一 target pair 不能规定所有植物 miRNA 的主导作用模式；完整 phenotype causality 仍依赖构建与背景。

## DEC-B02：HEN1 是否直接修饰 plant miRNA

- **problem**：hen1 mutant 的 miRNA 异常来自加工缺陷还是成熟 duplex 的共价末端修饰缺失？
- **alternatives**：DCL1 processing failure；非直接稳定性效应；HEN1-mediated methylation。
- **chosen evidence**：hen1 genetics、beta-elimination/mass analysis 与 recombinant HEN1 methyltransferase assay [src-doi-10-1126-science-1107130; src-doi-10-1093-nar-gkj474; claim-chen-b04; claim-chen-b05]。
- **decision**：把 HEN1 放在 Dicer product/duplex 后的 terminal 2'-O-methylation step。
- **why**：遗传表型、化学端基信息和体外催化共同排除了仅凭 steady-state abundance 的歧义。
- **limitation**：体外底物选择不等于所有组织内的动力学；HEN1 同时作用多类 small RNA。

## DEC-B03：未甲基化 small RNA 的端异质性来源

- **problem**：hen1 中较长/较短 small-RNA species 是不精确加工、随机降解，还是 3' tailing/trimming？
- **alternatives**：DCL processing imprecision；templated precursor variants；untemplated uridylation plus trimming。
- **chosen evidence**：genotype comparison、3'-end analysis、methylation-sensitive assay [src-doi-10-1016-j-cub-2005-07-029; claim-chen-b04]。
- **decision**：支持 methylation 防止 3' uridylation/trimming；端异质性属于 stability/turnover 轴。
- **why**：端序列与 methylation state 比总丰度更直接地定位变化。
- **limitation**：tailing 与 trimming 的具体酶及先后顺序需要后续 genetics/biochemistry；不能从单个 gel band 推断全部 isomiR。

## DEC-B04：HEN1 substrate specificity

- **problem**：HEN1 识别单链 mature RNA、任意 dsRNA，还是具有尺寸/结构要求的 small-RNA duplex？
- **alternatives**：single-strand recognition；sequence-specific recognition；duplex-structure/size recognition。
- **chosen evidence**：recombinant HEN1 与一组长度、突出端和结构不同的 substrates 的 methyltransferase assays [src-doi-10-1093-nar-gkj474; claim-chen-b05]。
- **decision**：支持 HEN1 对 21–24 nt small-RNA duplex 的结构/尺寸识别，并修饰 3' terminal ribose。
- **why**：受控 substrate panel 能把 sequence 与 geometry 的替代解释分开。
- **limitation**：体外 panel 不能覆盖所有 endogenous duplex modifications，也不能直接迁移到动物 miRNA pathway。

## DEC-B05：hen1-2 suppressor 的机制含义

- **problem**：第二位点突变恢复 hen1-2 表型/miRNA 是直接 pathway restoration、旁路，还是 substrate competition 改变？
- **alternatives**：提高 HEN1 expression/activity；阻断降解；减少竞争 siRNA substrate。
- **chosen evidence**：suppressor mapping、Pol IV/RDR2 epistasis、miRNA methylation 与 small-RNA class measurements [src-doi-10-1093-nar-gkq348; claim-chen-b06]。
- **decision**：支持 Pol IV-dependent siRNAs 与 miRNAs 对 partial HEN1 capacity 的竞争。
- **why**：第二位点基因身份与不同 small-RNA classes 的反向变化提供机制方向。
- **limitation**：partial `hen1-2` 的容量竞争不能不加限定地外推到 null allele、所有组织或 HEN1 过量情境。

## DEC-B06：HESO1 是否是未甲基化 miRNA 的 uridyltransferase

- **problem**：hen1 background 的 U-tails 由哪个 enzyme 产生，tailing 是否与 degradation 相连？
- **alternatives**：HESO1；另一 terminal transferase；degradation 的被动副产物。
- **chosen evidence**：hen1 suppressor genetics、HESO1 enzyme assay、methylation inhibition 与 small-RNA end profiles [src-doi-10-1016-j-cub-2012-02-052; claim-chen-b04]。
- **decision**：支持 HESO1 uridylates unmethylated small RNAs，并促进其 turnover。
- **why**：loss-of-function 与 purified-enzyme substrate behavior 在同一端修饰上会合。
- **limitation**：Xuemei Chen 为中间共同作者；应作为团队证据。某些 truncation 可能由不同 enzyme 产生。

## DEC-B07：3' modification 是否可脱离 AGO context 解读

- **problem**：miRNA-specific tailing/truncation 是否仅由 methylation state 决定？
- **alternatives**：uniform protection model；sequence-only model；AGO1/substrate-context-dependent model。
- **chosen evidence**：Arabidopsis/rice small-RNA end profiling、AGO1 dependence/association 和跨物种比较 [src-doi-10-1105-tpc-113-114603; src-doi-10-1073-pnas-1405083111; claim-chen-b10]。
- **decision**：选择 context-dependent interpretation：methylation、AGO association、miRNA identity 与 species/context 共同塑造 end profile。
- **why**：不同 miRNA 的 modification pattern 与 AGO1 context 不一致于统一尾化率假设。
- **limitation**：cross-species pattern 不证明同名 family 正交；end-state snapshot 不等同 degradation kinetics。

## DEC-B08：pre-miRNA 端异质性属于哪一阶段

- **problem**：成熟 miRNA isomiR 是否能代表全部 processing imprecision，还是 pre-miRNA 已存在独立的 3' end variation？
- **alternatives**：只有 mature product tailing；microprocessor cleavage imprecision；pre-miRNA cytidylation/uridylation。
- **chosen evidence**：3' RACE sequencing of pre-miRNAs、microprocessor mutants、HESO1/URT1 in vitro and in vivo assignments（限摘要明确内容）[src-doi-10-1038-s41477-019-0562-1; claim-chen-b02]。
- **decision**：把前体末端异质性作为独立于成熟 product 的可测层级，并支持 HESO1/URT1 参与特定 pre-miRNA additions。
- **why**：直接测 pre-miRNA ends 避免从 mature read 倒推 precursor。
- **limitation**：本轮无合法开放全文，只能使用摘要支持的范围，不写具体 locus/figure 或超出摘要的酶分工细节。

## DEC-B09：TREX-2/NPC 位于 processing、loading 还是 export

- **problem**：核孔相关 factor 的 miRNA phenotype 来自一般核运输、pri-miRNA processing、AGO1 loading，还是 miRISC export？
- **alternatives**：单一 export defect；上游 processing defect；多阶段连接但各阶段可分辨。
- **chosen evidence**：genetics、protein interactions/localization、pri/mature RNA、AGO1 loading 与 export readouts [src-doi-10-1038-s41477-020-0726-z; claim-chen-b08]。
- **decision**：支持 TREX-2/NPC 连接多个关键阶段，同时保留 processing/loading/export 为不同可测节点。
- **why**：仅有核孔定位不足；跨节点 readouts 能检验多阶段模型。
- **limitation**：physical interaction 或 colocalization 不自动说明直接催化；不同 mutant 的广泛核运输效应需要控制。

## DEC-B10：RBV phenotype 是 biogenesis 还是 loading defect

- **problem**：rbv mutant 中 miRNA function 降低是否完全由 total miRNA 下降解释？
- **alternatives**：transcription/processing-only；AGO1 abundance-only；额外的 loading-efficiency defect。
- **chosen evidence**：total small-RNA sequencing、AGO1 immunoprecipitated small RNAs、genetics/complementation 与 interaction/localization [src-doi-10-1038-s41467-022-28872-x; claim-chen-b07]。
- **decision**：把 total abundance 与 AGO1 loading 分开，支持 RBV 同时影响 miRNA biogenesis 和 loading。
- **why**：input-normalized AGO1-associated fraction 提供总量读数没有的阶段信息。
- **limitation**：AGO1-IP 受 protein abundance 与 recovery 影响，必须有输入和 AGO1 controls；RBV 的保守性不代表功能在所有植物完全相同。

## DEC-B11：mobile miRNA 的 source-cell loading 选择

- **problem**：miR165/166 的非细胞自主作用由产生量、source-cell AGO1 loading、移动或 recipient response 哪一步限制？
- **alternatives**：更多 transcription/processing；AGO1 loading 促进移动；source-cell AGO1 loading 与移动竞争。
- **chosen evidence**：cell-type-specific KTN1 genetics/rescue、microtubule perturbation、AGO1 loading assays、movement/recipient reporters [src-doi-10-1016-j-devcel-2022-03-015; claim-chen-b09]。
- **decision**：在测试的 root context 支持 microtubules/KTN1 抑制 source-cell cytoplasmic AGO1 loading，从而允许 miR165/166 exit 和 non-cell-autonomous action。
- **why**：source/recipient 分区和 loading/movement 双读数可区分“产生更多”与“更易移动”。
- **limitation**：不能推广为所有 miRNA 均需避免 AGO loading 才能移动；target response 和 root phenotype 仍是下游轴。

## DEC-B12：aar2 中 pri-miRNA 降低来自 transcription 还是 decay

- **problem**：aar2 mutant 的 pri-/mature-miRNA 变化是 MIR promoter activity 降低、processing acceleration，还是 pri-miRNA destabilization？
- **alternatives**：transcription defect；processing defect；HYL1-dependent pri-miRNA decay。
- **chosen evidence**：MIR promoter reporters、pri-miRNA abundance/decay assays、AAR2-HYL1 interaction/localization 与 genetic dependence [src-doi-10-1073-pnas-2208415119; claim-chen-b11]。
- **decision**：正常 promoter activity 排除简单 transcription explanation；加速 decay 支持 post-transcriptional pri-miRNA stability defect。
- **why**：promoter 与 decay 两类 assay 直接比较相邻 lifecycle alternatives。
- **limitation**：AAR2 的 splicing role 使 pleiotropy 不能被完全排除；正式 correction（DOI 10.1073/pnas.2219264119）影响 Fig. 1/Fig. S3 legends 及 Figs. 6/S2/S6，而本 decision 的 promoter/decay 证据映射到 Figs. 3/4。受影响 panel 复用必须使用已更正版本，correction 不计独立支持。

## Decision-case synthesis

这 12 个案例重复产生一组可迁移问题：检测的 RNA entity 是什么、变化处于 lifecycle 哪一步、是否有相邻阶段的排除实验、genetic evidence 是否有 stage-matched biochemistry/RNA readout、location 是否与机制匹配，以及 direct target/action/phenotype 是否分开。跨案例将其写成统一三角规则属于 `agent_inference` [claim-chen-b12]，不是专家第一人称陈述。
