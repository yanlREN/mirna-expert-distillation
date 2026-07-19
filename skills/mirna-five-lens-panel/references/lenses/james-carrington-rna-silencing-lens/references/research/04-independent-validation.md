# James C. Carrington — Dimension 04: Independent Validation, Conflict and Boundaries

## Scope and network rule

This dimension evaluates external support, limits and status records relevant to Carrington-associated claims about viral silencing suppressors, antiviral RNAi and DCL/AGO/RDR/small-RNA pathway organization. Papers are counted by laboratory/collaboration network rather than by article count. No result is treated as Carrington's personal position merely because it is consistent with his work.

Five external networks are represented:

1. Baulcombe/Voinnet/Carr network — several sources, counted once;
2. Burgyan/Silhavy/Hall network — two mechanistic sources, counted once;
3. Vaucheret/Bartel network — DCL genetics;
4. Poethig network — tasiRNA biogenesis;
5. Qu/Morris network — RDR6 antiviral genetics.

The retracted Brigneti article and its retraction notice are status records, not positive replication.

## 1. Independent source table

| Source ID | Network | System and method | Finding used | Independence/status boundary |
|---|---|---|---|---|
| `src-doi-10-1073-pnas-96-24-14147` | Baulcombe/Voinnet | plant virus panel; PTGS reporters | diverse tested viruses encode suppressors with distinct modes | one network; standing record at cutoff |
| `src-doi-10-1093-emboj-17-22-6739` | Baulcombe/Voinnet/Ding | GFP PTGS reporter | none used positively | **retracted**; excluded |
| `src-doi-10-15252-embj-201570030` | publisher/status | retraction notice | authoritative invalidation of the 1998 paper as evidence | status evidence only |
| `src-doi-10-1016-s0092-8674-03-00984-x` | Hall/Burgyan | p19-siRNA crystallography and binding | p19 is a 21-nt duplex-size-selective molecular caliper | abstract-bounded; not all suppressors |
| `src-doi-10-1128-jvi-01963-05` | Silhavy/Burgyan | multi-suppressor dsRNA binding comparison | several suppressors bind dsRNA but differ in size specificity | proposal of generality is panel-bounded |
| `src-doi-10-1371-journal-pone-0014639` | Baulcombe/Carr | Arabidopsis AGO mutant panel and AGO-bound vsiRNAs | AGO2 restricts TCV/CMV as a conditional second layer | same broad Baulcombe network; TMV boundary |
| `JCC-B-S012` | Vaucheret/Bartel | dcl single/double mutants | DCL4 primary for tasiRNA; DCL2/3 partial compensation | endogenous pathway; abstract-bounded |
| `src-doi-10-1101-gad-1352605` | Poethig | tasiRNA pathway genetics | independent RDR6/SGS3/DCL4-associated pathway resolution | endogenous/developmental, not antiviral by itself |
| `src-doi-10-1128-jvi-79-24-15209-15217-2005` | Qu/Morris | NbRDR6 knockdown × virus × temperature | antiviral RDR6 contribution is host-, tissue- and temperature-conditioned | knockdown and tested-panel limits |
| `src-doi-10-1073-pnas-0505461102` | Baulcombe | AGO1 IP and Slicer assays | AGO1 cargo/slicing specificity; tested vsiRNAs not recovered | one network; assay/time/virus limits |

## 2. Supported claims

### 2.1 Viral suppression is real, but suppressors are mechanistically plural

Standing external PTGS studies support the general counterdefense concept, and p19 structure gives a direct molecular example of siRNA-duplex sequestration. The multi-suppressor binding study extends dsRNA binding to several unrelated proteins but explicitly separates size-selective and size-independent behavior.

Evidence cards: `claim-carrington-c-007`, `claim-carrington-c-010`, `claim-carrington-c-011`.

Highest safe statement: tested viral proteins can suppress RNA silencing, and some do so by binding small or long dsRNA. Unsafe statement: every viral suppressor acts by the same RNA-binding mechanism.

### 2.2 AGO function is specialized and conditional

Baumberger and Baulcombe directly resolved AGO1 cargo and Slicer activity in Arabidopsis. Harvey et al. later showed a strong AGO2 susceptibility phenotype for TCV and CMV, AGO2 induction and associated viral siRNAs, while reporting no comparable AGO2 susceptibility effect for TMV. Together these findings support component-specific loading and layered antiviral defense, not a single AGO that universally handles all viral siRNAs.

Evidence cards: `claim-carrington-c-012`, `claim-carrington-c-016`.

### 2.3 DCL and RDR pathways combine primary roles with backup or context dependence

Independent dcl genetics supports DCL4 as the primary endogenous tasiRNA processor and partial compensation by DCL2/DCL3 in particular mutant backgrounds. The Poethig laboratory independently resolved RDR6/SGS3/DCL4-associated tasiRNA biogenesis. In antiviral work, NbRDR6 knockdown increased susceptibility across the tested panel, with stronger effects at higher growth temperatures and a shoot-apex phenotype.

Evidence cards: `claim-carrington-c-013`, `claim-carrington-c-014`, `claim-carrington-c-015`.

These sources validate component decomposition while preventing universal transfer from endogenous tasiRNAs to viral siRNAs or from Nicotiana to every plant/virus system.

## 3. Retraction and publication-status audit

### Brigneti 1998

