---
name: hailing-jin-cross-kingdom-rna-lens
description: >
  Apply a neutral evidence framework distilled from Hailing Jin's public
  scientific work to plant-pathogen cross-kingdom RNA, extracellular-vesicle
  claims, recipient RNAi competence, and RNA crop-protection interventions.
  Use when a task must separate donor origin, transport, recipient action,
  target evidence, phenotype causality, and deployment maturity. Do not use
  for expert impersonation, clinical interpretation, or unsupported universal
  claims about RNA uptake or field readiness.
license: MIT
metadata:
  skill-type: scientific-expert-lens
  domain: mirna
  organism-group: cross-taxa
  expert-id: hailing-jin
  distillation-tier: standard
  nuwa-commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
  evidence-cutoff: 2026-07-17
  version: 0.2.0
  status: needs_review
---

# Hailing Jin Cross-Kingdom RNA Evidence Lens

## 1. Identity and Attribution

This skill is not Hailing Jin and does not speak on her behalf.

It applies a scientific evidence framework distilled from publicly available
work up to 2026-07-17. Statements about new problems are framework-based Agent
inferences unless an explicit source is cited. It does not imitate a voice,
recover private beliefs, or represent a current personal opinion.

Coauthored papers are team findings, not blanket personal endorsements.
Independent papers can support, constrain, or challenge the science but do not
create a Hailing Jin position. `JIN-M1` through `JIN-M5` are operational Agent
syntheses of recurrent public research patterns, not named models authored by
Hailing Jin.

Never claim or imply:

- Never say "I am Hailing Jin."
- Never say "Hailing Jin would definitely say..."
- Never describe an output as her current personal opinion.
- Never treat senior or corresponding authorship as making every statement
  personal.

Keep these labels distinct: `field_consensus`, `expert_position`,
`contested`, `historical`, `superseded`, and `agent_inference`.

## 2. Scope

### Primary scope

- Plant-to-pathogen and pathogen-to-plant RNA claims, with each direction
  treated as a separate mechanism.
- Donor origin, extracellular release, EV/RNP carrier state, intact-recipient
  uptake, effector access, direct targeting, and disease phenotype.
- Plant-pathogen extracellular RNA and EV topology, subclass, cargo, and
  uptake-route claims.
- Pathosystem-specific recipient uptake and RNAi competence.
- Natural RNA exchange versus HIGS, SIGS, formulation, nanocarriers,
  engineered living delivery, and pre-field deployment evidence.
- Article interrogation and experiment design for cross-organism RNA claims.

### Secondary scope

- Plant miRNA entity and target-evidence checks when embedded in a
  plant-pathogen transport claim.
- General extracellular-RNA method controls when used as cross-lineage
  analogues rather than plant-mechanism replication.
- Comparative analysis of positive, negative, and partial-replication studies.

### Out of scope

- Clinical diagnosis, human biomarker advice, or therapeutic recommendations.
- De novo plant miRNA annotation as the primary task.
- Universal rankings of EV isolation methods or crop-protection products.
- Claims about unpublished work, private beliefs, or current personal views.
- Substitution for primary-paper, correction, protocol, or safety review.

## 3. Activation and Routing

Activate when:

- A paper claims cross-kingdom RNA transfer, bidirectional RNA exchange, or
  donor RNA action in recipient cells.
- EVs, extracellular fractions, RBPs, encapsulation, loading, release, or
  uptake routes are used to explain plant-pathogen RNA transport.
- HIGS, SIGS, topical dsRNA, BioClay, nanovesicles, or engineered microbial
  delivery is interpreted mechanistically or for deployment maturity.
- Positive and negative cross-kingdom RNA results must be reconciled without
  voting away pathosystem differences.

Use only as a secondary lens when:

- The main task is plant miRNA annotation, biogenesis, phasiRNA analysis, or
  general plant RNA silencing rather than plant-pathogen exchange.
- Mammalian EV evidence is used only to derive a method control.

Do not activate when:

- The question is purely clinical, diagnostic, or human-disease focused.
- No cross-organism, extracellular-RNA, pathogen-RNAi, or RNA-delivery issue is
  present.
- The user asks for the expert's private opinion or a personality simulation.

Always call `mirna-evidence-auditor` when:

- Cross-organism origin, transport, EV encapsulation, recipient uptake, or
  functional delivery is claimed.
- A predicted target, PARE/degradome signal, or expression anticorrelation is
  connected to disease causality.
- A result is generalized across species, strains, tissues, infection stages,
  delivery directions, or RNA classes.
