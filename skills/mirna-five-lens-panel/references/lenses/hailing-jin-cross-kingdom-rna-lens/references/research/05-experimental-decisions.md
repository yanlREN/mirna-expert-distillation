# Hailing Jin — Dimension 05: Experimental Decisions

## Scope

These cases reconstruct recurring experimental decisions from identity-audited Jin-team publications and independent primary checks. They are team-level evidence patterns, not claims about Hailing Jin's private reasoning or current personal views. Mechanism evidence is limited to the project cutoff **2026-07-17**.

Each case follows the required form:

```text
Context → Alternatives → Decision → Evidence → Outcome → Heuristic → Failure condition
```

## Case 1 — Foreign RNA in an infected sample: transfer or mixture?

**Claim closure:** `HJ-B-C001`, `HJ-B-C003`.

**Context.** Botrytis-derived sRNAs were observed during plant infection, and later plant-derived sRNAs or mRNAs were detected in fungal cells isolated from infected leaves [HJ-A-S006, HJ-A-S009, HJ-A-S015].

**Alternatives.** (A) genuine inter-organism transfer; (B) adherent donor material; (C) host/fungal cell carryover during purification; (D) extracellular contamination; (E) shared or ambiguously mapped sequences.

**Decision.** Do not rely on mixed-tissue abundance. Purify recipient cells and process a deliberately mixed negative control—cultured pathogen combined with uninfected donor tissue—through the same workflow. Add donor/recipient markers, nuclease or detergent treatments and direct localization when possible.

**Evidence.** Plant-to-fungus studies compared fungal cells isolated from infected plants with cultured Botrytis mixed with uninfected leaves; the mRNA study also used tagged transcripts and imaging [HJ-A-S009, HJ-A-S015]. The fungal-to-plant study added AGO1 association and genetics beyond sequence detection [HJ-A-S006].

**Outcome.** Selected RNAs passed a stronger transfer threshold than mixed-sample detection alone.

**Generalizable heuristic.** Build a contamination control that experiences the same purification and mapping pipeline but lacks biological contact. Then require a recipient-localized or recipient-active readout.

**Failure condition.** Purity markers are absent, the mixed control is not processed identically, or the exact sequence maps equally well to donor and recipient.

## Case 2 — Is a fungal sRNA a virulence effector or an infection correlate?

**Claim closure:** `HJ-B-C004`, `HJ-C-C011`.

**Context.** Selected Botrytis sRNAs were proposed to suppress plant immunity genes [HJ-A-S006].

**Alternatives.** (A) sequence-specific host RNAi hijacking; (B) generic response to infection; (C) fungal growth/fitness defect in an sRNA-biogenesis mutant; (D) target changes secondary to tissue damage; (E) computational target coincidence.

**Decision.** Test multiple causal nodes: fungal DCL-dependent production, host AGO1 association, host target repression and disease in fungal and host pathway mutants.

**Evidence.** The study combined fungal `dcl1 dcl2`, host `ago1`, AGO1-bound sRNAs, target-expression assays and infection phenotypes in Arabidopsis and tomato [HJ-A-S006]. Later EV/CME work measured uptake, AGO1 loading and target suppression in transport-route perturbations [HJ-A-S014].

**Outcome.** The claim became a multi-node mechanism in the tested system rather than a sequence correlation.

**Generalizable heuristic.** For a proposed cross-kingdom effector, perturb donor biogenesis and recipient effector machinery, then measure the direct molecular intermediate before phenotype.

**Failure condition.** The donor mutant has broad growth defects without complementation, host AGO mutants are pleiotropic, or target repression is not sequence-specific.

## Case 3 — Does externally applied RNA enter a fungus, and by which route?

**Claim closure:** `HJ-B-C012`, `HJ-B-C013`, `HJ-C-C015`, `HJ-C-C016`.

