# Scientific Reasoning Models — Blake C. Meyers Lens Candidate

```yaml
expert_id: blake-c-meyers
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
phase: N2
model_count: 5
```

These are operational syntheses from public research, not statements by Blake C. Meyers and not evidence of his current personal views. Coauthored papers are treated as team results. Each model passed recurrence in at least two distinct scientific contexts, prospective usefulness, and distinctiveness beyond generic research caution. `field_consensus`, `expert_position`, `contested`, `historical`, `hypothesis`, and `agent_inference` remain separate.

## Model M1 — Layered small-RNA evidence escalation

model_id: MEYERS-M1

```yaml
name: discovery_to_identity_to_biogenesis_to_action_to_phenotype
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
recurrence_test: passed
generative_test: passed
distinctiveness_test: passed_when_small_rna_specific_gates_are_retained
source_ids:
  - src-doi-10-1105-tpc-114-131847
  - src-doi-10-1038-nbt1417
  - src-doi-10-1073-pnas-1619159114
  - src-doi-10-1038-s41467-020-16634-6
  - src-doi-10-1073-pnas-2402285121
claim_ids:
  - claim-meyers-b-layered-escalation-candidate
  - claim-meyers-a-soybean-multiaxis-annotation
  - claim-meyers-a-pare-cleavage-not-phenotype
  - claim-meyers-a-pms1t-causality-with-unknown-downstream
  - claim-meyers-a-dcl5-genetics-temperature-boundary
  - claim-meyers-a-premeiotic-24nt-negative-evidence-calibrated
```

### Two distinct recurrence contexts

1. In soybean discovery/annotation, PHAS calling, trigger evidence, tissue accumulation, and predicted targets were kept as separate axes (`src-doi-10-1105-tpc-114-131847`; `claim-meyers-a-soybean-multiaxis-annotation`).
2. In reproductive genetics, rice PMS1T and maize DCL5 studies connected locus/pathway perturbation to fertility while retaining unresolved downstream targets or environmental penetrance (`src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`; `claim-meyers-a-pms1t-causality-with-unknown-downstream`, `claim-meyers-a-dcl5-genetics-temperature-boundary`). PARE and Zea negative-trigger work independently delimit intermediate gates.

### Procedure

1. Fix the entity and context: species, assembly, tissue/cell type, developmental stage, genotype, treatment, library, MIR locus/precursor or PHAS locus, mature product, and mapping policy.
2. State the assay-level observation only: mapped reads, reproducible processing, phase register, trigger-compatible cleavage, pathway dependency, AGO association, target cleavage, protein effect, or phenotype.
3. Place the observation on separate gates: discovery; identity/class; trigger/biogenesis; molecular action; phenotype causality.
4. List the next gate's required assay and at least one alternative explanation. Do not let evidence at a downstream gate retroactively validate an upstream identity.
5. Upgrade only the gate directly supported. Report all other gates as `supported`, `partially_supported`, `unsupported`, `conflicting`, or `not_tested`.
6. Preserve context and transfer boundaries in the conclusion.

### Upgrade thresholds

- Discovery to class/identity: biological replication, stable locus/precursor definition, mapping/mappability controls, and class-appropriate processing or phase-register evidence.
- Class to trigger/biogenesis: coordinate/register coherence plus dependency or a supported noncanonical initiation alternative.
- Biogenesis to molecular action: direct target/action assay in a matched sample; PARE supports cleavage only.
- Molecular action to phenotype: target-site genetics, rescue, equivalent causal intervention, or a matched pathway perturbation with explicit residual uncertainty.

### Failure and stop conditions

- Stop at discovery when only abundance, clustering, a database entry, or one caller supports the candidate.
- Stop at cleavage when PARE/degradome is the strongest evidence; do not infer protein effect or phenotype.
- Downgrade if species, stage, cell type, genotype, environment, assembly, or mapping policy is missing.
- Do not use a Dicer/pathway phenotype to validate every individual product or target.

## Model M2 — Trigger–register–dependency chain with canonical-exception branch

model_id: MEYERS-M2

```yaml
name: trigger_register_dependency_and_exception_audit
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_team_results
recurrence_test: passed
generative_test: passed
distinctiveness_test: passed
source_ids:
  - src-doi-10-1101-gad-177527-111
  - src-doi-10-1073-pnas-2402285121
  - src-doi-10-1073-pnas-2504349122
claim_ids:
  - claim-meyers-a-mirna-triggered-nlrr-phasing
  - claim-meyers-b-trigger-chain-nblrr
  - claim-meyers-a-premeiotic-24nt-negative-evidence-calibrated
  - claim-meyers-b-noncanonical-trigger-stop
  - claim-meyers-b-wheat-cross-species-test
```

### Two distinct recurrence contexts