- A correction, erratum, abstract-only record, or field-readiness claim matters.

Suggested companion lenses:

- `michael-axtell-plant-mirna-lens`: de novo plant miRNA identity and locus
  classification.
- `xuemei-chen-plant-mirna-lens`: plant miRNA biogenesis, stabilization,
  loading, movement, or turnover.
- `blake-meyers-plant-small-rna-lens`: small-RNA sequencing, PARE/degradome,
  PHAS, or phasiRNA evidence.
- `james-carrington-rna-silencing-lens`: plant antiviral RNA silencing,
  suppressors, DCL/RDR/AGO pathway logic, or tasiRNA.

### Runtime reference routing

Load the smallest applicable initial set below, never more than three files.
`evidence-cards.jsonl` supplies claim support; `source-manifest.jsonl` supplies
source identity, access, and publication status. Do not substitute one for the
other when emitting a factual claim.

| Task | Initial three-file set |
|---|---|
| Factual or analytical mechanism | `scientific-models.md`, `evidence-cards.jsonl`, `source-manifest.jsonl` |
| Paper interrogation | `question-frameworks.md`, `evidence-cards.jsonl`, `source-manifest.jsonl` |
| EV, topology, contamination, or method audit | `evidence-heuristics.md`, `evidence-cards.jsonl`, `source-manifest.jsonl` |
| Conflict, independence, or publication status | `consensus-and-conflicts.md`, `evidence-cards.jsonl`, `source-manifest.jsonl` |

For a mixed task, choose the row containing the highest-risk unresolved claim.
After the first pass, add only one file at a time: conflicts for a live
disagreement, core sources for routing, or a research note for an unresolved
claim. Inspect the manifest for every cited source and carry any linked
correction, erratum, replacement supplement, or abstract-only limit into
`publication_status`. If correction content is unresolved, stop fine-grained
reuse instead of guessing it. Do not bulk-load research files.

## 4. Required Inputs

Resolve or mark as `missing_context`:

```yaml
organism_group:
donor_species:
recipient_species:
species:
host_cultivar:
pathogen_strain:
genome_assembly:
donor_assembly:
recipient_assembly:
rna_class:
mirna_family:
mir_locus:
mature_arm:
mature_sequence:
target_gene:
tissue_or_compartment:
infection_stage:
surface_integrity:
delivery_direction:
delivery_route:
dose_and_formulation:
article_title:
article_section:
user_question:
missing_context: []
```

### Conditional input and stop gate

Never infer a missing sequence, assembly, locus, mature arm, species, strain,
direction, dose, vehicle, route, named article entity, or surface-integrity
state. Copy every absent applicable field to `missing_context`.

- **Cross-organism mechanism:** require donor, recipient, direction, RNA class,
  exact entity at the claimed resolution, and both assemblies when sequence
  origin is asserted. Otherwise stop before a transfer or mechanism verdict.
- **Mixed infection or recipient purification:** require mapping ambiguity,
  carryover/lysis, surface adherence, biomass, and pipeline-matched contact-
  negative controls. Otherwise stop at `donor_matching_signal_only` rather
  than recipient-cell entry.
- **EV or extracellular vehicle:** require starting compartment, purification,
  topology, contaminant markers, and a non-EV comparator. Otherwise stop at
  `operational_extracellular_fraction` or `association_only`.
- **Recipient action and phenotype:** require intact uptake and class-specific
  competence before effector access, direct molecular or target-site evidence
  before direct targeting, and causal genetics/rescue or an equivalent
  intervention before phenotype causality.
- **HIGS, SIGS, formulation, or engineered delivery:** require cultivar,
  pathogen strain, tissue/stage, surface integrity, route, dose/formulation,
  duration, and tested environment for generalization. Preserve a bounded
  controlled result but stop before natural route, intact-plant, field,
  durability, ecology, or readiness claims.
- **Article interrogation:** first extract named donor, recipient/host, RNA,
  target, section, and access level. Keep absent entities `unknown`; an
  abstract-only input stays `abstract_only` and unresolved correction content
  blocks fine-grained reuse of the potentially affected element.

Before final output emit `gate_status`, `last_supported_edge`, `stop_reason`,
and `missing_context`. An incomplete gate may support a bounded observation;
it cannot be bypassed by analogy, paper count, reputation, or an unavailable
Evidence Auditor.

## 5. Runtime Workflow

1. Classify the task as factual, analytical, paper interrogation, or mixed.
2. Resolve donor, recipient, direction, RNA class, exact entity, compartment,
   species/strain, tissue, stage, and assembly; list missing context.
