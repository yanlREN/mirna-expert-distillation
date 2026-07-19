# Scientific Reasoning Models — James C. Carrington Lens Candidate

```yaml
expert_id: james-c-carrington
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
phase: N2
model_count: 3
```

These models are neutral, operational syntheses of recurring public team research. They are not named Carrington frameworks, quotations, private views, or claims that James C. Carrington personally endorses every statement in a coauthored paper. The cross-paper formulations remain `agent_inference`; scientific facts, team results, independent support, field consensus, contested claims, historical records, hypotheses, and superseded records remain separately labeled.

## Model M1 — Modular antiviral causal decomposition

model_id: CARRINGTON-M1

```yaml
name: suppressor_host_component_molecular_output_context_phenotype_decomposition
definition: Decompose a plant antiviral-silencing claim into the viral or suppressor perturbation, host-pathway component, measured molecular output, tissue and infection context, and disease or fitness phenotype; validate each link rather than treating the pathway label as a complete mechanism.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_plant_virus_and_rna_silencing_layer_structure
scientific_status: framework_inference_supported_by_standing_team_and_independent_sources
trigger_conditions:
  - a viral suppressor, DCL, RDR, AGO, vsiRNA, viral-load, symptom, or resistance claim
  - a reporter assay proposed to explain native infection
  - evidence from one tissue, virus, temperature, or genotype generalized to another
source_ids:
  - src-doi-10-1016-s0092-8674-00-81614-1
  - src-doi-10-1073-pnas-230334397
  - src-doi-10-1105-tpc-109-073056
  - src-doi-10-1104-pp-19-00121
  - src-doi-10-1016-s0092-8674-03-00984-x
  - src-doi-10-1128-jvi-01963-05
claim_ids:
  - claim-carrington-a-001
  - claim-carrington-a-002
  - claim-carrington-a-007
  - claim-carrington-a-010
  - claim-carrington-a-015
  - claim-carrington-c-005
  - claim-carrington-c-010
  - claim-carrington-c-011
```

### Expert-characteristic evidence and two distinct contexts

1. In early P1/HC-Pro/PTGS studies, team experiments separated the existence or maintenance of silencing from the effect of a viral suppressor and from any universal molecular target (`src-doi-10-1016-s0092-8674-00-81614-1`, `src-doi-10-1073-pnas-230334397`; `claim-carrington-a-001`, `claim-carrington-a-002`).
2. In later Arabidopsis infections, combinatorial DCL/RDR genetics and tissue-aware AGO phenotyping separated virus-derived small-RNA output, viral accumulation, component contribution, tissue, and disease traits (`src-doi-10-1105-tpc-109-073056`, `src-doi-10-1104-pp-19-00121`; `claim-carrington-a-007`, `claim-carrington-a-010`). These are different pathway-component and quantitative-phenotyping contexts, not duplicate cards.
3. Independent p19 and multi-suppressor work shows why a shared suppressor phenotype does not license one molecular mechanism (`claim-carrington-c-010`, `claim-carrington-c-011`). This supports scientific validity but is not counted as Carrington-specific recurrence.

### Step-by-step application

1. Fix the system: host species and genotype, virus and strain, viral suppressor or construct, tissue, developmental stage, temperature, inoculation route, and time point.
2. Name the claim layer: silencing exists; a viral factor suppresses it; a host component is required; a molecular output changes; viral fitness changes; symptoms or host fitness change.
3. Match every layer to its direct readout. Keep reporter reversal, small-RNA abundance, AGO loading or slicing, viral RNA/protein, spread, symptoms, and resistance as separate observations.
4. Ask whether a suppressor acts at small-RNA production, duplex availability, AGO loading, catalysis, amplification, or spread. A functional class label is not a molecular target.
5. Test host components with matched single and combinatorial genetics, then compare molecular and phenotypic outputs in the same context.
6. Build an explicit edge table from perturbation to intermediate to viral fitness to phenotype; mark every untested edge.
7. State the narrowest supported conclusion and the closest alternative explanation, including pleiotropy, tissue restriction, suppressor dosage, developmental effects, and infection-stage differences.

