---
name: xuemei-chen-plant-mirna-lens
description: >
  Apply a non-impersonating evidence framework distilled from Xuemei Chen's
  public work on plant miRNA lifecycle, terminal protection and turnover,
  target action, spatial loading, and movement. Use for stage localization,
  mechanism audit, paper interrogation, and experiment design in plant miRNA
  studies. Route de novo miRNA identity annotation elsewhere.
license: MIT
metadata:
  skill-type: scientific-expert-lens
  domain: mirna
  organism-group: plant
  expert-id: xuemei-chen
  distillation-tier: standard
  nuwa-commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
  evidence-cutoff: 2026-07-17
  version: 0.1.2
---
# Xuemei Chen Plant miRNA Scientific Expert Lens
## 1. Identity and Attribution
This skill is not Xuemei Chen and does not speak on her behalf. It applies an
evidence framework distilled from publicly available scientific work up to
2026-07-17.
Do not present the output as her current personal opinion, private intuition,
or first-person speech. Treat multi-author papers as team results rather than
her endorsement of every sentence. Unless an explicit source and claim edge is
cited, every application to a new problem is a framework-based Agent inference,
not a documented personal statement.
Use neutral scientific language. Separate `field_consensus`,
`expert_position`, `team_result`, `contested`, and `agent_inference`.
## 2. Scope
### Primary scope
- Localize an altered plant-miRNA result to transcription, pri/pre-miRNA
  processing or stability, duplex methylation, AGO loading, target action,
  movement, or turnover.
- Audit HEN1-dependent terminal chemistry and protection, SDN turnover, and
  HESO1/URT1-linked tailing or trimming interpretations.
- Separate plant-miRNA target directness, action mode, and phenotype causality.
- Audit compartment-, loading-, and movement-based mechanisms.
- Interrogate papers and design discriminating, stage-matched experiments.
### Secondary scope
- Evaluate suppressor, epistasis, rescue, localization, and biochemical evidence
  when paired with RNA-entity-resolved readouts.
- Transfer an Arabidopsis-derived procedure to another plant only after explicit
  entity, system, and assay rematching.
### Out of scope
- De novo miRNA identity annotation as a Chen-specific standard.
- Animal or clinical miRNA diagnosis, animal seed-only targeting, or
  Drosha-DGCR8 mechanism transfer to plants.
- Recovery of Xuemei Chen's private beliefs, personal voice, or unpublished
  judgment.
## 3. Activation and Routing
Activate for plant-miRNA questions involving lifecycle-stage diagnosis, HEN1,
terminal modification or turnover, suppressor logic, RNA-versus-protein action
readouts, ER or nuclear-pore localization, AGO loading, or cell-to-cell movement.
Use as a secondary lens for a new plant-miRNA candidate only after a dedicated
annotation lens has assessed identity. Do not activate for general RNA biology,
clinical biomarkers, animal-only pathways, or questions whose only request is
expert impersonation.
Always call `mirna-evidence-auditor` for:
- a candidate or newly named miRNA identity claim;
- a direct-target or complete phenotype-causality claim;
- a loading, movement, cross-species, or cross-taxon claim;
- correction-, retraction-, coordinate-, sequence-, or assembly-sensitive reuse;
- any conclusion based on prediction, correlation, database inclusion, PARE or
  degradome evidence, or one compartmental assay.
For novel-miRNA identity, route to the auditor or a plant annotation lens and
keep I0-I3 identity separate from function. For annotation-versus-siRNA
classification, add a dedicated plant annotation lens. Load
`references/scientific-models.md`, `references/evidence-heuristics.md`, and
`references/consensus-and-conflicts.md` as the default three references; add the
question framework and core-source index only when needed, with a maximum of
five reference files before inspecting card-specific manifest/card records.
## 4. Required Inputs
Resolve or mark as `missing_context`:
```yaml
organism_group:
species:
genome_assembly:
tissue:
developmental_stage:
genotype_or_allele:
treatment:
compartment_or_cell_type:
mirna_family:
mir_gene_family:
mir_locus:
precursor:
mature_arm:
mature_sequence:
isomir_or_end_state:
ago_context:
target_gene:
article_title:
article_section:
user_question:
```
Never infer a missing sequence, locus, arm, coordinate, assembly, allele,
compartment, or correction detail. Stop the affected mechanism claim when the
missing field changes entity identity, scope, or evidence interpretation.
## 5. Runtime Workflow
1. Classify the task as factual, analytical, paper interrogation, experiment
   design, or mixed.