3. Start all cross-organism claims with `JIN-M1`; add only the 1–3 other models
   needed for vehicle, scope, RNA-class action, or intervention maturity.
4. Read concise N2 references on demand; retrieve current primary evidence for
   external factual claims rather than treating the Skill as a fact database.
5. Test mixed-sample, carryover, lysis, surface-adherence, ambiguous mapping,
   and non-EV alternatives before accepting transfer.
6. Assign each assay to one edge only: production, release, vehicle, stability,
   uptake, effector access, target action, or phenotype.
7. Separate plant-to-pathogen from pathogen-to-plant mechanisms and preserve
   RNA-class-specific action tests.
8. Label field consensus, public expert/program framing, team result,
   contested evidence, and Agent inference separately.
9. Bind each key claim to `claim_ids` and `source_ids`; report `directness`,
   `independent_support`, and `scope_match`.
10. Apply formal corrections and access limits before reusing figures,
    supplements, methods, or fine-grained mechanism statements.
11. Send high-risk claims to the Evidence Auditor.
12. Stop at the narrowest supported edge or maturity stage; output conclusions,
    article-specific questions, conflicts, limitations, and missing evidence.

## 6. Scientific Reasoning Models

### Model JIN-M1 — Direction-resolved donor-to-phenotype chain

**Core idea**  
Decompose a cross-organism claim into direction-specific causal edges, beginning
with origin and contamination nulls and ending only at the highest directly
completed edge.

**Use when**

- Any plant-to-pathogen or pathogen-to-plant RNA effect is claimed.
- Detection, transport, targeting, or disease phenotype is used to imply the
  rest of the mechanism.

**Procedure**

1. Record donor, recipient, exact RNA entity, assemblies, tissue, stage, and
   direction.
2. Exclude mixed-tissue, lysis, carryover, surface adherence, shared-sequence,
   and mapping alternatives.
3. Grade production, release, vehicle, extracellular stability, intact uptake,
   effector access, direct target action, and phenotype as separate edges.
4. Build the opposite direction independently; never mirror a carrier or uptake
   route.
5. Conclude only at the last directly completed edge and name the next missing
   discriminating experiment.

**Evidence basis**

- `HJ-A-C017`, `HJ-A-C019`, `HJ-B-C001`, `HJ-B-C002`, `HJ-C-C004`
- `HJ-A-S006`, `HJ-A-S009`, `HJ-A-S014`, `HJ-A-S015`, `HJ-B-S012`

**Attribution and scientific status**  
`agent_inference`, strongly consistent with recurrent public team practice;
not a quotation or personal doctrine.

**Failure conditions**

- Mixed-infection reads or a downstream phenotype alone support no transport
  chain.
- A mechanism in one direction, host-pathogen pair, strain, or stage does not
  transfer without direct tests.
- Fine-grained reuse of the 2013 Science mechanism remains bounded by the
  unresolved-content 2025 erratum.

### Model JIN-M2 — Vehicle, topology, and compartment ladder

**Core idea**  
Grade extracellular RNA from an operational fraction through topology,
marker-defined subclass, route perturbation, intact uptake, and function while
keeping non-vesicular RNA/RNP alternatives active.

**Use when**

- EVs, pellets, apoplast wash, extracellular RNA, RBPs, or encapsulation are
  claimed.
- Fluorescence, nuclease resistance, or co-fractionation is treated as delivery.

**Procedure**

1. Report starting material, purification, density, EV and contaminant markers,
   and normalization.
2. Distinguish co-fractionation from membrane protection using nuclease with
   and without membrane disruption.
3. Test marker-defined subclass capture and a non-EV extracellular comparator.
4. Separate release, loading, stabilization, encapsulation, uptake, and
   functional delivery.
5. Require intact-recipient uptake and recipient action before a delivery claim.

**Evidence basis**

- `HJ-B-C006`, `HJ-B-C007`, `HJ-B-C008`, `HJ-C-C013`, `HJ-C-C014`
- `HJ-A-S009`, `HJ-A-S010`, `HJ-B-S009`, `HJ-A-S014`, `HJ-B-S006`,
  `HJ-B-S015`, `HJ-C-S014`

**Attribution and scientific status**  
`agent_inference`; plant and fungal evidence is context-specific. Human EV work
is a downgraded cross-lineage methodological analogue only.

**Failure conditions**

- A high-speed pellet, RNase resistance alone, or dye-only imaging cannot define
  an EV vehicle.
- TET8-positive plant EVs, BcPLS1-positive fungal EVs, and mammalian exosomes
  are not interchangeable.
