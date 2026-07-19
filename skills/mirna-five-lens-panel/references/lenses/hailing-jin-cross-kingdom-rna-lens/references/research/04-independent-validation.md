# Hailing Jin — 独立验证、批评与适用范围底稿

## 审计范围

- `expert_id`: `hailing-jin`
- 负责维度：04（独立验证与批评）
- 机制证据截止：2026-07-17
- 检索日：2026-07-18
- 专家身份：已由 N0.5 以 UCR、ORCID `0000-0001-5778-5193`、研究主题和作者网络交叉核验。
- 严格独立规则：独立性按实验室/合作网络而非论文数；Jin 团队来源只作为被审查主张与方法背景，不计入 strict independent items。

## 1. Independent source table

| 独立项 | Source ID | 外部网络 | 物种/体系 | 方法 | 关系分类 | 核心结论 | 主要限制 |
|---|---|---|---|---|---|---|---|
| IND-1 | HJ-B-S012 | Guo / CAS（外部主导；UCR 机构邻近，降级） | cotton–Verticillium | 受体菌丝纯化、miRNA、靶位点抗性、遗传与毒力 | 外部支持；不计保守 strict 6 | 天然 plant→fungus miRNA 可在另一体系形成因果边 | 不证明 EV 路线；含 UCR 同部门/研究社区邻近的 Ding，不计最保守严格门槛 |
| IND-2 | HJ-C-S010 | Rothamsted / Syngenta（严格外部） | wheat–Zymoseptoria | sRNA-seq、DCL/AGO mutants、HIGS、摄取成像 | 范围差异/负结果 | 未验证跨界靶标；RNAi mutants 毒力不减；HIGS/摄取失败 | 不能反驳 Botrytis；可能有非典型或非切割效应 |
| IND-3 | HJ-C-S011 | ETH Zurich（严格外部） | wheat–Zymoseptoria | dual sRNA/mRNA-seq、matched PARE | 独立负结果 | 不同 strain/cultivar 下仍无清晰跨界 mRNA 切割 | PARE 不排除翻译/转录调控；整组织稀释稀有事件 |
| IND-4 | HJ-C-S012 | Wageningen / Kaiserslautern（严格外部） | tomato–Botrytis early infection | dual profiling、transposon deletion、dcl1 dcl2、毒力 | 部分不复现/直接批评 | >99% transposon-sRNA reduction 未降低毒力 | 早期 tomato、B05.10、特定 sRNA 类；不是 Arabidopsis AGO1-IP 复刻 |
| IND-5 | HJ-B-S006；HJ-B-S015；HJ-CORR-S002 | Innes / Meyers（严格外部；同网络合并计 1） | Arabidopsis EV/extracellular RNA | apoplast EV、sRNA-seq、mapping、compartment comparison | 独立扩展/组分差异 | EV 中有多类 RNA，但 10–17 nt tiny RNAs 高度富集且功能不明；leaf-surface/apoplast/EV RNA 不可混同 | 纯化与建库差异；不测试真菌递送；HJ-CORR-S002 仅改资助致谢 |
| IND-6 | HJ-C-S014 | Coffey / Vanderbilt（跨类群方法类比，降级） | mammalian EV | 高分辨密度、immunocapture、proteomics、RNA | analogous/uncertain；不计保守 strict 6 | RNP/RNA 可在非囊泡组分；所测 exosome 无 AGO1-4 | 哺乳动物≠植物；只能作 control analogue，不能作植物机制复现 |
| IND-7 | HJ-B-S013 | Kogel / Giessen（严格外部） | barley–Fusarium | SIGS、长 dsRNA movement、fungal DCL genetics | 独立支持/扩展 | 离体叶片可发生 distal RNA movement 与 fungal DCL-dependent protection | 非田间；不同病原/guide/delivery |
| IND-8 | HJ-B-S014 | Zhou / Nanjing Agricultural University（严格外部） | wheat–Fusarium spp. | SIGS、time course、uptake、sRNA-seq | 支持并限定 | 作用短暂、伤口影响摄取、植物扩增延长、物种响应不同 | 切割子叶鞘/培养体系；不能给出田间持久性 |

