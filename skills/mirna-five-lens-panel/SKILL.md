---
name: mirna-five-lens-panel
description: >
  Analyze a miRNA, plant small-RNA, RNA-silencing, or cross-kingdom RNA
  question or supplied text through five distinct neutral scientific lenses:
  Michael Axtell, Xuemei Chen, Blake Meyers, James Carrington, and Hailing Jin.
  Use when the user wants side-by-side concerns, interpretations, evidence
  gaps, follow-up questions, common ground, or disagreements from several
  public research frameworks. Never impersonate the experts or decide
  scientific facts by voting.
---

# miRNA Five-Lens Scientific Panel

## Purpose and boundary

Analyze one question or supplied passage through five public scientific research
frameworks. Treat every section as an Agent application of a framework distilled
from public work, not as the named person's current opinion or words.

This distributed package is a `github_public_candidate`, not a production public
release. Four lenses are validated; Jin remains `supervised_preview`. Preserve
those labels even when the user requests a shorter answer or a consensus view.

Never write in first person as an expert. Never write “X would definitely say”.
Do not infer private beliefs, rank experts, or use majority vote as scientific
evidence. Attribute a statement to a named publication only after verifying its
source. Label a new application of a framework as `agent_inference`.

Use the five fixed lenses in `references/lens-registry.md`. Do not add Bartel,
the Evidence Auditor, or any unlisted expert to the panel. The four validated
lenses and Jin's supervised-preview lens have different release status; preserve
that distinction in every result.

## Input handling

Accept either:

- a direct scientific question;
- a title, abstract, results passage, figure legend, or user-authorized text;
- a claim that the user wants challenged;
- a request for questions to ask before accepting a conclusion.

Extract or mark unknown:

```yaml
task_type: question|text_analysis|claim_audit|question_generation|comparison
organism_group:
species:
strain_or_cultivar:
tissue_or_compartment:
treatment_or_infection_stage:
genome_assembly:
rna_class:
entity_level: family|MIR_gene_family|locus|precursor|mature|5p|3p|isomiR|sequence|database_record|unknown
methods_present: []
claimed_conclusion:
missing_context: []
```

Do not invent missing species, assembly, sequence, locus, arm, strain, method,
experimental condition, or access level. Ask at most three decision-changing
clarifying questions when those fields block analysis. Otherwise proceed with a
bounded answer and list the missing context.

## Load the lenses

Read `references/lens-registry.md` first. For the default full-panel request,
read each of these five instruction files before analysis:

1. `references/lenses/michael-axtell-plant-mirna-lens/SKILL.md`
2. `references/lenses/xuemei-chen-plant-mirna-lens/SKILL.md`
3. `references/lenses/blake-meyers-plant-small-rna-lens/SKILL.md`
4. `references/lenses/james-carrington-rna-silencing-lens/SKILL.md`
5. `references/lenses/hailing-jin-cross-kingdom-rna-lens/SKILL.md`

Follow each Lens's identity, scope, scientific, citation, and stop rules. Load
its detailed reference files only when needed for the user's claim. Do not
bulk-load all evidence cards. If a current factual claim exceeds the evidence
cutoff, retrieve current primary evidence when tools are available; otherwise
state that current verification is required.

For a full-panel request, include all five sections. Set `applicability` to
`primary`, `complementary`, or `low`. A low-relevance Lens must explain the
scope mismatch briefly and may contribute one boundary question; do not invent
a position merely to fill the panel.

## Analysis workflow

1. Restate the decision or claim being examined in one neutral sentence.
2. Separate miRNA identity, direct target evidence, and phenotype causality.
3. Distinguish family, MIR gene family, locus, precursor, mature product, arm,
   isomiR, exact sequence, database record, coordinates, and assembly.
4. Assign `applicability` independently for all five lenses.
5. Apply every Lens to its distinct responsibility; do not let one Lens answer
   on behalf of another.
6. For each substantive conclusion, label it `documented_framework`,
   `field_consensus`, `contested`, or `agent_inference`. Add `claim_ids` and
   `source_ids` when the bundled evidence is actually used.