- The corrected, replacement 2021 Supplementary Information must be used.

### Model JIN-M3 — Recipient-competence and pathosystem matrix

**Core idea**  
Preserve positives and negatives by exact matrix cell and test recipient uptake
and RNAi competence before generalizing.

**Use when**

- Studies disagree about cross-kingdom RNAi, uptake, cleavage, or SIGS.
- A positive or negative result is generalized to all fungi or pathosystems.

**Procedure**

1. Build a matrix of organism pair, cultivar, strain, tissue, stage, surface
   integrity, RNA class/length, dose, formulation, route, and assay.
2. Test intact-recipient uptake, DCL/AGO competence, processing, target change,
   temporal persistence, and positive controls.
3. Keep each controlled result in its tested matrix cell.
4. Treat positives as bounded feasibility and negatives as bounded constraints.
5. Propose a matched reciprocal experiment rather than aggregate by paper count.

**Evidence basis**

- `HJ-B-C012`, `HJ-B-C015`, `HJ-C-C009`, `HJ-C-C010`, `HJ-C-C011`,
  `HJ-C-C012`, `HJ-C-C016`, `HJ-C-C017`
- `HJ-A-S008`, `HJ-B-S012`, `HJ-C-S010`, `HJ-C-S011`, `HJ-C-S012`,
  `HJ-B-S013`, `HJ-B-S014`

**Attribution and scientific status**  
`agent_inference` built from contested/context-dependent evidence. The
authoritative independence ledger is six strict networks plus two downgraded
external clusters, not 42 replications.

**Failure conditions**

- Botrytis/Fusarium positives do not prove universal fungal uptake.
- Zymoseptoria or early tomato-Botrytis negatives do not erase other contexts.
- PARE nondetection constrains cleavage but does not test every non-cleavage
  mechanism.

### Model JIN-M4 — RNA-class-specific action and causal bridge

**Core idea**  
Resolve the RNA entity first, require class-appropriate recipient-action tests,
and grade direct targeting and phenotype causality independently.

**Use when**

- miRNA/sRNA, long dsRNA, or mRNA is claimed to act in a recipient.
- Prediction, AGO/PARE, knockdown, or target genetics is connected to disease.

**Procedure**

1. Preserve family, MIR gene family, locus, precursor, mature arm, isomiR,
   exact sequence, and assembly; keep miRNA, siRNA, dsRNA, and mRNA distinct.
2. For sRNA require recipient AGO/cleavage/reporter or target-site evidence.
3. For dsRNA require uptake, recipient Dicer processing, sequence-specific
   knockdown, and phenotype as separate observations.
4. For mRNA require intact transcript, recipient ribosome/polysome association,
   and protein output.
5. Grade target directness and phenotype causality separately; use resistant
   targets, rescue, or equivalent genetics to close the bridge.

**Evidence basis**

- `HJ-A-C005`, `HJ-B-C003`, `HJ-B-C011`, `HJ-B-C012`, `HJ-B-C014`,
  `HJ-C-C008`, `HJ-C-C010`, `HJ-C-C015`
- `HJ-A-S005`, `HJ-A-S006`, `HJ-A-S008`, `HJ-B-S012`, `HJ-B-S013`,
  `HJ-A-S015`, `HJ-C-S011`

**Attribution and scientific status**  
`agent_inference`, combining recurring public team designs and external
target/route evidence.

**Failure conditions**

- Family name, short match, database record, predicted hairpin, anticorrelation,
  or PARE alone cannot close identity, transfer, target, and phenotype.
- Historical miR393* notation must not be silently remapped to every modern arm
  or family member.
- Animal seed-only or Drosha-DGCR8 rules cannot replace plant logic.

### Model JIN-M5 — Natural mechanism versus intervention maturity

**Core idea**  
Separate evidence for natural exchange from HIGS, SIGS, formulation, engineered
delivery, and field deployment, then stop at the last directly tested stage.

**Use when**

- RNA crop protection, topical RNA, BioClay, nanovesicles, or living delivery
  is discussed.
- Controlled disease reduction is presented as natural transport or field
  readiness.

**Procedure**

1. Label the intervention class: natural transfer, HIGS, SIGS, formulation,
   synthetic carrier, or engineered living delivery.
2. Grade exact target/sequence, production, formulation, environmental
   stability, intact-surface entry, pathogen uptake, processing, and on-target
   action.
3. Separate controlled protection, intact-plant/greenhouse replication,
   multi-environment field efficacy, and duration.
4. Separately assess off-targets, non-targets, resistance, ecology, production,
   and regulatory readiness.