保守严格独立网络总数：**6**（IND-2、3、4、5、7、8），满足 Hailing Jin 最低 6 项要求。另保留 2 个降级外部簇：IND-1 为外部主导但存在 UCR 机构邻近，IND-6 为 human-EV 跨类群方法类比；二者不计入 strict 6。证据边或论文数均不替代网络计数。

## 2. Supported claims

### 2.1 天然 plant→fungus 小 RNA 功能可在非 Jin 网络成立

- **Finding**：HJ-B-S012 在 cotton–Verticillium 中用 miR166/miR159、菌丝内检测、靶位点抗性 fungal alleles 和 virulence assays 建立了比“检测到 reads”更强的因果链。
- **Why it matters**：这是对广义 cross-kingdom RNAi 的有力外部主导支持，但因 UCR 机构邻近不计最保守 strict 6；它仍表明最有判别力的实验是 target-site resistance，而不只是表达反相关。
- **Source ID**：HJ-B-S012；卡 HJ-C-C008。
- **Source type / expert role**：外部原始研究 / Jin not author。
- **Species / context**：Gossypium hirsutum–Verticillium dahliae。
- **Evidence directness**：direct genetics + recipient RNA evidence。
- **Limitations**：不同物种、组织、guide 和 target；没有证明 TET8-positive EV delivery。
- **Confidence**：高。

### 2.2 SIGS 在某些真菌体系具备外部机制支持

- **Finding**：HJ-B-S013 显示喷施长 dsRNA 可在离体 barley 叶片移动，并在 Fusarium uptake 后由 fungal DCL1 处理；HJ-B-S014 又在 Fusarium 中验证摄取/沉默，但指出持续性和物种差异。
- **Why it matters**：支持 Jin 项目将 external RNA 视为可设计保护策略，同时否定“一个配方可普遍适用”的过度外推。
- **Source ID**：HJ-B-S013、HJ-B-S014；卡 HJ-C-C015、HJ-C-C016。
- **Source type / expert role**：两套严格外部原始研究。
- **Species / context**：barley–F. graminearum；wheat coleoptile–F. asiaticum/other Fusarium。
- **Evidence directness**：direct molecular/genetic/disease evidence。
- **Limitations**：离体叶片、切割组织和培养体系；缺少多环境田间证据。
- **Confidence**：高（proof-of-concept），低（field readiness）。

### 2.3 植物 EV 与 extracellular RNA 的组成异质性获外部支持

- **Finding**：HJ-B-S006 独立确认 Arabidopsis EV 中有多类 sRNA，但其主要发现之一是 10–17 nt tiny RNA 的强富集，并明确功能未知、可能含降解产物。
- **Why it matters**：支持“植物 EV 含 RNA”的广义事实，却要求把功能 guide 与 EV-associated fragment 分开。
- **Source ID**：HJ-B-S006；卡 HJ-C-C013。
- **Source type / expert role**：严格外部原始研究。
- **Species / context**：Arabidopsis apoplastic EV preparations。
- **Evidence directness**：direct sequencing/composition evidence。
- **Limitations**：不同纯化、ligation、size-selection 可改变谱；不测试跨界 uptake。
- **Confidence**：高。

## 3. Contested claims

### 3.1 “跨界 RNAi 是所有植物–真菌互作的通用毒力机制”不成立

- **Finding**：两套独立 wheat–Zymoseptoria 研究分别从遗传、摄取、HIGS、dual-omics 和 PARE 得到负结果；Z. tritici 的外源 RNA uptake 不可检测，canonical RNAi components 对全毒力并非必需。
- **Why it matters**：跨界 RNAi 必须按 organism pair 与 recipient competence 分层，不得从 Botrytis/Verticillium 直接迁移到 Zymoseptoria。
- **Source ID**：HJ-C-S010、HJ-C-S011；卡 HJ-C-C009、HJ-C-C010、HJ-C-C012。
- **Source type / expert role**：两个严格外部实验室网络。
- **Species / context**：不同 wheat cultivars 与 Z. tritici strains。
- **Evidence directness**：direct negative genetics/uptake/PARE evidence。
- **Limitations**：不能排除翻译抑制、转录沉默、稀有细胞或未测时间窗。
- **Confidence**：高（该 pathosystem 的否定边界）。

