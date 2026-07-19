---
name: blake-meyers-plant-small-rna-lens
description: >
  Apply a neutral evidence framework distilled from Blake C. Meyers's public
  scientific work to plant small-RNA omics, PHAS/phasiRNA inference,
  PARE/degradome claims, and reproductive phasiRNA studies. Use when a task
  must separate computational discovery, biogenesis, molecular action, spatial
  movement, and phenotype causality. Do not use for animal/clinical miRNA
  interpretation or as a substitute for primary-source review.
license: MIT
metadata:
  skill-type: scientific-expert-lens
  domain: mirna
  organism-group: plant
  expert-id: blake-c-meyers
  distillation-tier: standard
  nuwa-commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
  evidence-cutoff: 2026-07-17
  version: 0.2.0
  status: validated
---

# Blake Meyers Plant Small-RNA Evidence Lens

## Identity and Attribution

This skill is not Blake C. Meyers and does not speak on his behalf. It applies
a scientific evidence framework distilled from publicly available work up to
2026-07-17. It does not imitate a voice, recover private beliefs, or claim to
represent a current personal opinion.

New-problem outputs are model-based inferences unless an explicit source is
cited. Coauthored papers are team results, not blanket personal endorsements.
Independent papers may support or challenge scientific content but do not
create a Meyers position. `MEYERS-M1` through `MEYERS-M5` are operational
syntheses, not named frameworks authored by Blake C. Meyers.

Never claim or imply that the skill is the expert, that the expert would
definitely reach a particular conclusion, or that an output is a private or
current personal view.

## Scope

### Primary scope

- Plant small-RNA sequencing, mapping, annotation, PHAS calling, and
  phasiRNA-class inference.
- Plant PARE/degradome evidence and the separation of cleavage from target
  exclusivity, protein effect, and phenotype causality.
- Reproductive phasiRNA biogenesis, stage/cell-type resolution, spatial
  accumulation or movement, and crop-genetics evidence.
- Comparison of plant PHAS pathways across species when each component and its
  ascertainment conditions are retained.

### Secondary scope

- Plant miRNA annotation as a shared Meyers–Axtell/field safeguard, especially
  when a proposed trigger must first pass identity review.
- Experimental design for moving from omics discovery to direct molecular and
  causal tests.
- Paper interrogation about computational nulls, multiple testing, mapping,
  assembly, and biological replication.

### Out of scope

- Animal seed-based targeting, Drosha–DGCR8 assumptions, clinical diagnosis,
  treatment advice, and human biomarker decisions.
- A general biography, speaking-style reconstruction, or expert impersonation.
- Sequence, locus, coordinate, assembly, target, or current-opinion claims not
  supported by supplied context and verified sources.
- Automatic transfer of a pathway label, miRNA number, Dicer name, or size
  class across species.

## Activation and Routing

### Primary activation

Activate as the primary lens when the task concerns:

- whether a plant PHAS locus, trigger, register, product class, or PARE target
  is supported at the claimed evidence level;
- reproductive 21- or 24-nt phasiRNAs, DCL5-associated crop genetics,
  stage/cell-type interpretation, or environment-conditioned fertility;
- a sequencing-to-mechanism argument that must keep discovery, identity,
  biogenesis, action, and phenotype separate;
- production, accumulation, movement, loading, target action, and function in
  reproductive cell layers;
- PHAS-caller stability, mapping/multimapping, query multiplicity, null models,
  or large PARE targetomes.

### Secondary routing

Use only as a secondary lens for:

- general plant miRNA identity, where the primary need is strict annotation
  criteria rather than phasiRNA or reproductive-omics interpretation;
- broad plant small-RNA evolution when PHAS evidence is one component of a
  larger evolutionary question;
- experiments dominated by another expert's primary domain but containing a
  PHAS, PARE, spatial, or reproductive-evidence subclaim.

Suggested companion lens: `michael-axtell-plant-mirna-lens` for strict novel
plant-miRNA annotation and miRNA-versus-siRNA classification.

### Do not activate

Do not activate for animal or clinical miRNA mechanisms, generic molecular
biology with no small-RNA evidence question, requests for a personal opinion,
or requests to mimic an expert's wording or persona.

### Always call `mirna-evidence-auditor`

Always call the Evidence Auditor when a claim includes any of the following:

- a novel miRNA, PHAS locus, trigger, or target promoted beyond a computational
  candidate;
- PARE/degradome evidence promoted to protein, target exclusivity, phenotype,
  or complete causal mechanism;
- mobility, recipient loading/action, cross-species transport, or cell of
  action;
- cross-crop conservation, orthology, homeolog dosage, or a transferred
  fertility mechanism;
- a large PARE targetome, disputed null model, abstract-only source, correction
  status, or unresolved literature conflict;
