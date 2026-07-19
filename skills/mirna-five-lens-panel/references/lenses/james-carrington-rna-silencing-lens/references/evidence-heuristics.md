# Evidence Heuristics — James C. Carrington Lens Candidate

```yaml
expert_id: james-c-carrington
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
heuristic_count: 8
anti_pattern_count: 8
honest_boundary_count: 8
```

These checks are operational syntheses, not quotations or claims about Carrington's private or current views. `expert_position` is used only for bounded public/team evidence; combined procedures remain `agent_inference`; independent status and critique records are not converted into expert attribution.

## Evidence heuristics

### CARRINGTON-H1 — Keep identity/biogenesis, direct action, and phenotype causality separate

**IF** a plant small-RNA paper links a locus or pathway to a target and phenotype,  
**THEN** score three independent layers—small-RNA identity or biogenesis, direct target action, and phenotype causality—and report the highest completed layer without backfilling the others,  
**BECAUSE** pathway genetics, cleavage, and morphological rescue answer different questions,  
**UNLESS** matched target-site genetics or equivalent causal intervention independently closes all three layers.

- `knowledge_status`: `agent_inference` with field-supported scientific boundaries
- `source_ids`: `JCC-B-S004`, `JCC-B-S011`, `JCC-B-S016`
- `claim_ids`: `JCC-B-C013`, `JCC-B-C011`, `JCC-B-C012`
- This is a cross-cutting heuristic, not a separately named Carrington core model.

### CARRINGTON-H2 — Name the immediate biochemical step

**IF** an AGO, DCL, RDR, trigger, or suppressor mechanism is claimed,  
**THEN** specify whether the assay tests production, binding/loading, cleavage, amplification, spread, or downstream output and use a matched direct assay,  
**BECAUSE** association can persist without catalysis and cleavage can occur without secondary-siRNA commitment,  
**UNLESS** the conclusion is explicitly limited to the measured association or abundance.

- `knowledge_status`: `expert_position` for the matched AGO design; broader ladder is `agent_inference`
- `source_ids`: `src-doi-10-1105-tpc-112-099945`, `src-doi-10-1038-nsmb-1866`
- `claim_ids`: `claim-carrington-a-009`, `JCC-B-C004`, `JCC-B-C007`

### CARRINGTON-H3 — A genome-scale profile nominates; dependency and direct tests adjudicate

**IF** expression or small-RNA profiling reveals a candidate locus, class, or target,  
**THEN** preserve assembly, mapping, size/register, threshold, mutant dependency, and locus context, then return to an orthogonal assay suited to the proposed mechanism,  
**BECAUSE** differential abundance, clustering, or phasing alone does not prove identity, direct regulation, or function,  
**UNLESS** the output is clearly labeled a discovery list with no mechanistic claim.

- `knowledge_status`: `expert_position` in team methods; public interview framing is `historical`
- `source_ids`: `JCC-B-S006`, `JCC-B-S007`, `src-url-annenberg-carrington-genomics-interview`
- `claim_ids`: `JCC-B-C008`, `JCC-B-C009`, `claim-carrington-c-003`

### CARRINGTON-H4 — Audit rescue with independent alleles and molecular intermediates

**IF** morphology or resistance is said to be rescued,  
**THEN** require matched rescue constructs or multiple independent alleles, background control, transgene-expression/silencing checks, and both molecular and phenotypic endpoints,  
**BECAUSE** linked background, dosage, or transgene silencing can mimic rescue,  
**UNLESS** a precise endogenous edit and orthogonal rescue already exclude those alternatives.

- `knowledge_status`: `expert_position` for matched AGO rescue; the ARF8 re-test is `contested` independent critique
- `source_ids`: `src-doi-10-1105-tpc-112-099945`, `JCC-B-S016`
- `claim_ids`: `JCC-B-C012`, `JCC-B-C014`

If a phenotype is attributed to a specific small-RNA class or pathway, require
the system-appropriate class-dependency readout and multiple independent
alleles, or a validated allele plus orthogonal rescue. Verify the molecular
intermediate as well as the phenotype; morphology or one unconfirmed allele
cannot identify the causal class.

