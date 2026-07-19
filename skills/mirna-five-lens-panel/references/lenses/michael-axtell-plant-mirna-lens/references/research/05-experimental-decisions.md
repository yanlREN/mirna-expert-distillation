# 05 — Experimental and Annotation Decisions: Michael J. Axtell

## Metadata

```yaml
expert_id: michael-j-axtell
expert_name: Michael J. Axtell
dimension: 05-experimental-decisions
agent_role: Research Agent B
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope

Each case is reconstructed from public papers and expressed as `Context → Competing explanations → Decision → Evidence → Outcome → Generalizable heuristic → Failure condition`. “Decision” denotes a documented team or criteria-paper choice, not a claim about Axtell's private intent. Target cleavage, miRNA identity, and phenotype causality are kept separate.

## Case 1 — Make precise precursor processing the primary plant-miRNA gate

**Context.** Deep sequencing exposed very large, diverse plant small-RNA populations, including abundant siRNAs, while annotation practices varied.

**Competing explanations.** A candidate read from a foldback might be a bona fide miRNA/miRNA* product, an siRNA from a long dsRNA/inverted repeat, or a degradation fragment that happens to overlap a predicted hairpin.

**Decision.** The 2008 consensus criteria made precise excision of a miRNA/miRNA* duplex from a qualifying single-stranded stem-loop the necessary and sufficient core criterion; ancillary target or conservation evidence was not allowed to substitute for processing.

**Evidence.** The paper specifies duplex geometry, stem constraints, locus-wide precision, and explains why one or two reads cannot exclude heterogeneous processing. Source: `src-doi-10-1105-tpc-108-064311`; claim: `claim-axtell-b01`.

**Outcome.** Candidate evaluation moved from “hairpin plus small RNA” to a locus-level processing test.

**Generalizable heuristic.** When the negative/background class is biologically abundant, define the positive class by its causal biogenesis signature rather than by superficial shape or function.

**Failure condition.** The rule cannot be applied confidently without a correct genomic/precursor sequence and adequate sRNA sampling; low coverage warrants an unresolved status.

**Attribution.** Explicit multi-laboratory consensus; Axtell was a coauthor, not the sole originator. A more specific correspondence role is not asserted here without a dedicated author-note verification.

## Case 2 — Tighten the annotation gate for big-data false positives

**Context.** Ten years of large sRNA-seq datasets produced many questionable plant MIRNA annotations.

**Competing explanations.** A candidate may satisfy the older local hairpin/precision checks in one library yet reflect a rare stochastic pattern, a 24-nt siRNA locus, or a homology-only projection.

**Decision.** The 2018 revision required sRNA-seq, biological replication for novel annotations, provisional status for homology-only calls, and especially strong evidence for 23–24-nt candidates; it also limited implausibly long foldbacks and emphasized false-positive minimization.

**Evidence.** Side-by-side revision of the 2008 criteria and discussion of plant siRNA base rates. Source: `src-doi-10-1105-tpc-17-00851`; claims: `claim-axtell-b02`, `claim-axtell-b03`.

**Outcome.** The default moved from accepting incomplete annotations to explicit provisional/rejected categories.

**Generalizable heuristic.** Scale evidence thresholds with both dataset size and the prevalence of confounding classes; replication guards against library-specific artifacts.

**Failure condition.** These thresholds prioritize specificity and may miss truly expressed, tissue-restricted, or very low-abundance MIR loci when appropriate libraries are unavailable.

**Attribution.** Explicit Axtell–Meyers criteria paper.

## Case 3 — Use RDR dependency to audit database MIRNA records, without making it a one-test identity proof

**Context.** miRBase21 contained 325 Arabidopsis MIRNA loci, only a subset labeled high-confidence.

**Competing explanations.** Suspect records could be true MIRNAs, RDR-dependent siRNAs overlapping predicted hairpins, or too low/variable for classification.

**Decision.** Sequence three biological replicate libraries from wild-type Col-0 and `rdr1-1/rdr2-1/rdr6-15` inflorescences, then test database loci for dependence on the major RDRα enzymes expected for many siRNAs but not canonical hairpin miRNAs.

**Evidence.** Fifty-eight annotated MIRNA loci were significantly downregulated in the triple mutant; 52 of 58 were 24-nt dominated. Another 118 were ambiguous because counts/variance prevented reliable inference. Source: `src-doi-10-1111-tpj-13919`; claims: `claim-axtell-b04`, `claim-axtell-b05`.

**Outcome.** The team proposed that the 58 RDR-dependent records were not true MIRNAs while preserving low-information cases as ambiguous. Thirty-eight RDR1/2/6-independent non-hairpin loci were left unclassified rather than forced into a known class.

**Generalizable heuristic.** Choose mutants that test a class-defining precursor pathway; use the result primarily to exclude incompatible identities, and retain an indeterminate bin.

**Failure condition.** RDR independence is not sufficient for MIRNA identity, and residual/redundant pathways or tissue-specific effects can complicate negative results.

**Attribution.** Team result in Polydore and Axtell; the category logic is consistent with the criteria papers.

## Case 4 — Refuse PHAS calls that pass algorithms but fail biological coherence

**Context.** Several phasing algorithms repeatedly called 24-nt-dominated Arabidopsis loci as PHAS loci; the genome contains very many 24-nt hc-siRNA loci.

**Competing explanations.** The candidates could be genuine 24-nt phasiRNA loci or abundant hc-siRNA loci producing chance in-register reads.

**Decision.** Test multiple orthogonal expectations: repeatability of the same dominant phase register across libraries, RDR6 versus RDR2/Pol IV pathway dependence, miRNA-trigger evidence (including MIR2275), genomic context, and a known TAS2 positive control. Extend the audit to four other eudicots lacking evident MIR2275 homologs.

**Evidence.** Algorithm-passing Arabidopsis candidates lacked consistent phase registers and expected triggers/dependencies; comparable false positives appeared in Brassica rapa, cucumber, common bean, and potato. Source: `src-axtell-31245701`; claims: `claim-axtell-b06`, `claim-axtell-b07`.

**Outcome.** The study concluded that no true 24-nt PHAS loci were supported in Arabidopsis and that phasing-score algorithms alone can misclassify abundant 24-nt loci.

**Generalizable heuristic.** A defining periodic pattern must recur in the same register and cohere with pathway genetics; algorithm agreement is not independent biological replication.

**Failure condition.** A genuinely noncanonical PHAS pathway could violate known dependencies or triggers; rejecting it requires saying which novel evidence would overturn the classification.

**Attribution.** Team result in Polydore, Lunardon, and Axtell.

## Case 5 — Build a locus evidence vector rather than a miRNA-only pipeline

**Context.** Many organisms produce diverse small-RNA genes; MIRNA loci may be a minority, so a miRNA-only discovery pipeline can hide alternative classifications.

**Competing explanations.** A read cluster may be MIRNA, another hairpin RNA, phased siRNA, hc-siRNA, or an unclassified locus; read counts alone cannot separate them.

**Decision.** ShortStack was designed to annotate de novo loci and report size distribution, strandedness, repetitiveness, hairpin association, MIRNA status, phasing, and abundance from genome-aligned sRNA-seq data.

**Evidence.** Performance was demonstrated on four plants (Arabidopsis, tomato, rice, maize) and three animals with class-relevant outputs rather than a single score. Source: `src-doi-10-1261-rna-035279-112`; claim: `claim-axtell-b08`.

**Outcome.** Annotation became an inspectable evidence vector, enabling later criteria updates and cross-species standardization.

**Generalizable heuristic.** Preserve intermediate features and alternative labels so reviewers can audit why a locus was classified.

**Failure condition.** Outputs inherit reference-assembly, alignment, library, and parameter errors; software classification is not experimental validation.

**Attribution.** Sole-author method paper; this is the clearest individual methodological source in this set.

## Case 6 — Resolve multi-mapping with tested local context, not random choice or blanket deletion

**Context.** sRNA-seq contains many reads with multiple genomic matches, common around duplicated MIR loci and repetitive siRNA loci.

**Competing explanations.** Randomly place reads (higher apparent sensitivity, low precision), discard multimappers (higher apparent precision, low sensitivity), or infer likely origin from neighboring unique reads.

**Decision.** Develop local genomic weighting, test it on simulated datasets from Arabidopsis, rice, and maize, and compare real-data results using MIR paralogs and known-origin 24-nt siRNAs; impose a default high-multiplicity cutoff rather than pretend every read is placeable.

**Evidence.** Local weighting outperformed common alternatives in simulation and biological comparisons. Source: `src-axtell-27175019`; claim: `claim-axtell-b09`.

**Outcome.** The method was incorporated into ShortStack with uncertainty-aware handling of high-multiplicity reads.

**Generalizable heuristic.** For ambiguous mappings, benchmark precision and sensitivity using both simulation and orthogonal biological truth sets.

**Failure condition.** Local weighting fails when the true locus lacks informative neighboring unique reads, the assembly collapses repeats, or all paralogs have indistinguishable contexts.

**Attribution.** Team method result; Axtell was senior/corresponding author.

## Case 7 — Use degradome data both for target cleavage and precursor-processing inference

**Context.** Degradome sequencing captures uncapped, polyadenylated RNA 5′ ends and was developed mainly to find sliced small-RNA targets.

**Competing explanations.** Peaks can reflect miRNA/siRNA-guided target cleavage, ordinary RNA decay, or cleavage intermediates from MIR precursor processing.

**Decision.** Analyze position-specific degradome signals against predicted target sites and MIR hairpin structure, rather than treating every peak as a target-cleavage event.

**Evidence.** In Physcomitrium patens, the study identified sliced targets and found MIR319 hairpin remnants consistent with precise loop-first processing. Source: `src-axtell-19850910`; claim: `claim-axtell-b10`.

**Outcome.** One assay yielded two distinct inference types, separated by sequence/structural context.

**Generalizable heuristic.** Interpret a molecular readout through all biological processes that can create it; use positional context to distinguish them.

**Failure condition.** Degradome capture is biased toward stable uncapped/polyadenylated products; absence of a peak does not exclude cleavage, and a peak alone does not establish phenotype causality.

**Attribution.** Team result; Axtell was senior/corresponding author.

## Case 8 — Quantify plant miRNA targeting at RNA and protein levels with site-specific controls

**Context.** Complementarity rules predict many plant miRNA targets, but sequence-pairing scores do not directly quantify repression and cannot distinguish RNA-level from protein-level effects.

**Competing explanations.** A sensor change may be caused by genuine target-site-dependent repression, altered coding sequence/protein properties, transcript abundance effects, or experimental variation.

**Decision.** Use N. benthamiana agroinfiltration with a firefly-luciferase sensor and Renilla internal control; measure qRT-PCR and dual-luciferase activity from the same samples; for coding-region sites, construct a distinct synonymous negative control with disrupted complementarity.

**Evidence.** The assay compared perfect and natural target sites and observed variable efficacy, while controlling target-site sequence effects. Source: `src-doi-10-1105-tpc-113-120972`; claims: `claim-axtell-b11`, `claim-axtell-b12`.

**Outcome.** Targeting became a quantitative, site-dependent phenotype at both mRNA and protein levels rather than a binary complementarity prediction.

**Generalizable heuristic.** A direct-target test should perturb only the proposed interaction and assay the molecular levels relevant to the claimed mechanism.

**Failure condition.** Transient N. benthamiana leaves may not reproduce endogenous stoichiometry, tissue context, chromatin, or long-term phenotypes in another species.

**Attribution.** Team result; Axtell was senior/corresponding author.

## Case 9 — Standardize cross-species annotation but retain `nearMIRNA`

**Context.** Public sRNA-seq datasets from many plants differ in depth, tissue, assembly quality, and prior annotation conventions.

**Competing explanations.** A foldback with a dominant small RNA but no sequenced miRNA* might be a true low-coverage MIRNA, another hairpin RNA, or an annotation artifact.

**Decision.** Apply one locus-centric pipeline across 47 plants and reserve `MIRNA` for loci meeting all criteria; use `nearMIRNA` for loci meeting most criteria but lacking the exact predicted miRNA* read.

**Evidence.** The resource annotated about 2.7 million sRNA-producing loci from 48 assemblies and explicitly separated MIRNA from nearMIRNA. Source: `src-axtell-32179590`; claim: `claim-axtell-b13`.

**Outcome.** Comparative analyses gained consistent categories without silently upgrading incomplete evidence.

**Generalizable heuristic.** Use harmonized definitions for comparison, but preserve an evidence-gap category so missing data are not converted into false certainty.

**Failure condition.** `nearMIRNA` is not a fixed biological class; new tissue-specific libraries may promote or reject a locus, and assembly differences can change precursor reconstruction.

**Attribution.** Team resource result; Axtell was senior/corresponding author.

## Cross-case synthesis

| recurring decision | cases | evidence of recurrence | expert-framework status |
|---|---|---|---|
| Define classes by biogenesis and locus pattern | 1, 3, 5, 9 | criteria, genetics, software, comparative resource | strong |
| Raise thresholds where the background class is enormous | 2, 3, 4 | questionable MIRNAs and 24-nt PHAS false positives | strong |
| Convert algorithm outputs into biological hypotheses | 4, 5, 6 | phasing, annotation, mapping | strong |
| Preserve provisional/unclassified categories | 2, 3, 9 | homology-only, low-information, nearMIRNA | strong |
| Match assay to claim layer | 7, 8 | processing/cleavage versus targeting efficacy | medium; field-general but repeatedly operationalized |

## Decision anti-patterns

- Accepting a database record as experimental validation.
- Accepting a predicted foldback without locus-wide processing evidence.
- Counting algorithm agreement as independent biological support.
- Calling a 24-nt locus PHAS without a stable phase register and pathway context.
- Assigning multi-mappers randomly without reporting the choice.
- Calling a degradome cleavage peak a complete phenotype mechanism.
- Calling a complementarity score a validated target.
- Forcing low-information loci into familiar classes instead of preserving `nearMIRNA`, ambiguous, or unclassified status.

## Quality self-check

- [x] Nine cases use the required decision-chain structure.
- [x] Each case binds source IDs and claim IDs.
- [x] Team results are not presented as private individual opinions.
- [x] Species, genotype, methods, and failure conditions are explicit.
- [x] miRNA identity, target directness, and phenotype causality remain separate.
- [x] No raw sequence data or restricted full text were downloaded.
- [x] Search snippets were not used as sole support for experimental detail.