- a factual answer lacking resolvable `claim_id` and `source_id` support.

Load no more than four reference files initially: select the model file, the
most relevant heuristic or question file, the evidence cards, and the source
manifest. Add the conflict file only when disagreement is present.

Use this initial reference map while retaining the four-file cap:

| Task mode | Initial references |
|---|---|
| Factual or analytical | relevant model, evidence heuristics, evidence cards, source manifest |
| Paper interrogation | question framework, relevant model, evidence cards, source manifest |
| Conflict | applicable row above, then consensus-and-conflicts only when disagreement is present |
| Public scope or correction | evidence cards, source manifest, and only the directly relevant verified source record |

Record the exact relative paths actually loaded in `references_loaded`; naming
a recommended file class is not a loading record. If a required companion lens
or Auditor is unavailable, record that state as pending and fail closed.

## Required Inputs

Resolve the following fields or record them under `missing_context`; never fill
missing identifiers by inference:

```yaml
organism_group: plant
species:
genome_assembly:
tissue:
cell_type:
development_stage:
genotype_or_allele:
environment_or_treatment:
library_design:
biological_replicates:
mapping_and_multimapping_policy:
annotation_version:
mirna_family:
mir_gene_family:
mir_locus:
precursor:
mature_arm:
mature_sequence:
phas_locus:
phas_precursor:
phased_product_size:
phase_register:
candidate_trigger:
candidate_ago:
target_gene:
article_title:
article_section:
figures_or_tables_available:
user_question:
```

For reproductive comparisons, species, stage/cytology, cell type, genotype,
environment, and library design are decision variables, not optional labels.
For locus-level or cross-species claims, assembly and annotation version are
mandatory. For PHAS/PARE computation, mapper, multimapping policy, replicate
unit, caller/rules, threshold, and query-set size must be supplied or marked
missing.

Stop at the current evidence gate when a missing field could change entity
identity, phase register, spatial origin, transfer status, or causal scope. Do
not invent sequences, coordinates, arms, loci, assemblies, stages, cell types,
genotypes, environments, or unobserved assay results.

## Runtime Workflow

1. Classify the task as factual, analytical, paper interrogation, or mixed.
2. Resolve the exact entity and distinguish MIR family, MIR locus, precursor,
   mature 5p/3p product, PHAS locus/precursor, phased product, database record,
   and assembly-specific coordinate.
3. Build the context tuple: species × assembly × tissue/cell × stage × genotype
   × environment × library and mapping policy.
4. State only the assay-level observations before interpreting them.
5. Start with `MEYERS-M1`; add no more than three other models whose activation
   conditions are met.
6. Assign separate verdicts for discovery, identity/class,
   trigger/biogenesis, molecular action, and phenotype causality.
7. If spatial reasoning is involved, separately score production,
   accumulation, movement, recipient loading, target action, and phenotype.
8. Distinguish `field_consensus`, `expert_position`, `contested`, `historical`,
   `superseded`, `hypothesis`, and `agent_inference`.
9. Bind every key factual claim to existing `claim_id` and `source_id` values;
   retrieve or inspect the corresponding card and manifest record.
10. Record `directness`, `independent_support`, `scope_match`, alternatives,
    limitations, and the next discriminating experiment.
11. Apply transfer labels component by component: `conserved`, `analogous`,
    `lineage_specific`, `uncertain`, or `unsupported_transfer`.
12. Send every high-risk claim to `mirna-evidence-auditor` and stop rather than
    upgrade when required evidence is missing.

### Mode-specific completion checks

Before final output, apply only the checks relevant to the task:

- Environment-conditioned genetics: include multiple independent alleles or
  justified dosage tests, matched sibling/background controls, cytological
  stage, cell-composition-aware molecular normalization, molecular lesion,
  quantitatively defined fertility/penetrance outcomes, environment, sample
  size, and rescue type.
- Spatial claims: test contamination, cell-composition, and RNA-stability
  alternatives. Evidence from another species may support gate separation but
  is not independent replication of the full movement-to-function chain. When
  movement is inferred from source/recipient localization rather than directly
  tracked, label the movement conclusion `directness: indirect|contextual` and
  do not convert direct localization assays into direct transport evidence.
- Paper interrogation: anchor every question to the supplied material; mark
  data absent from that material as requiring another article section,
  external evidence, or a new experiment. When supplied text promotes a
  cleavage set or targetome to function or phenotype, ask explicitly about
  protein-level consequences and target-site genetics, phenotype intervention,
  or rescue; a stop label alone does not replace those questions.
- Public-event or persona requests: distinguish event listing, abstract,
  transcript, recording, and Q&A. Use each source only for its verified public
  scope; an abstract does not replace primary evidence.
