# Hailing Jin — 公开报告、问题响应与本人参与综述底稿

## 范围与证据等级

- `expert_id`: `hailing-jin`
- 负责维度：02（公开报告/问题响应）
- 机制证据截止：2026-07-17
- 本次检索日：2026-07-18（仅作为检索元数据；没有纳入截止日后的机制主张）
- 身份锚点：Hailing Jin、UCR、ORCID `0000-0001-5778-5193`，与 N0.5 审计一致。
- 重要降级：没有找到足以支撑“现场回答风格”的高质量、长期可访问 lecture/Q&A transcript。为避免用宣传采访或二手视频凑数，本维度以专家本人参与撰写的 review/perspective 和开放原始论文 Discussion 为主。它们能支持公开方法框架和不确定性语言，不能重建口语风格，也不能代表专家当前私人意见。

## 1. Source inventory

| Source ID | 年份 | 类型 / Jin 角色 | 公开内容用途 | 主要边界 |
|---|---:|---|---|---|
| HJ-C-S001 | 2015 | review / review author | 跨界 sRNA 对话的双向框架 | 综述，不是独立验证 |
| HJ-C-S002 | 2015 | review / review author | 植物免疫、病原毒力与 RNAi 的层次 | 将领域描述为尚待探索，不能后见之明抹去 |
| HJ-C-S003 | 2017 | perspective / review author | environmental RNAi 和作物保护愿景 | 应用前景不等于田间有效性 |
| HJ-A-S008 | 2016 | primary / senior | 外源 RNA 摄取、HIGS/SIGS 的实验证据 | Jin 团队；特定病原体系 |
| HJ-A-S009 | 2018 | primary / senior | TET8/9 EV、跨界递送、靶标和表型链 | Jin 团队；Arabidopsis–Botrytis |
| HJ-A-S010 | 2021 | primary / senior | RBP 与 TET8-positive EV 中 sRNA 选择/稳定 | 有 Publisher Correction；非所有 EV |
| HJ-A-S011 | 2021 | formal correction / senior | 出版状态守卫 | 官方通知说明错误 Supplementary Information 文件已被正确文件替换；不推断未陈述的结论变化 |
| HJ-C-S008 | 2023 | review / review author | 植物、微生物、哺乳动物 EV 比较和开放问题 | 跨类群只能作类比，不可默认保守 |

## 2. Response patterns

### Pattern A — 把“跨界 RNAi”拆成方向、载体和效应体系

- **Finding**：公开综述反复先问 RNA 从谁到谁，再问如何进入受体，最后问受体是否执行基因沉默；“病原→宿主”和“宿主→病原”被当作两个可分别成立的方向，而不是一句泛化的“RNA 能跨界”。
- **Why it matters**：面对新论文时，必须明确 donor、recipient、guide、recipient AGO/DCL、target 与 phenotype，不能仅凭另一物种样本中出现 reads 就升级为运输与功能。
- **Source ID**：HJ-C-S001、HJ-C-S002、HJ-C-S003、HJ-C-S008；结构化卡 HJ-C-C001、HJ-C-C002。
- **Source type / expert role**：专家参与综述 / review author。
- **Species / context**：植物–真菌为主，另用害虫、寄生物与哺乳动物系统作比较。
- **Evidence directness**：contextual；框架明确，机制事实需回到原始论文。
- **Limitations**：多作者综述不等于 Jin 对每句话的个人背书；跨系统类比不能自动变成保守机制。
- **Confidence**：高（公开框架），低（个体现场回答风格）。

### Pattern B — 从现象推进到机制时逐级增加控制

- **Finding**：Jin 团队的实证路线从双向小 RNA 现象，推进到外源 RNA 摄取，再到 EV 亚类与 RBP 装载；每一步都加入新的纯化、遗传和生化控制。
- **Why it matters**：对新主张应检查它停在哪一层：检测、富集、膜保护、进入受体细胞、AGO 结合、靶标直接性还是因果表型。
- **Source ID**：HJ-A-S008、HJ-A-S009、HJ-A-S010；卡 HJ-C-C004、HJ-C-C005、HJ-C-C006。
- **Source type / expert role**：原始研究 / senior author。
- **Species / context**：Arabidopsis–Botrytis、Arabidopsis EV。
- **Evidence directness**：direct within reported systems；不是独立重复。
- **Limitations**：同一研究网络连续深化不能替代外部实验室验证；任何一步的成功都不能替代下一步。
- **Confidence**：高。

### Pattern C — 以应用可设计性表述前景，但需把愿景与部署证据分开

- **Finding**：2017 perspective 使用积极的应用语言，把 HIGS/SIGS 视为可设计、可扩展的作物保护路线。
- **Why it matters**：这是该公开研究项目的重要方法偏好；但 Lens 应把它标成 `expert_position`，并另外询问田间剂量、稳定性、雨淋、递送、非靶标、耐受演化和法规。
- **Source ID**：HJ-C-S003；独立边界 HJ-B-S013、HJ-B-S014；卡 HJ-C-C003、HJ-C-C015、HJ-C-C016。
- **Source type / expert role**：专家 perspective + 外部原始研究。
- **Species / context**：Botrytis、Fusarium、植物叶片与收获后表面。
- **Evidence directness**：perspective contextual；独立实验 direct but pre-field。
- **Limitations**：离体叶片、切割子叶鞘和收获后组织不是多地点田间试验。
- **Confidence**：高。

### Pattern D — 对机制未知使用显式的“仍不清楚/仍待发现”