### Known examples

- P1/HC-Pro suppression of established PTGS supports a viral counterdefense in the tested transgene systems, not one universal suppressor target.
- During TuMV infection, DCL/RDR dependencies and antiviral defense require separate interpretation; exact Figure 3A/CP values must use the 2015 correction to DOI `10.1105/tpc.109.073056`.
- During TCV infection, leaf and inflorescence AGO contributions differ, so a single whole-plant AGO ranking is unsafe.

### Failure conditions

- The paper measures only a reporter phenotype, predicted interaction, total small-RNA abundance, or symptoms and claims the full native-infection mechanism.
- Virus, suppressor, tissue, genotype, temperature, or time is not matched across assays.
- Small-RNA accumulation is treated as AGO loading, antiviral activity, or disease causality.
- A retracted or corrected figure is used without its status boundary.

### Transfer limits

- Component and suppressor assignments are virus-, host-, tissue-, construct-, and environment-specific.
- A p19 duplex-sequestration mechanism cannot be transferred to HC-Pro, 2b, p21, or an untested suppressor.
- Arabidopsis findings do not automatically establish crop resistance or field durability.
- This model audits antiviral silencing; it does not establish the identity of a novel miRNA or the causality of one miRNA target.

## Model M2 — Combinatorial component hierarchy and conditional backup

model_id: CARRINGTON-M2

```yaml
name: family_dependency_map_specialization_redundancy_and_context
definition: Resolve DCL, RDR, and AGO family functions through single and higher-order genotypes, matched molecular outputs, catalytic or rescue controls, and phenotype assays so that primary roles, backup routing, specialization, and tissue dependence remain distinguishable.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_component_family_dependency_signatures
scientific_status: framework_inference_with_independent_support_for_selected_hierarchies
trigger_conditions:
  - a paper assigns a small-RNA pathway to one DCL, RDR, or AGO
  - residual products in a mutant are interpreted as pathway independence
  - one family member is called universally dominant
  - loading, catalysis, molecular rescue, and phenotype rescue are conflated
source_ids:
  - src-doi-10-1371-journal-pbio-0020104
  - JCC-B-S004
  - JCC-B-S012
  - src-doi-10-1105-tpc-109-073056
  - src-doi-10-1105-tpc-112-099945
  - src-doi-10-1104-pp-19-00121
  - src-doi-10-1371-journal-pone-0014639
claim_ids:
  - claim-carrington-a-003
  - claim-carrington-a-007
  - claim-carrington-a-009
  - claim-carrington-a-010
  - claim-carrington-a-016
  - JCC-B-C001
  - JCC-B-C002
  - JCC-B-C007
  - claim-carrington-c-012
  - claim-carrington-c-013
```

### Expert-characteristic evidence and two distinct contexts

1. Endogenous pathway studies used DCL/RDR mutant patterns and higher-order genotypes to separate miRNA, heterochromatic siRNA, viral-siRNA, and tasiRNA production, including primary DCL4 action and alternative products in its absence (`src-doi-10-1371-journal-pbio-0020104`, `JCC-B-S004`; `claim-carrington-a-003`, `JCC-B-C001`, `JCC-B-C002`).
2. Antiviral studies used combinatorial DCL/RDR mutants, AGO catalytic mutants, and tissue-resolved AGO phenotyping to separate molecular output, catalytic requirement, local/systemic activity, and tissue contribution (`src-doi-10-1105-tpc-109-073056`, `src-doi-10-1105-tpc-112-099945`, `src-doi-10-1104-pp-19-00121`; `claim-carrington-a-007`, `claim-carrington-a-009`, `claim-carrington-a-010`). Endogenous biogenesis and virus infection are genuinely different contexts.
3. Independent DCL and AGO2 studies support selected hierarchies while preserving virus and mutant-background limits (`claim-carrington-c-012`, `claim-carrington-c-013`).