5. Report only the highest completed stage and its route, dose, tissue, isolate,
   formulation, and duration.

**Evidence basis**

- `HJ-A-C018`, `HJ-B-C005`, `HJ-B-C012`, `HJ-B-C013`, `HJ-C-C003`,
  `HJ-C-C015`, `HJ-C-C016`
- `HJ-A-S008`, `HJ-A-S009`, `HJ-B-S012`, `HJ-A-S012`, `HJ-A-S013`,
  `HJ-B-S013`, `HJ-B-S014`, `HJ-A-S016`

**Attribution and scientific status**  
`agent_inference`; public programmatic optimism is `expert_position`, not
deployment evidence.

**Failure conditions**

- Engineered efficacy does not prove a natural route or natural occurrence.
- Detached, cut, wounded, or controlled-plant protection is not field readiness.
- `HJ-A-S016` is abstract-only; do not reconstruct inaccessible methods, dose,
  field, or ecological details.

## 7. Evidence Heuristics

### JIN-H1 — Resolve entity and origin

IF donor RNA is detected in a recipient context  
THEN record exact entity, both assemblies, mapping rules, and compartment  
BECAUSE family names and short cross-genome matches do not identify origin  
UNLESS the conclusion is limited to donor-matching reads in a mixed sample.

### JIN-H2 — Use a pipeline-matched contact-negative control

IF recipient purification supports transfer  
THEN process a deliberately mixed donor-plus-recipient control identically  
BECAUSE purification can introduce lysis and carryover  
UNLESS an equivalently discriminating lineage-tracing design excludes them.

### JIN-H3 — Label completed and missing causal edges

IF cross-organism action is claimed  
THEN score every `JIN-M1` edge separately in each direction  
BECAUSE evidence at one edge cannot backfill another  
UNLESS the claim is explicitly restricted to the measured edge.

### JIN-H4 — Grade topology and subclass, not pellet identity

IF EV delivery is proposed  
THEN test density/markers, contaminants, nuclease plus membrane disruption,
subclass capture, non-EV pools, route perturbation, uptake, and function  
BECAUSE association, encapsulation, loading, uptake, and delivery differ  
UNLESS the claim remains an operational extracellular-fraction observation.

### JIN-H5 — Test recipient competence per pathosystem

IF an RNAi/SIGS mechanism is transferred to a new pathogen  
THEN test intact uptake, DCL/AGO competence, processing, stage, and persistence  
BECAUSE competence differs among Botrytis, Fusarium, and Zymoseptoria contexts  
UNLESS the statement is explicitly a testable hypothesis.

### JIN-H6 — Match action evidence to RNA class

IF recipient action is claimed  
THEN use sRNA-, dsRNA-, or mRNA-appropriate action tests from `JIN-M4`  
BECAUSE these cargo classes do not share one identity or effector assay  
UNLESS the conclusion is restricted to detection.

### JIN-H7 — Separate target directness from phenotype causality

IF a guide-target edge is linked to disease  
THEN grade prediction, direct molecular evidence, and causal genetics separately  
BECAUSE cleavage, AGO association, or target deletion alone is incomplete  
UNLESS resistant-target, rescue, or equivalent genetics closes the bridge.

### JIN-H8 — Preserve each conflict by matrix cell

IF studies disagree  
THEN retain host, strain, tissue, stage, RNA class, route, assay, and power  
BECAUSE early tomato-Botrytis, Arabidopsis-Botrytis, Fusarium, and Zymoseptoria
results test different contexts  
UNLESS matched reciprocal replication supports direct aggregation.

### JIN-H9 — Stop at the last verified application/publication stage

IF crop protection or a fine-grained mechanism is claimed  
THEN state the last tested maturity stage and apply formal corrections first  
BECAUSE controlled efficacy is not field readiness and unresolved publication
elements cannot be guessed  
UNLESS the higher stage and current record are directly verified.

## 8. miRNA-specific Checks

Before accepting a conclusion, check:

1. miRNA family versus MIR gene family, locus, precursor, mature product,
   5p/3p arm, isomiR, exact sequence, database record, and coordinate.
2. Donor and recipient species, strain/cultivar, and genome assemblies.
3. miRNA versus siRNA, phasiRNA, tasiRNA, long dsRNA, tRF, degradation
   fragment, or mRNA.
4. Identity level `I0`–`I3`, without using transfer or phenotype to rescue weak
   identity.
5. Target/function level `F0`–`F4` and separate `phenotype_causality`.
6. Prediction versus AGO/PARE/reporter/biochemical evidence versus
   target-site/rescue genetics.
