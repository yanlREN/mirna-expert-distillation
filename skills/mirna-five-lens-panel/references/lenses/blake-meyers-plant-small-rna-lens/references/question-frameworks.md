# Paper Interrogation Framework — Blake C. Meyers Lens Candidate

```yaml
expert_id: blake-c-meyers
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
dimension_count: 6
evidence_cutoff: 2026-07-17
```

The six dimensions are reusable review axes. They do not imitate an expert's voice and do not claim to represent Blake C. Meyers's current opinion.

## Dimension 1 — Entity, measurement, and evidence gate

dimension_id: MEYERS-Q1

Ask:

1. What is the exact entity: MIR family, MIR locus, precursor, mature 5p/3p sequence, PHAS locus/precursor, phased product, isomiR, database record, or genomic coordinate/assembly?
2. What does each assay directly measure: read abundance, mapping, processing precision, phase register, dependency, cleavage, loading, protein effect, or phenotype?
3. Which gate is actually supported: discovery, identity/class, trigger/biogenesis, molecular action, or phenotype causality?
4. Is a downstream phenotype being used to retroactively validate weak identity, or is PARE being used to claim complete causality?
5. What alternative class—siRNA, repeat product, degradation fragment, or mapping artifact—has been excluded?

Output separate gate verdicts and the next discriminating assay. Sources: `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1105-tpc-114-131847`, `src-doi-10-1038-nbt1417`. Claims: `claim-meyers-b-mirna-annotation-replication`, `claim-meyers-a-soybean-multiaxis-annotation`, `claim-meyers-b-layered-escalation-candidate`.

## Dimension 2 — PHAS calling, trigger, register, and null model

dimension_id: MEYERS-Q2

Ask:

1. Which assembly, mapping/multimapping policy, counting unit, biological replicates, caller, score threshold, and annotation were used?
2. Is the phase register stable across replicates and robust to reasonable model/caller choices?
3. Does the proposed trigger cleavage coordinate establish the phase offset, and is pathway dependency supported?
4. Were sequence-shuffled, nonauthentic, register-shifted, or abundance-matched nulls used for PHAS or PARE claims?
5. How does query-set size affect the expected false-positive count?
6. If canonical evidence is negative, were sensitivity, stage, alternate AGOs, and noncanonical initiation tested before classifying the exception?

Output a trigger verdict and a computational-signal verdict separately. Sources: `src-doi-10-1101-gad-177527-111`, `src-doi-10-1186-s12864-017-4031-9`, `src-doi-10-1093-nar-gky609`, `src-doi-10-1111-nph-17910`, `src-doi-10-1073-pnas-2402285121`. Claims: `claim-meyers-b-trigger-chain-nblrr`, `claim-meyers-c-005`, `claim-meyers-c-004`, `claim-meyers-c-011`, `claim-meyers-b-noncanonical-trigger-stop`.

## Dimension 3 — Developmental, cellular, genetic, and environmental match

dimension_id: MEYERS-Q3

Ask:

1. Are species, anther stage/cytology, cell layer, genotype/allele, background, and environment matched?
2. Could a bulk difference reflect changing tissue composition rather than altered production or action?
3. Do multiple alleles, homeolog dosage, sibling controls, or rescue separate pathway requirement from background effects?
4. Is molecular depletion stable while fertility changes with temperature or photoperiod?
5. Are numeric stage proxies calibrated within the tested species and growth regime?
6. What is the smallest context in which the claim remains true?

Output a context matrix and mark missing cells. Sources: `src-doi-10-1073-pnas-1418918112`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122`. Claims: `claim-meyers-a-maize-stage-cell-type-matching`, `claim-meyers-b-pms1t-context-causality`, `claim-meyers-b-dcl5-temperature-decoupling`, `claim-meyers-b-wheat-cross-species-test`.

## Dimension 4 — Spatial production, movement, loading, and action

dimension_id: MEYERS-Q4

Ask:

1. Where are the precursor and biogenesis factors produced, and where do mature products accumulate?
2. Does the evidence distinguish production from stability, accumulation, and movement?
3. Are source and recipient cells physically separated with contamination and cell-composition controls?
4. Is recipient AGO loading or target engagement directly measured?
5. Is cleavage spatially matched to the relevant stage/cell population?
6. Does any evidence connect recipient action to phenotype, or should the conclusion stop at mobility?

Output six gate verdicts: source production, local accumulation, movement, recipient loading, target action, phenotype. Sources: `src-doi-10-1111-nph-18167`, `src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`. Claims: `claim-meyers-a-spatial-origin-mobility-function-separation`, `claim-meyers-c-007`, `claim-meyers-c-008`.

## Dimension 5 — Comparative and crop-transfer decomposition

dimension_id: MEYERS-Q5

Ask:

1. Is the claim about pathway presence, homologous biogenesis, analogous architecture, or conserved function?
2. Could absence be caused by assembly, annotation, stage, depth, or trigger/caller sensitivity?
3. Are loci, precursor architectures, mature sequences, trigger families, Dicer/RDR, AGO, cell context, targets, and environment equivalent?
4. In polyploid crops, is homeolog dosage and rescue tested?
5. Is the transfer type `conserved`, `analogous`, `lineage_specific`, `uncertain`, or `unsupported_transfer`?
6. Which component is conserved, and which must be retested?

Output component-level transfer labels, not a single conserved/not-conserved verdict. Sources: `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122`, `src-doi-10-1038-s41467-020-16637-3`. Claims: `claim-meyers-a-angiosperm-presence-is-not-universal`, `claim-meyers-b-distribution-not-function`, `claim-meyers-b-wheat-cross-species-test`, `claim-meyers-c-012`.

## Dimension 6 — Claim status, independent support, conflict, and stop rule

dimension_id: MEYERS-Q6

Ask:

1. Is the statement `field_consensus`, `expert_position`, `contested`, `historical`, `superseded`, `hypothesis`, or `agent_inference`?
2. Is the expert's role first/corresponding/senior/coauthor/review author/speaker/not author, and is a team result being misattributed as a personal view?
3. Do supporting sources represent independent laboratories/networks or semantic duplication/collaboration-linked evidence?
4. Are four abstract-bounded records being used beyond their verified minimum, or are talk pages being treated as transcripts?
5. Does a correction alter science or only publication metadata?
6. What observation would falsify the claim, and where must the review stop today?

Output attribution, knowledge status, independence, directness, conflict, source-access boundary, and stop reason. Sources: `src-doi-10-1038-s41467-023-37355-6`, `src-url-ista-2025-phased-secondary-sirnas`, `src-url-sustech-2026-phased-secondary-sirnas`, `src-doi-10-1002-tpg2-70107`. Claims: `claim-meyers-c-010`, `claim-meyers-a-public-seminar-unknown-function-emphasis`, `claim-meyers-a-talk-inventory-evidence-thin`, `claim-meyers-c-013`, `claim-meyers-c-015`.

## Required review output

For every interrogated paper, return:

```yaml
entity_and_context:
assay_observations: []
evidence_gates:
  discovery:
  identity_or_class:
  trigger_or_biogenesis:
  molecular_action:
  phenotype_causality:
spatial_gates:
  production:
  accumulation:
  mobility:
  recipient_loading:
  target_action:
transfer_type:
knowledge_status:
attribution:
independent_support:
conflicts: []
missing_context: []
stop_reason:
next_discriminating_experiment:
source_ids: []
claim_ids: []
```

