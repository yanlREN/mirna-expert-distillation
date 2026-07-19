# James C. Carrington — Dimension 05: Experimental Decisions and Failure Modes

## Scope

This document extracts recurring experimental decisions from identity-audited Carrington-team primary studies and checks them against independent primary research. It is a neutral scientific lens, not impersonation or attribution of personal opinion.

## High-value experimental decisions

### ED-01 — Begin with discriminating genetics, not a single favored component

**Decision.** Use a small panel of pathway mutants or perturbations spanning plausible branches (for example DCL1/2/3/4, RDR2/RDR6, or AGO1/AGO7), then read out the relevant RNA class and phenotype.

**Why it recurs.** DCL/RDR mutant panels separated miRNA, viral-siRNA, heterochromatic-siRNA, and tasiRNA functions [src-doi-10-1371-journal-pbio-0020104, JCC-B-S004, JCC-B-S006, JCC-B-S007]. Independent DCL work confirmed both specialization and partial redundancy [JCC-B-S012].

**Failure prevented.** Calling a global “RNA silencing” phenotype pathway-specific on the basis of one mutant.

**Boundary.** Loss of a product in a mutant establishes dependency in that system, not direct enzymatic contact or universality across plant species.

### ED-02 — Pair profiling with mutant dependence and an explicit computational rule

**Decision.** For genome-wide small-RNA discovery, predefine size, abundance, phase, genomic-context, and dependency criteria; disclose how conclusions change under permissive versus stringent thresholds.

**Why it recurs.** RDR/DCL-resolved profiling mapped distinct small-RNA populations [JCC-B-S006]. The RDR6/DCL4 study explicitly used phased-cluster filters and reported threshold-sensitive candidate counts [JCC-B-S007].

**Failure prevented.** Treating any dense cluster or apparent periodicity as a functional tasiRNA/phasiRNA locus.

**Boundary.** Computational phasing plus sequencing supports a biogenesis hypothesis; direct targeting and phenotype require separate tests.

### ED-03 — Isolate one mechanistic variable with matched constructs

**Decision.** Compare perturbations that differ in one primary feature: guide length, AGO catalytic residue, target-site cleavage competence, or 5′ nucleotide.

**Examples.**

- 21- versus 22-nt guide variants separated cleavage competence from secondary-siRNA triggering [src-doi-10-1038-nsmb-1866, JCC-B-S015].
- Slicer-defective AGO variants, evaluated with matched protein levels and guide association, separated loading/binding from catalysis [src-doi-10-1105-tpc-112-099945].
- Target-site and AGO substitutions dissected miR390/TAS3 specificity [src-doi-10-1016-j-cell-2008-02-033, JCC-B-S013].
- 5′-nucleotide engineering tested AGO sorting directly [JCC-B-S014].

**Failure prevented.** Assigning causality to the intended feature when sequence, expression, loading, localization, or target affinity also changed.

### ED-04 — Verify the immediate biochemical step before the downstream phenotype

**Decision.** Choose a direct assay matching the claim: cleavage mapping for slicing, AGO immunoprecipitation for loading/association, catalytic mutants for slicer dependence, or phase-register analysis for processive DCL output.

**Why it recurs.** TAS studies combined target sites, cleavage positions, phase registers, genetic dependencies, and downstream targets [src-doi-10-1016-j-cell-2005-04-004, JCC-B-S007, src-doi-10-1016-j-cell-2008-02-033, src-doi-10-1038-nsmb-1866, JCC-B-S013]. AGO work added biochemical purification and catalytic mutants [src-doi-10-1105-tpc-112-099945, JCC-B-S014].

**Failure prevented.** Inferring direct binding or cleavage from expression anticorrelation or target prediction.

### ED-05 — Use independent alleles and control transgene behavior in phenotype rescue

**Decision.** For a genetic rescue, use multiple independent alleles or precise edits, track the transgene across generations, and measure both molecular and morphological endpoints.

**Why it matters.** Re-evaluation of a proposed ARF8 explanation for P1/HC-Pro developmental defects showed that a SALK T-DNA line could confound a 35S-driven transgene through transcriptional silencing; two independent arf8 mutations did not support the single-target model [JCC-B-S016]. Earlier work had already framed the link between viral suppressor, miRNA dysfunction, and development as partial rather than complete [JCC-B-S001].

**Failure prevented.** Mistaking transgene silencing, linked background, or generation-specific segregation for rescue of the proposed causal pathway.

### ED-06 — Test hierarchy and backup explicitly

**Decision.** When a primary processor is lost, examine product-size shifts and higher-order mutants to distinguish true absence from rerouting through backup enzymes.

**Why it recurs.** DCL4 loss caused loss of canonical tasiRNAs and alternative products; double-mutant analyses established hierarchical redundancy [JCC-B-S004, JCC-B-S012]. Genome-wide mutant profiles extended this principle [JCC-B-S006].

**Failure prevented.** Concluding that residual products prove independence from the primary enzyme.

### ED-07 — Separate pathway output from target and phenotype causality

**Decision.** Maintain three result columns:

1. small-RNA/pathway identity and biogenesis;
2. direct target evidence;
3. phenotype causality.

