# James C. Carrington — Dimension 03: Reasoning DNA

## Scope and identity boundary

This is an independent reconstruction of recurring reasoning patterns in publications that passed the James C. Carrington identity audit (ORCID `0000-0003-3572-129X`) plus independent primary studies used as scientific checks. It is not Carrington's voice, does not imply his personal endorsement of every team-authored statement, and does not extrapolate beyond publicly documented work. Carrington-team papers were admitted only when name, coauthor network, institution/topic, and author position matched the N0.5 audit.

The analysis keeps four levels separate: small-RNA identity, target directness, pathway mechanism, and phenotype causality. It also keeps miRNAs, tasiRNAs/phasiRNAs, heterochromatic siRNAs, and viral siRNAs distinct.

## Recurrent reasoning patterns

### RDNA-01 — Decompose a broad phenotype into pathway-specific genetic dependencies

The recurring move is to replace a unitary label such as “RNA silencing defect” with a dependency map across DCL, RDR, and AGO components. In Arabidopsis, mutant panels separated DCL1-linked miRNA production, DCL3/RDR2-linked heterochromatic siRNA production, DCL2-linked viral siRNAs, and DCL4-linked tasiRNAs [src-doi-10-1371-journal-pbio-0020104, JCC-B-S004, JCC-B-S006]. Independent DCL studies reproduced the logic of primary and backup processors [JCC-B-S012].

Transferable rule: before assigning mechanism, perturb multiple plausible pathway nodes and ask which RNA class, molecular output, and phenotype move together. A single mutant or a global change in small-RNA abundance is not enough.

Distinctiveness: the informative object is the **pattern of dependencies**, not merely the presence of a small RNA.

### RDNA-02 — Require ordered evidence gates from trigger to phenotype

Across tasiRNA and viral-suppressor studies, claims become stronger only when successive gates are crossed:

1. a candidate interaction or small-RNA species exists;
2. cleavage or binding is directly demonstrated;
3. the predicted downstream small-RNA output changes with the correct genetic dependency and register;
4. the target output changes;
5. a phenotype follows in a causally discriminating perturbation or rescue.

The TAS pathway work illustrates the middle gates: miRNA-guided cleavage can define a processing register, but cleavage alone does not guarantee secondary-siRNA production [src-doi-10-1016-j-cell-2005-04-004, JCC-B-S007, src-doi-10-1038-nsmb-1866, JCC-B-S013, JCC-B-S015]. The P1/HC-Pro literature illustrates the final gate: interference with miRNA-regulated transcripts can accompany morphology, yet a proposed single-target phenotype mechanism can fail when tested with independent alleles and controls for transgene silencing [JCC-B-S001, JCC-B-S016].

Transferable rule: report the highest completed gate and explicitly name the missing next gate. Do not let target prediction, cleavage evidence, or expression anticorrelation stand in for phenotype causality.

### RDNA-03 — Explain specificity by controlled contrasts, not correlations alone

Recurring Carrington-team designs change one mechanistic variable while holding others as constant as practical. Examples include:

- comparing 21-nt and 22-nt guide variants with shared target complementarity to test secondary-siRNA triggering [src-doi-10-1038-nsmb-1866];
- engineering AGO catalytic residues while matching protein accumulation and guide loading to isolate slicer activity [src-doi-10-1105-tpc-112-099945];
- contrasting cleavage-competent and noncleavable TAS3 sites and AGO contexts to distinguish binding, cleavage, and recruitment functions [src-doi-10-1016-j-cell-2008-02-033, JCC-B-S013].

Independent studies using guide-length conversion and 5′-nucleotide engineering support this contrast-based reasoning [JCC-B-S014, JCC-B-S015].

Transferable rule: identify the closest counterfactual construct or genotype. If a perturbation changes multiple properties at once, conclusions remain composite.

### RDNA-04 — Treat pathway rules as conditional and retain exceptions

Several initially simple rules become conditional under further testing. DCL4 is the principal tasiRNA processor, but other DCLs can generate alternative sizes in its absence [JCC-B-S004, JCC-B-S012]. A 5′ terminal nucleotide influences AGO sorting, yet AGO7–miR390 specificity cannot be reduced to this feature alone [src-doi-10-1016-j-cell-2008-02-033, JCC-B-S014]. miRNA-guided cleavage can establish phasing, but many cleaved targets do not spawn secondary siRNAs; two-hit architecture or a 22-nt trigger provides additional context-dependent commitment mechanisms [src-doi-10-1016-j-cell-2005-04-004, src-doi-10-1038-nsmb-1866, JCC-B-S013, JCC-B-S015].

Transferable rule: state rules with their organism, locus, guide, AGO, and mutant context. Preserve counterexamples as constraints rather than averaging them away.

