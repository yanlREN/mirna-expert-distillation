# Question Frameworks — Hailing Jin Cross-Kingdom RNA Lens Candidate

```yaml
expert_id: hailing-jin
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
question_dimension_count: 6
```

These six dimensions are a neutral interrogation framework derived from public team research and independent scope evidence. They are not Hailing Jin's words or current personal opinion. Each dimension can be scored independently; a strong answer in one dimension does not complete another.

## Dimension Q1 — RNA entity, donor origin and clean sampling

dimension_id: JIN-Q1

**Core question:** What exact RNA entity is claimed, where was it produced, and can donor origin be distinguished from mixture, carryover and ambiguous mapping?

Ask:

1. Is the entity a miRNA family, MIR gene family, MIR locus, precursor, mature 5p/3p product, isomiR, exact sRNA, long dsRNA or full-length mRNA?
2. Are exact sequence, length, donor/recipient assemblies, multi-hit/mismatch policy and shared/low-complexity sequence handling reported?
3. Is the sample mixed infection tissue, purified recipient cells, surface/apoplast material, EV fraction or another compartment?
4. Was a deliberately mixed non-contact control processed through the same purification and mapping pipeline?
5. Are donor cellular/organelle markers, recipient markers, pathogen biomass and surface-removal controls available?

**Verdicts:** entity_and_origin_supported; exact_entity_supported_origin_unresolved; donor_matching_signal_only; unsupported.

- `source_ids`: HJ-A-S006, HJ-A-S009, HJ-A-S015, HJ-B-S006, HJ-B-S015
- `claim_ids`: HJ-B-C001, HJ-B-C003, HJ-C-C004

## Dimension Q2 — Direction, release, vehicle and extracellular topology

dimension_id: JIN-Q2

**Core question:** For this donor→recipient direction, what evidence distinguishes release, EV association, membrane encapsulation, non-EV RNP and extracellular persistence?

Ask:

1. Is plant→fungus analyzed separately from fungus→plant?
2. Does the evidence stop at an operational pellet, or include density, markers, contaminant markers, nuclease ± detergent and subclass immunocapture?
3. Were non-EV extracellular RNA/RNP pools measured in parallel?
4. Do release/biogenesis mutants change cargo after normalization for EV abundance and broader physiology?
5. Are association, loading, stabilization and encapsulation stated as different propositions?

**Verdicts:** topology_and_subclass_supported; marker_fraction_association_only; extracellular_association_only; vehicle_unresolved.

- `source_ids`: HJ-A-S009, HJ-A-S010, HJ-B-S009, HJ-A-S014, HJ-B-S015, HJ-C-S014
- `claim_ids`: HJ-B-C006, HJ-B-C007, HJ-B-C008, HJ-C-C013, HJ-C-C014

## Dimension Q3 — Intact-recipient uptake and competence

dimension_id: JIN-Q3

**Core question:** Does the RNA enter intact recipient cells, and does that recipient possess the processing or uptake machinery required in the tested pathosystem?

Ask:

1. Were surface-bound RNA and free dye removed or destroyed with topology-appropriate controls?
2. Is uptake localized inside intact recipient cells or inferred only from downstream effects?
3. Are recipient DCL/AGO or translation components expressed, engaged and genetically required where claimed?
4. Were direct uptake and plant-passage routes compared?
5. Are host cultivar, pathogen strain, tissue integrity, infection stage, dose, formulation and persistence matched?
6. Does a negative result have a positive control and enough sensitivity to constrain the claimed route?

**Verdicts:** uptake_and_competence_supported; uptake_supported_processing_unresolved; association_only; competent_route_not_supported_in_tested_context.

- `source_ids`: HJ-A-S008, HJ-A-S014, HJ-C-S010, HJ-B-S013, HJ-B-S014
- `claim_ids`: HJ-B-C010, HJ-B-C012, HJ-C-C009, HJ-C-C015, HJ-C-C016

## Dimension Q4 — Recipient effector, direct target and phenotype causality

dimension_id: JIN-Q4

**Core question:** What recipient event is directly shown, how direct is the target edge, and what genetics connect it to the phenotype?

Ask:

1. For sRNA, is there recipient AGO/RISC association, cleavage, reporter, target-site resistance or rescue?
2. For dsRNA, are uptake, recipient Dicer processing, sequence-specific target knockdown and phenotype separated?
3. For mRNA, are intactness, recipient ribosome/polysome association and protein output shown?
4. Is evidence only prediction/anticorrelation, direct molecular action, or a causal target-to-phenotype bridge?
5. Could route/DCL/AGO mutants be pleiotropic, or target-site edits alter protein/transcript properties independently?
6. Is the conclusion “contributes to phenotype” or an overclaim that one target fully explains disease?

**Verdicts:** class_specific_action_and_causal_bridge_supported; direct_target_supported_phenotype_partial; recipient_action_supported_target_partial; prediction_or_correlation_only.

- `source_ids`: HJ-A-S005, HJ-A-S006, HJ-A-S008, HJ-B-S012, HJ-B-S013, HJ-A-S015, HJ-C-S011
- `claim_ids`: HJ-A-C005, HJ-B-C011, HJ-B-C012, HJ-B-C014, HJ-C-C008, HJ-C-C010, HJ-C-C015

## Dimension Q5 — Pathosystem scope, conflict and independent validation

dimension_id: JIN-Q5

**Core question:** In which exact biological contexts does the result hold, fail or remain unresolved, and how independent are the supporting networks?

Ask:

1. Are positive and negative results indexed by organism pair, host/cultivar, pathogen strain, tissue, stage, RNA class, vehicle and method?
2. Does the study match the original mechanism closely enough to count as replication, or only as analogy/scope evidence?
3. Are same-network papers folded rather than counted repeatedly?
4. Are six strict networks and two downgraded clusters preserved, with 42 method edges not mislabeled as networks?
5. Are Zymoseptoria negatives, early tomato–Botrytis non-replication, cotton–Verticillium support and Fusarium route limits all retained?
6. What matched reciprocal experiment would resolve each conflict?

**Verdicts:** independently_bounded_support; context_dependent_conflict; analogous_only; insufficient_independence.

- `source_ids`: HJ-B-S012, HJ-C-S010, HJ-C-S011, HJ-C-S012, HJ-B-S013, HJ-B-S014
- `claim_ids`: HJ-C-C009, HJ-C-C010, HJ-C-C011, HJ-C-C012, HJ-C-C017

## Dimension Q6 — Intervention maturity, publication integrity and attribution

dimension_id: JIN-Q6

**Core question:** Does the claim concern natural transfer or engineered intervention, what is its last tested maturity stage, and is the evidence record current and correctly attributed?

Ask:

1. Is the evidence natural exchange, HIGS, SIGS, formulation, nanovesicle or engineered-living delivery?
2. Are target validity, production, stability, uptake, on-target action, controlled protection, intact-plant, field and ecological/safety stages separated?
3. Are dose, duration, rain/UV/temperature, crop tissue, isolate diversity, off-targets, non-targets and resistance evolution tested?
4. Was the 2011 corrected Figure 4b or the 2021 replaced Supplementary Information used where relevant?
5. Is the 2025 Science erratum content still marked unknown and the 2026 article abstract-bounded?
6. Are team findings, expert public framing, field consensus, contested evidence and Agent inference separately labeled, with no impersonation?

**Verdicts:** maturity_and_integrity_supported; controlled_proof_of_concept; abstract_or_correction_bounded; overclaimed_or_misattributed.

- `source_ids`: HJ-A-S004, HJ-A-S007, HJ-A-S011, HJ-A-S012, HJ-A-S013, HJ-A-S016
- `claim_ids`: HJ-A-C011, HJ-A-C016, HJ-A-C018, HJ-A-C020, HJ-C-C003

## Integrated answer protocol

1. State the exact question and biological context without inventing a crop, pathogen, sequence or delivery route.
2. Route through Q1→Q4 for mechanism; add Q5 for scope/conflict and Q6 for application/publication status.
3. For every conclusion, state evidence layer, directness, independence, organism/tissue/stage scope and publication boundary.
4. Preserve unknowns and negative evidence. Never let a later edge imply an earlier untested edge.
5. End with the narrowest supported conclusion, the closest alternative explanation and the next most discriminating experiment.