### 3.2 Botrytis fungal-sRNA virulence 在 early tomato 中未被功能复现

- **Finding**：HJ-C-S012 删除产生约 10% fungal sRNA 的 transposon 区域，并构建 dcl1 dcl2 double mutant；后者使 transposon-derived sRNA 减少超过 99%，但多宿主 virulence 未显著下降。
- **Why it matters**：这是和 2013 Jin-team Botrytis model 直接相关的外部批评，必须进入 conflict record；不能仅以“不同实验室”抹去。
- **Source ID**：HJ-C-S012；卡 HJ-C-C011、HJ-C-C012。
- **Source type / expert role**：严格外部原始研究。
- **Species / context**：B. cinerea B05.10–tomato early infection，12/16/24 h profiling。
- **Evidence directness**：direct genetics + profiling + virulence。
- **Limitations**：没有复刻 Arabidopsis AGO1-IP；宿主、时间窗、菌株和 sRNA 来源不同；不排除 later/rare effects。
- **Confidence**：高（partial non-replication），不应写成全领域 refutation。

### 3.3 “EV 富集即证明运输”不成立

- **Finding**：HJ-B-S006 表明 EV 组分可富集功能未知短片段；HJ-C-S014 在哺乳动物体系进一步表明 RNA/RBP 可位于非囊泡组分，粗颗粒与真正 exosome composition 不同。
- **Why it matters**：需要 density、membrane protection、marker、immunocapture、non-vesicular comparator 和 intact-recipient uptake 控制。
- **Source ID**：HJ-B-S006、HJ-C-S014；卡 HJ-C-C013、HJ-C-C014。
- **Source type / expert role**：外部植物研究 + 跨类群方法研究。
- **Species / context**：Arabidopsis；human cell/plasma/tissue EV。
- **Evidence directness**：direct in each source；跨类群迁移为 analogous/uncertain。
- **Limitations**：不能用 human AGO-negative exosome 直接反驳 Arabidopsis AGO1-positive TET8 fractions。
- **Confidence**：高（控制原则），中低（跨类群机制相同）。

## 4. Methodological critiques

### 4.1 污染与组织混样

最小控制集：

1. 感染组织中分离 recipient cells，并报告纯度指标；
2. “未感染 donor tissue + cultured recipient 后混合”过程控制；
3. recipient cell wall/surface nuclease 或 protease 保护对照；
4. donor organelle、nuclear、abundant housekeeping RNA contamination markers；
5. pathogen biomass 和 cell-type composition normalization；
6. microscopy 与 molecular recovery 交叉验证。

HJ-A-S009 的 sequential protoplast purification 是正例，但仍需外部同体系重复。HJ-C-S010 用 Botrytis 作 uptake positive control 说明“看不见 uptake”并非成像系统整体失败。

### 4.2 双基因组 mapping ambiguity

- 报告 donor/recipient assembly 与版本；
- exact sequence、read length、multi-map count、mismatch policy；
- 对超短 10–17 nt RNA 不允许凭跨物种同名或短匹配判定来源；
- 去除 rRNA/tRNA/repeat/adapter/低复杂度与实验室载体污染；
- 用同一序列对两套 genome/transcriptome 竞争比对；
- guide 需要明确 family/locus/arm/isomiR/sequence 层级。

HJ-C-S010–S012 的负结果提醒：大规模预测会制造大量候选；表达下调不能区分直接靶向、病原负荷变化和宿主免疫响应。

### 4.3 EV 富集不等于 EV 包封或功能递送

建议按以下阶梯报告：

```text
粗 extracellular pellet
→ density-defined fraction
→ membrane marker / contaminant marker
→ nuclease ± detergent protection
→ EV-subclass immunocapture
→ RNA/RBP co-recovery
→ intact recipient uptake
→ recipient AGO/RISC access
→ direct target
→ causal phenotype
```