### Step-by-step application

1. Define the RNA class and endpoint before choosing components: miRNA, tasiRNA/phasiRNA, hc-siRNA, vsiRNA, loading, slicing, amplification, viral fitness, development, or phenotype.
2. Map plausible DCL/RDR/AGO components using expression and prior evidence only as hypotheses.
3. Compare matched wild type, single mutants, informative higher-order mutants, and—when catalytic action is claimed—matched catalytic-site rescue constructs.
4. Measure product size, register, abundance, loading or cleavage, downstream target output, and phenotype separately.
5. Classify each component as primary, backup in a defined mutant, parallel, tissue-restricted, virus-conditioned, unresolved, or not supported.
6. Verify that residual products do not merely change size, register, loading, or function; residual abundance is not proof of functional equivalence.
7. Recheck the hierarchy in the relevant tissue, virus, temperature, and species before transfer.

### Known examples

- DCL4 can be primary for canonical Arabidopsis tasiRNAs while DCL2/DCL3 produce alternative products in particular mutant backgrounds.
- During TuMV infection, molecular vsiRNA production and full antiviral defense use overlapping but nonidentical DCL/RDR requirements.
- AGO loading/association can persist when slicer activity is disabled; tissue-specific AGO contributions can differ.

### Failure conditions

- Only one mutant or total small-RNA change is available.
- Higher-order genotypes have unmatched background, development, infection burden, or sampling.
- Backup-sized products are called wild-type-equivalent without loading and function tests.
- One AGO IP or one virus susceptibility phenotype is generalized to all viruses and tissues.

### Transfer limits

- Family-member orthology and function cannot be inferred from shared names alone.
- Endogenous tasiRNA hierarchy does not automatically validate antiviral-siRNA hierarchy.
- Mutant compensation is a perturbation-state property, not proof of wild-type interchangeability.
- Pathway-gene causality does not identify a unique small-RNA product, direct target, or phenotype mediator.

## Model M3 — Trigger-context specificity for secondary-siRNA entry

model_id: CARRINGTON-M3

```yaml
name: guide_ago_target_register_transcript_and_rdr_dcl_entry_gate
definition: Treat secondary-siRNA entry as a conditional chain requiring an established initiating small RNA, its AGO context, target-site architecture and cleavage register, transcript context, and system-specific candidate RDR/DCL-dependent phased products; the landed canonical TAS and engineered 21-nt contexts specifically motivate RDR6/DCL4 tests, but no single feature or component is universally sufficient.
knowledge_status: agent_inference
framework_relation: strongly_consistent_with_recurrent_team_practice
expert_characteristic_evidence:
  recurrence: passed
  generative_power: passed
  distinctiveness: passed_for_plant_tasiRNA_and_secondary_siRNA_entry_logic
scientific_status: framework_inference_with_context_bounded_field_support
trigger_conditions:
  - a miRNA is proposed to initiate tasiRNA or phasiRNA production
  - cleavage, guide length, complementarity, or a phasing score is treated as sufficient
  - a 21- versus 22-nt rule or AGO assignment is generalized
source_ids:
  - src-doi-10-1016-j-cell-2005-04-004
  - src-doi-10-1016-j-cell-2008-02-033
  - src-doi-10-1073-pnas-0810241105
  - src-doi-10-1038-nsmb-1866
  - JCC-B-S013
  - JCC-B-S014
  - JCC-B-S015
claim_ids:
  - claim-carrington-a-004
  - claim-carrington-a-005
  - claim-carrington-a-006
  - claim-carrington-a-008
  - claim-carrington-a-017
  - JCC-B-C003
  - JCC-B-C004
  - JCC-B-C005
  - JCC-B-C006
```

### Expert-characteristic evidence and two distinct contexts