### RDNA-05 — Use genome-scale profiles as maps, then return to genetic and biochemical anchors

Genome-wide small-RNA profiling was repeatedly paired with mutant libraries and explicit filters for size, phasing, genomic context, and dependence on specific biogenesis factors [JCC-B-S006, JCC-B-S007]. These studies were careful about threshold effects and did not equate broad locus correlations with direct gene regulation. The same logic appears in AGO immunoprecipitation followed by sequencing, where biochemical partitioning makes the global profile interpretable [JCC-B-S014].

Transferable rule: a profile nominates loci and patterns; it does not by itself prove identity, direct targeting, or biological function. Require orthogonal validation appropriate to the claim.

### RDNA-06 — Distinguish pathway entry, catalytic action, amplification, and biological output

The literature repeatedly separates:

- guide recognition/loading;
- target binding;
- target cleavage;
- RDR6 recruitment and secondary-siRNA amplification;
- downstream target repression;
- developmental or antiviral phenotype.

Slicer-defective AGO experiments show that loading and association can be retained when cleavage is lost [src-doi-10-1105-tpc-112-099945]. Guide-length experiments show that cleavage-competent complexes can differ in amplification competence [src-doi-10-1038-nsmb-1866, JCC-B-S015]. Viral suppressor work shows that perturbing a shared silencing component can affect several branches and phenotypes without identifying a single causal target [JCC-B-S001].

Transferable rule: name the biochemical step directly assayed; avoid collapsing all steps into “silencing.”

### RDNA-07 — Let negative results narrow the model

Negative or discordant results are used as model constraints: few nearby genes showed evidence of direct regulation by heterochromatic siRNA loci [JCC-B-S006]; stringent RDR6/DCL4 scans did not reveal large classes of new noncoding TAS-like loci [JCC-B-S007]; DCL1 overexpression could alleviate P1/HC-Pro morphology without correcting the measured miRNA defects, and independent arf8 alleles did not support ARF8 as the single cause [JCC-B-S016].

Transferable rule: a well-controlled failure to rescue or failure to reproduce should reduce causal scope. It should not be discarded merely because an earlier model was attractive.

## Candidate decision sequence for new problems

1. Define the biological entity precisely: MIR locus, precursor, mature arm/sequence, tasiRNA/phasiRNA, heterochromatic siRNA, or viral siRNA.
2. Specify organism, tissue, developmental stage, genotype, treatment, and genome assembly.
3. Build competing pathway models and choose perturbations that discriminate among them.
4. Measure the direct molecular event before downstream abundance or phenotype.
5. Test pathway dependency with matched controls, multiple alleles, catalytic mutants, or rescue constructs.
6. For secondary siRNAs, test register, guide length, trigger architecture, AGO context, and RDR6/DCL4 dependency.
7. For phenotype claims, separate molecular rescue from morphological rescue and rule out transgene or background effects.
8. State the supported gate, unresolved alternatives, and system boundary.

## Framework validation matrix

| Candidate framework | Context 1 | Context 2 | Transferable? | Distinctive? | Status |
|---|---|---|---|---|---|
| Genetic dependency maps before mechanism | miRNA/hc-siRNA/viral-siRNA DCL/RDR mutants [S002] | tasiRNA DCL4 hierarchy and genome-wide mutant profiles [S004, S006, S007] | Yes | Yes | retained |
| Ordered evidence gates | tasiRNA trigger → phasing → targets [S003, S007, S009] | viral suppressor → miRNA changes → proposed phenotype [S001, S015] | Yes | Yes | retained |
| Controlled mechanistic contrasts | 21- vs 22-nt guides [S009] | slicer-competent vs slicer-defective AGO [S010] | Yes | Yes | retained |
| Conditional rules with exceptions | DCL redundancy [S004, S012] | AGO sorting and trigger exceptions [S008, S013, S014, S015] | Yes | Yes | retained |
| Genome-scale discovery plus anchors | mutant small-RNA landscapes [S006, S007] | AGO IP/sRNA sequencing [S014] | Yes | Moderate | retained |
| Negative results narrow causality | limited nearby-gene effects [S006] | ARF8/transgene-silencing re-evaluation [S016] | Yes | Yes | retained |

`Sxxx` in the table abbreviates the corresponding `JCC-B-Sxxx` source ID.

## Limitations

- Team-authored results cannot establish Carrington's individual present-day opinion.
- Most mechanistic evidence here is from Arabidopsis; transfer to crops or other plant lineages requires new validation.
- Several Cell/Current Biology articles were available only at abstract or publisher-summary level during this run; claims from them are intentionally bounded.
- Small-RNA sequencing used in the cited studies is published evidence, not raw data acquired or reprocessed in this project.
- This analysis does not establish miRNA identity for any new locus and must not be used as a substitute for annotation criteria.
