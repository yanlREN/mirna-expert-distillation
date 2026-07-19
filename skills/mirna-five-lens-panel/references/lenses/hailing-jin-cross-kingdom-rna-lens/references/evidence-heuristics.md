# Evidence Heuristics — Hailing Jin Cross-Kingdom RNA Lens Candidate

```yaml
expert_id: hailing-jin
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
heuristic_count: 9
anti_pattern_count: 9
```

These checks are neutral operational syntheses, not quotations or private/current opinions. Multi-author papers remain team findings. Every combined procedure is labeled `agent_inference` even when it is strongly consistent with the public research record.

## Evidence heuristics

### JIN-H1 — Resolve entity and organismal origin before transfer

**IF** an RNA from one organism is reported in another, **THEN** record RNA class, exact sequence, family/locus/precursor/arm where applicable, both assemblies, multi-map policy, low-complexity/shared-sequence handling and compartment, **BECAUSE** a family name or cross-genome short match does not identify either the molecule or its donor, **UNLESS** the conclusion remains explicitly limited to donor-matching reads in a mixed sample.

- `source_ids`: HJ-A-S006, HJ-A-S009, HJ-B-S006, HJ-B-S015
- `claim_ids`: HJ-B-C003, HJ-C-C004

### JIN-H2 — Use a contact-negative control that shares the pipeline

**IF** recipient purification is used to support transfer, **THEN** process a deliberately mixed donor-tissue plus cultured-recipient control through the same purification, washing, marker and mapping workflow, **BECAUSE** lysis and carryover can be introduced by the procedure itself, **UNLESS** an equivalently discriminating lineage-tracing design excludes those routes.

- `source_ids`: HJ-A-S009, HJ-A-S015
- `claim_ids`: HJ-B-C001, HJ-B-C002

### JIN-H3 — Label every completed and missing causal edge

**IF** a cross-kingdom mechanism is claimed, **THEN** score donor production, release, vehicle, extracellular stability, intact-recipient uptake, effector access, direct target and phenotype separately in each direction, **BECAUSE** evidence at one edge cannot backfill the rest, **UNLESS** the claim itself is explicitly restricted to the measured edge.

- `source_ids`: HJ-A-S006, HJ-A-S009, HJ-A-S014, HJ-B-S012
- `claim_ids`: HJ-A-C017, HJ-A-C019, HJ-B-C002, HJ-C-C004

### JIN-H4 — Grade EV topology and subclass, not pellet identity

**IF** EV-mediated delivery is proposed, **THEN** report starting material, density/marker fraction, contaminant markers, nuclease ± membrane disruption, subclass immunocapture, non-EV comparator and route perturbation, **BECAUSE** association, encapsulation, loading, uptake and function are different claims, **UNLESS** the conclusion is limited to an operational extracellular fraction.

- `source_ids`: HJ-A-S009, HJ-A-S010, HJ-B-S009, HJ-B-S006, HJ-B-S015
- `claim_ids`: HJ-B-C006, HJ-B-C007, HJ-B-C008, HJ-C-C013

### JIN-H5 — Test recipient competence in every pathosystem

**IF** an RNAi or SIGS effect is transferred to a new pathogen, **THEN** test intact-cell uptake, DCL/AGO competence, processing, target knockdown, stage and persistence in that recipient, **BECAUSE** Botrytis/Fusarium positives and Zymoseptoria negatives show that competence is organism- and context-dependent, **UNLESS** the statement is only a hypothesis for testing.

- `source_ids`: HJ-A-S008, HJ-C-S010, HJ-C-S011, HJ-B-S013, HJ-B-S014
- `claim_ids`: HJ-B-C012, HJ-C-C009, HJ-C-C010, HJ-C-C015, HJ-C-C016

### JIN-H6 — Match action evidence to RNA class

**IF** recipient action is claimed, **THEN** require AGO/cleavage/reporter or resistant-target evidence for sRNA, uptake/Dicer/sequence-specific knockdown for dsRNA, and intact transcript/ribosome/protein output for mRNA, **BECAUSE** miRNA, siRNA, long dsRNA and mRNA do not share one identity or effector test, **UNLESS** the conclusion is restricted to detection.

- `source_ids`: HJ-A-S006, HJ-A-S008, HJ-B-S012, HJ-B-S013, HJ-A-S015
- `claim_ids`: HJ-B-C011, HJ-B-C012, HJ-B-C014, HJ-C-C008, HJ-C-C015

### JIN-H7 — Separate direct target from full phenotype causality

**IF** a guide–target edge is connected to disease, **THEN** grade prediction/association, direct target evidence and phenotype causality independently and seek resistant-target alleles, rescue or matched recipient-machinery genetics, **BECAUSE** cleavage, PARE, AGO association or target deletion alone cannot make one target the sole disease cause, **UNLESS** equivalent discriminating genetics closes the causal bridge.

- `source_ids`: HJ-A-S006, HJ-A-S009, HJ-B-S012, HJ-C-S011
- `claim_ids`: HJ-B-C011, HJ-C-C008, HJ-C-C010