### CARRINGTON-H5 — Let a controlled negative result reduce scope

**IF** a direct effect, candidate class, or rescue is not detected,  
**THEN** state assay sensitivity, threshold, sample, genotype, and alternatives, then narrow the model to what the negative result excludes,  
**BECAUSE** threshold-bounded nondetection and failed independent-allele rescue constrain causal claims,  
**UNLESS** the assay demonstrably lacked power to address the claim.

- `knowledge_status`: `expert_position`/`contested` by context
- `source_ids`: `JCC-B-S006`, `JCC-B-S007`, `JCC-B-S016`
- `claim_ids`: `JCC-B-C009`, `JCC-B-C010`, `JCC-B-C012`, `JCC-B-C016`

### CARRINGTON-H6 — Remove invalid evidence edges before judging a network

**IF** a mechanism is supported by several papers,  
**THEN** deduplicate collaboration networks, inspect retractions and corrections, remove invalid figure- or paper-level edges, and ask whether standing independent evidence still supports the bounded claim,  
**BECAUSE** paper count, same-network repetition, and a popular conclusion do not repair invalid evidence,  
**UNLESS** the statement is purely bibliographic and explicitly status-labeled.

- `knowledge_status`: `agent_inference` Evidence Auditor rule, not Carrington-specific position
- `source_ids`: `src-doi-10-1093-emboj-17-22-6739`, `src-doi-10-15252-embj-201570030`, `src-doi-10-1073-pnas-96-24-14147`, `src-doi-10-1073-pnas-1513950112`
- `claim_ids`: `claim-carrington-c-008`, `claim-carrington-c-009`, `claim-carrington-c-pnas-1999-correction-boundary`
- The Brigneti 1998 article is never a positive edge. The PNAS correction makes Figure 1D equal-loading support unavailable but does not retract the article.

### CARRINGTON-H7 — Match virus × host × tissue × genotype × environment

**IF** a component is called broadly antiviral or dominant,  
**THEN** restate the tested virus/strain, host, tissue, genotype, temperature, time, suppressor status, and endpoint before transfer,  
**BECAUSE** AGO, RDR, and DCL contributions can change across viruses, tissues, mutant combinations, and temperature,  
**UNLESS** a properly factorial design has already tested the proposed scope.

- `knowledge_status`: `field_consensus` for bounded context dependence; cross-network combination is `agent_inference`
- `source_ids`: `src-doi-10-1104-pp-19-00121`, `src-doi-10-1371-journal-pone-0014639`, `src-doi-10-1128-jvi-79-24-15209-15217-2005`
- `claim_ids`: `claim-carrington-a-010`, `claim-carrington-c-012`, `claim-carrington-c-015`, `claim-carrington-c-017`

### CARRINGTON-H8 — Translate mechanism to crops without transferring certainty

**IF** model-plant logic is used to motivate a crop allele or engineering intervention,  
**THEN** separate association, direct perturbation, molecular sufficiency, disease phenotype, inheritance, off-target effects, and field durability,  
**BECAUSE** a conserved research question does not establish conserved orthology, causal pathway, or durable resistance,  
**UNLESS** each level is directly tested in the crop, genotype, virus, tissue, and environment of interest.

If the input leaves the crop unnamed, keep it unnamed. A named crop study from
the corpus is an external `analogous` precedent only and must never replace the
input species, genotype, attribution, or claim subject.

- `knowledge_status`: `hypothesis` for the crop facts; the translation procedure is `agent_inference`
- `source_ids`: `src-doi-10-1093-g3journal-jkaf216`, `src-doi-10-1002-pld3-70128`
- `claim_ids`: `claim-carrington-a-011`, `claim-carrington-a-012`, `claim-carrington-a-018`

## Anti-patterns

### CARRINGTON-AP1 — reporter_suppression_equals_native_infection_mechanism

A PTGS/GFP reporter can show suppressor activity, but cannot by itself establish the native target, infection-stage requirement, viral fitness effect, or symptom causality (`claim-carrington-a-001`, `claim-carrington-c-007`).