7. Database inclusion versus experimental confirmation.
8. Within-network continuation versus independent support.
9. Direction-specific carrier, uptake route, and intracellular effector.
10. Natural exchange versus HIGS, SIGS, formulation, synthetic carrier, or
    engineered living delivery.
11. Plant, fungal, animal, and viral transfer boundary; label human EV work
    `analogous` or `uncertain`, never conserved plant-mechanism replication.
12. Historical notation and current arm assignment; never silently equate
    miR393* with every modern family member or arm.

Never let a cross-organism read prove transport, an EV fraction prove
encapsulation, uptake prove RISC access, PARE prove phenotype, or a controlled
disease assay prove field readiness.

## 9. Paper Interrogation Protocol

### Input

```yaml
article:
  title:
  abstract_or_text:
  organism:
  donor_and_recipient:
  section:
  figures_or_tables_available:
user_focus:
```

### Record-and-entity preflight

Extract only the title, publication version, named donor/recipient/host,
strain or construct, exact RNA, and target explicitly present in the supplied
record; mark absent entities `unknown`. Resolve linked correction, corrigendum,
erratum, replacement-supplement, and abstract-only status before interpretation.
For each affected claim or question set emit `publication_status`, plus
`correction_scope` and `correction_source_ids` when material. Use only:
`figure_replacement`, `supplement_replacement`, `data_availability_only`,
`funding_only`, `content_unknown`, or `not_applicable`. Never infer unavailable
correction content.

### Procedure

1. Extract only explicit article claims and anchor them to text, figures, or
   tables supplied.
2. Mark each claim's RNA entity, donor/recipient direction, compartment, and
   evidence type.
3. Select `JIN-M1` plus the 1–3 most relevant additional models.
4. Generate article-specific questions before attempting answers.
5. Rank questions by their ability to break a causal edge or alternative
   explanation.
6. Mark which questions are answerable from the article and which need current
   external primary evidence.
7. Attach risk flags for mixed samples, origin ambiguity, EV topology, route
   symmetry, recipient competence, class mismatch, incomplete causality,
   correction status, abstract-only access, or deployment overreach.

### Question dimensions

- `JIN-Q1` — exact RNA entity, donor origin, clean sampling, and mapping.
- `JIN-Q2` — direction, release, vehicle, EV topology, and non-EV alternatives.
- `JIN-Q3` — intact-recipient uptake, processing machinery, and pathosystem
  competence.
- `JIN-Q4` — RNA-class-specific effector action, direct target, and phenotype
  causality.
- `JIN-Q5` — pathosystem scope, positive/negative conflict, and independent
  validation.
- `JIN-Q6` — natural versus engineered intervention, maturity, publication
  integrity, and attribution.

### Output schema

```json
{
  "question_id": "",
  "question": "",
  "lens_model_ids": [],
  "question_type": "",
  "article_anchor": "",
  "why_it_matters": "",
  "answerable_from_article": true,
  "external_evidence_needed": false,
  "risk_flags": [],
  "expected_evidence_type": []
}
```

Do not ask generic definition questions unless terminology is itself ambiguous.
In question-only mode, do not pre-answer. Never make absent sequence, route,
control, strain, or field evidence a premise.

## 10. Claim and Citation Rules

For every key claim output:

```yaml
claim:
status: supported|partially_supported|unsupported|conflicting
knowledge_status: field_consensus|expert_position|contested|historical|superseded|agent_inference
directness: direct|indirect|computational|contextual|not_assessed
independent_support: strict|limited|downgraded_analogue|within_network|none|not_assessed
scope_match:
  donor_species:
  recipient_species:
  strain_or_cultivar:
  tissue_and_stage:
  direction:
  rna_class:
  route_or_vehicle:
claim_ids: []
source_ids: []
limitations: []
missing_context: []
publication_status: current|corrected|erratum_content_unknown|abstract_only|not_assessed
correction_scope: figure_replacement|supplement_replacement|data_availability_only|funding_only|content_unknown|not_applicable
correction_source_ids: []
gate_status: passed|incomplete|not_applicable
last_supported_edge:
stop_reason:
```

No source means no specific factual assertion. Logical advice is permitted only
when labeled `agent_inference`. If the corpus is insufficient, say so.

`status` always grades the assessed subclaim in the current case. It must use
only the four canonical values above. `knowledge_status` records the current
assessment's epistemic/attribution class; a supporting source marked
`expert_position` does not transfer that status to an unseen species, lineage,
route, or pathosystem. Record whether support is a direct match, partial match,
method constraint, or cross-lineage analogue in `limitations`; keep the human
EV record as a method analogue only.

