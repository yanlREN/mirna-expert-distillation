# Evidence Heuristics — Blake C. Meyers Lens Candidate

```yaml
expert_id: blake-c-meyers
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
heuristic_count: 10
anti_pattern_count: 8
honest_boundary_count: 7
```

These operational checks are not quotations or private views. `expert_position` refers only to recurring public frameworks; independent critiques are `field_consensus` or `contested` as appropriate; combined procedures are `agent_inference`.

## Evidence heuristics

### MEYERS-H1 — PARE cleavage is direct, but not phenotype causality

**IF** a PARE/degradome peak aligns with the expected plant small-RNA-guided cleavage position,  
**THEN** call the cut direct molecular evidence in the sampled RNA pool and separately score AGO loading, protein effect, target exclusivity, and phenotype causality,  
**BECAUSE** cleavage-product capture answers a narrower question than complete regulatory or organismal causality,  
**UNLESS** matched target-site genetics, rescue, protein, and phenotype evidence independently close those later gates.

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-doi-10-1038-nbt1417`, `src-doi-10-1016-j-cub-2008-04-042`, `src-doi-10-1038-s41467-020-19034-y`
- `claim_ids`: `claim-meyers-a-pare-cleavage-not-phenotype`, `claim-meyers-c-002`, `claim-meyers-c-003`, `claim-meyers-c-008`

### MEYERS-H2 — Audit caller, register, mapping, replication, and nulls together

**IF** a paper reports PHAS loci or a large PARE targetome,  
**THEN** record the caller/rules, phase register, assembly and multimapping policy, biological replication, query-set size, and fit-for-purpose null behavior,  
**BECAUSE** abundance, background, targeting rules, transcript annotation, and multiplicity can change calls,  
**UNLESS** the claim is explicitly limited to a computational candidate list with no biological validation claim.

- `knowledge_status`: `contested`
- `source_ids`: `src-doi-10-1093-bioinformatics-btu628`, `src-doi-10-1186-s12864-017-4031-9`, `src-doi-10-1093-nar-gky609`, `src-doi-10-1111-nph-17910`
- `claim_ids`: `claim-meyers-c-005`, `claim-meyers-c-004`, `claim-meyers-c-011`

### MEYERS-H3 — A PHAS trigger must align to register and dependency

**IF** a miRNA or other initiator is proposed for a PHAS locus,  
**THEN** test trigger identity, cleavage coordinate, phase offset/register, replicate stability, and pathway dependency as a linked chain,  
**BECAUSE** complementarity and phasing can coexist by chance or arise from another initiator,  
**UNLESS** the trigger remains clearly labeled a computational hypothesis.

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1101-gad-177527-111`, `src-doi-10-1073-pnas-2402285121`, `src-doi-10-1073-pnas-2504349122`
- `claim_ids`: `claim-meyers-b-trigger-chain-nblrr`, `claim-meyers-b-noncanonical-trigger-stop`, `claim-meyers-b-wheat-cross-species-test`

### MEYERS-H4 — Reproductive comparisons require stage × cell type × genotype

**IF** reproductive phasiRNA abundance, cleavage, loading, or fertility differs between samples,  
**THEN** match species, cytological stage, cell layer, genotype/allele, and sampling method before assigning mechanism,  
**BECAUSE** whole-anther averages can mix premeiotic, meiotic, postmeiotic, somatic-wall, and germ-cell populations,  
**UNLESS** the conclusion is only an explicitly bulk-tissue observation.

- `knowledge_status`: `field_consensus`
- `source_ids`: `src-doi-10-1073-pnas-1418918112`, `src-doi-10-1038-s41467-020-16637-3`, `src-doi-10-1038-s41467-020-19034-y`
- `claim_ids`: `claim-meyers-a-maize-stage-cell-type-matching`, `claim-meyers-c-006`, `claim-meyers-c-007`, `claim-meyers-c-008`

### MEYERS-H5 — Hold the molecular lesion constant across environment