`src-doi-10-1093-emboj-17-22-6739` is marked retracted in PMC/PubMed. The authoritative notice is `src-doi-10-15252-embj-201570030` (PMID `26286615`, PMCID `PMC4609191`). It must never support HC-Pro, 2b, PTGS suppression or antiviral-defense claims.

Card: `claim-carrington-c-008`.

The broader suppressor/counterdefense model retains standing support from other sources, but that conclusion is an evidence-network inference and not a rehabilitation of the retracted article (`claim-carrington-c-009`).

### Other selected sources

No retraction or expression of concern was identified in the checked PubMed/PMC/publisher metadata for the other selected scientific sources as of the 2026-07-18 retrieval/status-verification date. This date does not expand the 2026-07-17 scientific evidence cutoff. The check is dated, not a permanent guarantee. The Baulcombe/Voinnet network is not multiplied into independent replications merely because several papers remain standing.

## 4. Contested claims and context-dependent differences

### Conflict A — Is dsRNA binding a general suppressor strategy?

- Support: the Merai panel found dsRNA binding in several unrelated suppressors.
- Boundary: p19 is strongly resolved as a 21-nt duplex caliper, whereas other proteins bind long and/or short dsRNA differently.
- Conflict type: generality and mechanistic identity, not whether the tested proteins have suppression activity.
- Resolution: matched mutants that selectively disrupt RNA binding, tested during native infection with viral accumulation, small-RNA loading and disease phenotypes.

### Conflict B — AGO1 versus AGO2 in antiviral defense

- AGO1 directly loads selected endogenous small RNAs and is catalytically active; viral siRNAs from the tested infections were not recovered in that 2005 AGO1 assay.
- AGO2 has a direct susceptibility phenotype and vsiRNA association for TCV/CMV in 2011, but not a universal effect across the tested viruses.
- Conflict type: virus, suppressor, tissue, time and AGO-layer differences, not a simple contradiction.
- Resolution: matched AGO IP/CLIP, catalytic mutants and infection time courses for each virus/suppressor/context.

### Conflict C — Primary DCL assignments versus redundancy

- DCL4 is primary for tasiRNA production in the tested Arabidopsis context.
- DCL2 and DCL3 can produce substitute products in particular double-mutant backgrounds.
- Conflict type: primary wild-type role versus compensatory mutant routing.
- Resolution: product size/register, AGO loading and phenotype measured in matched single and combinatorial genotypes.

### Conflict D — Is RDR6 broadly antiviral?

- The Nicotiana study supports a broad effect across its tested viruses.
- The effect is explicitly temperature-dependent and uses downregulation rather than a clean locus-null series.
- Conflict type: scope and penetrance, not a direct reversal.
- Resolution: independent alleles/complementation across matched temperatures, tissues, virus strains and suppressor states.

## 5. Methodological critiques and audit rules

1. A GFP/PTGS reversal assay demonstrates reporter suppression; it does not alone establish the native viral target, infection-stage requirement or symptom causality.
2. Viral-protein RNA binding establishes biochemical capacity; native-infection necessity requires separation-of-function mutants and rescue.
3. A susceptibility phenotype in a dcl/ago/rdr mutant needs matched background, viral accumulation, component loading/action and pleiotropy controls.
4. Small-RNA abundance is not equivalent to AGO loading or antiviral activity.
5. “Broad-spectrum” means the tested virus panel under the tested temperatures and host, not universal plant-virus immunity.
6. DCL compensation in mutant combinations is not evidence that DCL proteins are interchangeable in wild type.
7. Endogenous tasiRNA pathway genetics cannot automatically validate an antiviral-siRNA mechanism.
8. A database or PubMed record confirms metadata, not an experiment; retraction/correction status must be checked before scientific use.

## 6. Unresolved conflicts

| Question | Current status | Decisive next evidence |
|---|---|---|
| How often is suppressor activity explained primarily by direct dsRNA/sRNA binding? | supported for a tested subset; not universal | native-virus separation-of-function mutants across suppressor families |
| Which AGO is dominant for a given plant-virus pair? | virus/suppressor/tissue dependent | matched AGO loading, catalytic genetics and time-resolved viral fitness |
| When does DCL backup preserve antiviral function versus only change siRNA size? | context dependent | combinatorial mutants with loading, viral spread and rescue |
| How portable is Nicotiana RDR6 temperature dependence? | unresolved across species | factorial host × temperature × virus × RDR6 allele designs |
| Does a reporter-defined suppressor mechanism explain disease symptoms? | frequently incomplete | native infection, symptom genetics and molecular rescue |

## 7. Cross-source synthesis boundary

`claim-carrington-c-017` summarizes the external literature as a modular, conditional pathway architecture. It is explicitly `agent_inference`: DCL, AGO and RDR results come from different species, substrates, tissues and endpoints and cannot be fused into one causal chain. The synthesis is suitable as an article-question generator, not as a claim that Carrington personally stated a universal rule.

## 8. Dimension decision

```yaml
dimension: 04-independent-validation
status: complete
selected_scientific_sources: 10
positive_external_networks: 5
retracted_sources_used_as_positive_evidence: 0
authoritative_retraction_records: 1
unresolved_conflict_groups: 5
database_record_as_validation: false
```

The independent dimension is sufficiently populated for N1.5. The most important release guard is the explicit rejection of the retracted 1998 Brigneti paper and the preservation of virus/host/tissue/temperature/network boundaries.
