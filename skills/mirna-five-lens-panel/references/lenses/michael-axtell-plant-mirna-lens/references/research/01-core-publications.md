# 01 — 核心论文与系统研究：Michael J. Axtell

## Metadata

```yaml
expert_id: michael-j-axtell
expert_name: Michael J. Axtell
dimension: core_publications
agent_role: research_agent_a
run_id: run-20260717-1730-cst
started_at: 2026-07-17
completed_at: 2026-07-17
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope and source overview

本稿只提炼 Axtell 公开论文中反复出现的科学判断动作，不把共同作者论文的每句话归于其个人。共核验 14 篇论文，覆盖 2005–2023 年；其中 12 篇为 Axtell 第一作者、末位/通讯或共同标准作者，2 篇为方法/共识协作。标识符以 PubMed、期刊页和 Axtell 实验室官方书目互相核对；未完成核对的 PMCID 留空。未下载原始测序数据，也未使用受限全文。

## Core publication table

| source_id | year | type | expert role | species/context | method focus | access / verification |
|---|---:|---|---|---|---|---|
| `src-doi-10-1105-tpc-105-032185` | 2005 | primary research | first | land plants | comparative genomics, target conservation | OA article; metadata verified |
| `src-doi-10-1105-tpc-107-051706` | 2007 | primary research | first | moss + flowering plants | small-RNA profiling, comparative analysis | PMC/Plant Cell; DOI+PMID verified |
| `src-doi-10-1016-j-cub-2008-04-042` | 2008 | primary research | senior/corresponding | *Arabidopsis thaliana* | degradome sequencing | abstract/full legal link; DOI+PMID verified |
| `src-doi-10-1105-tpc-108-064311` | 2008 | method/standard | coauthor | plants | annotation criteria | OA; DOI+PMID verified |
| `src-doi-10-1105-tpc-110-073882` | 2010 | primary research | senior/corresponding | *A. lyrata*, *A. thaliana* | comparative small-RNA genomics | OA; DOI+PMID verified |
| `src-doi-10-1261-rna-035279-112` | 2013 | method/primary | sole author | reference-based small-RNA data | ShortStack annotation | OA; DOI+PMID verified |
| `src-doi-10-1146-annurev-arplant-050312-120043` | 2013 | review/framework | sole review author | plants | small-RNA classification | abstract only; DOI+PMID verified |
| `src-doi-10-1105-tpc-113-120972` | 2014 | primary research | senior/corresponding | *Nicotiana benthamiana* assay | dual-luciferase targeting assay | OA; DOI+PMID verified |
| `src-doi-10-1105-tpc-15-00228` | 2015 | primary research | senior/corresponding | *Physcomitrella patens* | genetics + small-RNA annotation | OA; DOI+PMID verified |
| `src-doi-10-1105-tpc-17-00851` | 2018 | method/standard | first | plants | revised miRNA criteria | PMC; DOI+PMID verified |
| `src-doi-10-1111-tpj-13919` | 2018 | primary research | senior/corresponding | *A. thaliana* | rdr mutants + small-RNA sequencing | legal author copy/abstract; DOI+PMID verified |
| `src-doi-10-1038-nature25027` | 2018 | primary research | senior/corresponding | *Cuscuta campestris*–host interface | small-RNA sequencing + target cleavage/host assays | legal author copy; DOI+PMID verified |
| `src-doi-10-7554-elife-49750` | 2019 | primary research | senior/corresponding | *Cuscuta*–host pairs | comparative target-site evolution | OA; DOI verified |
| `src-doi-10-1093-plcell-koad076` | 2023 | primary research | senior/corresponding | *C. campestris* | promoter dissection / small-RNA genomics | OA; DOI verified |

## Findings

### Finding AXT-A-F01 — 先判定小 RNA 身份，再讨论功能

**Finding.** Axtell 相关标准从 2008 年到 2018 年持续把精确加工、miRNA/miRNA* duplex、发卡结构及与 siRNA 产生模式的区分置于注释核心；数据库收录或单条成熟序列不足以完成身份认定。2018 年修订正是对大数据时代误注释风险的收紧，而不是把预测发卡放宽为充分条件。

**Why it matters.** 它把“这是 miRNA”与“它有什么靶标/表型”拆成两个独立待证问题，直接支持项目 I0–I3 与 F0–F4 双轴。

**Evidence.** `src-doi-10-1105-tpc-108-064311`; `src-doi-10-1105-tpc-17-00851`; team/consensus result; plant small-RNA annotation; criteria and sRNA-seq patterns; directness=method standard. **Limitations:** 两篇均为标准/方法框架，不替代特定候选的实验验证。 **Confidence:** high. **Claim:** `claim-axtell-a-identity-before-function`.

### Finding AXT-A-F02 — 用多参数位点画像抵抗单一特征误判

**Finding.** ShortStack 将大小分布、重复性、链特异性、发卡关联、相位性和丰度联合报告；后续在 *Arabidopsis* rdr 背景和苔藓全基因组注释中，遗传背景与跨位点模式被用于清理 MIRNA/siRNA 边界。

**Why it matters.** 这不是“跑一个分类器”，而是让候选在彼此独立的生物发生特征上接受交叉检查。

**Evidence.** `src-doi-10-1261-rna-035279-112`; `src-doi-10-1111-tpj-13919`; `src-doi-10-1105-tpc-15-00228`; sole-author method + senior team results; multiple plant contexts; computational annotation plus genetics. **Limitations:** 参考基因组、建库偏差和样本覆盖仍限定可见性。 **Confidence:** high. **Claim:** `claim-axtell-a-multiparameter-locus-profile`.

### Finding AXT-A-F03 — 保守性是历史与优先级证据，不是单独的身份或功能证明

**Finding.** 从陆生植物古老 miRNA/靶标到 *Arabidopsis* 属内短寿命 MIRNA 位点的对比，长期框架同时容纳深度保守与快速出生—消亡：保守性可增强古老调控关系的可信度，但非保守候选需要更强的生物发生与功能证据。

**Evidence.** `src-doi-10-1105-tpc-105-032185`; `src-doi-10-1105-tpc-110-073882`; comparative genomics in distant and close taxa. **Limitations:** 缺失可来自真实丢失、组织未采样或基因组/组装质量。 **Confidence:** high. **Claim:** `claim-axtell-a-conservation-calibrates-prior`.

### Finding AXT-A-F04 — 靶标直接性与表型因果必须分层

**Finding.** 降解组能直接定位与小 RNA 引导切割相符的断点，而定量瞬时 reporter 能测量互补位点改变对抑制的影响；二者都强于纯预测，但均不能单独证明某个靶标解释完整表型。

**Evidence.** `src-doi-10-1016-j-cub-2008-04-042`; `src-doi-10-1105-tpc-113-120972`; *Arabidopsis* degradome versus *N. benthamiana* reporter. **Limitations:** degradome 有组织/丰度盲区；瞬时异源 assay 不等于原生组织因果。 **Confidence:** high. **Claim:** `claim-axtell-a-target-evidence-ladder`.

### Finding AXT-A-F05 — 用反例和异常类别修正规则，而非隐藏例外

**Finding.** 2018 年 rdr 独立小 RNA 分析既改善 MIRNA 注释又暴露新 siRNA 位点；2015 年苔藓研究显示陆生植物异染色质 siRNA 途径具有保守骨架但具体产物/因子背景不同。分类因此被当作可被遗传和比较证据修订的工作模型。

**Evidence.** `src-doi-10-1111-tpj-13919`; `src-doi-10-1105-tpc-15-00228`; two different species/genetic contexts. **Limitations:** 不能把 *Arabidopsis* rdr 诊断模式机械迁移到所有植物。 **Confidence:** medium-high. **Claim:** `claim-axtell-a-exceptions-revise-classification`.

### Finding AXT-A-F06 — 跨物种 miRNA 主张要求“界面富集—宿主靶向—演化相容”链条

**Finding.** *Cuscuta* 工作由宿主界面表达/富集与宿主转录本靶向起步，继而用靶位点补偿性变异检验长期相互作用，并追溯这些 trans-species MIRNA 的特殊 U6-like 启动子。这个路线比“在另一物种样本中检测到 reads”严格得多。

**Evidence.** `src-doi-10-1038-nature25027`; `src-doi-10-7554-elife-49750`; `src-doi-10-1093-plcell-koad076`; parasitic plant–host interfaces, cleavage/target and comparative/promoter evidence. **Limitations:** 这些结果是特定寄生植物体系，不能自动推广到膳食 RNA、所有跨界 RNA 或一般植物间转运。 **Confidence:** high. **Claim:** `claim-axtell-a-transspecies-chain`.

## Recurring methods and controls

- 明确位点/前体/成熟臂/具体序列层级，避免用 family 名称替代位点证据（`claim-axtell-a-entity-resolution`; sources: 2008/2018 criteria）。
- 将 sRNA-seq 的加工精度、双臂证据、长度分布、链偏向、重复性与相位性联合解释，而不是选一个最好看的参数（`claim-axtell-a-multiparameter-locus-profile`）。
- 靶标路线按 prediction → cleavage/reporter → genetics/rescue 升级，且每一级只支持相应直接性（`claim-axtell-a-target-evidence-ladder`）。
- 比较研究先审查采样、参考基因组和可检测性，再解释“缺失”或“新生”（`claim-axtell-a-conservation-calibrates-prior`）。
- 跨物种 reads 必须排查污染/组织混合，并需要受体效应系统与靶标证据（`claim-axtell-a-transspecies-chain`）。

## Candidate reasoning models

| candidate_id | model idea | two distinct contexts | distinctive | source_ids | disposition |
|---|---|---|---|---|---|
| `cand-axtell-a-01` | 身份优先的分层审查：先判 MIRNA 生物发生，再评靶标，再评表型 | 标准修订；rdr 突变体清理注释 | high | 2008/2018 criteria; TPJ 2018 | retain |
| `cand-axtell-a-02` | 多参数位点画像：加工、长度、链、重复、相位、遗传背景共同裁决 | ShortStack；苔藓/拟南芥遗传注释 | high | RNA 2013; Plant Cell 2015; TPJ 2018 | retain |
| `cand-axtell-a-03` | 比较证据校准先验：古老保守关系与短寿命位点采用不同证据门槛 | 跨陆生植物；*Arabidopsis* 属内 | medium-high | Plant Cell 2005; Plant Cell 2010 | retain |
| `cand-axtell-a-04` | 跨物种主张链：来源位点—界面表达—受体加载/靶向—演化补偿 | 2018 功能发现；2019 补偿；2023 启动子起源 | high | Nature 2018; eLife 2019; Plant Cell 2023 | retain |

## Historical changes

1. 2005–2010：以跨谱系保守性、降解组和近缘物种比较建立 miRNA/靶标与位点寿命框架。
2. 2013–2018：转向可复现的软件化注释、多参数分类及大数据时代标准收紧；遗传背景成为识别混杂 siRNA 的工具。
3. 2018–2023：在不降低证据门槛的前提下扩展到寄生植物 trans-species miRNA，从现象、靶点、共演化到启动子机制。

## Gaps and cautions

- 2013 Annual Review 仅按可公开摘要/元数据用于宏观分类，不据此声称正文中的具体实验细节。
- “专家主导”按第一、末位/通讯或明确标准共同作者记录；不把合著结果当作 Axtell 对每个句子的个人背书。
- 此来源集服务于框架提炼，不是完整书目；未纳入的论文不得据此被理解为不重要。
- 未在本轮完成每篇 correction/retraction 的专门数据库审计，后续 Citation Verifier 仍需独立检查。

## Quality self-check

- [x] 每项关键 finding 绑定 source_id 与 claim_id
- [x] 专家角色、物种、方法与直接性已区分
- [x] 搜索摘要未用于复杂实验细节
- [x] 未使用未授权全文，未下载原始数据
- [x] DOI/PMID 仅在官方书目或 PubMed 核验后保留
- [x] 专家框架、团队结果与 Agent 综合推断已分开