- **Finding**：2015–2023 的公开综述没有把路线图写成完成图；对 RNA 选择、不同 EV 亚类、受体摄取和跨类群共性保留未知。
- **Why it matters**：面对证据空缺时应保留 `unknown`，而不是用机制图中的箭头代替实验。
- **Source ID**：HJ-C-S001、HJ-C-S002、HJ-A-S010、HJ-C-S008。
- **Source type / expert role**：review + primary Discussion。
- **Species / context**：多系统比较、Arabidopsis EV。
- **Evidence directness**：explicit uncertainty statements in public literature。
- **Limitations**：发表后的新工作可能解决部分问题；必须以证据截止日为准逐条更新。
- **Confidence**：高。

## 3. Uncertainty language

建议在最终 Lens 中保留的中性表达（是本项目转述，不是模拟专家原话）：

1. “在该物种对和感染时间窗内，现有数据支持/不支持……”
2. “该结果证明了 EV 富集，但尚未单独证明进入受体效应体系。”
3. “该 guide–target 关系仍需要受体 AGO 关联、靶位点抗性或等价直接性证据。”
4. “外源 RNA 在这一真菌中可被摄取，不能外推为所有真菌均可摄取。”
5. “实验室或离体组织保护是部署前证据，不等于田间有效性。”
6. “跨类群结果在此仅作 analogous/uncertain transfer，不标记为 conserved。”
7. “本结论来自 Jin 团队公开研究框架，不代表专家本人当前意见。”

## 4. Recurrent questions

### Q1. donor RNA 的身份可靠吗？

- 是 miRNA family、具体 MIR locus、5p/3p、isomiR、siRNA，还是降解片段？
- 是否有 precursor/miRNA*、精确加工与重复证据？
- 在混合感染样本中，序列能否唯一分配到 donor assembly？

### Q2. 如何排除样本污染与组织混样？

- 是否有未感染组织与“感染后混合”对照？
- 受体细胞是否经独立纯化；是否检测 donor 细胞/叶绿体/核 RNA 污染指标？
- RNA 是否在完整受体细胞内部，而非黏在细胞壁、囊泡表面或纯化杂质中？

### Q3. EV 证据到哪一步？

- 是粗离心颗粒、密度分级、膜保护、marker-positive fraction，还是 immunocapture 的特定 EV 亚类？
- 是否同时测量非囊泡 extracellular RNA/RNP？
- EV 富集是否与功能递送、受体摄取和靶标调控分别验证？

### Q4. 受体是否具备摄取与 RNAi 能力？

- 外源 dsRNA/sRNA 是否真正进入完整受体细胞？
- 受体 DCL/AGO 是否表达、被装载并对表型必要？
- 阴性病原是否因为不能摄取、缺少扩增、时间窗不匹配或 RNAi 丢失？

### Q5. 靶标直接性达到什么级别？

- 计算预测或反相关（F1/F2）不能替代 AGO association、PARE/5′ RACE、reporter、靶位点抗性或 rescue（F3/F4）。
- 多重预测产生的显著下调需要 multiplicity-aware null 和病原负荷/组织比例控制。

### Q6. 表型是否真由这条 guide–target 边导致？

- DCL/AGO 或 EV 通路突变是否多效？
- 靶基因删除导致低毒力不等于该 guide 在野生型感染中的作用已被证明。
- 靶位点抗性、等位基因 rescue 或互补是否把分子边连接到病害表型？

### Q7. 应用是否越过 proof-of-concept？

- 递送剂量、持续时间、雨淋、紫外、温度、叶面屏障、病原窗口、重复施用、制剂和成本是否测试？
- 是否有温室、田间、多地点、多季节和非靶标数据？

## 5. Candidate interrogation heuristics

1. **方向先行**：先写 donor → recipient，再谈“cross-kingdom”。
2. **六闸门**：origin/clean sampling → extracellular association → intact-cell uptake → recipient RISC → direct target → causal phenotype。
3. **EV 不跳级**：富集≠包封；包封≠运输；运输≠受体摄取；摄取≠RNAi；RNAi≠完整表型因果。
4. **双基因组 mapping 守卫**：报告 assembly、唯一性、多重比对政策、序列长度和同源区；超短 reads 尤其谨慎。
5. **病原能力先验不得通用化**：以目标物种的摄取与 DCL/AGO 数据为准。
6. **正负结果按情境并存**：Botrytis/Verticillium 正结果与 Zymoseptoria 负结果是适用范围信息，不用票数抹平。
7. **应用证据分级**：分子作用、离体/温室病害控制、田间有效性、生态安全分别报告。
8. **出版状态结伴**：HJ-A-S010 必须与 HJ-A-S011 一起携带并使用替换后的 Supplementary Information；通知未陈述的影响仍不得猜测。

## 6. Missing evidence

- 缺少高质量、可核验的公开 lecture Q&A transcript，因此不能声称掌握专家面对现场质疑时的口头节奏、措辞或个人立场变化。
- 对不少 guide–target 边，外部实验室的同体系、同时间窗、同遗传设计重复仍有限。
- 对植物 EV 中 AGO/RBP 的定位，独立植物实验室需要以同等纯化和免疫捕获强度复核；哺乳动物 EV 结果只能作方法类比。
- SIGS 仍需要公开的多环境田间有效性、剂量–反应、持久性、非靶标和抗性演化证据后，才能从“有潜力”升级为部署结论。
- 2021 Publisher Correction 已确认替换错误 Supplementary Information 文件；这不等于通知声明了撤稿或特定结论改变。2013 Science 论文的 2025 erratum 内容仍不可合法核实，图级复用保持受限。

## 7. 本维度结论

公开资料足以提炼“方向—递送—效应体系—靶标—表型”的可执行问题分解方式，以及对 environmental RNAi 的公开应用偏好；不足以复刻人物语言或把合作论文写成个人口述。建议 N2 将这些内容作为候选 interrogation model，与 Agent C 的独立正反证据一起验证，而不是单独据此标记为专家独特且科学已确认的机制。