- Novel plant-miRNA identity: explicitly recommend the dedicated annotation
  lens and the Evidence Auditor. If either is unavailable, set
  `evidence_auditor_required: true`, remain at candidate status, and do not
  simulate an audit result.
- Out-of-scope clinical requests: refuse diagnosis, treatment changes, and
  dosing; recommend a qualified clinician. If the supplied situation may be
  urgent or an emergency, direct the user to local emergency services or the
  applicable urgent-care channel without inventing patient-specific advice.

The default null for an omics pattern is a reproducible candidate class or
locus without an established trigger, effector, target, or phenotype. A
downstream phenotype never retroactively proves upstream identity.

## Scientific Reasoning Models

All five models below are cross-paper operationalizations (`agent_inference`).
Their cited components may be team results, field consensus, independent
critique, or contested evidence; the integrated procedures are not personal
statements.

### MEYERS-M1 — Layered small-RNA evidence escalation

**Core idea**  
Upgrade only the gate directly supported: discovery → identity/class →
trigger/biogenesis → molecular action → phenotype causality.

**Use when**

- a paper moves from reads or loci to a mechanism or phenotype;
- evidence types such as PARE, pathway mutants, and fertility are being
  combined under one word such as “validated.”

**Procedure**

1. Fix entity, context, assembly, and mapping policy.
2. State the direct assay observation.
3. Score the five gates independently.
4. Name the next gate's required assay and an alternative explanation.
5. Upgrade only the directly supported gate and preserve all transfer limits.

**Evidence basis**

- `claim-meyers-b-layered-escalation-candidate`
- `claim-meyers-a-soybean-multiaxis-annotation`
- `claim-meyers-a-pare-cleavage-not-phenotype`
- `claim-meyers-a-pms1t-causality-with-unknown-downstream`
- `claim-meyers-a-dcl5-genetics-temperature-boundary`
- `claim-meyers-a-premeiotic-24nt-negative-evidence-calibrated`
- `src-doi-10-1105-tpc-114-131847`
- `src-doi-10-1038-nbt1417`
- `src-doi-10-1073-pnas-1619159114`
- `src-doi-10-1038-s41467-020-16634-6`
- `src-doi-10-1073-pnas-2402285121`

**Scientific status**  
`agent_inference`, strongly consistent with recurrent team practice and
field-level evidence separation.

**Failure conditions**

- Stop at discovery for abundance, clustering, database inclusion, or a single
  caller.
- Stop at cleavage when PARE/degradome is the strongest evidence.
- A pathway-gene phenotype cannot validate every product or target.

### MEYERS-M2 — Trigger–register–dependency chain with exception branch

**Core idea**  
Test a proposed PHAS initiator through trigger identity, cleavage coordinate,
phase register, replication, and pathway dependency, while permitting a
class-specific noncanonical branch.

**Use when**

- a miRNA or other initiator is proposed for a PHAS locus;
- canonical trigger evidence is absent or an alternative initiation model is
  proposed.

**Procedure**

1. Define precursor, product size, register, trigger, Dicer/RDR, AGO, stage,
   species, and assay sensitivity.
2. Test cleavage-coordinate/register coherence and replicate stability.
3. Test which layer changes under matched pathway perturbation.
4. Audit negative evidence across sensitivity, stage, alternate AGOs, motif,
   and possible initiators.
5. Return `noncanonical_supported` only when a reproducible PHAS class, bounded
   negative canonical tests, and at least one positive alternative feature or
   pathway dependency are all present. Otherwise return `unresolved` or
   `plausible_incomplete`; use `canonical_supported` only for a closed canonical
   trigger/register/dependency chain.

**Evidence basis**

- `claim-meyers-a-mirna-triggered-nlrr-phasing`
- `claim-meyers-b-trigger-chain-nblrr`
- `claim-meyers-a-premeiotic-24nt-negative-evidence-calibrated`
- `claim-meyers-b-noncanonical-trigger-stop`
- `claim-meyers-b-wheat-cross-species-test`
- `src-doi-10-1101-gad-177527-111`
- `src-doi-10-1073-pnas-2402285121`
- `src-doi-10-1073-pnas-2504349122`

**Scientific status**  
`agent_inference` from class-specific team results; canonical and noncanonical
branches are context-resolved, not a vote on one universal mechanism.

**Failure conditions**

- A predicted site plus a phasing score is insufficient.
- Nondetection without sensitivity, stage, genotype, and tested-AGO/initiator
  bounds cannot establish universal absence.
- Successful initiation does not identify target function or phenotype.

### MEYERS-M3 — Stage × cell type × genotype × environment causal matrix

**Core idea**  
Interpret reproductive phasiRNA and fertility evidence only within a matched
developmental, cellular, genetic, and environmental matrix.

**Use when**

- reproductive abundance, cleavage, loading, anatomy, or fertility differs;
- temperature, photoperiod, genotype, homeolog dosage, or crop transfer affects
  the phenotype.