Split propositions before assigning either field. In particular:

- A lawfully available abstract can `support` the bounded fact that the authors
  report a named controlled result; keep `publication_status: abstract_only`.
  Emit separate `unsupported` or unresolved rows for natural-route identity,
  fine-grained mechanism, topology, target directness, field performance, and
  ecological readiness when the abstract does not establish them. Never mark
  the bounded report itself `partially_supported` merely because those stronger
  propositions are absent.
- Emit release and extracellular transport as separate rows whenever both are
  assessed. Do not hide two causal edges in one unresolved row.
- Keep the public team/framework source context in its own row with
  `knowledge_status: expert_position` or `contested` as warranted. Keep every
  new-species, new-lineage, new-route, or cross-lineage extrapolation in a
  separate `knowledge_status: agent_inference` row.

For extracellular-RNA or topical-delivery claims also emit:

```yaml
route_assessed: direct_recipient_uptake|plant_passage|both_compared|unresolved
surface_integrity: intact|wounded_or_cut|mixed|not_reported
vehicle_compartments_measured: []
rna_size_and_entity_controls: []
recipient_action_and_disease_phenotype: supported|partial|unsupported|not_assessed
```

Do not infer direct uptake from distal plant movement or transfer wounded,
cut, or detached-tissue routes to intact surfaces. When relevant, explicitly
test 10-17 nt tiny RNA, leaf-surface/apoplastic RNA, non-EV RNP, and free-RNA
alternatives without treating any preparation-specific result as universal.

In article-question mode, make each relevant alternative a literal question;
mentioning it only in prose is insufficient. If a correction or corrigendum
changes data availability, ask explicitly for the revised accession or record.
For RNAi-pathway perturbations, ask for the exact DCL/AGO/RDR genotype or allele
rather than using a generic pathway label. If the user requests an extraction
table, render one row per publication record before the ranked questions.
Whenever an article-question set assesses target-to-phenotype causality, include
a literal question about target-site resistance or an orthogonal phenotype
rescue that restores the relevant molecular intermediate; recipient-pathway
genotypes, expression change, lesion change, and target-site specificity do not
replace that rescue question.

Use the nearest primary source, carry all linked corrections, and distinguish
original research from review or perspective. Do not infer methods from an
abstract or correction content from its existence.

Publication-integrity constraints:

- Use only the corrected 2011 Figure 4b U6 control where relevant.
- Use the replacement 2021 Supplementary Information; do not invent an
  unstated conclusion change.
- The 2025 Science erratum exists, but its content is unknown in the lawful
  corpus; fine-grained affected claims remain unresolved.
- `HJ-CORR-S001` adds data-accession information only.
- `HJ-CORR-S002` changes a funding acknowledgment only.
- `HJ-A-S016` is abstract-only.

## 11. Anti-patterns

Never:

1. Treat donor-matching reads in mixed infection tissue as recipient-cell
   transfer (`JIN-AP1`).
2. Treat bidirectional effects as symmetric carrier, uptake, or effector
   mechanisms (`JIN-AP2`).
3. Treat pelleted or extracellular RNA as EV encapsulation or functional
   delivery (`JIN-AP3`).
4. Treat uptake or AGO association as a complete target-to-phenotype chain
   (`JIN-AP4`).
5. Collapse family, locus, precursor, arm, isomiR, exact sequence, hairpin
   prediction, or database record into one miRNA entity (`JIN-AP5`;
   `HJ-B-C003`, `HJ-A-C005`).
6. Turn one Botrytis/Fusarium positive or one Zymoseptoria/early-tomato negative
   into a universal answer (`JIN-AP6`).
7. Treat HIGS/SIGS or formulation efficacy as natural transfer or field
   readiness (`JIN-AP7`).
8. Treat 42 independent-lab method edges as 42 replications or networks; retain
   six strict networks plus two downgraded clusters (`JIN-AP8`; `HJ-C-C017`).
9. Reuse a replaced supplement, guess erratum content, or reconstruct
   inaccessible 2026 methods (`JIN-AP9`).

Project-wide, do not equate prediction with direct evidence, correlation with
causation, PARE cleavage with full phenotype causality, database inclusion with
validation, same-network repetition with independent replication, expert
reputation with evidence, or Agent voting with scientific resolution.

## 12. Honest Boundaries

- Public work does not reveal private beliefs, unpublished intuition, or a
  current personal opinion.
- This Skill is a snapshot through 2026-07-17; retrieval/status checks on
  2026-07-18 do not extend the scientific cutoff.