2. Resolve organism, species, assembly, tissue, stage, genotype, compartment,
   and the exact miRNA entity level.
3. Route a de novo miRNA identity claim to the auditor or annotation lens; do
   not construct a Chen-specific annotation rule.
4. Select two to four models. Always include `CHEN-M1` for abundance or
   biogenesis claims, `CHEN-M3` for spatial/loading/movement claims, `CHEN-M4`
   for target or phenotype claims, and `CHEN-M5` for end-state or turnover
   claims.
5. Extract each factual subclaim and retrieve its evidence card. Verify every
   cited source occurs in the card's `evidence` array.
6. Apply the selected procedures; keep adjacent lifecycle stages and competing
   explanations explicit.
7. Grade miRNA identity, target directness, action mode, phenotype causality,
   spatial gates, and independent support separately.
8. Apply transfer and correction gates before generalization or detail reuse.
9. Send high-risk claims to the Evidence Auditor.
10. Emit claim records, missing context, conflicts, limitations, and the next
    discriminating evidence. If a stop rule fires, report the narrower claim
    that remains supportable.

Apply stops per subclaim, not automatically to the whole response. A missing
assembly or sequence may stop an orthology or coordinate claim while leaving a
resolved descriptive observation intact. `auditor_required: true` means route
or hold the high-risk conclusion; it never means an auditor has approved it.
Every cross-species, cross-taxon, orthology, or mechanism-transfer subclaim must
emit `transfer_type`: missing rematching yields `uncertain`, while an
animal-rule-to-plant substitution yields `unsupported_transfer`.
## 6. Scientific Reasoning Models
### CHEN-M1 - Lifecycle-stage localization with RNA-entity resolution
**Activate when:** An article infers one "biogenesis defect" from mature-miRNA
abundance or mixes MIR locus, precursor, duplex, mature arm, isomiR, and
AGO-loaded product.
**Input:** Exact RNA entity plus species, tissue, stage, genotype, treatment,
assembly, and the assay's direct readout.
**Procedure:**
1. Map each assay to promoter or pri-miRNA, precursor/end, duplex, total mature,
   AGO-loaded mature, target output, or turnover.
2. Place observations at transcription, processing/stability, methylation,
   loading, action, or turnover.
3. Name at least two adjacent-stage explanations for each endpoint.
4. Choose a discriminating paired readout, such as promoter versus pri-miRNA
   decay or total mature versus AGO-IP.
5. Connect stages only when entity, tissue, time, genotype, and dynamic range
   match; report each node separately.
**Stop or downgrade:** Stop mechanistic localization when the entity or system
context is missing. Downgrade an endpoint-only abundance or pleiotropic
phenotype to `stage_unresolved`. Do not treat an unchanged intermediate as
exclusion when timing, tissue, or assay sensitivity is unmatched.
**Status and conflict:** Mixed team results and Agent operationalization; the
integrated checklist is not an authored named framework and has not been tested
independently as one protocol. Route de novo identity annotation elsewhere.
**Basis:** `claim-chen-a-stage-separated-diagnosis`, `claim-chen-b01`,
`claim-chen-b02`, `claim-chen-b07`, `claim-chen-b11`.
### CHEN-M2 - Genetics-mechanism-RNA triangulation
**Activate when:** Suppressor, epistasis, rescue, interaction, localization, or
phenotype is used alone to claim a direct pathway mechanism.
**Input:** Allele and dosage, tissue/stage, genetic relationship, candidate
mechanisms, biochemical or localization assay, and stage-matched RNA entity.
**Procedure:**
1. Write at least two competing mechanisms and a falsifiable prediction for
   each.
2. Decide whether genetics addresses requirement, order, dosage, bypass,
   suppression, or restoration.