**Context.** External dsRNAs/sRNAs targeting Botrytis DCL genes reduced gray mold on multiple detached commodities, while SIGS studies in Fusarium implicated a plant passage [HJ-A-S008, HJ-B-S013].

**Alternatives.** (A) direct fungal uptake; (B) uptake by plant followed by transfer; (C) RNA remaining on the surface; (D) nonspecific RNA toxicity; (E) plant immune stimulation; (F) sequence-specific fungal RNAi.

**Decision.** Separate routes experimentally. Test uptake in cultured fungi, apply nuclease to remove external material, assay conversion of dsRNA into sRNAs, use fungal Dicer mutants, compare local and distal plant tissue, and include unrelated-sequence controls.

**Evidence.** Botrytis uptake was evaluated by internal fluorescence, nuclease treatment, fungal DCL-dependent processing, target reduction and disease [HJ-A-S008]. Independent Fusarium work showed distal activity involving plant passage and fungal DCL1 [HJ-B-S013]. The 2017 perspective explicitly kept both route models [HJ-B-S003].

**Outcome.** Different systems supported different route contributions; no universal entry path was required.

**Generalizable heuristic.** Treat “spray works” as the start of route analysis. Distinguish direct pathogen uptake from plant passage and require recipient RNAi dependence.

**Failure condition.** Only lesion size is measured, uptake imaging lacks a surface-removal control, or the pathogen's RNAi competence is unknown.

## Case 4 — Is a natural plant miRNA–fungal target link causal for disease?

**Claim closure:** `HJ-B-C011`, `HJ-C-C008`.

**Context.** Cotton miR166 and miR159 were reported to enter Verticillium dahliae and repress `Clp-1` and `HiC-15` [HJ-B-S012].

**Alternatives.** (A) sequence-specific fungal target repression; (B) general cotton defense response; (C) fungal expression changes secondary to reduced growth; (D) another host RNA causes the phenotype; (E) target prediction without causal target engagement.

**Decision.** Engineer fungal target alleles resistant to the respective host miRNA while preserving the target protein's role, then measure fungal virulence in cotton.

**Evidence.** The independent study reports that fungal strains expressing miRNA-resistant `Clp-1` or `HiC-15` had enhanced virulence [HJ-B-S012].

**Outcome.** Target-site genetics tied selected natural host miRNAs more directly to fungal virulence than expression anticorrelation alone.

**Generalizable heuristic.** A resistant-target test is a high-value bridge from direct targeting to phenotype, provided the allele is otherwise matched.

**Failure condition.** The target-site change alters protein coding, transcript stability, basal expression or another regulatory motif independently of RNA pairing.

## Case 5 — Is an RNA inside a plant EV, and which EV subclass?

**Claim closure:** `HJ-B-C006`, `HJ-B-C007`, `HJ-C-C013`, `HJ-C-C014`.

**Context.** Plant EV fractions were proposed to transport sRNAs into Botrytis, but plant EV preparations are heterogeneous and extracellular RNA is not exclusively vesicular [HJ-A-S009, HJ-B-S006, HJ-B-S009, HJ-B-S015].

**Alternatives.** (A) intravesicular RNA cargo; (B) RNA bound to the EV exterior; (C) RNA-protein complex co-pelleting; (D) organelle/debris contamination; (E) a different EV subclass; (F) non-EV apoplastic or leaf-surface RNA.

**Decision.** Improve physical specificity in stages: clean apoplastic wash, differential centrifugation, density gradient, EV/contaminant markers, nuclease protection with membrane-disruption control and TET8 immunoisolation. Analyze non-EV fractions in parallel.

**Evidence.** Jin-team studies used nuclease protection, density gradients, TET8-positive fractions and immunoisolation [HJ-A-S009, HJ-A-S010, HJ-B-S009]. Independent studies found tiny RNAs enriched in EV preparations and distinct abundant non-EV leaf-surface RNA [HJ-B-S006, HJ-B-S015].