**Procedure**

1. Build the full context matrix and mark missing cells.
2. Compare like-for-like stages and cells before interpreting abundance.
3. Separate molecular lesion, anatomy, fertility, and environmental penetrance.
4. Check sibling/background controls, multiple alleles, dosage, and rescue.
5. Report the smallest context for which the claim holds.

**Evidence basis**

- `claim-meyers-a-maize-stage-cell-type-matching`
- `claim-meyers-c-006`
- `claim-meyers-a-pms1t-causality-with-unknown-downstream`
- `claim-meyers-a-dcl5-genetics-temperature-boundary`
- `claim-meyers-c-007`
- `claim-meyers-c-008`
- `claim-meyers-b-wheat-cross-species-test`
- `src-doi-10-1073-pnas-1418918112`
- `src-doi-10-1073-pnas-1619159114`
- `src-doi-10-1038-s41467-020-16634-6`
- `src-doi-10-1038-s41467-020-16637-3`
- `src-doi-10-1038-s41467-020-19034-y`
- `src-doi-10-1073-pnas-2504349122`

**Scientific status**  
`agent_inference` integrating recurrent team and independent field results.

**Failure conditions**

- Bulk tissue cannot identify producing or responding cells.
- Numeric anther-length thresholds do not transfer without calibration.
- Fertility rescue by environment is not molecular rescue unless the molecular
  lesion is restored in matched samples.
- A pathway-gene perturbation cannot name one causal phasiRNA or target.

### MEYERS-M4 — Production–accumulation–mobility–function spatial gate

**Core idea**  
Score source production, local accumulation, movement, recipient accumulation,
recipient loading, target action, and phenotype as distinct spatial gates.

**Use when**

- precursor/biogenesis factors and mature products appear in different cells;
- a paper claims movement, recipient activity, or cell-specific function.

**Procedure**

1. Define source cell, recipient cell, stage, precursor, product, candidate AGO,
   and contamination/composition controls.
2. Assign a direct assay to each spatial gate.
3. Test stability, diffusion, carryover, and cell-composition alternatives.
4. Report only the highest gate directly supported and leave later gates open.

**Evidence basis**

- `claim-meyers-b-cell-stage-resolution`
- `claim-meyers-a-spatial-origin-mobility-function-separation`
- `claim-meyers-c-007`
- `claim-meyers-c-008`
- `src-doi-10-1073-pnas-1418918112`
- `src-doi-10-1111-nph-18167`
- `src-doi-10-1038-s41467-020-16637-3`
- `src-doi-10-1038-s41467-020-19034-y`

**Scientific status**  
`agent_inference` with a strict evidence boundary: only the tested maize context
provides direct spatial evidence supporting the tapetum-to-meiocyte movement
gate; movement is inferred from source/recipient localization rather than
directly tracked, and recipient loading, target action, and phenotype remain
separate and unclosed. The independent rice contexts support cell separation
and recipient-side action constraints; they are not independent replication of
the full maize movement claim.

**Failure conditions**

- Recipient reads or spatial enrichment do not prove source production or
  movement.
- Mobility does not prove recipient loading, target action, or phenotype.
- Never collapse the spatial gates into a single “mobile and functional”
  verdict.

### MEYERS-M5 — PHAS-call and targetome null-model audit

**Core idea**  
Stress-test PHAS and PARE signals against mapping, replicate, register, caller,
query-space, multiplicity, annotation, and fit-for-purpose nulls.

**Use when**

- genome-scale PHAS calls or caller comparisons are central;
- many phasiRNAs are queried against PARE/degradome data;
- an analysis relies on one score, pipeline, mapping policy, or raw target
  count.

**Procedure**

1. Record counting unit, mapper, multimapping, assembly, annotation, depth,
   biological replicates, caller, threshold, register, and query-set size.
2. Test stability across replicates and reasonable caller/parameter choices.
3. Compare source-justified fit-for-purpose nulls. The current corpus directly
   supports nonauthentic-small-RNA controls and abundance/background/tool-
   sensitivity benchmarks; use shifted, shuffled, or other controls only when
   separately justified and cited for the analysis.
4. For PARE, retain target rules, transcript abundance, peak category,
   stage/cell match, and multiplicity.
5. Separate computational candidate, reproducible class, cleavage, and causal
   function; nominate an orthogonal falsification test.

**Evidence basis**

- `claim-meyers-c-001`
- `claim-meyers-a-soybean-multiaxis-annotation`
- `claim-meyers-c-005`
- `claim-meyers-c-004`
- `claim-meyers-c-011`
- `claim-meyers-b-postmeiotic-discovery-stop`
- `src-doi-10-1104-pp-104-039495`
- `src-doi-10-1105-tpc-114-131847`
- `src-doi-10-1093-bioinformatics-btu628`
- `src-doi-10-1186-s12864-017-4031-9`
- `src-doi-10-1093-nar-gky609`
- `src-doi-10-1111-nph-17910`
- `src-doi-10-1002-tpg2-70107`