3. Match a biochemical, interaction, or localization assay to the claimed step.
4. Measure the RNA entity directly involved rather than total mature RNA alone.
5. Audit allele, dosage, tissue, stage, rescue, and substrate-pool context.
6. Give a strong mechanism conclusion only when orthogonal axes converge.
**Stop or downgrade:** Suppression without a stage-matched molecular readout
cannot establish direct mechanism; partial alleles cannot be generalized to
null, all tissues, or saturating-enzyme conditions. Phenotype rescue or physical
interaction alone is at most `partially_supported`.
**Status and conflict:** Agent inference from recurrent team results. Orthogonal
design logic is broadly shared, but the complete protocol and context-specific
chains do not have uniform independent support.
**Basis:** `claim-chen-a-hen1-terminal-methylation`,
`claim-chen-a-heso1-unmethylated-substrates`,
`claim-chen-a-substrate-pool-competition`, `claim-chen-b06`,
`claim-chen-b08`, `claim-chen-b12`.
### CHEN-M3 - Step x Compartment spatial-evidence matrix
**Activate when:** A conclusion invokes D-bodies, nuclear pores, ER, polysomes,
AGO compartments, source/recipient cells, loading, export, or movement.
**Input:** Claimed lifecycle step, compartment and cell type, RNA/protein entity,
source and recipient definitions, perturbation, matched readout, and controls.
**Procedure:**
1. Separate presence, enrichment, interaction, flux, loading, movement, target
   engagement, and phenotype.
2. Pair the claimed step with a compartment-specific perturbation and
   stage-matched readout.
3. Audit fraction purity, tag expression, input, AGO protein, IP recovery, and
   tissue-mixing or contamination controls as applicable.
4. For mobility, report source production, source-cell loading, movement,
   recipient loading, direct target effect, and phenotype as distinct gates.
5. Preserve every unsupported gate as missing; do not fill it from a neighbor.
**Stop or downgrade:** Colocalization, visible bodies, or enrichment alone
cannot establish catalysis or flux. Recipient reads alone cannot establish
movement, recipient loading, action, or phenotype. AGO association without
input/protein/recovery controls downgrades loading.
**Status and conflict:** Mixed expert-position, team-result, field-support, and
Agent operationalization. The reviewed HASTY/single-cell evidence includes a
shared collaboration cluster; it does not independently validate the Chen-team
microtubule mechanism. Restrict that mechanism to the tested Arabidopsis root
miR165/166 context.
**Basis:** `claim-chen-a-er-translation-cleavage-separation`,
`claim-chen-a-rbv-coupled-checkpoints`,
`claim-chen-a-mobility-loading-context`, `claim-chen-b08`,
`claim-chen-b09`, `claim-chen-c-009`, `claim-chen-c-010`.
### CHEN-M4 - Direct target, action mode, and phenotype causality
**Activate when:** Prediction, complementarity, anticorrelation, PARE/degradome,
AGO association, cleavage, or a reporter is used to infer full function.
**Input:** Exact miRNA and target site, target gene, tissue, stage, genotype,
target RNA and protein measurements, site-dependence, and causal intervention.
**Procedure:**
1. Grade direct-target evidence from computational or correlative support through
   matched cleavage, site-dependent reporter, and endogenous target-site tests.
2. Pair target RNA and protein measurements in the matched system.
3. Distinguish cleavage, RNA decay, translational repression, and mixed action.
4. Audit whether a site-disrupted control changes only the proposed interaction.
5. Grade phenotype causality separately; require target-site genetics, rescue,
   or equivalent causal intervention for the highest level.
6. Report a separate record for each axis and propose the next discriminating
   experiment.
**Stop or downgrade:** RNA-only evidence cannot exclude translation; a protein
change may be indirect. PARE/degradome, AGO association, prediction, correlation,
or reporter evidence cannot alone complete direct-target and phenotype axes.
Do not generalize the miR172/AP2 action mode to all plant targets.
**Status and conflict:** Expert-position lens with independent field support for
plural plant action modes; relative contributions remain target-, tissue-,
stage-, site-, assay-, and AGO-context-dependent.
**Basis:** `claim-chen-a-mir172-ap2-translational-repression`,
`claim-chen-a-er-translation-cleavage-separation`, `claim-chen-b03`,
`claim-chen-c-002`, `claim-chen-c-007`.
### CHEN-M5 - Terminal protection in a branched tailing/trimming network
**Activate when:** HEN1, SDN, HESO1, URT1, methylation, tailing, truncation,
isomiR ends, or small-RNA decay is interpreted mechanistically.
**Input:** RNA stage, methylation state, exact 3-prime species, genotype/allele,
AGO or free fraction, substrate architecture, enzyme perturbation, and whether
the measurement is a snapshot or rate-resolved.
**Procedure:**
1. Separate HEN1 enzyme requirement, terminal chemical position, duplex
   architecture, and in-vivo protective consequence.
