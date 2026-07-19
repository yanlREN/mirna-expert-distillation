# 03 — Scientific Reasoning DNA: Michael J. Axtell

## Metadata

```yaml
expert_id: michael-j-axtell
expert_name: Michael J. Axtell
dimension: 03-scientific-reasoning-dna
agent_role: Research Agent B
evidence_cutoff: 2026-07-17
status: complete_with_limitations
impersonation: forbidden
voice: neutral_scientific
```

## Scope and attribution guard

This file extracts recurring reasoning moves from Axtell-authored primary studies, methods papers, and author-written reviews. It does not claim access to private beliefs and does not attribute every statement in a multi-author paper to Axtell personally. Labels used below are:

- **explicit framework**: an author-written review, criteria paper, or methods paper directly states the rule;
- **team result**: a coauthored primary study reports the result;
- **Agent inference**: a reusable procedure inferred from two or more public research contexts.

The strongest evidence for an Axtell-associated lens is the repeated combination of (i) biogenesis-first classification, (ii) an explicit false-positive budget, and (iii) classification by locus-level read patterns and genetic dependencies. Generic practices such as replication or use of negative controls are not treated as distinctive by themselves.

## Source inventory

| source_id | year | type | expert role | species/context | access/verification |
|---|---:|---|---|---|---|
| `src-doi-10-1105-tpc-108-064311` | 2008 | consensus criteria | coauthor | plants; MIRNA annotation | PMC; DOI/PMID/PMCID verified; conservative role label pending any explicit correspondence note |
| `src-doi-10-1105-tpc-17-00851` | 2018 | criteria/perspective | first, co-corresponding | plants; big-data annotation | PMC; DOI/PMID/PMCID verified |
| `src-doi-10-1146-annurev-arplant-050312-120043` | 2013 | sole-author review | sole author | plant small-RNA classes | PubMed abstract; DOI/PMID verified |
| `src-doi-10-1261-rna-035279-112` | 2013 | method/primary | sole, corresponding | seven plant/animal datasets; ShortStack | PMC; DOI/PMID/PMCID verified |
| `src-axtell-27175019` | 2016 | method/primary | senior/corresponding | Arabidopsis, rice, maize; multimappers | PMC; DOI/PMID/PMCID verified |
| `src-doi-10-1111-tpj-13919` | 2018 | primary | senior/corresponding | Arabidopsis inflorescence; rdr1/2/6 | publisher full text; DOI/PMID verified |
| `src-axtell-31245701` | 2018 | primary/method critique | senior/corresponding | Arabidopsis plus four eudicots; PHAS calls | PMC; DOI/PMID/PMCID verified |
| `src-axtell-32179590` | 2020 | primary/resource | senior/corresponding | 47 plant species; standardized annotations | PMC; DOI/PMID/PMCID verified |
| `src-doi-10-1105-tpc-113-120972` | 2014 | primary/method | senior/corresponding | Nicotiana benthamiana transient targeting assay | PMC; DOI/PMID/PMCID verified |
| `src-axtell-19850910` | 2009 | primary | senior/corresponding | Physcomitrium patens degradome; MIR319 | PMC; DOI/PMID/PMCID verified |
| `src-doi-10-1105-tpc-105-032185` | 2005 | primary | first author | diverse land plants; conserved miRNAs/targets | PMC; DOI/PMID/PMCID verified |
| `src-axtell-21554756` | 2011 | review | first author | plant–animal comparison | PMC; DOI/PMID/PMCID verified |

## 1. Default assumptions

### D1 — The null hypothesis for a candidate plant miRNA is “another small-RNA product,” not “miRNA until disproved”

**Finding.** A hairpin prediction, database entry, DCL dependence, target prediction, or a few reads is not independently decisive. In plants, abundant endogenous siRNAs create many opportunities for chance hairpins, apparent local precision, and database carry-over. The positive identity claim is therefore earned by locus-level evidence for precise excision of a miRNA/miRNA* duplex from a qualifying single-stranded foldback.