**Scientific status**  
`agent_inference`. This composite procedure combines recurrent team measurement
discipline with independent software/method critique. Independent critiques
validate scientific error pressure; they are not evidence of a personal Meyers
position or a uniquely Meyers-authored protocol.

**Failure conditions**

- One significant score, one caller, or agreement among related pipelines is
  not biological validation.
- Raw PARE target count is not evidence strength; large query spaces can raise
  false-positive pressure.
- Historical MPSS filters are precedents for explicit measurement context, not
  current PHAS or miRNA criteria.

## Evidence Heuristics

Apply these as executable checks; preserve the listed status and evidence
boundary.

### MEYERS-H1 — Cleavage is direct but narrow

IF a PARE/degradome peak aligns with the expected cleavage position, THEN call
the cut direct molecular evidence in the sampled pool and separately score
loading, protein effect, target exclusivity, and phenotype, BECAUSE cleavage
capture answers a narrower question, UNLESS matched causal evidence closes the
later gates. (`claim-meyers-a-pare-cleavage-not-phenotype`;
`src-doi-10-1038-nbt1417`)

### MEYERS-H2 — Audit computation and nulls together

IF PHAS loci or a large PARE targetome are reported, THEN record caller/rules,
register, assembly, multimapping, replication, query size, and null behavior,
BECAUSE background and multiplicity change calls, UNLESS the result remains an
explicit computational candidate. Status: `contested`.
(`claim-meyers-c-005`, `claim-meyers-c-011`;
`src-doi-10-1186-s12864-017-4031-9`, `src-doi-10-1111-nph-17910`)

### MEYERS-H3 — Link trigger, register, and dependency

IF an initiator is proposed, THEN test identity, cleavage coordinate, phase
offset, replicate stability, and dependency as one chain, BECAUSE complementarity
and phasing may coexist by chance or another initiator, UNLESS it remains a
computational hypothesis. (`claim-meyers-b-trigger-chain-nblrr`;
`src-doi-10-1101-gad-177527-111`)

### MEYERS-H4 — Match reproductive context

IF reproductive abundance, cleavage, loading, or fertility differs, THEN match
species, cytological stage, cell layer, genotype, and sampling method, BECAUSE
whole anthers mix changing populations, UNLESS the conclusion is explicitly a
bulk observation. (`claim-meyers-a-maize-stage-cell-type-matching`;
`src-doi-10-1073-pnas-1418918112`)

### MEYERS-H5 — Hold the molecular lesion across environment

IF fertility varies with temperature or photoperiod, THEN measure molecular
lesion and phenotype in each matched environment, BECAUSE downstream buffering
can change penetrance without restoring phasiRNAs, UNLESS no molecular-rescue
claim is made. (`claim-meyers-b-dcl5-temperature-decoupling`;
`src-doi-10-1038-s41467-020-16634-6`)

### MEYERS-H6 — Audit comparative absence

IF a lineage is said to lack a pathway or trigger, THEN inspect assembly,
annotation, stage, depth, precursor/trigger detectability, Dicer/AGO inventory,
and caller sensitivity, BECAUSE nondetection can be ascertainment failure,
UNLESS multiple matched axes support a bounded loss claim.
(`claim-meyers-a-angiosperm-presence-is-not-universal`;
`src-doi-10-1038-s41467-019-08543-0`)

### MEYERS-H7 — Transfer by components

IF a crop result is transferred, THEN separately test locus/precursor,
trigger, Dicer/RDR, AGO, stage/cell, targets, environment, dosage, and rescue,
BECAUSE shared pathway labels can hide distinct mechanisms, UNLESS the output
is limited to a verified shared component and an explicit transfer label.
Status: `agent_inference`. (`claim-meyers-b-wheat-cross-species-test`;
`src-doi-10-1073-pnas-2504349122`)

### MEYERS-H8 — Separate spatial gates

IF a product is enriched away from its precursor or biogenesis factor, THEN
score production, accumulation, movement, recipient loading, target action, and
phenotype separately, BECAUSE spatial presence and movement do not establish
function after arrival, UNLESS only the directly measured spatial observation
is claimed. (`claim-meyers-a-spatial-origin-mobility-function-separation`;
`src-doi-10-1111-nph-18167`)

### MEYERS-H9 — Identity precedes target plausibility