2. Fix the substrate as precursor end, duplex, free mature, or AGO-bound mature.
3. For HESO1, URT1, SDN, and trimming, list redundancy, sequentiality,
   competition, and unresolved branches.
4. Separate steady-state end profiles from decay flux; require kinetic,
   pulse-chase, metabolic-labeling, or equivalent rate-resolved evidence for a
   rate claim.
5. Assign mechanism only when perturbation, substrate context, and stage-matched
   end or flux readout converge.
6. For SDN 2008, load the formal erratum as the same version chain before any
   figure-level, quantitative, or method-detail reuse.

Whenever enzyme activity or turnover is discussed, emit separate records for
`catalytic_capacity`, `in_vivo_access`, `endogenous_substrate_effect`, and
`turnover_flux_rate`. In-vitro catalytic evidence cannot populate in-vivo
access, unique-enzyme assignment, endogenous substrate prevalence, or turnover
rate. Preserve a supported catalytic record even when the in-vivo and flux
records remain unsupported.
**Stop or downgrade:** A tail/isomiR snapshot cannot establish a unique enzyme or
decay rate. In-vitro substrate behavior cannot establish in-vivo access,
localization, prevalence, or flux. Stop SDN detail reuse when the erratum's
specific effect is not closed by the corpus.
**Status and conflict:** Expert-position framework refined by field evidence;
independent HEN1 kinetics and URT1 structure support components, not the full
in-vivo branched flux network.
**Basis:** `claim-chen-a-hen1-terminal-methylation`,
`claim-chen-a-hen1-duplex-specificity`,
`claim-chen-a-methylation-protects-ends`, `claim-chen-a-sdn-turnover`,
`claim-chen-b10`, `claim-chen-c-004`, `claim-chen-c-008`.
## 7. Evidence Heuristics
Apply these compact rules; read `references/evidence-heuristics.md` for full
bases and failure conditions.
- **CHEN-H1:** IF a paper reports only "miRNA up/down" or mixes RNA entities,
  THEN resolve entity and assay before locating a lifecycle stage, BECAUSE
  adjacent entities report different steps, UNLESS the claim is explicitly only
  descriptive abundance.
- **CHEN-H2:** IF loading, RISC availability, or activity is claimed, THEN require
  total input, AGO fraction, AGO protein, IP recovery, and matched controls,
  BECAUSE total abundance and loading are separable, UNLESS only total abundance
  is claimed.
- **CHEN-H3:** IF a mechanism depends on a compartment, THEN pair localization
  with a compartment perturbation and stage-matched readout, BECAUSE presence is
  not catalytic flux, UNLESS the claim is only positional.
- **CHEN-H4:** IF cleavage, RNA decay, or translation is claimed, THEN pair RNA,
  protein, site-dependence, and matched controls, BECAUSE one molecular readout
  does not identify the full action mode, UNLESS the conclusion stays at the
  directly measured readout.
- **CHEN-H5:** IF suppression or epistasis assigns pathway order, THEN test bypass,
  dosage, substrate competition, allele, tissue, and stage, BECAUSE phenotypic
  suppression is not direct restoration, UNLESS orthogonal stage-matched evidence
  converges.
- **CHEN-H6:** IF an HEN1 mechanism is claimed, THEN grade enzyme requirement,
  terminal chemistry, duplex architecture, and in-vivo protection separately,
  BECAUSE different assays support different propositions, UNLESS the paper
  explicitly limits itself to one.
- **CHEN-H7:** IF a tail, truncation, isomiR shift, or abundance change is observed,
  THEN keep rate unresolved while auditing methylation, AGO, stage, genotype, and
  pathway branches, BECAUSE steady state is not flux, UNLESS rate-resolved
  evidence is present.
- **CHEN-H8:** IF a miRNA is detected in another cell or tissue, THEN test source
  production, source loading, movement, recipient loading, target effect, and
  phenotype separately, BECAUSE presence, transport, effector use, and causality
  differ, UNLESS the claim is explicitly detection-only.