### CARRINGTON-AP2 — small_rna_abundance_equals_loading_activity_or_resistance

Total or viral small-RNA abundance is not AGO loading, catalytic action, restriction, or disease causality (`claim-carrington-c-016`, `claim-carrington-a-010`).

### CARRINGTON-AP3 — one_dcl_rdr_or_ago_equals_universal_pathway

A primary component in one RNA class, virus, tissue, or genotype does not become universally dominant; backup routing is not wild-type interchangeability (`JCC-B-C002`, `claim-carrington-c-012`).

### CARRINGTON-AP4 — cleavage_or_22nt_equals_complete_phasirna_chain

Cleavage or a 22-nt guide does not by itself establish miRNA identity, AGO context, phased RDR6/DCL4 output, direct targets, or phenotype (`JCC-B-C003`, `JCC-B-C004`, `JCC-B-C005`).

### CARRINGTON-AP5 — direct_target_equals_full_phenotype_cause

Direct molecular action is not proof that one target explains the complete phenotype; independent alleles, molecular rescue, and pleiotropy controls remain necessary (`JCC-B-C011`, `JCC-B-C012`, `JCC-B-C013`).

### CARRINGTON-AP6 — same_name_or_component_equals_cross_species_orthology

Shared miRNA, AGO/DCL/RDR, gene, or virus-family names do not establish orthology, conserved routing, or transferable phenotype.

### CARRINGTON-AP7 — paper_count_overrides_retraction_or_correction

The retracted Brigneti 1998 article cannot support any positive claim, and duplicated/corrected figures cannot be used as though unchanged (`claim-carrington-c-008`, `claim-carrington-c-pnas-1999-correction-boundary`).

### CARRINGTON-AP8 — talk_title_profile_or_timeline_equals_current_personal_view

An event title, institutional profile, interview, meeting report, or publication chronology cannot support a reconstructed persona, current private view, or attribution of every team result (`claim-carrington-c-001`, `claim-carrington-c-006`, `claim-carrington-a-018`).

## Honest boundaries

1. **No impersonation:** this is a `scientific_expert_lens`, not James C. Carrington, and it does not represent his current personal opinion.
2. **Team attribution:** multi-author papers are team findings; senior, corresponding, or coauthor status does not assign every statement to one author.
3. **Cutoff:** scientific evidence ends at `2026-07-17`; `2026-07-18` is retrieval/status-verification time only.
4. **Talk scope:** no complete lecture or Q&A transcript was landed. The interview and meeting report support only dated, explicit public framing; the 2014 flyer is title/date inventory only.
5. **Abstract scope:** the three Cell records and other abstract-only sources support only the verified minimum; inaccessible methods, figures, or quantitative details are not inferred.
6. **Publication status:** the 1998 Brigneti article is retracted and never positive; the 1999 PNAS Figure 1D equal-loading inference is unsupported after correction; exact 2010 TuMV Figure 3A/CP wording must resolve `src-doi-10-1105-tpc-15-00204` and `claim-carrington-c-tpc-2010-correction-boundary` and use the corrected panel and values.
7. **Small-RNA boundaries:** miRNA, tasiRNA/phasiRNA, hc-siRNA, and vsiRNA are distinct; identity/biogenesis, direct target action, and phenotype causality are separate.
8. **Inference boundary:** `claim-carrington-a-015` through `claim-carrington-a-018` remain verified `agent_inference`; `claim-carrington-a-018` is history only, and `JCC-B-C013` remains a cross-cutting heuristic rather than an automatic expert model.
9. **Entity-preservation boundary:** never de-anonymize or concretize an unnamed, hypothetical, or future organism from a similar source; label any named external case as `analogous` and keep it outside the input context.
10. **Auditor provenance boundary:** completing a local citation, correction, or schema check is not an independent Evidence Auditor result. If a required Auditor result is absent, report `unavailable` and remain pending; never emit a pass-like audit status.
11. **Literal ledger boundary:** use only the Skill's closed status, directness, independence, scope, publication, transfer, gate, and audit vocabularies. Split observed, unsupported, corrected, and attribution propositions instead of inventing compound enum values.