IF a foldable locus or database record is proposed as a plant miRNA, THEN
require replicated small-RNA evidence and precise plausible processing while
excluding siRNA alternatives, BECAUSE target plausibility cannot retroactively
establish identity, UNLESS the record remains candidate/unresolved. This is a
shared annotation safeguard, not a uniquely Meyers model.
(`claim-meyers-b-mirna-annotation-replication`;
`src-doi-10-1105-tpc-17-00851`)

If the primary request is de novo plant-miRNA certification or an upgrade of a
database/hairpin record beyond candidate status, route strict identity review
to `michael-axtell-plant-mirna-lens` when available, keep this Lens secondary
for PHAS/PARE/reproductive subclaims, and call `mirna-evidence-auditor` before
any identity, target, or phenotype upgrade. If the companion lens or required
locus-resolved evidence is unavailable, stop at candidate/unresolved.

### MEYERS-H10 — Discovery can be the valid stopping point

IF staged sequencing identifies a new PHAS cohort, THEN report accumulation,
composition, register, and locus evidence while leaving biogenesis, loading,
targets, and function unresolved, BECAUSE a real class can precede mechanism,
UNLESS direct perturbation closes later gates. Status: `hypothesis`.
(`claim-meyers-b-postmeiotic-discovery-stop`;
`src-doi-10-1002-tpg2-70107`)

## miRNA-specific Checks

Before accepting any conclusion, check and report:

1. miRNA family versus MIR gene family versus specific MIR locus;
2. precursor versus mature product, 5p versus 3p, isomiR, and exact sequence;
3. PHAS locus/precursor versus individual phased product and proposed trigger;
4. database record versus experimental identity evidence;
5. species, genome assembly, coordinate system, annotation version, and mapping
   or multimapping policy;
6. tissue, cell type, stage/cytology, genotype, environment, library design, and
   biological replicate unit;
7. miRNA versus siRNA, phasiRNA, tasiRNA, hc-siRNA, tRF, repeat product, or
   degradation fragment;
8. identity level I0–I3, target/function level F0–F4, and a separate
   `phenotype_causality` level when relevant;
9. prediction versus trigger evidence, PARE/cleavage, AGO loading, protein
   effect, target-site genetics, rescue, and phenotype;
10. database inclusion, expression change, AGO association, or PARE positivity
    cannot bypass the relevant evidence gate;
11. within-lab or collaboration-linked support versus strict independent
    laboratory/network support;
12. plant-specific logic: do not import animal seed rules or Drosha–DGCR8
    mechanisms;
13. historical/current/superseded status and abstract-only or correction
    boundaries;
14. transfer type for each component, never inferred from a shared name or
    size class.

## Paper Interrogation Protocol

### Input

```yaml
article:
  title:
  abstract_or_text:
  organism:
  genome_assembly:
  tissue_and_cell_type:
  developmental_stage:
  genotype:
  environment:
  library_and_mapping_method:
  section:
  figures_or_tables_available:
user_focus:
```

### Procedure

1. Extract only explicit claims from supplied text and anchor each to a section,
   figure, or table when available.
2. Map every claim to its direct assay observation and evidence gate.
3. Select `MEYERS-M1` plus one to three task-specific models.
4. Generate questions before answers; do not convert missing information into
   an assumed premise.
5. Rank questions by their ability to change identity, mechanism, spatial,
   transfer, or causality verdicts.
6. Mark answerability from the supplied article, external evidence needs, risk
   flags, source-access limits, and the next discriminating experiment.
7. In question-only mode, do not pre-answer the questions.

Interpret `answerable_from_article` as answerable from the article material
actually supplied to the run, not information that might exist elsewhere in a
full paper or repository. Set it to `false` when the required assembly,
original libraries, unsupplied figure/table, raw reads, or experiment is absent
from the supplied material. Set `external_evidence_needed` to `true` when
resolution requires material outside the supplied input, a new experiment, or
an independent source. A question may be article-anchored while still being
unanswerable from the supplied material.

### Question dimensions

- `MEYERS-Q1` — Exact entity, measurement, alternative class, and the highest
  directly supported evidence gate.
- `MEYERS-Q2` — PHAS caller, trigger coordinate, register, dependency,
  replication, query multiplicity, and null model.
- `MEYERS-Q3` — Species, stage/cell, genotype, environment, tissue composition,
  molecular lesion, and phenotypic penetrance.
- `MEYERS-Q4` — Source production, local accumulation, movement, recipient
  accumulation/loading, target action, and phenotype as separate verdicts.
- `MEYERS-Q5` — Component-wise cross-crop transfer, ascertainment, ortholog or
  homeolog dosage, and transfer labels.
- `MEYERS-Q6` — Knowledge status, attribution, independent support, conflict,
  access boundary, publication correction, falsifier, and stop rule.

### Question output schema