### JIN-H8 — Preserve controlled negatives and positives by matrix cell

**IF** studies disagree, **THEN** retain host, cultivar, pathogen strain, tissue, stage, RNA class, vehicle, assay and power for each result, **BECAUSE** early tomato–Botrytis, Arabidopsis–Botrytis and wheat–Zymoseptoria address different cells of the scope matrix, **UNLESS** a matched reciprocal replication justifies direct aggregation.

- `source_ids`: HJ-A-S006, HJ-C-S010, HJ-C-S011, HJ-C-S012
- `claim_ids`: HJ-C-C009, HJ-C-C010, HJ-C-C011, HJ-C-C012

### JIN-H9 — Stop application and citation claims at the last verified stage

**IF** a study motivates crop protection or a fine-grained mechanism, **THEN** state the last tested maturity stage and check formal corrections before using figures or supplements, **BECAUSE** controlled efficacy is not field readiness and corrected/unknown publication elements cannot be silently reused, **UNLESS** the higher stage and current record are directly verified.

- `source_ids`: HJ-A-S004, HJ-A-S007, HJ-A-S011, HJ-A-S012, HJ-A-S013, HJ-A-S016
- `claim_ids`: HJ-A-C011, HJ-A-C016, HJ-A-C018, HJ-A-C020, HJ-C-C003
- The 2021 Supplementary Information was replaced and must use the corrected file; the 2025 Science erratum content remains unknown; the 2026 article is abstract-only.

## Anti-patterns

### JIN-AP1 — mixed_sample_reads_equal_cross_kingdom_transfer

Detection in infected tissue without matched purification, contamination and mapping controls is not recipient-cell transfer (`HJ-B-C001`, `HJ-C-C004`).

### JIN-AP2 — bidirectional_effect_equals_symmetric_mechanism

Plant→fungus and fungus→plant cannot inherit one another's vehicle, uptake receptor or intracellular effector (`HJ-A-C019`).

### JIN-AP3 — extracellular_or_pelleted_rna_equals_ev_encapsulation

Co-pelleting or EV enrichment is not membrane encapsulation, and encapsulation is not functional delivery (`HJ-B-C006`, `HJ-B-C008`).

### JIN-AP4 — uptake_or_ago_association_equals_complete_target_and_phenotype_chain

Uptake, AGO association, target repression and disease causality are separate gates (`HJ-B-C002`, `HJ-B-C011`).

### JIN-AP5 — family_name_prediction_or_short_match_equals_exact_mirna

miRNA family, MIR gene family, MIR locus, precursor, mature arm, isomiR and exact sequence must not be collapsed; predicted hairpin or database presence does not prove identity (`HJ-B-C003`).

### JIN-AP6 — one_fungus_or_one_negative_equals_universal_answer

Botrytis/Fusarium positives do not establish universal fungal uptake, and Zymoseptoria or early-tomato negatives do not erase other bounded contexts (`HJ-C-C009`, `HJ-C-C011`, `HJ-C-C012`).

### JIN-AP7 — hig_sigs_or_formulation_efficacy_equals_natural_transfer_or_field_readiness

Engineered HIGS/SIGS demonstrates intervention feasibility, not the same natural route; detached or wounded tissues do not establish field durability (`HJ-B-C012`, `HJ-B-C013`).

### JIN-AP8 — method_edges_or_paper_count_equals_independent_replication

The 42 independent-lab method edges are not 42 networks. The conservative result is six strict networks plus two downgraded external clusters (`HJ-C-C017`).

### JIN-AP9 — correction_omission_or_content_guessing

Do not reuse the replaced 2021 Supplementary Information, guess the 2025 Science erratum content, or reconstruct inaccessible 2026 methods (`HJ-A-C007`, `HJ-A-C011`, `HJ-A-C016`).

## Honest boundaries

1. This Skill is not Hailing Jin and does not represent her current personal opinion.
2. Senior, corresponding or coauthor status does not turn every team result into an individual endorsement.
3. No durable high-quality lecture/Q&A transcript was found; public reasoning is inferred from authored reviews, perspectives and team experimental designs, not vocal style.
4. Mechanism evidence ends at 2026-07-17; 2026-07-18 is retrieval/status-verification time.
5. The strongest high-resolution mechanism chain remains concentrated in the Jin network and Arabidopsis–Botrytis; same-network continuation is not independent replication.
6. Six conservative strict independent networks and two downgraded external clusters meet the special minimum, but do not replicate every edge.
7. Mammalian EV evidence is analogous/uncertain, not conserved plant evidence; the Guo/CAS study is external-led but institutionally proximate and is downgraded for the conservative count.
8. 2025 Science erratum content remains unknown; 2021 corrected Supplementary Information is content-resolved; 2026 evidence is abstract-bounded.
9. miRNA identity, target directness and phenotype causality remain separate; plant and animal small-RNA mechanisms must not be conflated.
10. No raw sequencing data, model training, local LLM, or unauthorized full text was used.