**Why it recurs.** The RDR6/DCL4 work could identify phased loci without automatically establishing their targets [JCC-B-S007]. TAS pathway genetics linked biogenesis to developmental timing but still required target-specific tests for a particular causal route [JCC-B-S004, JCC-B-S011]. Viral suppressor work showed broad miRNA-target changes while later genetics rejected one proposed single-target phenotype explanation [JCC-B-S001, JCC-B-S016].

**Failure prevented.** Converting pathway perturbation into an unsupported statement that one target causes the full phenotype.

### ED-08 — Design an independent-lab check for rules that look universal

**Decision.** Before treating a mechanism as general, seek replication in a different laboratory, construct system, or organism.

**Examples.**

- DCL4 specialization and redundancy were supported by independent Arabidopsis genetics [JCC-B-S004, JCC-B-S012].
- A 22-nt trigger rule was supported by Carrington-team Arabidopsis engineering and independent Nicotiana transient assays [src-doi-10-1038-nsmb-1866, JCC-B-S015].
- AGO sorting by the 5′ nucleotide was established independently, while AGO7–miR390 work defined an important specificity boundary [src-doi-10-1016-j-cell-2008-02-033, JCC-B-S014].

**Failure prevented.** Promoting a locus-specific or construct-specific observation to a field-wide law.

## Failure-mode register

| ID | Failure mode | Diagnostic sign | Corrective action | Key sources |
|---|---|---|---|---|
| FM-01 | Small-RNA class conflation | miRNA, tasiRNA/phasiRNA, hc-siRNA, and viral siRNA discussed as interchangeable | name precursor, size class, DCL/RDR/AGO dependency, and function separately | S002, S004, S006 |
| FM-02 | Cleavage = amplification | a sliced transcript is assumed to produce secondary siRNAs | test guide length, two-hit architecture, RDR6/DCL4 dependence, and phasing | S003, S009, S013, S015 |
| FM-03 | Prediction = direct target | complementarity or anticorrelation is the only support | add cleavage mapping, reporter perturbation, or AGO-context evidence | S001, S003, S007 |
| FM-04 | Direct target = phenotype cause | target abundance tracks a phenotype without discriminating genetics | use independent alleles/edits and molecular plus phenotypic rescue | S001, S011, S016 |
| FM-05 | Single allele rescue artifact | rescue appears only with a T-DNA line or changes across generations | test independent alleles and assay transgene expression/silencing | S016 |
| FM-06 | Sequencing profile = mechanism | cluster abundance or phasing score is treated as sufficient | anchor with pathway mutants and direct assays; report thresholds | S006, S007, S014 |
| FM-07 | Residual products = pathway independence | alternative-sized RNAs persist after primary DCL loss | test higher-order mutants and product-size hierarchy | S004, S012 |
| FM-08 | 5′ nucleotide rule treated as absolute | AGO assignment predicted solely from guide first base | validate by AGO IP/loading and account for specialized AGO–guide pairing | S008, S014 |
| FM-09 | Viral suppressor treated as clean pathway knockout | pleiotropic infection/transgene effects are attributed to one host branch | compare infection and transgene contexts; measure multiple silencing branches | S001, S016 |
| FM-10 | Cross-species overgeneralization | Arabidopsis rule asserted for all plants | revalidate components, loci, and phenotype in the target species | all sources; especially S013, S015 |

`Sxxx` abbreviates `JCC-B-Sxxx`.

## Minimal experimental templates

### Template A — Does a candidate plant miRNA trigger phasiRNAs?

1. First establish candidate miRNA identity independently; a predicted hairpin is insufficient.
2. Map the guide and exact target transcript/assembly.
3. Demonstrate target cleavage or binding with an appropriate direct assay.
4. Test phased output and register, including explicit statistical thresholds.
5. Compare 21- and 22-nt guide variants where biologically justified.
6. Test RDR6 and DCL4 dependence; inspect alternative sizes in higher-order mutants.
7. Test AGO context rather than inferring it solely from the 5′ base.
8. Assess targets and phenotype in separate experiments.

### Template B — Does a viral suppressor phenotype arise through one miRNA target?

1. Separate infection, suppressor-transgene, and empty-vector effects.
2. Measure the relevant mature miRNA, direct target event, and target abundance.
3. Use two independent target alleles or precise edits.
4. Track suppressor-transgene expression and silencing across generations.
5. Require molecular rescue and phenotype rescue to agree.
6. If they disagree, narrow the model to pathway perturbation and retain alternative causes.

### Template C — Does an AGO require slicer activity for a process?

1. Introduce a catalytic-site mutant with a matched wild-type rescue construct.
2. Match protein abundance and localization.
3. Verify guide loading/association.
4. Measure direct cleavage separately from downstream small-RNA production.
5. Test biological rescue; a loaded but catalytically inactive AGO is an informative intermediate, not a null.

## System boundaries

- The strongest evidence base is Arabidopsis, with an independent Nicotiana transient-expression check for the 22-nt trigger.
- None of these decisions makes a new miRNA annotation by itself.
- PARE/degradome or cleavage mapping can establish a direct cleavage event, not complete phenotype causality.
- A viral suppressor perturbs host pathways pleiotropically and is not interchangeable with a precise host-gene knockout.
- Multi-author publications document team results; this lens must remain neutral and cannot claim Carrington's current personal view.