**Evidence and recurrence.** The 2008 criteria define precise stem-loop processing as the central criterion; the 2018 revision explicitly responds to questionable annotations and emphasizes replication/minimization of false positives. The rdr1/2/6 study then uses a genetic-dependency test to show that 58 miRBase21 MIRNA annotations were RDR1/2/6-dependent and thus suspect, most being 24-nt dominated (`src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1111-tpj-13919`).

**Attribution.** Explicit framework in consensus/criteria papers; team result in the mutant study.

**Boundary.** RDR independence alone does not prove miRNA identity; it removes one major siRNA explanation. Conversely, an unresolved low-count locus should be called ambiguous, not automatically rejected.

### D2 — Classify the locus and its biogenesis before assigning a familiar RNA label

**Finding.** The recurring unit of reasoning is the producing locus plus precursor, read distribution, strandedness, dominant size, repetitiveness, phasing, and genetic dependence. A mature sequence name or length is insufficient.

**Evidence and recurrence.** The classification review separates hairpin-derived RNAs from dsRNA-derived siRNAs; ShortStack reports locus properties rather than only mature sequences; the 47-plant resource uses standardized locus categories and retains a `nearMIRNA` category when the predicted miRNA* is not sequenced (`src-doi-10-1146-annurev-arplant-050312-120043`, `src-doi-10-1261-rna-035279-112`, `src-axtell-32179590`).

**Attribution.** Explicit review/method framework; `nearMIRNA` is a team operational category.

**Boundary.** Locus classes are operational hypotheses constrained by the available assembly, sampled tissues, library depth, and annotation version.

### D3 — A computational score is a candidate generator; orthogonal biological expectations decide the class

**Finding.** Passing an algorithm is not equivalent to satisfying a biological definition. When a class is rare but the background class is enormous, chance positives are expected even under stringent-looking scores.

**Evidence and recurrence.** Multiple PHAS algorithms called 24-nt-dominated Arabidopsis loci, but the candidates lacked reproducible phase registers, appropriate genetic dependence, and an evident trigger; similar errors appeared in four additional eudicots. In miRNA annotation, predicted hairpins and database status are likewise subordinated to processing evidence and replication (`src-axtell-31245701`, `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1111-tpj-13919`).

**Attribution.** Team result plus explicit annotation framework.

**Boundary.** This is not a rejection of computation. Computation narrows the search; it does not independently establish biogenesis.

## 2. Evidence thresholds and conclusion upgrades

| proposed conclusion | minimum defensible upgrade | evidence that does **not** by itself upgrade | principal sources |
|---|---|---|---|
| “expressed small RNA” → “plant miRNA locus” | genome-mapped sRNA-seq showing a qualifying foldback and precise miRNA/miRNA* duplex processing, reproduced in at least two biological libraries under the 2018 criteria | hairpin prediction, database record, target prediction, Northern signal, DCL reduction alone | `src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851` |
| “homologous-looking locus” → “orthologous MIRNA” | actual sRNA-seq fulfillment of the criteria in the claimed species; otherwise provisional homology annotation | conserved mature sequence/name alone | `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1105-tpc-105-032185` |
| “phasing score” → “PHAS locus” | reproducible dominant phase register plus expected trigger/context and compatible genetic dependencies | one or several phasing algorithms passing | `src-axtell-31245701` |
| “predicted target” → “direct molecular interaction” | assay of repression/cleavage with an appropriate target-site control; RNA and protein measurements resolve mode/extent | complementarity score or inverse expression alone | `src-doi-10-1105-tpc-113-120972` |
| “degradome peak” → “cleavage/processing event” | position-specific uncapped end consistent with slicing or precursor processing and the relevant sequence context | target prediction alone | `src-axtell-19850910` |
| “direct target” → “phenotype causality” | target-site genetics/rescue or equivalent causal intervention | degradome/PARE cleavage alone | framework implication; not directly established by the cited target-discovery papers |

## 3. Preferred triangulation

### T1 — Structure × processing precision × replication