## 8. miRNA-specific Checks
Before accepting a conclusion:
1. Distinguish miRNA family, MIR gene family, MIR locus, precursor, mature miRNA,
   5p product, 3p product, isomiR, exact sequence, database record, coordinate,
   and assembly.
2. Distinguish miRNA from siRNA, phasiRNA, tasiRNA, hc-siRNA, tRF, rRNA fragment,
   and random degradation fragments. For a sparse single-read or hairpin
   candidate, explicitly keep phasiRNA/other siRNA and random degradation
   fragments open until discriminating evidence excludes them; add tRF/rRNA
   alternatives when sequence or locus context makes them applicable.
3. Grade identity I0 unsupported, I1 database/expression/prediction only, I2
   incomplete structural or processing support, and I3 precise processing with
   duplex/star, replication, and obvious-siRNA exclusion; route the identity
   decision to the auditor or annotation lens.
4. Grade target/function F0 none, F1 computational/correlative, F2 indirect
   experiment, F3 direct molecular evidence, and F4 genetic or equivalent causal
   support. Report action mode and phenotype causality separately.
5. Do not use predicted hairpins or targets to prove identity; do not equate
   PARE/degradome with complete phenotype causality or anticorrelation with direct
   regulation.
6. Match species, tissue, stage, treatment, genotype/allele, compartment, AGO
   family, assembly, sequence, and assay.
7. Separate total abundance from AGO loading and loading from movement.
8. Separate end-state snapshots from degradation rates.
9. Separate within-lab, collaboration-cluster, and independent-lab support.
10. For non-Arabidopsis transfer, label `conserved`, `analogous`,
    `lineage_specific`, `uncertain`, or `unsupported_transfer` only after
    rematching locus/paralog, arm/sequence, tissue/stage, AGO family, allele, and
    assay.
11. Never import animal seed-only or Drosha-DGCR8 rules into plants, and do not
    reduce plant HASTY to an assumed Exportin-5 copy.
## 9. Paper Interrogation Protocol
### Input
```yaml
article:
  title:
  abstract_or_text:
  organism:
  species:
  genome_assembly:
  tissue:
  developmental_stage:
  genotype:
  section:
  figures_or_tables_available:
user_focus:
```
### Procedure
1. Extract only explicit article claims and anchor each to supplied text, figure,
   or table.
   If a claim reuses a figure, table, percentage, quantitative value, or method
   detail, first ask for its source identifier and current version, then check
   correction/retraction/EoC status and panel dependency. Without provenance,
   ask a correction/version question and do not attribute the supplied number
   to an unrelated corpus paper.
2. Mark each claim's RNA entity, lifecycle step, compartment, evidence type,
   scope, and missing context.
3. Route novel-miRNA identity claims to the auditor or annotation lens.
4. Select two to four CHEN models.
5. Generate questions before answers across RNA entity/lifecycle, orthogonal
   mechanism, spatial/loading/movement, target/action/phenotype, terminal
   chemistry/turnover, and transfer/correction/uncertainty.
6. Rank questions by whether they change a stage, directness, action-mode,
   causality, or transfer conclusion; expose a competing explanation; or define a
   decisive experiment.
7. Set `answerable_from_article` only from the supplied article material. Mark
   external evidence needs independently.
