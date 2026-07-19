# Paper-Interrogation Dimensions — James C. Carrington Lens Candidate

```yaml
expert_id: james-c-carrington
skill_type: scientific_expert_lens
impersonation: forbidden
voice: neutral_scientific
evidence_cutoff: 2026-07-17
question_dimension_count: 6
```

The six dimensions are used to interrogate a new paper or proposal. They are neutral framework-based questions, not simulated statements by James C. Carrington.

## Dimension Q1 — Entity, class, and evidence-layer resolution

dimension_id: CARRINGTON-Q1

Ask:

1. Is the entity a MIR gene family, MIR locus, precursor, mature 5p/3p product, isomiR, specific sequence, TAS/PHAS locus, tasiRNA/phasiRNA, hc-siRNA, vsiRNA, AGO cargo, database record, or genomic coordinate on a named assembly?
2. Which layer is actually measured: identity/biogenesis, direct target action, or phenotype causality?
3. Are prediction, database entry, expression anticorrelation, cleavage, loading, protein effect, and phenotype kept distinct?
4. Are miRNA, tasiRNA/phasiRNA, hc-siRNA, and vsiRNA definitions and dependencies kept separate?

Required output: an entity table, the highest supported evidence layer, the next missing test, and any class-conflation warning.

- `source_ids`: `src-doi-10-1371-journal-pbio-0020104`, `JCC-B-S004`, `JCC-B-S006`, `JCC-B-S016`
- `claim_ids`: `JCC-B-C013`, `JCC-B-C015`, `JCC-B-C011`, `JCC-B-C012`

## Dimension Q2 — Antiviral causal-chain decomposition

dimension_id: CARRINGTON-Q2

Ask:

1. What are the host species/genotype, virus/strain, suppressor/construct, tissue, stage, temperature, infection route, and time point?
2. Does the assay establish suppressor activity, the affected molecular step, a host-component dependency, viral restriction, spread, symptoms, or resistance?
3. Are reporter and native-infection evidence separated?
4. Is viral RNA/protein measured before or alongside symptoms, and are host pleiotropy and developmental effects tested?
5. Does a shared suppressor phenotype hide distinct molecular mechanisms?

Required output: a chain of directly tested edges—viral perturbation → host component → small-RNA/effector output → viral fitness → phenotype—with untested edges marked.

When question count is limited, do not drop host-component genetics or the
virus/strain, infection route, and infection-time context; combine them into a
single discriminating question if necessary.

- `source_ids`: `src-doi-10-1016-s0092-8674-00-81614-1`, `src-doi-10-1073-pnas-230334397`, `src-doi-10-1105-tpc-109-073056`, `src-doi-10-1104-pp-19-00121`
- `claim_ids`: `claim-carrington-a-015`, `claim-carrington-c-005`, `claim-carrington-c-010`, `claim-carrington-c-011`

## Dimension Q3 — Component dependency, hierarchy, and compensation

dimension_id: CARRINGTON-Q3

Ask:

1. Which DCL, RDR, and AGO family members are plausible for the named RNA class and context?
2. Are wild type, single mutants, higher-order mutants, catalytic mutants, and rescue constructs matched for background and sampling?
3. Do residual products change size, phase register, loading, catalysis, or function?
4. Is a primary wild-type role distinguished from backup routing in a mutant?
5. Are molecular output, target action, tissue phenotype, viral fitness, and organismal phenotype measured separately?

Required output: a component-by-readout matrix labeling primary, backup, parallel, tissue-restricted, virus-conditioned, unresolved, or unsupported roles.

- `source_ids`: `src-doi-10-1371-journal-pbio-0020104`, `JCC-B-S004`, `JCC-B-S012`, `src-doi-10-1105-tpc-112-099945`, `src-doi-10-1104-pp-19-00121`
- `claim_ids`: `claim-carrington-a-016`, `JCC-B-C001`, `JCC-B-C002`, `JCC-B-C007`, `claim-carrington-c-013`

## Dimension Q4 — Trigger, AGO, target architecture, and phase register

dimension_id: CARRINGTON-Q4

Ask:

1. Is the initiating miRNA identity independently established at the locus/precursor/mature-sequence level?
2. What is the exact target transcript and assembly, cleavage coordinate, target-site architecture, and proposed phase register?
3. Is AGO context measured, or merely predicted from the 5-prime nucleotide?
4. Does the design compare closest counterfactuals such as 21 versus 22 nt, cleavage-competent versus noncleavable sites, or one-hit versus two-hit architectures?
5. Are phased output, statistical threshold, the system's candidate RDR/DCL dependency, alternative-sized products, downstream targets, and phenotype tested as separate gates? Is RDR6/DCL4 invoked only for a supported canonical TAS or engineered 21-nt context rather than imposed on reproductive or 24-nt PHAS routes?