**IF** a pathway mutant has temperature- or photoperiod-dependent fertility,  
**THEN** measure the molecular lesion and phenotype in each environment with matched genotype controls,  
**BECAUSE** phenotypic rescue can arise through downstream or parallel buffering without restoring phasiRNA production,  
**UNLESS** the environmental claim is explicitly descriptive and makes no molecular-rescue inference.

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122`
- `claim_ids`: `claim-meyers-b-pms1t-context-causality`, `claim-meyers-b-dcl5-temperature-decoupling`, `claim-meyers-b-wheat-cross-species-test`

### MEYERS-H6 — Comparative absence must survive ascertainment audit

**IF** a lineage is said to lack a reproductive PHAS pathway or trigger,  
**THEN** audit assembly quality, locus annotation, matched developmental stage, library depth, precursor/trigger detectability, Dicer/AGO inventory, and caller sensitivity,  
**BECAUSE** nondetection can be biological absence or ascertainment failure,  
**UNLESS** multiple matched evidence axes support loss and the conclusion remains lineage- and assay-bounded.

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1073-pnas-2402285121`
- `claim_ids`: `claim-meyers-a-angiosperm-presence-is-not-universal`, `claim-meyers-b-distribution-not-function`

### MEYERS-H7 — Transfer crops by components, not pathway labels

**IF** a maize, rice, or wheat result is transferred to another crop,  
**THEN** separately test ortholog/homeolog dosage, precursor/locus architecture, trigger, Dicer/RDR, AGO/effector, stage/cell context, target action, environment, and rescue,  
**BECAUSE** shared DCL5 dependence or a 21-/24-nt label can coexist with different initiation, products, targets, and penetrance,  
**UNLESS** the conclusion is limited to a verified shared component and labeled `conserved`, `analogous`, `lineage_specific`, `uncertain`, or `unsupported_transfer`.

- `knowledge_status`: `agent_inference`
- `source_ids`: `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1073-pnas-2504349122`, `src-doi-10-1038-s41467-020-16637-3`
- `claim_ids`: `claim-meyers-b-wheat-cross-species-test`, `claim-meyers-c-012`

### MEYERS-H8 — Separate production, accumulation, mobility, and function