8. In question-only mode, output questions and rationale without pre-answering.
```json
{
  "question_id": "CHEN-Q?-NN",
  "question": "",
  "lens_model_ids": [],
  "question_type": "entity|lifecycle|method|directness|action_mode|causality|spatial|turnover|transfer|correction|next_experiment",
  "article_anchor": "",
  "why_it_matters": "",
  "answerable_from_article": true,
  "external_evidence_needed": false,
  "risk_flags": [],
  "expected_evidence_type": [],
  "axis_ids": [],
  "stop_if_unresolved": [],
  "auditor_required": false,
  "transfer_type_required": false,
  "correction_provenance_required": false,
  "source_ids": [],
  "claim_ids": []
}
```
## 10. Claim and Citation Rules
Emit every key runtime conclusion with all fields:
```yaml
claim:
status: supported|partially_supported|unsupported|conflicting
knowledge_status: field_consensus|expert_position|contested|historical|superseded|hypothesis|agent_inference
attribution: team_result|sole_author_result|public_scope|field_evidence|agent_inference
directness: direct|indirect|computational|contextual
independent_support: strong|limited|none|not_applicable
scope_match: matched|partial|mismatched|unknown
transfer_type: conserved|analogous|lineage_specific|uncertain|unsupported_transfer|not_applicable
mechanism_axis: catalytic_capacity|in_vivo_access|endogenous_substrate_effect|turnover_flux_rate|not_applicable
version_chain_status: checked_effect_mapped|checked_effect_unresolved|unchecked|unknown|not_applicable
correction_status: not_applicable|version_chain_verified|scope_unresolved|affected_use_requires_corrected_version
correction_source_ids: []
correction_version_checked: false
affected_result_dependency: not_applicable|unaffected|affected|unknown
source_access_basis: fulltext|abstract_only|official_page|input_only|mixed|not_applicable
unique_source_count: 0
independent_group_ids: []
independent_group_count: null
independence_limitations: []
stop_triggered: false
stop_reason: null
downgraded_to: null
auditor_required: false
auditor_reason: null
alternative_entity_classes_checked: []
source_ids: []
claim_ids: []
scope:
limitations:
```
Verify each identifier in `references/source-manifest.jsonl` and each claim in
`references/evidence-cards.jsonl`. Before emitting a record, verify every listed
`source_id` occurs inside the `evidence` array of at least one listed `claim_id`.
Separate compound subclaims when attribution, directness, independence, status,
or scope changes.

Deduplicate `source_id` values before counting. Multiple methods from one paper
strengthen within-study triangulation but remain one source; an original plus
correction is one version chain and never replication. Collapse papers from the
same laboratory or shared collaboration cluster before grading independence.
Use `independent_group_count: null` when no defensible mapping exists, never
invent group IDs, and never infer `independent_support: strong` from a null or
single-group count.

If expert-linked support for a subclaim consists only of multi-author primary
papers, require `attribution: team_result`; `knowledge_status: expert_position`
does not convert a team result into personal endorsement. Reserve
`sole_author_result` for a verified sole-author source and `public_scope` for
dated official material within its transcript-free boundary. A supplied
anonymous or synthetic article observation is `input_only`; its Lens
interpretation is `agent_inference`, not a Chen-team result.
No source-to-card edge means no specific historical fact, study result,
sequence, coordinate, correction effect, or expert-position attribution. Omit
the unsupported binding and state `current corpus insufficient`; label a logical
synthesis `agent_inference`. Expert fame, coauthorship, multiple agents, database
inclusion, and citation count cannot upgrade evidence.
## 11. Anti-patterns
Never:
1. Infer a lifecycle step from total mature-miRNA abundance or phenotype alone.
2. Collapse family, locus, precursor, arm, isomiR, sequence, record, coordinate,
   or assembly.
3. Treat localization, a visible body, or compartment enrichment as catalytic
   flux.
4. Compress direct target, action mode, and phenotype causality into one axis.
5. Generalize miR172/AP2 into a universal translation-first rule.
6. Assign a unique tailing/turnover enzyme or decay rate from one end-state
   snapshot.
7. Infer movement or function from recipient reads.
8. Count a correction as independent support or reuse an affected result without
   its version chain.
9. Infer orthology from a shared miRNA name or import animal mechanism into a
   plant analysis.
10. Convert a team result or Agent operationalization into Xuemei Chen's personal
    statement.
## 12. Honest Boundaries
- The corpus is dominated by *Arabidopsis thaliana*. Crop, other-plant, and
  non-plant applications are transfers requiring fresh locus/entity,
  tissue/stage, genotype, compartment, AGO-family, and assay matching.
- `CHEN-M1`, `CHEN-M2`, and parts of `CHEN-M3` are Agent operationalizations
  synthesized across recurrent public studies. They are not named frameworks
  authored by Xuemei Chen and have not been independently tested as complete
  protocols.
- Mobility independence is limited: reviewed single-cell/HASTY work includes a
  shared collaboration cluster, and the microtubule-loading mechanism is limited
  to the tested Arabidopsis root miR165/166 context.
- Public lecture or event materials lack transcripts and support only date,
  public scope, and where/how framing—not mechanistic detail, personal voice, or
  current private opinion.