Required output: one of `trigger_chain_supported`, `trigger_plausible_incomplete`, `phased_output_trigger_unresolved`, or `unsupported`, with the missing edge named.

`trigger_chain_supported` additionally requires an explicit phasing
criterion/register and phased products, tested AGO/target architecture, and the
system-appropriate RDR/DCL dependency. In a canonical TAS context explicitly
test RDR6/DCL4. If any required edge is missing, cap the result at
`trigger_plausible_incomplete` or `phased_output_trigger_unresolved`; do not
transfer DCL4 as a universal PHAS requirement.

- `source_ids`: `src-doi-10-1016-j-cell-2005-04-004`, `src-doi-10-1016-j-cell-2008-02-033`, `src-doi-10-1073-pnas-0810241105`, `src-doi-10-1038-nsmb-1866`
- `claim_ids`: `claim-carrington-a-017`, `JCC-B-C003`, `JCC-B-C004`, `JCC-B-C005`, `JCC-B-C006`

## Dimension Q5 — Experimental discriminability and negative evidence

dimension_id: CARRINGTON-Q5

Ask:

1. What competing models are plausible, and which perturbation changes one mechanistic variable most cleanly?
2. Are expression, localization, loading, target affinity, background, dosage, and transgene behavior matched?
3. Does profiling use declared mapping, assembly, phase, threshold, and dependency rules?
4. Does rescue include independent alleles and the molecular intermediate, not morphology alone?
5. If a candidate or rescue is absent, what sensitivity and threshold bound the negative conclusion?

Required output: a closest-counterfactual design, control gaps, and a scope-reduction statement for every informative negative result.

- `source_ids`: `JCC-B-S006`, `JCC-B-S007`, `src-doi-10-1105-tpc-112-099945`, `JCC-B-S016`
- `claim_ids`: `JCC-B-C008`, `JCC-B-C009`, `JCC-B-C014`, `JCC-B-C016`

## Dimension Q6 — Independence, publication status, transfer, and attribution

dimension_id: CARRINGTON-Q6

Ask:

1. How many genuinely independent laboratory/collaboration networks and methods support the claim?
2. Is any evidence retracted, corrected, abstract-only, talk-only, or institution-only?
3. Does the standing claim depend on the corrected 1999 PNAS Figure 1D equal-loading panel or uncorrected 2010 TuMV Figure 3A/CP values?
4. Are species, orthology, virus family, tissue, temperature, genotype, construct, and crop-field boundaries preserved?
5. Is the statement a team finding, field consensus, expert position, contested claim, historical/superseded record, hypothesis, or Agent inference?
6. Is any coauthored result, profile, talk title, or timeline improperly presented as a current personal view?
7. Has an unnamed, anonymized, hypothetical, or future organism been silently bound to a named species or source case? If an external precedent is used, is it labeled `analogous` and kept outside the input context?

Required output: publication-status ledger, independent-network count, transfer classification (`conserved`, `analogous`, `lineage_specific`, `unsupported_transfer`, or `uncertain`), and attribution label.

- `source_ids`: `src-doi-10-15252-embj-201570030`, `src-doi-10-1073-pnas-1513950112`, `src-doi-10-1093-g3journal-jkaf216`, `src-doi-10-1002-pld3-70128`, `src-url-umn-mpgi-carrington-2014-lecture`
- `claim_ids`: `claim-carrington-c-008`, `claim-carrington-c-009`, `claim-carrington-c-pnas-1999-correction-boundary`, `claim-carrington-a-011`, `claim-carrington-a-012`, `claim-carrington-c-006`

## Stable answer skeleton

For every new paper, answer in this order:

1. Entity and matched context (`CARRINGTON-Q1`).
2. Directly tested antiviral or small-RNA chain (`CARRINGTON-Q2` or `CARRINGTON-Q4`).
3. Component dependency and compensation (`CARRINGTON-Q3`).
4. Discriminating controls and negative-result scope (`CARRINGTON-Q5`).
5. Independence, status, transfer, and attribution (`CARRINGTON-Q6`).
6. Final verdict with supported layer, unresolved alternatives, decisive next experiment, and explicit uncertainty.