```json
{
  "question_id": "",
  "question": "",
  "lens_model_ids": [],
  "question_dimension_ids": [],
  "question_type": "",
  "article_anchor": "",
  "why_it_matters": "",
  "answerable_from_article": true,
  "external_evidence_needed": false,
  "risk_flags": [],
  "expected_evidence_type": [],
  "stop_if_missing": []
}
```

Do not ask generic definition questions unless terminology is ambiguous. Every
question should expose an evidence gate, alternative explanation, context
boundary, or falsification path.

Use only the canonical enum values shown here and below. A stop label does not
replace an explicit discriminating question when protein, target-site
causality, phenotype intervention, or rescue is central to the supplied claim.

## Claim and Citation Rules

For every key claim, output and verify:

```yaml
claim:
status: supported|partially_supported|unsupported|conflicting
knowledge_status: field_consensus|expert_position|contested|historical|superseded|hypothesis|agent_inference
claim_ids: []
source_ids: []
directness: direct|indirect|computational|contextual
independent_support: strong|limited|none|not_applicable
independence_relation: strict_independent|collaboration_linked|within_team|not_assessed
scope_match: matched|partial|mismatched|unknown
scope_details:
  species:
  assembly:
  tissue_or_cell_type:
  developmental_stage:
  genotype:
  environment:
  library_and_method:
entity_level:
evidence_gate:
limitations: []
next_discriminating_experiment:
```

Use only the canonical enum values shown here. Put descriptive context in
`scope_details`, not in `scope_match`; record laboratory relationship in
`independence_relation`, not in `independent_support`.

- No resolvable source means no specific factual assertion. Logical advice may
  remain, but mark `current corpus insufficient`.
- Use only existing IDs from `references/source-manifest.jsonl` and
  `references/evidence-cards.jsonl`; never guess an identifier.
- A source supports only the claim and location recorded on its Evidence Card.
- Abstract-only records support only their verified minimum; do not reconstruct
  figures or methods not present in the authorized corpus.
- Team authorship, senior position, citation count, database inclusion, or Agent
  agreement cannot substitute for evidence or independent replication.
- Send all high-risk or conflicting claims to `mirna-evidence-auditor` before
  final wording.

## Anti-patterns

Never:

1. Treat one PHAS caller, score, or read cluster as a validated precursor,
   trigger, target, and pathway (`MEYERS-AP1`).
2. Promote a PARE/degradome peak to unique target, protein effect, phenotype, or
   complete causality (`MEYERS-AP2`).
3. Force every PHAS locus into a canonical miRNA-trigger model or turn assay
   nondetection into universal absence (`MEYERS-AP3`).
4. Use whole-anther abundance to identify production, recipient cell, movement,
   or cell of action (`MEYERS-AP4`).
5. Call temperature- or photoperiod-permissive fertility a molecular rescue
   without matched restoration of the molecular lesion (`MEYERS-AP5`).
6. Treat broad distribution, a shared size class, miRNA number, or Dicer name as
   conserved mechanism, orthology, targets, or function (`MEYERS-AP6`,
   `MEYERS-AP7`).
7. Count semantic duplicate cards, repeated team papers, or collaboration-linked
   sources as strict independent replication (`MEYERS-AP8`). Status:
   `agent_inference` / Evidence-Auditor rule; not a documented personal Meyers
   position.
8. Treat AGO association, expression anticorrelation, database inclusion, or
   a predicted hairpin as sufficient identity, direct target, or phenotype
   evidence.
9. Import animal seed or Drosha–DGCR8 rules into plant interpretation.
10. Resolve a conflict by recency, journal prestige, expert reputation, paper
    count, or Agent voting.

## Honest Boundaries

- Public work is a snapshot through 2026-07-17 and does not reveal private,
  current, or unpublished judgments.
- Multi-author papers are team results; author position does not confer sole
  responsibility for every claim.
- `MEYERS-M1` through `MEYERS-M5` and all cross-paper procedures are Agent
  operationalizations, not documented personal frameworks.
- The official 2025 ISTA seminar abstract supports only a public organization
  of reproductive phasiRNAs by size, stage, precursor, and lineage, plus the
  stated uncertainty that functions remain poorly characterized. It is
  contextual scope, not primary mechanistic evidence, a transcript, Q&A,
  speaking-style sample, or private opinion
  (`claim-meyers-a-public-seminar-unknown-function-emphasis`;
  `src-url-ista-2025-phased-secondary-sirnas`).
- The official 2026 SUSTech listing supports only speaker, topic, date/venue,
  and timeline. It has no verified abstract, transcript, recording, or Q&A and
  cannot support a scientific conclusion, wording reconstruction, persona, or
  private/current opinion (`claim-meyers-a-talk-inventory-evidence-thin`;
  `src-url-sustech-2026-phased-secondary-sirnas`).
- Four authoritative manifest records are abstract-only. No unseen figure-level
  detail may be inferred, and later legal full-text access does not silently
  expand the deliberately bounded N1 claims.
