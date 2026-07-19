# Consensus, Status, and Methodological Tensions — Blake C. Meyers Lens Candidate

```yaml
expert_id: blake-c-meyers
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
tension_count: 6
```

This file preserves disagreement and scope differences. Independent papers can support a scientific claim without proving that it is Blake C. Meyers's personal position.

## Knowledge-status map

### Field consensus

- PARE/degradome can directly support a cleavage-compatible RNA end in a sampled pool, but not target exclusivity, protein effect, or phenotype causality (`src-doi-10-1038-nbt1417`, `src-doi-10-1016-j-cub-2008-04-042`; `claim-meyers-c-002`, `claim-meyers-c-003`).
- Reproductive phasiRNA interpretation must preserve stage and cell type because somatic-wall and germ-cell populations differ (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`; `claim-meyers-c-006`, `claim-meyers-c-007`, `claim-meyers-c-008`).
- Same size class or trigger-family name is not enough for one-to-one cross-species transfer (`claim-meyers-c-012`).

### Expert position

- The public program repeatedly separates discovery/annotation, trigger/biogenesis, action, and phenotype rather than using one generic validation label (`claim-meyers-a-soybean-multiaxis-annotation`, `claim-meyers-a-pms1t-causality-with-unknown-downstream`, `claim-meyers-a-premeiotic-24nt-negative-evidence-calibrated`).
- Canonical trigger chains are tested when supported, while negative trigger/loading/cleavage evidence is allowed to define a distinct class (`claim-meyers-b-trigger-chain-nblrr`, `claim-meyers-b-noncanonical-trigger-stop`).
- Broad angiosperm distribution is not treated as universal presence or conserved function (`claim-meyers-a-angiosperm-presence-is-not-universal`, `claim-meyers-b-distribution-not-function`).

### Contested

- PHAS calls vary with caller, abundance, background, register criteria, mapping, and assembly (`claim-meyers-c-005`).
- Degradome target calls vary with targeting rules, annotation, peak categories, and biological context (`claim-meyers-c-004`).
- Large phasiRNA query sets can inflate apparent PARE target counts; the breadth of reported targetomes remains context- and null-dependent (`claim-meyers-c-011`).

### Historical

- MPSS counting, normalization, uniqueness, and library-context discipline is a historical foundation, not a modern criterion set (`src-doi-10-1104-pp-104-039495`; `claim-meyers-c-001`).
- Deep sequencing expanded small-RNA catalogs, but historical candidates should not bypass current class-identity rules (`claim-meyers-a-deep-sequencing-reveals-heterogeneity`).
- The 2023 correction to the rice meiotic-progression paper is author-name metadata only (`src-doi-10-1038-s41467-023-37355-6`; `claim-meyers-c-010`).

### Superseded

- Platform-specific MPSS restriction/signature rules are superseded as current small-RNA discovery criteria, although the requirement to state the counting unit and mappability remains useful (`claim-meyers-a-mpss-mapping-before-interpretation`, `claim-meyers-c-001`).
- A single canonical tasiRNA or miRNA-trigger model cannot represent all reproductive PHAS classes; later Zea/wheat work supports class-specific noncanonical branches (`claim-meyers-a-phasirna-terminology-and-open-questions`, `claim-meyers-b-noncanonical-trigger-stop`).

### Hypothesis

- Newly described postmeiotic 21- and 24-nt PHAS cohorts are supported as stage-resolved classes, while biogenesis factors, targets, and functions remain unresolved (`src-doi-10-1002-tpg2-70107`; `claim-meyers-b-postmeiotic-discovery-stop`, `claim-meyers-c-013`).

### Agent inference

- `MEYERS-M1` through `MEYERS-M5` are cross-paper operationalizations, not personal statements (`claim-meyers-b-layered-escalation-candidate`, `claim-meyers-c-014`).
- Independence should be counted by laboratory/collaboration network, not paper count (`claim-meyers-c-015`).

## Methodological tensions

### MEYERS-T1 — Large phasiRNA targetomes versus multiplicity-driven PARE false positives

- Position A: purified male-germ-cell and stage-resolved degradome data support many 21-nt phasiRNA cleavage events (`src-doi-10-1038-s41467-020-19034-y`; `claim-meyers-c-008`).
- Position B: nonauthentic-sRNA controls and configurable target rules show that large query sets can generate many false assignments (`src-doi-10-1111-nph-17910`, `src-doi-10-1093-nar-gky609`; `claim-meyers-c-011`, `claim-meyers-c-004`).
- Status: `contested`, not resolved by choosing one paper.
- Resolution: matched cell/stage nulls, transcript abundance, replicate consistency, multiplicity correction, AGO evidence, target-site editing, protein readout, and phenotype rescue.
- Boundary: the critique does not invalidate well-controlled individual targets; PARE positivity does not prove phenotypic importance.

### MEYERS-T2 — Canonical miRNA-triggered PHAS chains versus noncanonical initiation

- Position A: legume NB-LRRs show a coherent 22-nt miRNA cleavage/register/phasing chain (`src-doi-10-1101-gad-177527-111`; `claim-meyers-b-trigger-chain-nblrr`).
- Position B: Zea and wheat premeiotic 24-nt classes show DCL5 dependence but negative canonical-trigger evidence and alternative motif architecture (`src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122`; `claim-meyers-b-noncanonical-trigger-stop`, `claim-meyers-b-wheat-cross-species-test`).
- Status: context-resolved as class-specific, not a universal contradiction.
- Resolution: assay-matched trigger, register, dependency, AGO, motif, and alternative-initiator tests.
- Boundary: negative evidence remains sensitivity- and stage-bounded.

### MEYERS-T3 — Broad evolutionary presence versus conserved function

- Position A: comparative analyses support broad angiosperm distribution of 24-nt reproductive phasiRNAs (`src-doi-10-1038-s41467-019-08543-0`; `claim-meyers-a-angiosperm-presence-is-not-universal`).
- Position B: triggers, precursor architectures, timing, AGOs, targets, and functions can differ or remain unknown (`src-doi-10-1073-pnas-2402285121`, `src-doi-10-1002-tpg2-70107`; `claim-meyers-b-distribution-not-function`, `claim-meyers-c-013`).
- Status: `field_consensus` that presence and function are separate; many function claims remain `hypothesis`.
- Resolution: lineage-matched perturbation, loading, target action, rescue, and phenotype evidence.
- Boundary: same-numbered miRNA or size class is not orthology.

### MEYERS-T4 — Stable molecular depletion versus environment-conditioned fertility

- Position A: maize DCL5 loss robustly depletes 24-nt phasiRNAs (`src-doi-10-1038-s41467-020-16634-6`; `claim-meyers-a-dcl5-genetics-temperature-boundary`).
- Position B: male fertility varies with temperature even when the molecular deficit is not restored (`claim-meyers-b-dcl5-temperature-decoupling`); rice PMS1T and wheat DCL5 add photoperiod or temperature dependence (`claim-meyers-b-pms1t-context-causality`, `claim-meyers-b-wheat-cross-species-test`).
- Status: strong pathway requirement with unresolved downstream/parallel buffering.
- Resolution: environment-by-genotype molecular, cytological, target, and rescue series.
- Boundary: permissive fertility is not evidence that phasiRNA biogenesis recovered.

### MEYERS-T5 — Classic premeiotic/meiotic waves versus added postmeiotic classes

- Position A: maize staging established a premeiotic 21-nt and meiotic 24-nt framework (`src-doi-10-1073-pnas-1418918112`; `claim-meyers-a-maize-stage-cell-type-matching`).
- Position B: a ten-stage rice series reports additional postmeiotic 21- and 24-nt classes (`src-doi-10-1002-tpg2-70107`; `claim-meyers-c-013`).
- Status: scope expansion, not direct contradiction.
- Resolution: independent reproduction plus perturbation of biogenesis, loading, targets, and reproductive consequences.
- Boundary: new register/abundance patterns are not completed mechanisms.

### MEYERS-T6 — Spatial mobility versus molecular function after arrival

- Position A: LCM and RNA/sRNA FISH support tapetum-to-meiocyte movement of maize 24-nt phasiRNAs (`src-doi-10-1111-nph-18167`; `claim-meyers-a-spatial-origin-mobility-function-separation`).
- Position B: spatial arrival alone does not identify recipient AGO loading, targets, or phenotype; independent rice data show that cell layer and 5-prime composition matter (`src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`; `claim-meyers-c-007`, `claim-meyers-c-008`).
- Status: mobility supported in the tested maize context; recipient function remains incomplete.
- Resolution: source-restricted perturbation, movement tracing, recipient loading, target-site genetics, and cell-specific rescue.
- Boundary: `production != accumulation != mobility != function`.

## Conflict-handling rules

1. Preserve species, stage, cell type, genotype, environment, assembly, and method before comparing conclusions.
2. Distinguish a true contradiction from scope expansion or a different causal gate.
3. Do not count semantically duplicated cards as independent recurrence.
4. Do not use independent critique to fabricate an expert position.
5. Store unresolved targetome breadth, postmeiotic function, and recipient-effector questions as conflicts or hypotheses rather than silently harmonizing them.
6. Recheck publication status at the final evidence cutoff; the current correction is bibliographic only.