HJ-A-S010 的 TET8 immunoaffinity 是强于粗离心的证据；HJ-B-S006 与 HJ-C-S014 说明仍应比较 non-vesicular extracellular pools 与不同 EV subclasses。

### 4.4 RNA 摄取、AGO 与靶标直接性

- 摄取应在 intact recipient cells 证明，排除表面黏附和染料游离；
- 受体 AGO loading 或等价 RISC evidence 不应由 donor AGO/EV association 代替；
- target prediction = F1；反相关/下调 = F2；AGO/PARE/5′ RACE/reporter/biochemistry = F3；target-site-resistant allele/rescue = F4；
- PARE cleavage 不等于 phenotype causality；无 PARE signal 也不完全排除 translational repression。

HJ-B-S012 的 target-site-resistant fungal alleles 是强因果模板。HJ-C-S011 的 matched PARE 是有力负证据，但只针对 mRNA cleavage。

### 4.5 HIGS/SIGS 与田间推广

必须把以下结果分开：

1. 外源 RNA 可被摄取；
2. 靶基因被序列特异性抑制；
3. controlled tissue disease 减轻；
4. intact plant/greenhouse 有效；
5. multi-location field efficacy；
6. persistence/rainfastness/formulation/cost；
7. non-target、off-target、resistance evolution 与监管。

HJ-B-S013 支持 1–3；HJ-B-S014 显示 uptake、wounding、amplification、duration 和 fungal species 都会改变结果。Agent C 未找到足以把本路线标为“已完成田间部署”的证据。

## 5. Context-dependent differences

| 问题 | 正面情境 | 负面/受限情境 | 当前状态 |
|---|---|---|---|
| 天然 plant→fungus RNAi | cotton–Verticillium（HJ-B-S012） | wheat–Zymoseptoria 无清晰功能（S010/S011） | organism-pair specific |
| fungal→plant sRNA virulence | Jin-team Botrytis–Arabidopsis | early Botrytis–tomato 未见功能（S012） | contested, host/time/strain bounded |
| 外源 RNA uptake | Botrytis、Fusarium（S004/S015/S016） | Z. tritici 不可检测（S010） | recipient competence gate |
| EV RNA composition | Jin-team TET8 sRNA/RBP（S005/S006） | external tiny-RNA-rich composition（S013） | EV subclass/method dependent |
| AGO in EV | Arabidopsis AGO1 in TET8 fractions（S006） | mammalian purified exosomes无 AGO1-4（S014） | lineage/subclass/method difference；不可直接互否 |
| SIGS persistence | controlled protection（S015） | transient without continuous supply、wound and species effects（S016） | pre-field, formulation/exposure limited |

## 6. Retraction/correction/expression-of-concern check

### 已发现

- **HJ-A-S010** 有正式 **Publisher Correction**：HJ-A-S011，DOI `10.1038/s41477-021-00901-5`，PMID `33762679`。官方通知说明错误的 Supplementary Information 文件已被正确文件替换；必须使用更正后补充材料，且不得推断通知未陈述的结论变化。
- **HJ-C-S012** 有正式 corrigendum：HJ-CORR-S001，DOI `10.1111/mpp.13303`，PMID `36779303`，PMCID `PMC9923388`。它补充 SRA/data-availability 信息，不声明改变该研究的科学结论；本项目未下载原始数据。
- **HJ-B-S015** 有正式 correction：HJ-CORR-S002，DOI `10.1073/pnas.2501042122`，PMID `39918924`，PMCID `PMC11874235`。它仅替换资助致谢，不改变 compartment-specific RNA 结果。

### 未发现

截至机制证据截止 2026-07-17，除上述记录及另行挂接的 2025 Science erratum 外，本次 PubMed/PMC/期刊状态审计未发现 retraction 或 expression of concern。此结论仅表示“本次状态审计未发现”，不等于未来不会更新。

## 7. Unresolved conflicts

### Conflict A — Botrytis fungal sRNA 是否对宿主毒力有可重复的主要贡献？