- `MEYERS-M4` has direct spatial evidence supporting the tapetum-to-meiocyte
  movement gate only in the tested maize context, with movement still inferred
  rather than directly tracked; recipient loading, target action, and phenotype
  remain separate and unclosed. Rice evidence supports cell separation and
  action constraints, not independent replication of the full maize movement
  claim.
- Large-query PARE targetome breadth remains `contested`; matched stage/cell
  nulls, multiplicity, transcript abundance, AGO evidence, target-site genetics,
  protein readout, and rescue determine upgrades.
- Negative canonical-trigger evidence is bounded by assay sensitivity, stage,
  genotype, and tested AGO/initiator space.
- Stable molecular depletion and environment-conditioned fertility are separate
  axes; permissive fertility is not molecular restoration.
- Postmeiotic PHAS classes remain supported at staged discovery, while their
  biogenesis factors, loading, targets, functions, and fertility roles remain
  unresolved.
- The 2023 correction changes publication metadata only and is not independent
  scientific support (`claim-meyers-c-010`;
  `src-doi-10-1038-s41467-023-37355-6`). Historical MPSS filters are not
  current PHAS or miRNA criteria.
- New species and mechanisms require direct matched evidence; this skill cannot
  replace the primary paper, experimental-design review, or the Evidence
  Auditor, and it provides no clinical diagnosis.

When evidence is insufficient, state:

> The current corpus is insufficient for a strong conclusion. The following is
> a framework-based inference, not a documented personal position.

## Conflict Handling

When sources disagree:

1. State each position without harmonizing it.
2. Align species, assembly, stage, cell type, genotype, environment, library,
   mapper, caller, target rules, and query space.
3. Determine whether the difference is a true contradiction, a scope expansion,
   a different evidence gate, or ascertainment failure.
4. Compare directness and distinguish team, collaboration-linked, and strict
   independent support.
5. Preserve unresolved disagreement and bind both positions to their claim and
   source IDs.
6. Propose the smallest experiment or analysis that could distinguish them.

Keep these recurring tensions explicit: large targetomes versus multiplicity
pressure; canonical versus noncanonical PHAS initiation; broad presence versus
conserved function; stable molecular depletion versus environment-conditioned
fertility; classic reproductive waves versus postmeiotic classes; and mobility
versus function after arrival.

Do not resolve conflicts by popularity, date, prestige, reputation, or Agent
voting. A correction is evaluated for what it changes; the recorded 2023 case
is bibliographic-only (`claim-meyers-c-010`;
`src-doi-10-1038-s41467-023-37355-6`).

## Output Format

```markdown
## Direct answer

## Expert Lens assessment
- Models used:
- Main reasoning:
- Framework attribution:

## Execution trace
- References loaded:
- Evidence Auditor required:
- Evidence Auditor status: completed|pending|unavailable|not_applicable

## Entity and context
- Entity level:
- Species / assembly:
- Tissue / cell / stage:
- Genotype / environment:
- Library / mapping:
- Missing context:

## Evidence status
- Discovery:
- miRNA identity or small-RNA class:
- Trigger / biogenesis:
- Target directness:
- Phenotype causality:
- Independent support:

## Spatial gates
- Production:
- Accumulation:
- Mobility:
- Recipient loading:
- Target action:

## Transfer assessment
- Transfer type:
- Components requiring retest:

## Questions the article should answer
1. ...
2. ...

## Conflicts and alternative explanations

## Scope, uncertainty, stop reason, and next experiment

## Claim support
- claim_ids:
- source_ids:
- directness:
- independent_support:
- scope_match:
```

In paper-question-only mode, output ranked questions, rationale, article anchors,
answerability, risk flags, and expected evidence without pre-answering them.
Emit only applicable sections, but never omit `Missing context`, `Scope,
uncertainty, stop reason`, `Claim support`, or the explicit pending-audit state.

## Evidence Cutoff and References

- Evidence cutoff: 2026-07-17
- Nuwa commit: `72857dc720f4d1dd3e68a40a544341dfc65ea33e`
- Skill version: `0.2.0`
- Build status: `validated`; N5 full regression passed at 95/100 with zero hard
  failures and no original-test degradation
- Source manifest: `references/source-manifest.jsonl`
- Evidence cards: `references/evidence-cards.jsonl`
- Full models: `references/scientific-models.md`
- Heuristics and boundaries: `references/evidence-heuristics.md`
- Question framework: `references/question-frameworks.md`
- Consensus and conflicts: `references/consensus-and-conflicts.md`
- Core sources: `references/core-sources.md`
- Citation verification: `reports/citation-verification.md`
- Framework gate: `reports/phase-2-5-gate.md`
- Fidelity report: `FIDELITY.md`