1. For legume NB-LRR loci, 22-nt miRNA placement, cleavage and phased products support a canonical trigger-to-PHAS chain (`src-doi-10-1101-gad-177527-111`; `claim-meyers-b-trigger-chain-nblrr`).
2. For Zea and durum wheat premeiotic 24-nt classes, negative nanoPARE/AGO evidence and an AU-rich motif supported class-specific, likely noncanonical initiation rather than forcing a miRNA trigger (`src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122`; `claim-meyers-b-noncanonical-trigger-stop`, `claim-meyers-b-wheat-cross-species-test`).

### Procedure

1. Define the PHAS precursor, product size, phase register, trigger candidate, cleavage coordinate, Dicer/RDR dependency, AGO context, stage, and species.
2. Test whether the proposed cleavage coordinate sets the observed phase register and whether the relationship recurs across biological replicates.
3. Test pathway dependency with matched mutants/perturbations; record whether loss affects precursor, phased production, loading, or only phenotype.
4. Audit trigger-specific negative evidence: detection power, stage, alternative AGOs, motif architecture, and other initiators.
5. Choose one verdict: canonical trigger supported; trigger plausible but incomplete; noncanonical initiation supported; initiation unresolved.
6. Never infer target function merely from successful initiation.

### Upgrade thresholds

- Canonical trigger: supported trigger identity plus cleavage/register coherence and dependency.
- Noncanonical initiation: reproducible PHAS class plus negative canonical tests and a positive alternative feature or dependency; negative evidence remains assay-bounded.
- Cross-species conservation: retest trigger, register, Dicer/RDR, AGO, and precursor architecture rather than transferring a class label.

### Failure and stop conditions

- A predicted site plus a significant phasing score is insufficient.
- Nondetection without sensitivity/stage analysis cannot prove universal absence.
- A shared 21- or 24-nt class, miRNA number, or DCL5 dependency does not establish identical initiation or function.

## Model M3 — Stage × cell type × genotype × environment causal matrix

model_id: MEYERS-M3

```yaml
name: reproductive_context_and_penetrance_matrix
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_team_and_independent_results
recurrence_test: passed
generative_test: passed
distinctiveness_test: passed
source_ids:
  - src-doi-10-1073-pnas-1418918112
  - src-doi-10-1073-pnas-1619159114
  - src-doi-10-1038-s41467-020-16634-6
  - src-doi-10-1038-s41467-020-16637-3
  - src-doi-10-1038-s41467-020-19034-y
  - src-doi-10-1073-pnas-2504349122
claim_ids:
  - claim-meyers-a-maize-stage-cell-type-matching
  - claim-meyers-c-006
  - claim-meyers-a-pms1t-causality-with-unknown-downstream
  - claim-meyers-a-dcl5-genetics-temperature-boundary
  - claim-meyers-c-007
  - claim-meyers-c-008
  - claim-meyers-b-wheat-cross-species-test
```

### Two distinct recurrence contexts

1. Staged maize anthers and independent rice cell-type studies show that whole-anther averages combine distinct developmental and cellular populations (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`; `claim-meyers-a-maize-stage-cell-type-matching`, `claim-meyers-c-007`, `claim-meyers-c-008`).
2. Rice PMS1T photoperiod and maize/wheat DCL5 temperature experiments show that a stable molecular lesion and organismal phenotype penetrance can diverge across environments (`src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122`).

### Procedure

1. Build a matrix with species/assembly, stage/cytology, cell type, genotype/allele/homeolog dosage, environment/treatment, and assay.
2. Compare like-for-like cells and stages before interpreting abundance or target action.
3. Separate molecular lesion (class depletion, dependency, cleavage) from anatomical defects, fertility, and environmental penetrance.
4. Use sibling/background controls, multiple alleles or rescue when available.
5. If phenotype improves without restoration of the molecular lesion, place buffering downstream or parallel and keep the mediator unresolved.
6. Report the smallest context for which the conclusion holds.

### Upgrade thresholds

- Cell-of-production/action: spatially or cell-type-resolved measurement with composition controls.
- Pathway necessity: multiple alleles or an equivalent perturbation plus molecular readout.
- Phenotype causality: matched molecular, cytological/phenotypic, and rescue or environment-by-genotype evidence.

### Failure and stop conditions

- Do not transfer numeric anther-length thresholds across species, genotypes, or growth regimes without calibration.
- Bulk tissue cannot identify producing or responding cells.
- Temperature or photoperiod rescue of fertility does not imply molecular restoration.
- Pathway-gene perturbation cannot name a unique causal phasiRNA or target.

## Model M4 — Production–accumulation–mobility–function spatial gate

model_id: MEYERS-M4

```yaml
name: spatial_rna_gate_chain
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_spatial_team_and_field_results
recurrence_test: passed
generative_test: passed
distinctiveness_test: passed
source_ids:
  - src-doi-10-1073-pnas-1418918112
  - src-doi-10-1111-nph-18167
  - src-doi-10-1038-s41467-020-16637-3
  - src-doi-10-1038-s41467-020-19034-y
claim_ids:
  - claim-meyers-b-cell-stage-resolution
  - claim-meyers-a-spatial-origin-mobility-function-separation
  - claim-meyers-c-007
  - claim-meyers-c-008
```

### Two distinct recurrence contexts

1. Maize staging/localization and tapetum-to-meiocyte analyses separate precursor/DCL5 location from product accumulation and movement (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1111-nph-18167`; `claim-meyers-a-spatial-origin-mobility-function-separation`).
2. Independent rice studies separate somatic wall and male-germ-cell populations and provide cell-matched cleavage evidence (`src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`; `claim-meyers-c-007`, `claim-meyers-c-008`).