For identity claims, first reconstruct the precursor using the correct genome assembly; then inspect exact miRNA and miRNA* positions, duplex geometry, off-register reads, and strand pattern; finally demand biological-library replication for novel annotations. This triangulation recurs from the 2008 criteria to the 2018 revision and the 47-species resource (`src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-17-00851`, `src-axtell-32179590`).

### T2 — Algorithmic call × genetic dependency × locus biology

For siRNA subclass calls, combine score-based discovery with the mutant dependency expected for the proposed pathway, reproducibility of the defining pattern, genomic context, and trigger evidence. This is directly instantiated in the rdr1/2/6 cleanup and PHAS false-positive studies (`src-doi-10-1111-tpj-13919`, `src-axtell-31245701`).

### T3 — Sequence complementarity × quantitative reporter × molecular level

For targeting, use complementarity to design candidate sites, but compare a target sensor with a deliberately disrupted control and measure both mRNA and protein in the same biological material. The N. benthamiana dual-luciferase/qRT-PCR assay operationalizes this (`src-doi-10-1105-tpc-113-120972`).

### T4 — Comparative conservation × direct expression/processing evidence

Cross-lineage conservation can strengthen an orthology/evolution argument, but detection and conserved target relationships must be separated from assumptions based on family names. The 2005 study directly profiled multiple land-plant clades, whereas the 2018 criteria make homology-only annotations provisional (`src-doi-10-1105-tpc-105-032185`, `src-doi-10-1105-tpc-17-00851`).

## 4. False-positive defenses

1. **Base-rate awareness.** Ask how many background siRNA loci could pass the same rule by chance. This is especially important for 24-nt-dominated loci (`src-doi-10-1105-tpc-17-00851`, `src-axtell-31245701`).
2. **Reject local beauty without global locus coherence.** A small segment can look hairpin-like or precisely processed while the whole locus has an siRNA pattern (`src-doi-10-1111-tpj-13919`).
3. **Require biological replication rather than read multiplicity.** Thousands of PCR-amplified reads in one library do not substitute for independent libraries (`src-doi-10-1105-tpc-17-00851`).
4. **Audit multi-mappers.** Random placement inflates precision errors; discarding all multimappers sacrifices sensitivity. Local genomic weighting is a tested compromise, and high-multiplicity reads retain explicit uncertainty (`src-axtell-27175019`).
5. **Use positive controls and defining-pattern reproducibility.** TAS2 showed a stable phase register while false PHAS candidates did not (`src-axtell-31245701`).
6. **Preserve an “unclassified” bin.** The 38 RDR1/2/6-independent, non-hairpin loci were not forced into known classes (`src-doi-10-1111-tpj-13919`).
7. **Separate identity, targeting, and causality.** Annotation evidence establishes what RNA is produced; reporter/degradome evidence addresses molecular targeting; neither alone establishes phenotype causality (`src-doi-10-1105-tpc-108-064311`, `src-doi-10-1105-tpc-113-120972`, `src-axtell-19850910`).

## 5. Transfer and entity boundaries

- **Plant vs animal:** plant and animal miRNAs share broad Dicer/AGO logic but differ enough in biogenesis, precursor architecture, and targeting that animal seed/Drosha rules must not be imported as plant annotation rules (`src-axtell-21554756`).
- **Species:** a mature-sequence match supports homology discovery but does not prove a locus meets miRNA criteria in the second species; call such records provisional until species-specific sRNA-seq evidence exists (`src-doi-10-1105-tpc-17-00851`).
- **Family vs locus:** conservation of a family does not imply every named locus is orthologous or functional. Report family, locus, mature arm/sequence, and assembly separately (`src-doi-10-1105-tpc-105-032185`, `src-axtell-32179590`).
- **24-nt products:** most 24-nt plant sRNAs arise from abundant hc-siRNA biology; a 23–24-nt miRNA or 24-nt PHAS claim needs unusually strong, class-specific evidence (`src-doi-10-1105-tpc-17-00851`, `src-axtell-31245701`).
- **Assembly/mapping:** locus identity and paralog-specific abundance depend on the reference assembly and multi-mapper treatment (`src-doi-10-1261-rna-035279-112`, `src-axtell-27175019`).
- **Tissue/stage:** absence from a library is absence under the sampled context, not proof that a locus never produces the RNA. This limitation is especially important in cross-species resources assembled from heterogeneous public libraries (`src-axtell-32179590`).

