# Scientific Reasoning Models — Hailing Jin Cross-Kingdom RNA Lens Candidate

```yaml
expert_id: hailing-jin
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
phase: N2
model_count: 5
```

These are neutral Agent syntheses of recurring, public team-level research patterns. They are not quotations, private views, or claims that Hailing Jin personally endorses every statement in a multi-author paper. `expert_position`, `field_consensus`, `contested`, `historical`, and `agent_inference` remain distinct. The five retained models emerged from 21 candidates after semantic clustering; details are in `phase-2-synthesis.md`.

## Model M1 — Direction-resolved donor-to-phenotype chain

model_id: JIN-M1

```yaml
name: direction_resolved_foreign_rna_causal_chain
definition: Begin with foreign-RNA origin and carryover alternatives, then grade donor production, release, vehicle, extracellular persistence, recipient uptake, recipient effector access, direct target action, and phenotype as separate direction-specific edges.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_cross_organism_rna_chain_decomposition
source_ids: [HJ-A-S006, HJ-A-S009, HJ-A-S014, HJ-A-S015, HJ-B-S012]
claim_ids: [HJ-A-C017, HJ-A-C019, HJ-B-C001, HJ-B-C002, HJ-C-C004]
```

### Two or more distinct contexts

1. Fungus→plant studies connect Botrytis sRNA production, plant AGO1/targets and virulence, with later fungal-EV release and plant clathrin-mediated uptake work (`HJ-A-S006`, `HJ-A-S014`; `HJ-A-C006`, `HJ-A-C014`).
2. Plant→fungus studies separately test Arabidopsis EV-associated sRNA delivery, cotton miRNA–fungal target-site genetics, and selected plant mRNA transfer/translation (`HJ-A-S009`, `HJ-B-S012`, `HJ-A-S015`; `HJ-A-C009`, `HJ-B-C005`, `HJ-B-C014`). These contexts differ in direction, RNA class, vehicle evidence, recipient machinery, and causal readout.

### Operational use

1. State donor, recipient, species/strain, tissue, infection stage, RNA class and exact entity.
2. Start from the nulls of mixed tissue, surface adherence, lysis, extracellular carryover, shared sequence and ambiguous mapping.
3. Put each assay on one edge only: production; release; association/encapsulation; uptake; effector access; target; phenotype.
4. Build plant→pathogen and pathogen→plant chains independently. “Bidirectional” never licenses a mirrored carrier or uptake mechanism.
5. Report the highest directly completed edge and list missing edges; do not backfill upstream transport from downstream phenotype.

### Failure conditions and transfer limits

- Mixed-infection reads without matched purification/mixing controls establish detection only.
- EV enrichment does not establish recipient uptake, and uptake does not establish RISC access.
- A mechanism in Arabidopsis–Botrytis cannot be transferred to cotton–Verticillium, wheat–Zymoseptoria, or another direction without re-testing.
- The 2013 Science fine-grained edge remains bounded by the unresolved-content 2025 erratum (`HJ-A-S007`, `HJ-A-C007`).

## Model M2 — Vehicle, topology and compartment evidence ladder

model_id: JIN-M2

```yaml
name: extracellular_rna_vehicle_topology_and_subclass_ladder
definition: Grade extracellular RNA from operational co-fractionation through topology, marker-defined subclass, route perturbation, recipient uptake and function while keeping non-vesicular RNA and RNP alternatives active.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_ev_rna_transport_claims
source_ids: [HJ-A-S009, HJ-A-S010, HJ-B-S009, HJ-A-S014, HJ-B-S006, HJ-B-S015, HJ-C-S014]
claim_ids: [HJ-B-C006, HJ-B-C007, HJ-B-C008, HJ-C-C013, HJ-C-C014]
```

### Two or more distinct contexts

1. Plant EV work uses density fractionation, nuclease protection, TET8/TET9 genetics or immunoisolation, and candidate RBPs to address association, protection, loading and stability (`HJ-A-S009`, `HJ-A-S010`, `HJ-B-S009`; `HJ-A-C009`, `HJ-A-C010`, `HJ-B-C009`).
2. Fungal EV/CME work uses BcPLS1-positive vesicles, plant uptake-route genetics, AGO1 and targets (`HJ-A-S014`; `HJ-B-C010`), whereas independent Arabidopsis studies show tiny-RNA-rich operational EV fractions and abundant non-EV leaf-surface RNA (`HJ-B-S006`, `HJ-B-S015`; `HJ-B-C008`).