- **Position A**：Jin-team Arabidopsis/Tomato work reports fungal sRNAs, host AGO1 engagement, immune-target repression, and reduced pathogenicity of fungal dcl mutants。
- **Position B**：HJ-C-S012 在 early tomato 中，dcl1 dcl2 使 transposon-derived sRNA 减少 >99% 而 virulence 未显著下降；HJ-CORR-S001 仅补充数据可用性/SRA 信息，不改变这一有边界的结论。
- **Context difference**：host species/cultivar、infection stage、strain background、sRNA source classes、target set、AGO assay。
- **What would resolve**：预注册同一 B. cinerea strain × Arabidopsis/tomato reciprocal replication；time-resolved recipient AGO-IP/CLIP；exact guide target-site-resistant plant alleles；fungal DCL complementation；pathogen biomass/cell-mixture controls。

### Conflict B — plant EV sRNA cargo 的主成分与功能载体是什么？

- **Position A**：HJ-A-S009/S006 支持 TET8-positive EV 中 selected sRNAs 与 AGO1/RHs/ANNs。
- **Position B**：HJ-B-S006 发现 tiny RNAs 高度富集且功能未知；HJ-C-S014 提醒 extracellular RNP/non-vesicular matter 可共纯化。
- **Context difference**：infection status、EV subclass、density/immunocapture、RNA size selection、plant vs mammalian lineage。
- **What would resolve**：跨实验室统一 EV isolation、spike-ins、nuclease ± detergent、TET8/PEN1 subclass immunocapture、single-particle/orthogonal imaging、absolute RNA quantification、recipient-cell functional delivery。

### Conflict C — SIGS 能否成为普适 RNA fungicide？

- **Position A**：Jin-team 与 HJ-B-S013 显示多种 controlled systems 中可保护组织。
- **Position B**：HJ-C-S010 显示 Z. tritici uptake/HIGS 失败；HJ-B-S014 显示 transient effect、wound dependence、species selectivity。
- **Context difference**：pathogen uptake competence、target choice、dsRNA length、dose、plant passage、tissue integrity、environmental exposure。
- **What would resolve**：标准化跨物种 uptake panel、dose–response、intact-plant and multi-environment field trials、formulation persistence、off-target/non-target and resistance-evolution tests。

## 8. Candidate evidence rules for synthesis

1. **Cross-kingdom causal chain rule**：来源→纯化→运输→摄取→RISC→靶标→表型逐级报告，禁止跨级。
2. **Recipient competence rule**：每个病原先证明 uptake 与 RNAi competence；不能从 Botrytis/Fusarium 外推到 Zymoseptoria。
3. **Dual-genome identity rule**：exact sequence、assembly、multi-map 和污染控制是最前置门槛。
4. **EV subclass rule**：粗 EV、TET8-positive EV、PEN1-positive EV 与 non-vesicular RNA/RNP 分开。
5. **Conflict preservation rule**：Botrytis positive/negative data 按 host–strain–time–method 保留，不以引用量裁决。
6. **Application tier rule**：molecular proof、controlled disease protection、greenhouse、field efficacy、deployment safety 五层分开。
7. **Publication-status rule**：原论文永远与更正记录结伴。HJ-A-S010 使用 HJ-A-S011 替换后的补充材料；HJ-A-S006/HJ-A-S007 的未知更正内容继续阻断细粒度复用；HJ-C-S012/HJ-CORR-S001 与 HJ-B-S015/HJ-CORR-S002 保留各自已核实的有限更正范围。

## 9. 结论

本维度不是“证明或推翻跨界 RNAi”，而是把其可靠适用范围变得可审计。六个保守严格网络与两个降级外部簇共同显示：cotton–Verticillium 有外部主导的强支持，若干 SIGS–Fusarium 体系有严格外部支持；wheat–Zymoseptoria 和 early tomato–Botrytis 存在实质负结果或部分不复现；EV 纯化和 RNA cargo 解释存在方法依赖。N2 应将“受体能力 + 因果链 + 情境边界”作为候选模型，将“跨界 RNA 普遍存在且可直接田间推广”列为 anti-pattern。