## 6. Uncertainty language extracted as reusable forms

These are paraphrased, not quotations:

- “The data are compatible with X, but do not distinguish X from Y because the relevant precursor/dependency is unresolved.”
- “This annotation is provisional pending direct sRNA-seq support in the claimed species.”
- “The locus meets most criteria but lacks sequenced miRNA*; retain it as near-MIRNA rather than promote it.”
- “A reduction in a dcl mutant supports regulated biogenesis but does not categorically distinguish miRNA from endogenous siRNA.”
- “The observed association/cleavage supports a molecular interaction, not the complete phenotype-causal chain.”
- “No currently defined class fits; preserve the locus as unclassified and state what experiment would resolve it.”

## 7. Candidate distinctive models

| candidate_id | model idea | two or more contexts | distinctiveness | disposition |
|---|---|---|---|---|
| `cand-axtell-b01` | **Biogenesis-first identity gate**: require locus-level precise duplex production before using “miRNA” | 2008/2018 criteria; rdr mutant cleanup; 47-plant resource | high within plant annotation | core candidate |
| `cand-axtell-b02` | **Background-class false-positive audit**: estimate how abundant siRNAs can satisfy a score by chance, then add orthogonal gates | questionable MIRNAs; 24-nt PHAS calls | high | core candidate |
| `cand-axtell-b03` | **Locus evidence vector**: classify using size, strand, repetitiveness, hairpin, phasing, dependence, and mapping rather than one feature | ShortStack; RDR study; multi-mapper study | high | core candidate |
| `cand-axtell-b04` | **Provisional category instead of forced naming** | `nearMIRNA` across 47 plants; unclassified RDR-independent loci | medium-high | core/heuristic candidate |
| `cand-axtell-b05` | **Method-to-claim matching**: reporter/degradome/target prediction answer different questions | MIR319 degradome; quantitative target assay | medium; partly field-general | heuristic, not uniquely Axtell |
| `cand-axtell-b06` | **Cross-lineage conservation with entity discipline** | antiquity survey; homology-only provisional rule; plant–animal review | medium | heuristic/model candidate |

## 8. Generic principles to exclude from expert-specific models

- “Use controls,” “replicate experiments,” and “consider alternative explanations” are general scientific practice. They become lens-specific here only when tied to plant small-RNA base rates and concrete locus properties.
- “Correlation is not causation” is generic. The useful Axtell-linked instantiation is the explicit separation of miRNA identity, target cleavage/repression, and phenotype causality.
- “Use multiple methods” is generic. The distinctive pattern is which methods are triangulated: precursor structure, processing precision, miRNA*, locus-wide read geometry, genetic dependency, and mapping ambiguity.
- The I3/F4 evidence scales are project-level synthesis, not terminology used by the source papers.

## 9. Limitations and confidence

- The criteria and review papers support explicit framework claims; primary-study decision chains remain team results.
- Some source metadata were verified through NCBI while experimental detail was taken only from legal PMC/publisher pages. No restricted full text or raw sequence data were downloaded.
- The 2005 conservation work predates current nomenclature and genome resources; its comparative conclusion should not be used to assign modern locus orthology without rechecking assemblies.
- Confidence: **high** for the annotation/false-positive framework; **medium** for claiming individual methodological preferences from multi-author primary studies.

## Quality self-check

- [x] Every key finding has source IDs.
- [x] Expert role and team attribution are separated.
- [x] Species, genotype, assembly, or method context is stated where decision-relevant.
- [x] Search snippets were used only for discovery; claims rely on PubMed metadata and legal PMC/publisher content.
- [x] No unauthorized full text or raw sequencing data were used.
- [x] No identifier was guessed.
- [x] Generic principles are excluded from distinctive models.
- [x] Failure conditions and unresolved categories are preserved.