**Outcome.** Marker-defined EV cargo can be supported in a tested preparation while preserving non-EV alternatives and EV-subclass heterogeneity.

**Generalizable heuristic.** Never let a 100,000×g pellet define the biological vehicle by itself; combine topology, markers and subclass separation.

**Failure condition.** No membrane-disruption control accompanies nuclease protection, apoplastic wash contains cytosolic markers, or immunoisolation specificity is untested.

## Case 6 — Is EV cargo selectively loaded or passively sampled?

**Claim closure:** `HJ-B-C008`, `HJ-B-C009`, `HJ-C-C006`.

**Context.** Selected Arabidopsis sRNAs appeared enriched in EVs, raising the question of passive abundance versus active loading/stabilization [HJ-B-S006, HJ-A-S010].

**Alternatives.** (A) selective RBP-mediated loading; (B) passive reflection of cellular abundance; (C) differential extracellular stability; (D) fractionation bias; (E) RNA degradation products.

**Decision.** Identify EV-associated RBPs, compare binding to EV-enriched and non-EV-enriched sRNAs, test RBP mutants, quantify sRNA in total and EV fractions, and measure immunity separately.

**Evidence.** AGO1, RH11/RH37 and ANN1/ANN2 were assayed by EV proteomics/fractionation, RNA immunoprecipitation and mutant analysis; selected mutants reduced EV sRNA secretion and altered Botrytis susceptibility [HJ-A-S010]. Independent compositional work showed that absolute cellular abundance does not simply predict EV enrichment and noted many tiny RNAs of uncertain function [HJ-B-S006].

**Outcome.** The data support contributions to loading and/or stabilization, while not resolving those two processes for every RBP.

**Generalizable heuristic.** Compare cargo in total, extracellular and marker-defined EV fractions and perturb the proposed selector. Preserve loading-versus-stability ambiguity unless kinetics or topology resolve it.

**Failure condition.** Only EV abundance is measured, mutant effects on EV number are ignored, or RBP mutants alter immunity independently of cargo.

## Case 7 — How does a fungal EV/sRNA enter a plant cell?

**Claim closure:** `HJ-B-C010`, `HJ-C-C004`.

**Context.** Earlier work established selected Botrytis sRNA action in host cells but did not fully define fungal release and plant uptake [HJ-A-S006].

**Alternatives.** (A) fungal EV secretion plus clathrin-mediated endocytosis; (B) free RNA or RNP uptake; (C) passive entry through damaged tissue; (D) another endocytic route; (E) altered disease due to unrelated functions of EV or CME genes.

**Decision.** Identify a fungal EV marker, purify and characterize fungal EVs, test cargo protection, use fungal marker mutants, observe infection-site vesicles, perturb plant CME, and measure uptake, AGO1 loading, targets and disease.

**Evidence.** BcPLS1-positive EVs, fungal sRNAs in protected EV fractions, plant clathrin-coated vesicles at infection sites, CME genetics, AGO1-loading changes and target effects were combined [HJ-A-S014].

**Outcome.** CME was supported as a major uptake route in the tested Botrytis-Arabidopsis interaction.

**Generalizable heuristic.** A transport-route claim should connect physical carrier, recipient entry machinery and downstream molecular action; phenotype alone cannot identify the route.

**Failure condition.** EV-marker or CME mutants have broad virulence/immune phenotypes without cargo and uptake intermediates, or the marker is assumed universal in another fungus.

## Case 8 — Is transferred plant mRNA intact and translated in fungal cells?

**Claim closure:** `HJ-B-C014`, `HJ-C-C004`.

**Context.** Cross-kingdom sRNA transfer does not establish that full-length mRNAs move or function in a recipient [HJ-A-S015].

**Alternatives.** (A) intact mRNA transfer and fungal translation; (B) plant mRNA fragments; (C) donor protein contamination; (D) plant ribosome carryover; (E) reporter artifact; (F) fungal expression changes unrelated to transferred RNA.