### Procedure

1. Define source cell, recipient cell, precursor, mature products, candidate AGO, stage, and contamination controls.
2. Score separate gates: source production; local accumulation; movement; recipient accumulation/loading; direct target action; phenotype.
3. Match each gate to its direct assay: precursor/localization, LCM/FISH, lineage or transport evidence, AGO association, target cleavage/site dependence, and causal perturbation.
4. Consider cell-composition change, diffusion, carryover, and differing stability as alternatives.
5. Report only the highest gate directly supported; leave downstream gates open.

### Upgrade thresholds

- Movement requires evidence beyond recipient reads, with source/recipient separation and contamination controls.
- Recipient action requires matched loading or target effect, not just accumulation.
- Function requires target or phenotype causality in the recipient context.

### Failure and stop conditions

- Spatial enrichment alone cannot identify production, transport, or function.
- Mobility evidence does not establish the molecular function after arrival.
- Whole-anther abundance cannot substitute for cell-resolved evidence.

## Model M5 — PHAS-call and targetome null-model audit

model_id: MEYERS-M5

```yaml
name: computational_signal_replicate_register_and_null_audit
knowledge_status: agent_inference
framework_relation: team_measurement_discipline_refined_by_independent_critique
recurrence_test: passed
generative_test: passed
distinctiveness_test: passed_for_phas_and_pare_scale_analysis
source_ids:
  - src-doi-10-1104-pp-104-039495
  - src-doi-10-1105-tpc-114-131847
  - src-doi-10-1093-bioinformatics-btu628
  - src-doi-10-1186-s12864-017-4031-9
  - src-doi-10-1093-nar-gky609
  - src-doi-10-1111-nph-17910
  - src-doi-10-1002-tpg2-70107
claim_ids:
  - claim-meyers-c-001
  - claim-meyers-a-soybean-multiaxis-annotation
  - claim-meyers-c-005
  - claim-meyers-c-004
  - claim-meyers-c-011
  - claim-meyers-b-postmeiotic-discovery-stop
```

### Two distinct recurrence contexts

1. PHAS-locus discovery depends on mapping, background, abundance, replication, register stability, and caller choice, as shown by atlas practice and independent PhaseTank/unitas comparisons (`src-doi-10-1105-tpc-114-131847`, `src-doi-10-1093-bioinformatics-btu628`, `src-doi-10-1186-s12864-017-4031-9`; `claim-meyers-c-005`).
2. Large-query PARE targetomes depend on targeting rules, transcript annotation, multiplicity, and null controls (`src-doi-10-1093-nar-gky609`, `src-doi-10-1111-nph-17910`; `claim-meyers-c-004`, `claim-meyers-c-011`).

### Procedure

1. Record counting unit, mapper, multimapping policy, assembly, annotation, library depth, biological replicates, caller, score threshold, and phase register.
2. Test call stability across replicates and reasonable parameter/caller alternatives.
3. Compare to sequence-shuffled, nonauthentic, register-shifted, abundance-matched, or other fit-for-purpose nulls.
4. For PARE, record targeting rules, transcript abundance, peak category, sample stage/cell type, query-set size, and multiplicity correction.
5. Distinguish computational candidate, reproducible class, direct cleavage, and causal function.
6. Nominate the orthogonal experiment most likely to falsify the call.

### Upgrade thresholds

- PHAS locus: stable phase register across biological evidence plus mapping/assembly controls; a second caller is helpful but not itself biological validation.
- Targetome event: matched direct signal that exceeds multiplicity-aware null behavior and fits the relevant cell/stage context.
- Functional target: target-site or equivalent genetic/biochemical validation beyond the computational/PARE call.

### Failure and stop conditions

- One significant score, one caller, or agreement among related pipelines is insufficient.
- More queried phasiRNAs can produce more false positives; raw target count is not evidence strength.
- Historical MPSS filters are evidence-discipline precedents, not modern PHAS or miRNA criteria.
- Independent critique defines error pressure; it is not a personal Meyers position.

## Cross-model routing

- Start with `MEYERS-M1` for every sequencing-to-mechanism claim.
- Add `MEYERS-M2` for PHAS initiation or a claimed trigger.
- Add `MEYERS-M3` for reproductive stage, genotype, crop, fertility, temperature, or photoperiod claims.
- Add `MEYERS-M4` for source/recipient cells, localization, movement, loading, or cell-specific action.
- Add `MEYERS-M5` for genome-scale calling, caller comparison, mapping ambiguity, PARE targetomes, or large multiple-testing spaces.
- Plant miRNA identity should invoke the shared annotation criteria and Evidence Auditor; it is not promoted as a uniquely Meyers core model.