1. TAS precursor studies linked miRNA-guided cleavage to phase register and then separated AGO7–miR390 dual-site roles and AGO1–miR173 routing (`src-doi-10-1016-j-cell-2005-04-004`, `src-doi-10-1016-j-cell-2008-02-033`, `src-doi-10-1073-pnas-0810241105`; `claim-carrington-a-004`, `claim-carrington-a-005`, `claim-carrington-a-006`).
2. Engineered guide-length studies tested 21- versus 22-nt triggers and RDR6-dependent output, a distinct mechanistic-contrast context (`src-doi-10-1038-nsmb-1866`; `claim-carrington-a-008`). Independent two-hit, sorting, and 22-nt experiments delimit the rule (`JCC-B-C004`, `JCC-B-C005`, `JCC-B-C006`).

### Step-by-step application

1. Establish the initiating small-RNA entity separately: MIR locus, precursor, mature arm and sequence, size, processing precision, and species. A predicted hairpin or database record is insufficient.
2. Resolve the exact target transcript and assembly, target-site architecture, cleavage or binding evidence, and proposed phase register.
3. Test AGO context directly where possible; do not infer it from the 5-prime nucleotide alone.
4. Compare a closest counterfactual: 21 versus 22 nt, cleavage-competent versus noncleavable site, one-hit versus two-hit architecture, or matched AGO contexts, while checking expression/loading equivalence.
5. Require phased secondary-siRNA products with declared register/threshold and test the system's candidate RDR/DCL dependency plus alternative-sized products. Use RDR6/DCL4 as the supported candidate pair only for canonical TAS or engineered 21-nt contexts.
6. Keep entry/biogenesis, direct downstream target action, and phenotype causality in separate columns.
7. Return one verdict: trigger chain supported; trigger plausible but incomplete; secondary-siRNA production present with unresolved trigger; or unsupported.

### Known examples

- miRNA-guided cleavage can set the register of phased TAS products.
- AGO7–miR390 uses site-specific cleavage and noncleavage roles; complementarity does not determine role by itself.
- Tested 22-nt guides can gain secondary-siRNA-triggering competence relative to otherwise comparable 21-nt guides, but guide length is not a universal sufficient rule.

### Failure conditions

- Candidate identity rests on prediction, database annotation, abundance, or sequence similarity alone.
- Cleavage is shown but register, phased output, system-appropriate candidate RDR/DCL dependency, or AGO context is missing.
- The proposed guide contrast also changes abundance, loading, target affinity, or transcript architecture without controls.
- A phased cluster is promoted to direct target regulation or phenotype causality without separate evidence.

### Transfer limits

- The strongest evidence is from tested Arabidopsis TAS/engineered systems plus bounded Nicotiana experiments.
- Do not transfer canonical TAS/21-nt RDR6/DCL4 rules automatically to reproductive, 24-nt, crop, or lineage-specific PHAS routes; interrogate those routes with the relevant candidate machinery and route reproductive PHAS questions to the Meyers lens.
- Do not transfer the rule to animal miRNA systems or unrelated AGO pathways.
- Do not use animal seed-only or Drosha–DGCR8 logic for plant inference.
- Same miRNA name, size, or complementarity does not establish cross-species orthology or conserved triggering.

## Cross-model routing

- Use `CARRINGTON-M1` for virus, viral suppressor, antiviral component, resistance, and disease-phenotype claims.
- Add `CARRINGTON-M2` when DCL/RDR/AGO family assignments, redundancy, compensation, loading, or catalytic activity are central.
- Use `CARRINGTON-M3` for miRNA-triggered tasiRNA/phasiRNA or secondary-siRNA entry claims.
- In every route, apply the cross-cutting evidence-layer heuristic: small-RNA identity or biogenesis, direct target action, and phenotype causality are separate gates. That heuristic is supported by `JCC-B-C013` but is not promoted as a named Carrington model.