7. Preserve conflicts caused by taxon, species, tissue, stage, genotype,
   method, compartment, dose, or evidence directness. Do not average them away.
8. Synthesize only after all five sections are complete.

Apply these hard scientific boundaries throughout:

- A predicted hairpin is not sufficient miRNA identity evidence.
- Target prediction is not direct target validation.
- PARE/degradome cleavage is not complete phenotype causality.
- Expression anticorrelation is not direct regulation.
- Animal seed rules and Drosha–DGCR8 cannot be imported as plant mechanisms.
- Same-name miRNAs across species are not automatically orthologous.
- miRNA, phasiRNA, tasiRNA, and hc-siRNA are not interchangeable.
- Database inclusion, paper count, reputation, or panel agreement cannot replace
  directness, independent support, and scope match.

## Distinct Lens responsibilities

Keep the five contributions recognizably different:

- **Axtell lens:** entity identity, annotation stringency, miRNA-versus-siRNA
  classification, precursor processing precision, locus/family/evolution logic.
- **Chen lens:** plant miRNA biogenesis and lifecycle, processing, methylation,
  AGO loading, movement or turnover, developmental and genetic mechanism.
- **Meyers lens:** small-RNA sequencing design, locus classification,
  PARE/degradome interpretation, PHAS/phasiRNA evidence, reproducibility and
  computational/experimental controls.
- **Carrington lens:** RNA-silencing pathway logic, DCL/RDR/AGO dependencies,
  tasiRNA or antiviral mechanisms, suppressors, genetic epistasis and systemic
  context.
- **Jin lens:** plant–pathogen directionality, donor origin, extracellular
  release or carrier state, intact-recipient uptake, recipient RNAi competence,
  direct target action, phenotype causality and intervention maturity.

## Jin supervised-preview guardrails

Jin is executable here only under `supervised_preview`; do not relabel it
`validated`. In every Jin section:

1. print `status: supervised_preview` and the evidence cutoff `2026-07-17`;
2. keep family, MIR gene family, locus, precursor, arm, isomiR, exact sequence,
   and assembly fields distinct;
3. separate plant-to-pathogen from pathogen-to-plant transfer;
4. separate RNA classes and require a class-appropriate recipient action path;
5. grade the chain edge by edge: origin → release/carrier → stability → intact
   uptake → effector access → direct target action → phenotype;
6. stop at the last supported edge and name missing controls;
7. distinguish natural exchange, HIGS, SIGS, formulation, engineered delivery,
   greenhouse evidence, and field readiness;
8. mark claims after the cutoff as requiring current source verification.

These guardrails permit supervised use; they do not erase the unresolved
release-completeness finding in Jin's original evaluation.

## Output contract

Match the user's language. For Chinese input, use Chinese labels and prose.
Begin with a compact overview table:

| Lens | Status | Applicability | Main concern | Provisional boundary |
|---|---|---|---|---|

Then provide exactly one section per Lens in the fixed order Axtell, Chen,
Meyers, Carrington, Jin:

```yaml
lens:
status: validated|supervised_preview
applicability: primary|complementary|low
framework_basis: documented_framework|agent_inference|mixed
focus:
analysis:
questions_to_ask: []
evidence_gaps: []
scope_limit:
claim_ids: []
source_ids: []
```

Use two to four decision-changing questions per primary or complementary Lens.
For `low`, keep the section short and do not force a verdict.

Finish with:

1. **共同点 / Common ground** — only claims supported independently, not a
   headcount.
2. **互补关注 / Complementary concerns** — which Lens covers which distinct
   uncertainty.
3. **需保留的分歧 / Preserved disagreements** — scope or evidence conflicts
   that cannot be merged.
4. **最能改变结论的证据 / Decision-changing evidence** — prioritized tests,
   controls, metadata, or primary sources.
5. **下一步问题 / Next questions** — a deduplicated prioritized list.
6. **边界声明 / Boundary note** — the output is framework-based Agent analysis,
   not the experts' current personal views; Jin is supervised preview.

Do not collapse the five sections into a single consensus answer unless the
user explicitly requests a synthesis, and even then preserve material
disagreements and status labels.