### Operational use

Grade, without skipping:

```text
operational pellet or extracellular fraction
→ density/marker-defined fraction
→ nuclease ± membrane-disruption topology
→ EV-subclass immunocapture
→ release/biogenesis perturbation
→ intact-recipient uptake
→ recipient molecular action
→ causal phenotype
```

At every rung report starting material, apoplast contamination controls, EV and contaminant markers, non-EV comparator, normalization, and whether the conclusion is association, encapsulation, loading, stabilization, uptake, or functional delivery.

### Failure conditions and transfer limits

- A 100,000×g pellet, RNase resistance alone, or fluorescent dye alone cannot define an EV vehicle.
- TET8-positive plant EVs, BcPLS1-positive fungal EVs and mammalian exosomes are not interchangeable subclasses.
- `HJ-C-S014` is a downgraded cross-lineage method analogue, not plant-mechanism replication (`HJ-C-C014`).
- The 2021 paper must use its replaced Supplementary Information file (`HJ-A-S011`, `HJ-A-C011`).

## Model M3 — Recipient-competence and pathosystem scope matrix

model_id: JIN-M3

```yaml
name: recipient_competence_context_and_conflict_matrix
definition: Preserve positive and negative results by organism pair, strain, host, tissue, stage, RNA class, uptake route and assay; test recipient uptake and RNAi competence before generalizing a cross-kingdom or SIGS mechanism.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_public_program_and_independent_scope_evidence
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_cross_pathosystem_rna_transfer_scope
source_ids: [HJ-A-S008, HJ-B-S012, HJ-C-S010, HJ-C-S011, HJ-C-S012, HJ-B-S013, HJ-B-S014]
claim_ids: [HJ-B-C012, HJ-B-C015, HJ-C-C009, HJ-C-C010, HJ-C-C011, HJ-C-C012, HJ-C-C016, HJ-C-C017]
```

### Two or more distinct contexts

1. Positive or supporting contexts include Botrytis uptake/topical protection, cotton–Verticillium natural miRNA action, and Fusarium SIGS with recipient DCL dependence (`HJ-A-S008`, `HJ-B-S012`, `HJ-B-S013`).
2. Negative or limiting contexts include two wheat–Zymoseptoria studies with no clear uptake/cross-kingdom cleavage evidence, early tomato–Botrytis partial non-replication, and transient/wound-dependent Fusarium responses (`HJ-C-S010`, `HJ-C-S011`, `HJ-C-S012`, `HJ-B-S014`).

### Operational use

1. Build a matrix keyed by donor/recipient, host cultivar, pathogen strain, tissue, infection stage, surface integrity, RNA class/length, dose/formulation and assay.
2. Test intact-recipient uptake, DCL/AGO competence, processing, target knockdown and temporal persistence before application generalization.
3. Treat a controlled negative as a boundary on the tested cells of the matrix, not a universal refutation.
4. Treat a positive as feasibility in the tested cells, not evidence that every fungus is competent.
5. Never use paper counts, 42 method edges, or same-network repetition as replication counts. The authoritative independence result is **6 strict networks + 2 downgraded external clusters** (`HJ-C-C017`).

### Failure conditions and transfer limits

- Collapsing Zymoseptoria negatives, Fusarium route differences and Botrytis positives into a yes/no vote destroys the evidence.
- Absence of PARE cleavage does not exclude every non-cleavage mechanism, but it does constrain cleavage claims.
- Early tomato–Botrytis results do not erase later stages or Arabidopsis; conversely, Arabidopsis results do not override the bounded non-replication.

## Model M4 — RNA-class-specific recipient action and causal bridge

model_id: JIN-M4

```yaml
name: rna_entity_effector_target_and_phenotype_separation
definition: Resolve the RNA entity first, then require RNA-class-appropriate recipient action and independently grade direct target evidence and phenotype causality.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_and_external_designs
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_cross_kingdom_rna_entity_and_action
source_ids: [HJ-A-S005, HJ-A-S006, HJ-A-S008, HJ-B-S012, HJ-B-S013, HJ-A-S015, HJ-C-S011]
claim_ids: [HJ-A-C005, HJ-B-C003, HJ-B-C011, HJ-B-C012, HJ-B-C014, HJ-C-C010, HJ-C-C015]
```

### Two or more distinct contexts

