# 03 — Scientific Reasoning DNA

## Metadata

```yaml
expert_id: blake-c-meyers
expert_name: Blake C. Meyers
dimension: 03-scientific-reasoning-dna
agent_role: read-only Research Agent B / Agent 3
run_id: run-20260717-1730-cst
started_at: 2026-07-18T02:08:00+08:00
completed_at: 2026-07-18T02:34:00+08:00
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope

This dimension extracts recurring evidence-upgrade and boundary-setting actions from verified Meyers-authored or coauthored publications, plus one clearly marked independent laboratory test. It does not infer private views, assign every team statement to Meyers, or synthesize a final Skill. The central audit question is how a sequencing-scale observation is moved—or deliberately not moved—through class identity, trigger/biogenesis, molecular action and phenotype causality.

## Source Inventory

| source_id | year | type | expert role | species/context | access | verification |
|---|---:|---|---|---|---|---|
| `src-doi-10-1038-nbt1417` | 2008 | primary | coauthor | Arabidopsis PARE | abstract only | DOI/PMID verified |
| `src-doi-10-1101-gad-177527-111` | 2011 | primary | senior | legume NB-LRR phasiRNAs | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1105-tpc-114-131847` | 2014 | primary | corresponding | soybean atlas | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1073-pnas-1418918112` | 2015 | primary | corresponding | maize anther cell/stage | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1093-jxb-erw361` | 2016 | primary | senior | rice reproductive stages | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1073-pnas-1619159114` | 2016 | primary | coauthor | rice PMS1T/photoperiod | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1105-tpc-17-00851` | 2018 | author review | review author | land-plant miRNA criteria | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1038-s41467-019-08543-0` | 2019 | primary | senior | angiosperm comparison | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1038-s41467-020-16634-6` | 2020 | primary | corresponding | maize DCL5/temperature | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1038-s41467-020-19034-y` | 2020 | primary | not author | independent rice male germ-cell cleavage | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1093-plphys-kiad654` | 2024 | primary | coauthor | rice cleavage/fertility | abstract only | DOI/PMID verified |
| `src-doi-10-1073-pnas-2402285121` | 2024 | primary | senior | Zea premeiotic 24-nt class | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1073-pnas-2504349122` | 2025 | primary | senior | durum wheat DCL5 | OA full text | DOI/PMID/PMCID verified |
| `src-doi-10-1002-tpg2-70107` | 2025 | primary | senior | ten-stage rice anther atlas | OA full text | DOI/PMID/PMCID verified |

## Default Assumptions

### Finding F1 — A sequencing pattern starts as a class or locus candidate, not a mechanism

**Finding.** Across the soybean atlas, comparative reproductive-phasiRNA studies and the newest rice staging work, abundance, phase register, size and genomic clustering are used to define candidate classes. Target action and biological function remain separate questions. The 2025 rice paper explicitly leaves newly observed postmeiotic classes as a foundation for functional studies.

**Why it matters.** This is the default null needed when reviewing a paper that discovers thousands of loci: the null is structured transcription/processing without an established trigger, effector, target or phenotype.

**Evidence.** `src-doi-10-1105-tpc-114-131847` (corresponding/team result; soybean; small-RNA atlas and phasing; direct for accumulation, computational for target predictions); `src-doi-10-1038-s41467-019-08543-0` (senior/team result; comparative angiosperms; direct for distribution); `src-doi-10-1002-tpg2-70107` (senior/team result; staged Kitaake anthers; direct for class accumulation).

**Attribution.** Recurring team practice; cross-source framing is an Agent inference.

**Limitations.** Discovery papers differ in assembly quality, sampling depth and stage alignment.

**Confidence.** High for recurrence; medium for expert distinctiveness.

### Finding F2 — The evidence ladder is layered, not a single “validation” label

**Finding.** The recurring layers are: (1) locus/class identity, (2) trigger or biogenesis, (3) molecular action such as cleavage, and (4) phenotype causality. PARE directly supports a cleavage boundary but not phenotype; a Dicer mutant supports pathway requirement but not the target of every product; a mapped fertility locus can support phenotype causality without assigning every phased product a target.

**Why it matters.** It prevents two common plant-small-RNA errors: equating PARE with full causal explanation and equating a PHAS locus with a validated regulatory network.

**Evidence.** `src-doi-10-1038-nbt1417` (coauthor/team; PARE cleavage discovery); `src-doi-10-1073-pnas-1619159114` (coauthor/team; rice genetic/transgenic fertility context); `src-doi-10-1038-s41467-020-16634-6` (corresponding/team; multiple dcl5 alleles plus temperature); `src-doi-10-1073-pnas-2402285121` (senior/team; trigger-negative premeiotic class).

**Attribution.** Agent-derived candidate framework recurring across team papers; not an explicit quotation.

**Limitations.** Individual papers do not necessarily name the same ladder.

**Confidence.** High for recurrence and generative utility; medium for distinctiveness pending N2 comparison.

## Evidence Thresholds

### Finding F3 — miRNA identity uses a false-positive-minimizing threshold

**Finding.** The 2018 two-author criteria paper explicitly prioritizes replicated small-RNA sequencing, precise hairpin processing and separation from the much larger endogenous-siRNA space. A predicted hairpin or database record is not enough.

**Why it matters.** It creates a hard stop before downstream target and phenotype reasoning: if identity is weak, later evidence cannot retroactively make a locus a miRNA.

**Evidence.** `src-doi-10-1105-tpc-17-00851` (review author; land plants; explicit criteria and false-positive audit).

**Attribution.** Explicit author position shared with Michael J. Axtell.

**Limitations.** This framework is jointly authored and should not be portrayed as unique to Meyers. Genuine low-expression loci may remain unresolved.

**Confidence.** High.

### Finding F4 — A trigger-to-PHAS claim needs register-aware linkage

**Finding.** In the NB-LRR study, 22-nt miRNA targeting, cleavage evidence and phased secondary production form a chain. In the 2024 Zea study, negative trigger evidence led the team not to force a miRNA trigger onto a DCL5-dependent premeiotic 24-nt class.

**Why it matters.** It converts “there is a predicted miRNA site near phased reads” into a testable chain: cleavage position, phase offset/register, dependency and alternative initiation.

**Evidence.** `src-doi-10-1101-gad-177527-111` (senior/team; legumes; small-RNA plus PARE); `src-doi-10-1073-pnas-2402285121` (senior/team; Zea; small-RNA, nanoPARE and mutant/AGO comparisons); `src-doi-10-1073-pnas-2504349122` (senior/team; wheat; AU-rich motif and nanoPARE).

**Attribution.** Team results; cross-context candidate model is Agent inference.

**Limitations.** Negative cleavage evidence depends on assay sensitivity and sampled stage.

**Confidence.** High for recurrence, medium-high for distinctiveness.

## Preferred Triangulation

### Finding F5 — Molecular, spatial and genetic evidence are deliberately combined

**Finding.** The stronger causal studies combine small-RNA measurement with orthogonal evidence: cell/stage resolution in maize, multiple mutant alleles and temperature regimes for maize DCL5, or genetics, rescue, nanoPARE and single-cell profiles in wheat.

**Why it matters.** Each axis removes a different alternative explanation: bulk-tissue averaging, allele-specific background, environmental conditionality, cleavage ambiguity or developmental delay.

**Evidence.** `src-doi-10-1073-pnas-1418918112` (corresponding/team; laser-captured maize anther cell types); `src-doi-10-1038-s41467-020-16634-6` (corresponding/team; four CRISPR alleles plus a transposon allele, cytology and temperature); `src-doi-10-1073-pnas-2504349122` (senior/team; wheat genetics, single-allele restoration, nanoPARE and single-cell RNA-seq).

**Attribution.** Recurring experimental design across Meyers-associated teams.

**Limitations.** These packages still do not validate every individual phasiRNA target.

**Confidence.** High.

## False-positive Defenses

1. **Entity stop:** preserve MIR locus, precursor, mature product, PHAS precursor and phased products as different entities (`src-doi-10-1105-tpc-17-00851`).
2. **Replication stop:** a singleton or unreplicated small-RNA pattern does not meet confident miRNA criteria (`src-doi-10-1105-tpc-17-00851`).
3. **Phase stop:** require a statistically supported phase register and record how multimapping/repeats and assembly influence the locus call (`src-doi-10-1105-tpc-114-131847`; `src-doi-10-1002-tpg2-70107`).
4. **Trigger stop:** a predicted site is not a demonstrated trigger; align cleavage/degradome evidence with the register and dependency (`src-doi-10-1101-gad-177527-111`).
5. **Negative-trigger stop:** do not force canonical miRNA initiation when nanoPARE, AGO loading and cis-cleavage evidence are negative (`src-doi-10-1073-pnas-2402285121`; `src-doi-10-1073-pnas-2504349122`).
6. **PARE stop:** cleavage evidence is direct for the cut but not for full phenotype causality (`src-doi-10-1038-nbt1417`; independent recurrence `src-doi-10-1038-s41467-020-19034-y`).
7. **Bulk-tissue stop:** whole-anther signal cannot identify the producing or responding cell type (`src-doi-10-1073-pnas-1418918112`).
8. **Environment stop:** a molecular defect with a temperature- or photoperiod-dependent phenotype must retain the environmental condition (`src-doi-10-1073-pnas-1619159114`; `src-doi-10-1038-s41467-020-16634-6`).

## Transfer Boundaries

### Tissue and stage

Premeiotic 21-nt, premeiotic 24-nt, meiotic 24-nt and candidate postmeiotic cohorts are not interchangeable. Anther length must be tied to genotype and growth conditions. Evidence from purified male germ cells should not be generalized to somatic anther wall cells without localization (`src-doi-10-1073-pnas-1418918112`; `src-doi-10-1038-s41467-020-19034-y`; `src-doi-10-1002-tpg2-70107`).

### Species and lineage

Presence across angiosperms supports distribution, not conserved targets or identical biogenesis (`src-doi-10-1038-s41467-019-08543-0`). Maize and durum wheat both show DCL5-linked thermosensitive male fertility, but wheat adds an AU-rich, miRNA-independent initiation mode; transfer therefore requires retesting trigger, dosage/homeolog and temperature response (`src-doi-10-1038-s41467-020-16634-6`; `src-doi-10-1073-pnas-2504349122`).

### Assembly and repeats

PHAS-locus boundaries, coding overlap and multimapping are assembly-dependent. A phase statistic can support ordered processing, but repeated reads or a register peak do not alone determine locus identity or function. The assembly and mapping policy must accompany any cross-species locus claim (`src-doi-10-1105-tpc-114-131847`; `src-doi-10-1002-tpg2-70107`).

## Uncertainty Language

The corpus recurrently distinguishes evidence levels with language equivalent to:

- “identified/accumulated/phased” for direct sequencing observations;
- “supports/is required in the tested background” for genetic dependency;
- “likely not triggered/not loaded/not capable” for negative mechanistic inference bounded by assay sensitivity (`src-doi-10-1073-pnas-2402285121`);
- “suggesting diverse mechanisms” and “foundation for further functional studies” when class discovery outruns function (`src-doi-10-1002-tpg2-70107`);
- “critical under tested growth regimes” rather than universal fertility causality (`src-doi-10-1038-s41467-020-16634-6`).

## Candidate Distinctive Models

| candidate_id | model idea | two or more contexts | distinctive? | source_ids | failure condition | disposition |
|---|---|---|---|---|---|---|
| B-RD1 | Layered evidence escalation: discovery → identity → trigger/biogenesis → molecular action → phenotype | Arabidopsis PARE; rice PMS1T; maize DCL5; Zea trigger-negative class | medium-high | `src-doi-10-1038-nbt1417`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2402285121` | becomes generic if not operationalized with class-specific stops | retain for synthesis testing |
| B-RD2 | Phase-chain audit: cleavage position/register/dependency must cohere; allow noncanonical initiation | legume NB-LRR; Zea premeiotic 24-nt; durum wheat AU-rich motif | high | `src-doi-10-1101-gad-177527-111`, `src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122` | fails when only target prediction or phasing score is available | retain |
| B-RD3 | Spatiotemporal deconvolution before function | maize cell-type atlas; rice germ-cell degradome; ten-stage Kitaake atlas | medium-high | `src-doi-10-1073-pnas-1418918112`, `src-doi-10-1038-s41467-020-19034-y`, `src-doi-10-1002-tpg2-70107` | fails when material cannot be staged or cell composition changes | retain |
| B-RD4 | Environment-conditioned genetics separates molecular necessity from phenotypic penetrance | rice PMS1T photoperiod; maize DCL5 temperature; wheat DCL5 temperature | high | `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122` | fails if environment and sibling controls are absent | retain |
| B-RD5 | Comparative presence first, function only after lineage-specific mechanism tests | broad angiosperm survey; Zea class; wheat DCL5 | medium | `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122` | collapses into generic caution without explicit trigger/AGO/target tests | downgrade candidate heuristic if not distinctive in N2 |

