# 02 — 学术报告与问题响应：Michael J. Axtell

## Metadata

```yaml
expert_id: michael-j-axtell
expert_name: Michael J. Axtell
dimension: talks_and_responses
agent_role: research_agent_a
run_id: run-20260717-1730-cst
completed_at: 2026-07-17
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Source inventory

| source_id | year | source | expert role | access | permitted inference |
|---|---:|---|---|---|---|
| `src-url-psu-sternberg-lecture-2023` | 2023 | Penn State, “Small but Mighty: MicroRNAs in Plants” | named public lecturer | official announcement; no recording/transcript located | title, planned scope, high-level research trajectory only |
| `src-url-unl-small-rna-seminar-2014` | 2014 | University of Nebraska–Lincoln, “Discovery and Functional Analysis of Plant Small Silencing RNAs” | invited seminar speaker | official event notice; no recording/transcript located | title and discovery→functional-analysis framing only |
| `src-url-imba-microsymposium-2011` | 2011 | IMBA 6th Microsymposium on Small RNAs, “Evolutionary perspectives on small RNA biogenesis and functions in plants” | listed plant-session speaker | official archived program PDF; no transcript | title and explicit evolutionary framing only |

## Evidence limitation / downgrade

本轮没有找到可核验的公开视频、逐字稿或 Q&A。因此不能声称 Axtell 在现场如何回答质疑、使用了哪些即兴类比、或如何措辞不确定性。三项来源是原始机构活动记录，足以确认报告主题，但不是报告内容证据。以下“响应模式”主要由报告题目与本人/团队的公开 perspective/review/标准论文交叉提炼，均标为 **strongly consistent** 或 **agent inference**，不标为现场原话。

补充讨论来源：`src-doi-10-1146-annurev-arplant-050312-120043`、`src-doi-10-1105-tpc-17-00851`、`src-doi-10-1016-j-pbi-2019-03-014`。最后一项是 Axtell 合著 perspective/review，专门讨论 *Cuscuta* trans-species miRNA 的起源、证据与未决问题。

## Response patterns

### Finding AXT-T-F01 — 把问题拆成发现、分类、功能三个阶段

2014 报告题目明确连接“Discovery and Functional Analysis”；论文体系则显示中间还必须经过身份/类别判定。可复用响应是先问候选如何被发现、何以属于 miRNA 而非 siRNA/片段、随后才问直接靶标与表型因果。**Attribution:** title-supported framing + strongly consistent synthesis, not a transcript quote. **Sources:** `src-url-unl-small-rna-seminar-2014`, `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1016-j-cub-2008-04-042`. **Claim:** `claim-axtell-talk-discovery-classification-function`. **Confidence:** medium-high.

### Finding AXT-T-F02 — 用演化问题暴露“同名即同源”的偷换

2011 报告明确以 evolution 同时审视 biogenesis 和 function；2005、2010 比较研究显示，序列保守、位点同源、靶标保守和功能保守是不同命题。面对跨物种主张，候选 interrogation 应要求明确 assembly、位点共线性/起源、加工证据和靶标关系。**Attribution:** talk-title supported + publication triangulation. **Sources:** `src-url-imba-microsymposium-2011`, `src-doi-10-1105-tpc-105-032185`, `src-doi-10-1105-tpc-110-073882`. **Claim:** `claim-axtell-talk-evolution-separates-homology-levels`. **Confidence:** medium-high.

### Finding AXT-T-F03 — 公开叙事从一般植物 small RNA 扩展到跨物种调控，但证据门槛未被省略

2023 公共讲座公告回顾 miRNA 发现/表征方法，并把寄生植物 trans-species miRNA 与未来作物工具列为后续方向。公告明确把未来利用写成未来尝试，不能写成已经实现的技术。**Attribution:** explicit official announcement for scope; agent inference for methodological continuity. **Sources:** `src-url-psu-sternberg-lecture-2023`, `src-doi-10-1038-nature25027`, `src-doi-10-7554-elife-49750`, `src-doi-10-1093-plcell-koad076`. **Claim:** `claim-axtell-talk-expansion-with-boundary`. **Confidence:** high for stated scope, medium for inferred response style.

## Uncertainty language recoverable from written discussion

- 标准论文倾向用“criteria”“evidence”“misannotation”等可检验术语，不用名望或数据库收录替代证据（`claim-axtell-a-identity-before-function`）。
- 对跨物种 RNA，perspective 将 origins、function 和未决机制分开；这支持把“检测到”“被受体 AGO 利用”“有直接靶标”“导致表型”分别报告（`claim-axtell-talk-transspecies-uncertainty-ladder`; `src-doi-10-1016-j-pbi-2019-03-014`）。
- 对未来应用，2023 公告使用前瞻性语义；应保留“attempting to use”这一状态而非升格为已验证作物改良（`claim-axtell-talk-expansion-with-boundary`）。

## Recurrent questions / candidate interrogation heuristics

1. 你说的是 MIR locus、precursor、成熟 5p/3p product，还是仅一个数据库名称？
2. 精确加工与 miRNA/miRNA* 证据能否排除 siRNA、tRF/rRNA 片段和随机降解？
3. 该靶标只有互补预测，还是有降解组/5′RACE、reporter、AGO 或遗传 rescue？
4. “跨物种”读段能否排除界面组织混合或污染，并证明受体效应系统中的功能？
5. 跨物种同名是否有位点起源/同源证据，还是仅成熟序列相似？
6. 结论是当前数据支持的机制，还是未来应用设想？

## Missing evidence

- 未找到报告录像、幻灯、Q&A 或可信 transcript；因此 response cadence、现场措辞和“被质疑时如何回答”均不可直接蒸馏。
- 机构活动公告是 S3 主题证据，不能单独支持复杂机制。
- 后续若找到原始录像，应逐段核对来源、日期与上下文，只保留短摘录，并将本稿的 agent inference 与 explicit statement 分栏更新。

## Quality self-check

- [x] 三项报告均来自主办机构原始页面/归档节目单
- [x] 无 transcript 时未臆造问答或引语
- [x] 报告主题与论文机制证据分开
- [x] 每个重要 finding 有 source_id 与 claim_id
- [x] 明确将该维度降级为 `complete_with_limitations`