**IF** a small RNA is enriched in a different cell from its precursor or biogenesis factor,  
**THEN** score source production, local accumulation, movement, recipient loading, target action, and phenotype as separate gates,  
**BECAUSE** spatial presence and movement do not establish effector use or biological function after arrival,  
**UNLESS** the claim is restricted to the exact spatial observation directly measured.

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1073-pnas-1418918112`, `src-doi-10-1111-nph-18167`, `src-doi-10-1038-s41467-020-19034-y`
- `claim_ids`: `claim-meyers-b-cell-stage-resolution`, `claim-meyers-a-spatial-origin-mobility-function-separation`, `claim-meyers-c-008`

### MEYERS-H9 — Plant miRNA identity precedes target plausibility

**IF** a foldable locus or database record is proposed as a plant miRNA,  
**THEN** require replicated small-RNA evidence and precise plausible hairpin processing while actively excluding siRNA-producing alternatives,  
**BECAUSE** target complementarity, conservation, or a predicted hairpin cannot retroactively establish miRNA identity,  
**UNLESS** the record remains explicitly `candidate` or `unresolved`.

- `knowledge_status`: `expert_position`
- `source_ids`: `src-doi-10-1105-tpc-17-00851`, `src-doi-10-1126-science-1114112`
- `claim_ids`: `claim-meyers-b-mirna-annotation-replication`, `claim-meyers-a-deep-sequencing-reveals-heterogeneity`
- Boundary: this is a shared Meyers–Axtell annotation position and field safeguard, not a uniquely Meyers core model.

### MEYERS-H10 — A new class may stop at discovery

**IF** stage-resolved sequencing identifies a new 21- or 24-nt PHAS cohort,  
**THEN** report accumulation, composition, register, and locus evidence while leaving biogenesis factors, AGO loading, targets, and function unresolved,  
**BECAUSE** a reproducible class can be real before its mechanism or phenotype is known,  
**UNLESS** direct perturbation and matched action/phenotype assays close those gates.

- `knowledge_status`: `hypothesis`
- `source_ids`: `src-doi-10-1002-tpg2-70107`
- `claim_ids`: `claim-meyers-b-postmeiotic-discovery-stop`, `claim-meyers-c-013`

## Anti-patterns

### MEYERS-AP1 — PHAS call equals biological pathway

Treating one caller, one score, or a read cluster as proof of a PHAS precursor, trigger, targets, and function. Apply `MEYERS-M5` and keep computation, replication, register, molecular action, and phenotype separate (`claim-meyers-c-005`).

### MEYERS-AP2 — PARE peak equals complete causality

Promoting cleavage to unique target, protein effect, or phenotype without additional evidence. Apply `MEYERS-H1` (`claim-meyers-c-003`, `claim-meyers-b-pare-cleavage-not-phenotype`).

### MEYERS-AP3 — Force every PHAS locus into a canonical miRNA-trigger model

Ignoring negative trigger, AGO, cis-cleavage, motif, or dependency evidence. Use `MEYERS-M2`; keep nondetection assay-bounded (`claim-meyers-b-noncanonical-trigger-stop`).

### MEYERS-AP4 — Whole-anther abundance identifies a cell of action

Conflating production, accumulation, movement, and response in a rapidly changing mixed tissue. Use `MEYERS-M3` and `MEYERS-M4` (`claim-meyers-c-007`, `claim-meyers-a-spatial-origin-mobility-function-separation`).

### MEYERS-AP5 — Environmental fertility rescue means molecular rescue

Assuming permissive temperature or photoperiod restores the upstream phasiRNA lesion. The maize DCL5 data explicitly separate stable molecular depletion from conditional penetrance (`claim-meyers-b-dcl5-temperature-decoupling`).

### MEYERS-AP6 — Broad presence means conserved function

Transferring trigger, AGO, target, or fertility roles from a broadly detected size class. Distribution is a separate verdict from mechanism and function (`claim-meyers-b-distribution-not-function`).

### MEYERS-AP7 — Same miRNA number or size class means orthology

Equating a shared miR number, 21-/24-nt label, or Dicer name with one-to-one locus, precursor, mature sequence, cell context, or target conservation (`claim-meyers-c-012`).

### MEYERS-AP8 — Paper count equals independent replication

Counting semantic duplicates or collaboration-linked papers as independent recurrence. Independence must be audited by laboratory/network and method/context; `claim-meyers-c-015` is an Agent-derived auditor rule, not an expert position.

## Honest boundaries

1. **Talk evidence is thin.** `src-url-ista-2025-phased-secondary-sirnas` supports public scope and explicit uncertainty; `src-url-sustech-2026-phased-secondary-sirnas` supports only date/title/topic. Neither supports response style, Q&A, or persona.
2. **Four records are abstract-bounded in the authoritative corpus.** No unobserved figure-level detail may be reconstructed from them; `src-doi-10-1038-nbt1417` supports only its verified cleavage-method minimum.
3. **Postmeiotic classes remain unresolved.** `claim-meyers-c-013` supports staged discovery, not biogenesis, target, or fertility function.
4. **PARE targetome breadth remains contested.** `claim-meyers-c-008` supports cell-matched cleavage, while `claim-meyers-c-011` requires multiplicity-aware nulls. Neither side erases the other.
5. **Correction scope is bibliographic only.** `src-doi-10-1038-s41467-023-37355-6` corrects one author spelling and reports no changed data, figures, analyses, or conclusions (`claim-meyers-c-010`). It is not independent scientific evidence.
6. **Historical MPSS discipline is not a current criterion set.** `claim-meyers-c-001` supports explicit counting/mapping context, not reuse of obsolete platform-specific filters.
7. **All cross-paper procedures are model-based inference.** Coauthorship, senior position, citation count, database inclusion, or Agent agreement cannot convert `agent_inference` into a personal view or scientific fact.