**Decision.** Detect full-length transcripts in marker-defined EVs and purified fungal cells; use RNA aptamer imaging; test fungal ribosome/polysome association with puromycin sensitivity; exclude donor protein in extracellular fractions; express transferred coding sequences in fungus; and test host knockouts/complementation.

**Evidence.** The study combined TET8 immunocapture, Broccoli-tag imaging, recipient-cell purification, fungal TRAP/polysome assays, mutated translation controls, fungal ectopic expression and Arabidopsis `sag21`/`aps1` genetics [HJ-A-S015].

**Outcome.** Selected plant mRNAs were supported as translated cargo that reduced infection in the tested system.

**Generalizable heuristic.** For transferred mRNA, require intactness, recipient ribosome engagement and protein output; sRNA-style target repression assays are not substitutes.

**Failure condition.** Ribosome fractions contain donor markers, the reporter protein is preloaded into EVs, transcript fragments mimic full-length assays, or ectopic expression uses nonphysiological dosage without corroborating host genetics.

## Case 9 — When does a promising SIGS result justify application claims?

**Claim closure:** `HJ-B-C012`, `HJ-C-C003`, `HJ-C-C015`, `HJ-C-C016`.

**Context.** Botrytis and Fusarium experiments show RNA-based disease reduction, but persistence, route and amplification differ [HJ-A-S008, HJ-B-S013, HJ-B-S014].

**Alternatives.** (A) robust, sequence-specific and durable control; (B) transient silencing requiring continuous RNA; (C) wound-dependent uptake; (D) target/pathogen-specific efficacy; (E) formulation or environmental failure; (F) off-target effects on host or non-target organisms.

**Decision.** Move through an application ladder: exact target selection and off-target audit; uptake/processing; time-course persistence; intact versus wounded surfaces; dose and formulation; multiple pathogen isolates; intact plants; greenhouse/field replication; environmental and non-target assessment.

**Evidence.** Botrytis external RNAs protected several detached commodities under controlled conditions [HJ-A-S008]. Fusarium studies showed plant-passage dependence in one setting [HJ-B-S013] and short-lived silencing without sustained amplification plus stronger uptake through wounded surfaces in another [HJ-B-S014].

**Outcome.** The literature supports feasibility and identifies route/persistence constraints, not a blanket field-readiness conclusion.

**Generalizable heuristic.** Report application maturity by the highest completed stage. Detached-tissue efficacy is a proof of concept, not field validation.

**Failure condition.** No persistence or formulation data, only one isolate/target, no sequence-specific controls, or field claims extrapolated from detached tissues.

## Cross-case decision matrix

| claim to assess | closest alternatives | minimum discriminating evidence | highest safe conclusion if missing |
|---|---|---|---|
| foreign RNA transfer | mixture, carryover, mapping ambiguity | recipient purification + mixed control + localization/activity | donor-matching RNA detected |
| EV cargo | exterior RNA, RNP co-pellet, debris | marker fraction + nuclease/topology + subclass control | RNA co-fractionates with operational pellet |
| recipient uptake | surface binding, damaged-cell entry | surface removal + internal localization + recipient molecular effect | RNA associated with recipient preparation |
| direct target | prediction, infection correlation | AGO/effector evidence, cleavage/reporter or resistant target | candidate target |
| phenotype causality | pleiotropy, multiple targets | matched genetics/rescue and molecular intermediates | contributes to phenotype |
| SIGS application | transient/wound-dependent effect | uptake, processing, persistence, formulation and intact-plant tests | controlled-condition proof of concept |

## Practical templates

### Template A — Audit a cross-kingdom sRNA paper

1. Record exact RNA sequence, class, family/locus/arm where applicable, donor and recipient assemblies.
2. Reproduce mapping with shared-sequence and multi-hit accounting if raw data are legally available; otherwise inspect reported rules.
3. Identify mixed-sample, lysis and surface-carryover controls.
4. Grade release/vehicle evidence separately from uptake.
5. Ask whether the RNA engages recipient AGO or another effector.
6. Grade target directness independently from phenotype causality.
7. Audit species, tissue, infection stage and genotype match.
8. Preserve non-EV or alternative-route explanations unless directly excluded.

