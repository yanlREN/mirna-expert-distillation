# 06 — Research Timeline

## Metadata

```yaml
expert_id: blake-c-meyers
expert_name: Blake C. Meyers
dimension: 06-research-timeline
agent_role: read-only Research Agent C
run_id: run-20260717-1730-cst
started_at: 2026-07-18T02:42:00+08:00
completed_at: 2026-07-18T03:31:00+08:00
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope

This is a timeline of public research methods and questions, not a personal biography. It follows the transition from sequence-tag quantification to cleavage-end profiling and then to staged reproductive phasiRNA biology. It records where later work adds cell-type resolution, genetics or explicit uncertainty. The evidence window is 2001-2026, but the first directly verified Meyers publication anchor in this Agent C corpus is 2004; no unsupported 2001-2003 milestone is invented.

## Source Inventory

| source_id | year | type | expert role | species/context | access | verification |
|---|---:|---|---|---|---|---|
| `src-doi-10-1104-pp-104-039495` | 2004 | database/method resource | first | *Arabidopsis* MPSS | OA full text | verified |
| `src-doi-10-1038-nbt1417` | 2008 | primary research | coauthor | *Arabidopsis* PARE | abstract only | verified |
| `src-doi-10-1016-j-cub-2008-04-042` | 2008 | primary research | not author | independent degradome | OA full text | verified |
| `src-doi-10-1073-pnas-1418918112` | 2015 | primary research | corresponding | maize staged anthers | OA full text | verified |
| `src-doi-10-1093-bioinformatics-btu628` | 2015 | method | not author | plant PHAS calling | abstract only | verified |
| `src-doi-10-1186-s12864-017-4031-9` | 2017 | method/benchmark | not author | small-RNA annotation | OA full text | verified |
| `src-doi-10-1093-nar-gky609` | 2018 | method/critique | not author | degradome target rules | OA full text | verified |
| `src-doi-10-1038-s41467-020-16637-3` | 2020 | primary research | not author | rice anther wall | OA full text | verified |
| `src-doi-10-1038-s41467-020-19034-y` | 2020 | primary research | not author | rice male germ cells | OA full text | verified |
| `src-doi-10-1038-s41467-020-19922-3` | 2020 | primary research | not author | rice meiosis/fertility | OA full text | verified; 2023 author-name correction |
| `src-doi-10-1111-nph-17910` | 2022 | primary critique | not author | grass MIR2118/PARE | OA full text | verified |
| `src-doi-10-1002-tpg2-70107` | 2025 | primary research | senior | rice ten-stage anthers | OA full text | verified |

## Timeline of Methods and Questions

| interval | verified public anchor | technical or thematic move | what became possible | boundary retained |
|---|---|---|---|---|
| 2001-2003 | no Agent C source selected | field technology-development interval | not asserted here | first verified relevant anchor is 2004 |
| 2004 | `src-doi-10-1104-pp-104-039495` | quantitative MPSS signatures, database and reliability filters | digital comparison across libraries and genome positions | tag bias, uniqueness and annotation constrain interpretation |
| 2008 | `src-doi-10-1038-nbt1417`; `src-doi-10-1016-j-cub-2008-04-042` | sequencing uncapped RNA ends to discover cleavage | transcriptome-scale small-RNA target evidence | cleavage is not protein effect or phenotype causality |
| 2009-2014 | method maturation is represented indirectly by later benchmarks | computational pipelines and phasing/target categories become central | scalable PHAS and target surveys | tool rules and reference choice become explicit sources of error |
| 2015 | `src-doi-10-1073-pnas-1418918112`; `src-doi-10-1093-bioinformatics-btu628` | staged maize anthers plus PHAS-calling software | separation of premeiotic 21-nt and meiotic 24-nt waves; genome-scale candidate loci | anther stage, cell layer and genotype must accompany abundance |
| 2017-2018 | `src-doi-10-1186-s12864-017-4031-9`; `src-doi-10-1093-nar-gky609` | independent tool benchmarking and configurable PARE rules | direct testing of software sensitivity, background and targeting assumptions | computational agreement is not biological validation |
| 2020 | `src-doi-10-1038-s41467-020-16637-3`; `src-doi-10-1038-s41467-020-19034-y`; `src-doi-10-1038-s41467-020-19922-3` | independent rice cell-type, cleavage and genetic studies | somatic-wall/germ-cell separation; direct cleavage; meiotic and fertility perturbation | different experiments support different causal gates |
| 2022 | `src-doi-10-1111-nph-17910` | evolutionary comparison plus nonauthentic-sRNA controls | tests target-search false-positive pressure at large query scale | source is collaboration-linked and does not invalidate well-controlled targets |
| 2023 | correction linked to `src-doi-10-1038-s41467-020-19922-3` | publication-record correction | correct author metadata | correction changes an author spelling, not reported science |
| 2025 | `src-doi-10-1002-tpg2-70107` | ten-stage rice anther atlas, postmeiotic PHAS classes | extends the temporal map beyond the classic premeiotic/meiotic pair | biogenesis and function remain proposed/unresolved |
| 2026 cutoff | identity audit plus 2025 endpoint | current public scope remains plant small-RNA genomics, PARE and reproductive phasiRNAs | future tests can target postmeiotic function and cell-specific causality | no 2026 mechanism paper was needed or invented for currency |

## Findings

### Finding T1 — Quantification began with explicit filtering, not raw-count literalism

**Finding**  
The 2004 MPSS resource made normalization, signature reliability, genomic matching and library annotation part of the measurement.

**Why it matters**  
This provides an early public precedent for treating high-throughput counts as assay outputs that require mapping and quality context.

**Evidence**
- Source: `src-doi-10-1104-pp-104-039495`
- Expert role: first author
- Species/context: *Arabidopsis*, multiple MPSS libraries
- Method: MPSS database, normalization and filters
- Directness: direct for database/method design
- Independent support: not assessed here; Meyers-team anchor

**Attribution**  
Team method/resource result.

**Limitations**  
MPSS technology and contemporary genome annotations differ from current small-RNA sequencing.

**Confidence**  
High.

### Finding T2 — The target question shifted from prediction to transcriptome-scale cleavage evidence

**Finding**  
In 2008, PARE/degradome methods made cleavage-end capture scalable, with a Meyers-team study and concurrent external study converging on the same assay concept.

**Why it matters**  
The transition created a new directness tier between computational complementarity and complete functional causality.

**Evidence**
- `src-doi-10-1038-nbt1417`; Meyers coauthor; *Arabidopsis* inflorescence; PARE; direct for recovered cleavage ends.
- `src-doi-10-1016-j-cub-2008-04-042`; not author; *Arabidopsis* degradome; direct external support, conservatively collaboration-linked.

**Attribution**  
Multi-lab team result plus concurrent external method result.

**Limitations**  
Both studies are in *Arabidopsis* and focus on cleavage-compatible regulation.

**Confidence**  
High.

### Finding T3 — Reproductive phasiRNA research introduced stage and cell identity as core metadata

**Finding**  
The 2015 maize work divided 21-nt and 24-nt phasiRNA accumulation across developmental windows and cell-layer dependencies. Independent 2020 rice studies then separated somatic and germ-cell populations and added cleavage/genetic tests.

**Why it matters**  
The unit of interpretation became a species × stage × cell type × genotype combination, not simply “anther phasiRNA.”

**Evidence**
- `src-doi-10-1073-pnas-1418918112`; Meyers corresponding; maize; staged sRNA-seq, mutants, in situ.
- `src-doi-10-1038-s41467-020-16637-3`; strict independent; rice anther-wall CRISPR and imaging.
- `src-doi-10-1038-s41467-020-19034-y`; strict independent; purified rice male-germ-cell degradome.
- `src-doi-10-1038-s41467-020-19922-3`; strict independent; rice genetics, target tests and cytology.

**Attribution**  
Meyers/Walbot team discovery map plus independent rice extensions.

**Limitations**  
The studies do not imply that maize and rice loci or product sequences are orthologous.

**Confidence**  
High.

### Finding T4 — The recent frontier broadens the catalog while strengthening uncertainty language

**Finding**  
The 2025 rice anther series adds postmeiotic 21- and 24-nt PHAS classes and reports distinct accumulation, composition and phase registers, but treats mechanisms and functions as unresolved.

**Why it matters**  
The current frontier is no longer only discovery of two canonical reproductive waves; it includes testing newly catalogued classes without promoting patterns to mechanisms prematurely.

**Evidence**
- Source: `src-doi-10-1002-tpg2-70107`
- Expert role: senior/final author
- Species/context: Kitaake rice, ten developmental stages
- Method: histology, sRNA-seq, transcriptomics, PHAS/register analysis
- Directness: direct for accumulation/annotation; computational or inferential for mechanism
- Independent support: not yet established for the new postmeiotic classes in this source set

**Attribution**  
Meyers-team result.

**Limitations**  
Functional perturbation and phenotype rescue remain missing for most new classes.

**Confidence**  
High for the timeline endpoint and uncertainty boundary.

## Historical Changes and Corrections

1. **Measurement scale:** signature databases (2004) → uncapped-end target maps (2008) → staged/cell-type small-RNA maps (2015 onward).
2. **Causal depth:** abundance and phasing → direct cleavage → target-site and pathway perturbation → phenotype/cytology, with no assumption that one assay supplies all layers.
3. **Biological scope:** *Arabidopsis* quantitative genomics/PARE → maize reproductive phasiRNA staging → rice cell-type, target and fertility mechanisms → postmeiotic classes.
4. **Error model:** tag reliability and genomic uniqueness → target-rule dependence → phasing background/tool sensitivity → large-query PARE false positives.
5. **Publication status:** the 2020 rice meiotic-progression paper received a 2023 Author Correction for one author-name spelling (`src-doi-10-1038-s41467-023-37355-6`); no scientific correction was reported.

## Candidate Interrogation Heuristics

- Ask what the counting unit is: raw read, unique sequence, locus-normalized abundance, phase register, cleavage peak or biological replicate.
- Require species, assembly, anther length/cytology, cell type, genotype and library method before comparing reproductive phasiRNA abundance.
- Keep the ladder explicit: PHAS annotation → trigger evidence → phased-product production → AGO loading → target cleavage → target effect → phenotype causality.
- Treat 2025 postmeiotic classes as hypotheses for mechanism/function until independently perturbed.

These are timeline-derived candidate questions for later synthesis, not a completed Meyers reasoning model.

## Contradictions and Tensions

| tension | source A | source B | context difference | unresolved? |
|---|---|---|---|---|
| hundreds of phasiRNA cleavage targets vs false-positive pressure | `src-doi-10-1038-s41467-020-19034-y` | `src-doi-10-1111-nph-17910` | purified germ-cell/stage data versus large-query null controls | yes; requires matched nulls and genetic validation |
| classic two-wave model vs additional postmeiotic classes | `src-doi-10-1073-pnas-1418918112` | `src-doi-10-1002-tpg2-70107` | maize classic staging versus deeper rice temporal sampling | not a direct contradiction; scope expansion |
| somatic U-rich vs germline C-biased 21-nt phasiRNAs | `src-doi-10-1038-s41467-020-16637-3` | `src-doi-10-1038-s41467-020-19034-y` | cell layer and AGO context | context-dependent difference, not contradiction |

## Current Public Research Scope at Cutoff

The identity audit verifies a 2024 return to UC Davis and current Genome Center/Plant Sciences leadership. The latest verified research anchor in this corpus is the 2025 Kitaake rice anther study (`src-doi-10-1002-tpg2-70107`), which continues the reproductive-phasiRNA program while broadening it to postmeiotic classes. This statement concerns public institutional and publication records only; it is not a claim about private or unpublished priorities.

## Missing Evidence

- A selected 2001-2003 expert-authored anchor was not available in this dimension; the timeline therefore begins substantively in 2004.
- No strict independent functional study of the newly described postmeiotic classes was found by the cutoff.
- Current 2026 institutional scope is verified in the N0.5 identity audit, but no 2026 mechanism publication was required for this N1 timeline.

## Quality Self-check

- [x] Every key finding has a source ID
- [x] Author identity and role verified
- [x] Species and context recorded
- [x] News not used for mechanism
- [x] Search snippets not used as experimental evidence
- [x] No unauthorized full text
- [x] No fabricated identifiers
- [x] Team results separated from agent timeline synthesis
- [x] Correction status preserved
- [x] Evidence cutoff stated