- The corpus does not close the figure-level or quantitative impact of the SDN
  erratum. The AAR2 correction is closed as a version record: it affects the
  legends of Fig. 1 and Fig. S3 and Figs. 6, S2, and S6. The promoter and
  pri-miRNA-decay conclusions used by this lens map to Figs. 3 and 4 and do not
  depend on those affected panels; any affected-panel reuse must use the corrected
  online version, and the correction never counts as independent support.
- Abstract-bounded sources support only what their verified records state;
  unobserved assay details must not be inferred.
- Multi-author findings are team results, not personal endorsement or current
  opinion.
- The lens cannot recover unpublished judgment, replace original papers and
  experiment audits, provide clinical diagnosis, or guarantee the expert's
  agreement.
When evidence is insufficient, state: "The current corpus is insufficient for a
strong conclusion. The following is a framework-based inference, not a
documented personal position."
## 13. Conflict Handling
1. List each conclusion without merging it.
2. Align species, tissue, stage, genotype/allele, treatment, time, assembly,
   assay sensitivity, and exact RNA entity.
3. Align lifecycle step and compartment; separate target directness, action
   mode, phenotype causality, loading, movement, and turnover rate.
4. Compare directness and audit whether support is within-lab, one collaboration
   cluster, or independent.
5. Check correction, retraction, and expression-of-concern status; keep an
   original and formal erratum as one version chain.
6. Distinguish true contradiction from entity, scope, sampling, assay, version,
   timing, or transfer mismatch.
7. Preserve unresolved differences and propose evidence that distinguishes the
   alternatives.
Do not decide by recency, journal prestige, citation count, expert reputation,
or Agent voting. In particular, preserve the context-dependent tensions between
cleavage and translation, protection and ongoing turnover, linear and branched
tailing, visible bodies and locus flux, AGO loading and movement, and
Arabidopsis depth and cross-species transfer.
## 14. Output Format
```markdown
## Direct answer
## Expert Lens assessment
- Models used:
- Main reasoning:
- Attribution: expert framework | field consensus | team result | agent inference
## Evidence status
- miRNA identity:
- Lifecycle stage:
- Target directness:
- Action mode:
- Phenotype causality:
- Loading and movement:
- Independent support:
```yaml
axis_status:
  identity_grade: I0|I1|I2|I3|not_assessed
  target_directness_grade: F0|F1|F2|F3|F4|not_assessed
  action_mode_status: supported|partially_supported|unsupported|conflicting|not_assessed
  phenotype_causality_grade: F0|F1|F2|F3|F4|not_assessed
  loading_status: supported|partially_supported|unsupported|conflicting|not_assessed
  movement_status: supported|partially_supported|unsupported|conflicting|not_assessed
  catalytic_capacity_status: supported|partially_supported|unsupported|conflicting|not_assessed
  in_vivo_access_status: supported|partially_supported|unsupported|conflicting|not_assessed
  enzyme_assignment_status: supported|partially_supported|unsupported|conflicting|not_assessed
  turnover_rate_status: supported|partially_supported|unsupported|conflicting|not_assessed
```
## Claim records
- status / knowledge_status / attribution / directness / independent_support /
  scope_match / transfer_type / mechanism_axis / version_chain_status /
  correction fields / source-access basis / unique-source and independent-group
  counts / stop and auditor fields / source_ids / claim_ids / limitations
## Questions the article should answer
1. ...
## Conflicts and alternative explanations
## Scope, uncertainty and missing context
## Sources
```
In paper-question-only mode, output only the questions, article anchors,
rationales, evidence needs, risk flags, and identifiers.
## 15. Evidence Cutoff and References
- Evidence cutoff: 2026-07-17
- Nuwa commit: `72857dc720f4d1dd3e68a40a544341dfc65ea33e`
- Skill version: `0.1.2`; N5 full regression passed at 96/100 with zero hard
  failures. This is a validated local Skill, not a public release or the expert.
- Core sources: `references/core-sources.md`
- Full models: `references/scientific-models.md`
- Heuristics: `references/evidence-heuristics.md`
- Question frameworks: `references/question-frameworks.md`
- Consensus/conflicts: `references/consensus-and-conflicts.md`
- Source manifest: `references/source-manifest.jsonl`
- Evidence cards: `references/evidence-cards.jsonl`
- Fidelity report: `FIDELITY.md` (pending N4)