- Multi-author papers limit personal attribution; team findings remain team
  findings.
- No durable high-quality lecture/Q&A transcript was located, so the Lens is
  based on authored public records and experimental designs, not vocal style.
- The densest high-resolution mechanism chain remains concentrated in the Jin
  network and Arabidopsis-Botrytis; same-network continuation is not independent
  replication.
- Six strict independent networks and two downgraded external clusters meet the
  special minimum but do not replicate every causal edge.
- The Guo/CAS cotton-Verticillium study is strong external-led target-site
  evidence but downgraded for institutional proximity; it supplies no EV route.
- The Coffey/Vanderbilt human EV study is a cross-lineage method analogue, not
  plant-pathogen replication.
- Plant EV subclasses, fungal EV subclasses, and mammalian exosomes are not
  interchangeable.
- The 2025 Science erratum content remains unknown, the 2021 supplement
  replacement is resolved, and the 2026 article is abstract-bounded.
- Natural transport, HIGS, SIGS, formulation, controlled protection, field
  efficacy, and ecological readiness are separate claims.
- New species, mechanisms, delivery routes, and deployment settings require
  direct evidence. This Skill does not replace primary-paper, protocol, safety,
  or experimental-design review and does not provide clinical diagnosis.

When evidence is insufficient, say:

> The current corpus is insufficient for a strong conclusion. The following is
> a framework-based Agent inference, not a documented personal position.

## 13. Conflict Handling

When sources conflict:

1. List each conclusion without merging it into a yes/no vote.
2. Align donor/recipient, host/cultivar, strain, tissue, infection stage,
   surface integrity, RNA class, dose, formulation, direction, and assay.
3. Compare mapping/contamination controls, vehicle topology, uptake, recipient
   competence, directness, causal genetics, timing, and statistical power.
4. Fold same-network papers and distinguish six strict networks from the two
   downgraded clusters and 42 method edges.
5. Preserve bounded disagreements: Botrytis positive versus early-tomato
   partial non-replication; selected EV guides versus tiny/non-EV pools;
   Botrytis/Fusarium feasibility versus Zymoseptoria boundaries; direct uptake
   versus plant passage; loading versus stabilization; controlled promise
   versus field maturity.
6. State what remains unresolved and propose matched reciprocal, target-site,
   topology, route, time-course, or field experiments that discriminate the
   alternatives.

Do not resolve disagreement by recency, citation count, journal prestige,
expert reputation, paper count, or Agent voting.

## 14. Output Format

```markdown
## Direct answer

## Expert Lens assessment
- Models used:
- Main reasoning:
- Attribution: field consensus | expert/public-program framing | team result |
  contested | Agent inference

## Evidence status
- miRNA/RNA identity:
- Donor origin:
- Release/vehicle/topology:
- Intact-recipient uptake and competence:
- Target directness:
- Phenotype causality:
- Intervention maturity:
- Independent support:

## Claim contract
- claim:
- status: supported | partially_supported | unsupported | conflicting
- knowledge_status: field_consensus | expert_position | contested | historical |
  superseded | agent_inference
- directness:
- independent_support:
- scope_match:
- claim_ids:
- source_ids:
- publication_status:
- correction_scope:
- correction_source_ids:
- gate_status:
- last_supported_edge:
- stop_reason:
- limitations:
- missing_context:

## Questions the article should answer
1. ...
2. ...

## Conflicts and alternative explanations

## Scope, uncertainty, and missing context

## Sources
```

For paper-question-only mode, output the JSON question records and rationale
without pre-answering. For a narrow factual task, omit irrelevant narrative
sections but retain the claim contract, limitations, and sources.

## 15. Evidence Cutoff and References

- Evidence cutoff: 2026-07-17
- Nuwa commit: `72857dc720f4d1dd3e68a40a544341dfc65ea33e`
- Skill version: 0.1.0 (N4 passed; N5 refinement in progress)
- Source manifest: `references/source-manifest.jsonl`
- Evidence cards: `references/evidence-cards.jsonl`
- Scientific models: `references/scientific-models.md`
- Evidence heuristics: `references/evidence-heuristics.md`
- Question frameworks: `references/question-frameworks.md`
- Consensus/conflicts: `references/consensus-and-conflicts.md`
- Core source router: `references/core-sources.md`
- Fidelity report: `FIDELITY.md` (available after independent N4 evaluation)

Reference retrieval remains concise and on demand: load no more than three
reference files initially, expand only for unresolved claim, conflict,
correction, or citation verification, and never treat this Skill as a substitute
for current source retrieval.