1. Small-RNA contexts use recipient AGO association, cleavage/repression, reporter or target-site-resistant alleles; cotton–Verticillium target-site genetics is a strong external-led bridge (`HJ-B-S012`, `HJ-C-C008`).
2. Transferred mRNA requires full-length detection, recipient ribosome/polysome association and protein output, as tested for selected plant mRNAs in Botrytis (`HJ-A-S015`, `HJ-A-C015`). dsRNA/SIGS instead requires uptake, recipient Dicer processing and sequence-specific target change (`HJ-A-S008`, `HJ-B-S013`).

### Operational use

1. Preserve miRNA family, MIR gene family, MIR locus, precursor, mature 5p/3p product, isomiR, exact sequence and assembly separately.
2. Keep miRNA, siRNA, long dsRNA and mRNA as distinct cargo and mechanism classes.
3. Match action assays: AGO/cleavage/reporter for sRNA; uptake/Dicer/knockdown for dsRNA; intactness/ribosome/protein for mRNA.
4. Grade targeting from prediction or correlation, through direct molecular evidence, to resistant-target/rescue genetics.
5. Grade phenotype causality independently; direct target evidence need not make one target the sole disease cause.

### Failure conditions and transfer limits

- Same family name, short match, database record, predicted hairpin, expression anticorrelation, or PARE alone cannot close identity, transport and phenotype together.
- Historical miR393* notation must not be silently remapped to every modern arm or family member (`HJ-A-S005`, `HJ-A-C005`).
- Plant rules cannot be replaced by animal seed-only or Drosha–DGCR8 logic.

## Model M5 — Natural-mechanism versus intervention maturity ladder

model_id: JIN-M5

```yaml
name: natural_transfer_engineered_delivery_and_deployment_ladder
definition: Separate evidence for natural RNA exchange from HIGS, SIGS, formulation and living-delivery interventions, then report application maturity at the highest directly tested stage.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_public_research_trajectory
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_rna_crop_protection_translation
source_ids: [HJ-A-S008, HJ-A-S009, HJ-B-S012, HJ-A-S012, HJ-A-S013, HJ-B-S013, HJ-B-S014, HJ-A-S016]
claim_ids: [HJ-A-C018, HJ-B-C005, HJ-B-C012, HJ-B-C013, HJ-C-C003, HJ-C-C015, HJ-C-C016]
```

### Two or more distinct contexts

1. Natural cross-kingdom evidence asks whether an endogenous RNA is produced, moves by a natural route, engages recipient machinery and changes infection (`HJ-A-S009`, `HJ-B-S012`).
2. Engineered intervention contexts include HIGS/topical RNA, BioClay, artificial nanovesicles, plant-passage SIGS and abstract-only engineered bacterial delivery (`HJ-A-S008`, `HJ-A-S012`, `HJ-A-S013`, `HJ-B-S013`, `HJ-A-S016`). These test feasibility and delivery engineering, not the natural route.

### Operational use

Report the last completed stage:

```text
target and exact sequence
→ production and formulation
→ environmental stability/persistence
→ intact-surface entry and pathogen uptake
→ recipient processing and on-target action
→ controlled disease protection
→ intact-plant/greenhouse replication
→ multi-environment field efficacy
→ non-target, resistance, ecological, regulatory and production assessment
```

Use route, dose, formulation, crop tissue, pathogen isolate, duration and surface integrity as mandatory scope fields.

### Failure conditions and transfer limits

- Detached commodity, cut coleoptile, or controlled leaf protection is not field readiness.
- Engineered efficacy does not prove that the same RNA naturally occurs or travels by the same vehicle.
- `HJ-A-S016` is abstract-only: no inaccessible method, dose, ecological, or field detail may be reconstructed (`HJ-A-C016`).
- Programmatic optimism in a perspective is labeled `expert_position`, not deployment evidence (`HJ-C-C003`).

## Cross-model routing

- Start every cross-organism RNA claim with `JIN-M1`.
- Add `JIN-M2` when extracellular fractions, EVs, RBPs, encapsulation or uptake routes are claimed.
- Add `JIN-M3` for cross-species transfer, negative results, replication, recipient competence or conflict resolution.
- Add `JIN-M4` for RNA identity, recipient effector, direct target or phenotype causality.
- Add `JIN-M5` for HIGS, SIGS, formulations, engineered carriers or deployment claims.
- Apply the correction-first and attribution guards from `evidence-heuristics.md` across every route.