## Generic Principles to Exclude

- “Use multiple methods” without naming which alternative each method excludes.
- “Correlation is not causation” without separating cleavage, biogenesis dependency and phenotype rescue.
- “More replication is better” without the miRNA-specific precise-processing and false-positive criteria.
- “Context matters” without specifying species, assembly, tissue/cell type, stage, genotype and environment.
- “Validate computational predictions experimentally” without a trigger-register or cleavage-location audit.
- “Be cautious across species” without testing whether trigger, Dicer/AGO usage and fertility conditionality are conserved.

These are scientifically sound but too generic to become expert-specific models unless tied to the recurring, source-backed decision structures above.

## Contradictions and Tensions

| tension | source A | source B | context difference | unresolved? |
|---|---|---|---|---|
| canonical miRNA-triggered reproductive PHAS versus miRNA-independent initiation | `src-doi-10-1101-gad-177527-111` | `src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122` | PHAS class, species and developmental stage | resolved as class-specific, not a universal conflict |
| broad distribution versus conserved function | `src-doi-10-1038-s41467-019-08543-0` | `src-doi-10-1002-tpg2-70107` | phylogenetic survey versus within-species stage atlas | function remains unresolved for many classes |
| severe molecular depletion versus conditional fertility | `src-doi-10-1038-s41467-020-16634-6` | same source across temperatures | molecular defect is stable; phenotypic penetrance varies | downstream buffering mechanism unresolved |
| cleavage is direct versus phenotype is incomplete | `src-doi-10-1038-nbt1417`, `src-doi-10-1038-s41467-020-19034-y` | `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1093-plphys-kiad654` | molecular target assay versus genetic/environmental causal chain | target-by-target phenotype attribution remains uneven |

## Missing Evidence

- Only abstract-level access was used for `10.1038/nbt1417` and `10.1093/plphys/kiad654`; no figure-level claims from those papers were retained.
- Author contribution statements were not available uniformly; “senior” marks final-author position plus identity continuity, not sole responsibility.
- The independent-laboratory source supports the cleavage hierarchy, but a full independent replication map belongs to dimension 04.
- Whether B-RD1–B-RD5 are distinctive relative to the other five locked experts must be decided by the independent synthesis stage.

## Quality Self-check

- [x] Every key finding has a source ID.
- [x] Author identity and role were verified; `Meyers BC` was never used alone.
- [x] Species, tissue/stage and environmental contexts are recorded where claims require them.
- [x] Search snippets were used only for discovery; evidence derives from PubMed/PMC metadata, abstracts and legal OA text.
- [x] No unauthorized full text or raw sequencing data was downloaded.
- [x] DOI/PMID/PMCID were verified through NCBI official metadata.
- [x] Expert/team findings, independent evidence and Agent inference are separated.
- [x] Conflicts and negative evidence are preserved.