### Template B — Test a proposed plant EV RNA cargo

1. Collect low-contamination apoplastic wash and document cytosolic contamination markers.
2. Use differential and density-gradient fractionation.
3. Report EV and non-EV fractions, particle measurements and subclass markers.
4. Run nuclease ± membrane disruption and appropriate protein-complex controls.
5. Use marker immunoisolation when available.
6. Compare total, apoplast, EV and supernatant RNA.
7. Test secretion/uptake perturbations and normalize for EV number.
8. Measure recipient uptake and activity, not cargo abundance alone.

### Template C — Advance an RNA spray candidate

1. Confirm pathogen target essentiality and exact sequence specificity.
2. Audit off-targets against host, pathogen isolates and representative non-target organisms.
3. Test direct pathogen uptake and plant-passage alternatives.
4. Test recipient Dicer/AGO competence and target knockdown.
5. Measure duration, dose, surface integrity and formulation stability.
6. Separate lesion size, pathogen biomass and host toxicity.
7. Replicate in intact plants and realistic environments.
8. Stop field-readiness claims at the last validated stage.

## Failure-mode register

| ID | failure mode | diagnostic sign | corrective action | key sources |
|---|---|---|---|---|
| HJ-FM01 | mixed tissue = transfer | only infected-tissue reads | recipient purification and matched mixed control | S001, S004, S011 |
| HJ-FM02 | ultracentrifuge pellet = exosome | no markers/topology | gradient, nuclease ± detergent, immunoisolation | S006, S007, S009 |
| HJ-FM03 | extracellular RNA = EV cargo | non-EV fractions ignored | analyze surface, apoplast, EV and supernatant separately | S006, S015 |
| HJ-FM04 | mapping = organismal origin | shared sequence/multi-hits unreported | exact-sequence and dual-genome audit | S001, S004, S006 |
| HJ-FM05 | target prediction = direct target | complementarity only | recipient effector, cleavage/reporter or resistant target | S001, S012 |
| HJ-FM06 | direct target = full phenotype | no rescue or target-site genetics | molecular and phenotypic causal perturbation | S001, S004, S012 |
| HJ-FM07 | route-mutant phenotype = transport mechanism | no cargo/uptake intermediate | measure EV, uptake, AGO and target steps | S007, S010 |
| HJ-FM08 | HIGS/SIGS = natural ckRNAi | engineered RNA only | test endogenous production and natural route separately | S002, S003, S013 |
| HJ-FM09 | one fungus = all fungi | uptake/processing generalized | test recipient competence and route in each pathogen | S002, S013, S014 |
| HJ-FM10 | detached tissue = field efficacy | no intact-plant/field data | application ladder and durability tests | S002, S014 |
| HJ-FM11 | sRNA rules = mRNA rules | RNA classes conflated | assay intactness and recipient translation for mRNA | S011 |
| HJ-FM12 | family name = exact miRNA | locus/arm/sequence absent | report entity hierarchy and exact sequence | S012 |

`Sxxx` abbreviates `HJ-B-Sxxx`.

## Honest boundaries

- The strongest mechanistic chain is concentrated in Arabidopsis-Botrytis; replication in additional laboratories and pathosystems is needed for universality.
- Cotton-Verticillium supports natural plant-to-fungus miRNA action but does not establish the same EV route.
- Fusarium SIGS findings support route and persistence heterogeneity, not direct contradiction of Botrytis uptake.
- Plant EV markers and fungal EV markers are system-specific until validated elsewhere.
- PARE/degradome, cleavage or AGO association can support direct action but not full disease causality by themselves.
- No raw sequencing data, original read files or local models were used in this work.
