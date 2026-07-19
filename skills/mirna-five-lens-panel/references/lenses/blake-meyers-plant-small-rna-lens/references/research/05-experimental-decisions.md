# 05 — Experimental Decisions

## Metadata

```yaml
expert_id: blake-c-meyers
expert_name: Blake C. Meyers
dimension: 05-experimental-decisions
agent_role: read-only Research Agent B / Agent 5
run_id: run-20260717-1730-cst
started_at: 2026-07-18T02:08:00+08:00
completed_at: 2026-07-18T02:34:00+08:00
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope

The cases below reconstruct only source-visible decision logic. They are team decisions unless an author-written review explicitly states a criterion. Each case uses the required sequence and ends with a failure condition so that a future Skill cannot turn a context-limited result into a universal rule.

## Decision Case 1 — Move target discovery from prediction to cleavage-end evidence

**Context.** Conventional plant miRNA target discovery relied heavily on sequence complementarity and subsequent one-target-at-a-time validation in Arabidopsis.

**Competing explanations.** A complementary transcript may be a real cleavage target; alternatively, it may be a prediction false positive, translationally regulated, or unrelated to the observed RNA ends.

**Decision.** Sequence polyadenylated RNA 5-prime ends genome-wide with PARE and include an AtXRN4-deficient library to enrich cleavage remnants.

**Evidence.** Expected cleavage-position signatures were recovered for validated and previously predicted targets; the mutant library increased detectability (`src-doi-10-1038-nbt1417`; coauthor/team result; Arabidopsis inflorescence; PARE; direct for cleavage location).

**Outcome.** PARE became a discovery-to-direct-molecular-evidence bridge, not a phenotype assay.

**Generalizable heuristic.** When target prediction is the bottleneck, profile the biochemical product of the proposed action and align its position to the proposed guide.

**Failure condition.** Stop at “cleavage-supported” if tissue/stage abundance, background degradation, target-site genetics or phenotype evidence are absent. Do not call a complete causal mechanism.

## Decision Case 2 — Reject weak plant miRNA annotations despite plausible hairpins

**Context.** Deep sequencing produced many candidate plant miRNA annotations, but endogenous siRNAs vastly outnumber true miRNAs.

**Competing explanations.** Reads on a foldable region may reflect a precisely processed MIR precursor or an siRNA-producing/inverted-repeat locus sampled by chance.

**Decision.** Require replicated small-RNA sequencing and precise, plausible hairpin processing; prioritize specificity and invalidate candidates that fit the siRNA alternative better.

**Evidence.** The updated two-author criteria explicitly emphasize replication and false-positive minimization and illustrate valid/invalid loci (`src-doi-10-1105-tpc-17-00851`; review author; land plants; explicit expert position).

**Outcome.** Database presence and predicted structure are demoted from validation to candidate support.

**Generalizable heuristic.** Test class identity before inferring targets: locus structure plus reproducible product geometry must exclude the dominant competing class.

**Failure condition.** If biological material is too limited to observe the star product or replication, report “candidate/unresolved”; do not compensate with target plausibility or conservation alone.

## Decision Case 3 — Establish a miRNA-triggered PHAS chain at NB-LRR genes

**Context.** Numerous legume NB-LRR transcripts produced phased secondary siRNAs and contained conserved sites for abundant 22-nt miRNAs.

**Competing explanations.** The miRNAs could merely bind NB-LRRs; phasing could arise independently; or conserved coding motifs could inflate computational matches.

**Decision.** Combine small-RNA phase analysis, conserved trigger-site placement and PARE-supported cleavage to connect 22-nt miRNA action to phased secondary production.

**Evidence.** Three abundant 22-nt families targeted conserved NB-LRR domains and were associated with phased trans-acting siRNA production (`src-doi-10-1101-gad-177527-111`; senior/team result; Medicago/soybean; small-RNA sequencing plus PARE; direct for chain components).

**Outcome.** The paper supported a gene-family regulatory architecture, while immune/symbiotic phenotype implications remained broader interpretations.

**Generalizable heuristic.** For a trigger claim, demand coherence among cleavage coordinate, phase offset/register, phased-product accumulation and pathway dependency.

**Failure condition.** A predicted trigger site plus a significant phasing score is insufficient if cleavage/register alignment or dependency is absent; PARE does not by itself prove phenotype causality.

## Decision Case 4 — Resolve whole-anther signal into cell type and developmental stage

**Context.** Reproductive phasiRNAs were abundant in maize anthers, but bulk data could not show where premeiotic and meiotic cohorts accumulated.

**Competing explanations.** The two size classes might be co-produced in the same cells, reflect changing cell composition, or mark distinct developmental compartments.

**Decision.** Pair precise anther staging with laser capture/cell-type sampling, small-RNA sequencing and localization rather than adding more bulk libraries alone.

**Evidence.** Premeiotic and meiotic phasiRNA accumulation was dynamic and cell-type dependent (`src-doi-10-1073-pnas-1418918112`; corresponding/team result; maize; cell-resolved sequencing/localization; direct for distribution).

**Outcome.** Stage and cell type became mandatory metadata for interpreting reproductive phasiRNA abundance.

**Generalizable heuristic.** When a tissue changes composition rapidly, deconvolve the compartment before assigning biogenesis, mobility or function.

**Failure condition.** Spatial enrichment does not identify targets or fertility mechanism; anther length cannot be transferred across genotype and environment without calibration.

## Decision Case 5 — Separate evolutionary presence from conserved function

**Context.** 24-nt reproductive phasiRNAs had been characterized mainly in grasses, inviting a claim of either grass specificity or universal angiosperm function.

**Competing explanations.** The pathway may be grass-specific, broadly distributed with conserved function, or repeatedly present with divergent triggers/effectors.

**Decision.** Survey reproductive small-RNA datasets across angiosperms and call distribution first, without requiring a universal target or phenotype claim.

**Evidence.** 24-nt reproductive PHAS loci were reported broadly across angiosperms (`src-doi-10-1038-s41467-019-08543-0`; senior/team result; comparative small-RNA/phasing; direct for detected distribution).

**Outcome.** Broad evolutionary presence was supported, while function remained a lineage- and context-specific test.

**Generalizable heuristic.** In comparative genomics, make “present,” “homologous biogenesis” and “conserved function” three separate verdicts.

**Failure condition.** Do not infer shared targets, AGO loading or fertility roles from size, motif or PHAS-locus presence alone; record assembly and stage mismatches.

## Decision Case 6 — Use multiple alleles and environmental regimes to parse DCL5 causality

**Context.** Maize DCL5 was proposed to generate meiotic 24-nt phasiRNAs, whose organismal role was unclear.

**Competing explanations.** A single allele could have background effects; phasiRNA loss might be noncausal; or fertility penetrance might depend on environment.

**Decision.** Test four CRISPR-derived alleles plus a transposon allele, quantify 24-nt phasiRNAs, inspect anther cytology and compare permissive/restrictive temperature regimes with sibling controls.

**Evidence.** Mutants had near-complete loss of the relevant phasiRNAs and abnormal anther/tapetal development, while male fertility varied with temperature; changing temperature did not restore the molecular small-RNA deficit (`src-doi-10-1038-s41467-020-16634-6`; Meyers and Walbot corresponding/team; maize; genetics, small-RNA sequencing, cytology and treatment; direct).

**Outcome.** DCL5 requirement and temperature-conditioned phenotypic penetrance were separated.

**Generalizable heuristic.** When a phenotype is conditional, hold the molecular lesion constant across environments and ask where the causal chain becomes buffered or exposed.

**Failure condition.** Do not infer the direct target of any 24-nt phasiRNA from DCL5 loss, and do not generalize a greenhouse temperature threshold to other genotypes or crops.

## Decision Case 7 — Purify the responding cell population before declaring phasiRNA targets

**Context.** Reproductive 21-nt phasiRNAs were abundant, but targets and action mode were obscured in bulk rice reproductive tissue.

**Competing explanations.** They could slice targets in germ cells, act in somatic layers, or have no detectable cleavage role.

**Decision.** Profile staged purified male germ cells and perform sensitive degradome sequencing alongside pathway mutants.

**Evidence.** The independent Qi laboratory detected cleavage of coding and transposon targets, especially in early prophase-I meiocytes (`src-doi-10-1038-s41467-020-19034-y`; not Meyers-authored; rice; purified cells, small-RNA and degradome sequencing; direct for cleavage).

**Outcome.** The molecular cleavage mode gained independent support in a spatially matched context, but target-by-target fertility causality remained incomplete.

**Generalizable heuristic.** A negative bulk degradome result should prompt cell/stage matching before rejecting target action.

**Failure condition.** This source is independent validation, not an expert-authored framework statement; cleavage counts must not be converted into universal phenotypic importance.

## Decision Case 8 — Accept a noncanonical PHAS initiation model when trigger evidence is negative

**Context.** A premeiotic 24-nt class in Zea resembled meiotic 24-nt phasiRNAs in genomic origin and DCL5 dependence, but the canonical miRNA-trigger model was uncertain.

**Competing explanations.** The class could be miRNA triggered like canonical reproductive PHAS loci, arise through an unobserved trigger, or use a different initiation mechanism.

**Decision.** Compare five maize inbreds and three teosinte taxa, test DCL5 dependency, query nanoPARE cleavage, compare AGO18 association and examine cis-cleavage potential.

**Evidence.** The class was DCL5 dependent yet reported as likely not miRNA triggered, not AGO18 loaded and not cis-cleaving (`src-doi-10-1073-pnas-2402285121`; senior/team result; Zea plus rice reanalysis; small-RNA, nanoPARE and genetic/AGO comparisons).

**Outcome.** The team defined a distinct class rather than forcing all 24-nt reproductive phasiRNAs into one canonical model.

**Generalizable heuristic.** Shared size and Dicer dependency do not guarantee shared initiation or effector; negative trigger evidence can justify class separation.

**Failure condition.** Use “likely” for negative mechanistic conclusions because assay sensitivity, stage and untested AGOs may leave alternatives open.

## Decision Case 9 — Test crop transfer with homolog dosage, rescue and motif mechanism

**Context.** Maize dcl5 thermosensitive sterility suggested a potentially conserved cereal mechanism, but durum wheat is tetraploid and could use different initiation rules.

**Competing explanations.** Wheat DCL5 could be dispensable because of homeolog redundancy; sterility could be unrelated to phasiRNAs; or maize-style miRNA triggering could be conserved.

**Decision.** Create/compare DCL5 homeolog genotypes, test a single functional allele for rescue, measure phasiRNAs across temperatures, use nanoPARE and motif analysis, and inspect cell states with cytology/single-cell RNA-seq.

**Evidence.** DCL5 loss depleted 24-nt phasiRNAs and caused thermosensitive sterility, one functional allele restored fertility, and premeiotic biogenesis was reported as miRNA independent and associated with an AU-rich motif (`src-doi-10-1073-pnas-2504349122`; senior/team result; durum wheat; genetics, rescue, small-RNA, nanoPARE and single-cell/cytology; direct for tested axes).

**Outcome.** A conserved DCL5/fertility requirement coexists with a crop-specific dosage and initiation analysis.

**Generalizable heuristic.** Transfer a mechanism by decomposing it into ortholog/homeolog requirement, environmental penetrance, trigger, effector and rescue—not by transferring a pathway label.

**Failure condition.** Conserved DCL5 dependence does not prove conserved individual targets or the proposed AGO effectors; candidate effector claims require direct loading/action evidence.

## Decision Case 10 — Stop a newly discovered stage class before overclaiming function

**Context.** Ten-stage Kitaake anther profiling revealed postmeiotic 21- and 24-nt PHAS groups beyond the two historically emphasized reproductive classes.

**Competing explanations.** These could be distinct functional pathways, shifted tails of known cohorts, mapping/annotation effects or stage-specific processing products.

**Decision.** Use biological replication, abundance clustering, nucleotide composition and register analysis to define candidates, while explicitly framing functional interpretation as future work.

**Evidence.** Distinct postmeiotic accumulation and register patterns were observed (`src-doi-10-1002-tpg2-70107`; senior/team result; Kitaake rice; staged small-RNA sequencing and computational phasing; direct for observation, not function).

**Outcome.** Discovery was preserved without inventing targets or effectors.

**Generalizable heuristic.** A new class may be publication-worthy while its mechanism remains unresolved; make the stopping point explicit.

**Failure condition.** Coexpression, nucleotide bias or a register peak cannot establish biogenesis protein, AGO loading, target cleavage or fertility role.

## Cross-case Heuristics

- **IF** sequencing discovers a class, **THEN** ask which separate assay supports identity, trigger, action and phenotype, **BECAUSE** none substitutes for the others, **UNLESS** the requested conclusion is explicitly limited to discovery.
- **IF** a PHAS trigger is proposed, **THEN** align cleavage coordinate and phase register and test dependency, **BECAUSE** complementarity and phasing can coexist by chance or through another initiator, **UNLESS** it remains labeled a computational hypothesis.
- **IF** PARE is positive, **THEN** call the cut direct but keep phenotype unresolved, **BECAUSE** molecular directness and organismal causality are different axes.
- **IF** anther small RNAs vary, **THEN** stage and deconvolve cell type before inferring mobility or function, **BECAUSE** tissue composition changes rapidly.
- **IF** a mutant has conditional fertility, **THEN** measure the molecular lesion under each environment, **BECAUSE** phenotypic rescue may occur downstream without molecular restoration.
- **IF** a cereal mechanism is transferred, **THEN** retest trigger, Dicer/AGO, homeolog dosage and environment, **BECAUSE** conserved class names can hide distinct initiation and effectors.

## Negative Results and Model Changes

- The absence of restored 24-nt phasiRNAs at permissive temperature in maize narrowed temperature action to a downstream or parallel buffering step rather than molecular rescue (`src-doi-10-1038-s41467-020-16634-6`).
- Negative nanoPARE/AGO18/cis-cleavage evidence prompted a noncanonical premeiotic 24-nt class rather than a forced miRNA-trigger model (`src-doi-10-1073-pnas-2402285121`).
- Wheat nanoPARE plus motif evidence further revised the assumption that premeiotic 24-nt phasiRNA biogenesis must be miRNA initiated (`src-doi-10-1073-pnas-2504349122`).
- The 2025 rice atlas deliberately stopped at class discovery and hypotheses when biogenesis and function were not directly tested (`src-doi-10-1002-tpg2-70107`).

## Limits and Attribution

- All original-paper decisions are team decisions. Author position and correspondence were recorded but do not confer sole attribution.
- `src-doi-10-1038-s41467-020-19034-y` is an independent-laboratory validation context, not a Meyers-authored result.
- The two abstract-only sources support only the limited claims explicitly present in their PubMed abstracts.
- These cases are inputs for later synthesis, not final Scientific Reasoning Models.

## Quality Self-check

- [x] Ten cases meet the required Context → Competing explanations → Decision → Evidence → Outcome → Generalizable heuristic → Failure condition format.
- [x] At least six cases combine a concrete experiment/control with a conclusion boundary.
- [x] Discovery, direct cleavage, biogenesis dependency and phenotype causality remain distinct.
- [x] Phasing statistics, repeats/mapping, miRNA triggers, PARE and transfer boundaries are explicitly audited.
- [x] No raw data, model weights or unauthorized full text were downloaded.
- [x] No final synthesis or expert impersonation was performed.

