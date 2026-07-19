# 01 — Core Publications

## Metadata

```yaml
expert_id: xuemei-chen
expert_name: Xuemei Chen
dimension: 01-core-publications
agent_role: Research Agent A
run_id: run-20260717-1730-cst
started_at: 2026-07-17T18:55:00+08:00
completed_at: 2026-07-17T19:25:00+08:00
evidence_cutoff: 2026-07-17
status: complete_with_limitations
```

## Scope

This dimension sampled identity-resolved, representative publications that expose a recurring experimental program across plant-miRNA discovery, DCL1/HEN1 biogenesis, terminal methylation and turnover, miR172/AP2 action, AGO1 loading, subcellular action and movement. It did not attempt a complete bibliography, did not use `Chen X` as a standalone key, and did not infer personal endorsement of every statement in a multi-author article. Search-result snippets were used only to locate records; claims below rest on verified PubMed/PMC metadata, lawful open full text where available, or abstract-bounded statements.

## Source Inventory

| source_id | year | type | expert role | species | access | verification |
|---|---:|---|---|---|---|---|
| `src-doi-10-1016-s0960-9822-02-01017-5` | 2002 | primary | senior | *A. thaliana* | PMC | verified |
| `src-doi-10-1126-science-1088060` | 2004 | primary | sole/first | *A. thaliana* | PMC | verified |
| `src-doi-10-1126-science-1107130` | 2005 | primary | corresponding | *A. thaliana* | PMC | verified |
| `src-doi-10-1016-j-cub-2005-07-029` | 2005 | primary | senior | *A. thaliana* | PMC | verified |
| `src-doi-10-1016-j-febslet-2005-07-071` | 2005 | review | review author | plants | PMC | verified |
| `src-doi-10-1093-nar-gkj474` | 2006 | primary | corresponding | *A. thaliana* | PMC | verified |
| `src-doi-10-1126-science-1163728` | 2008 | primary | corresponding | *A. thaliana* | PMC; erratum | verified with status flag |
| `src-doi-10-1126-science-aav2481` | 2018 | formal erratum | not author | *A. thaliana* | metadata only | verified |
| `src-doi-10-1093-nar-gkq348` | 2010 | primary | senior | *A. thaliana* | PMC | verified |
| `src-doi-10-1016-j-cub-2012-02-052` | 2012 | primary | coauthor | *A. thaliana* | PMC | verified |
| `src-doi-10-1016-j-cell-2013-04-005` | 2013 | primary | senior | *A. thaliana* | PMC | verified |
| `src-doi-10-1105-tpc-113-113159` | 2013 | review | review author | plants | PMC | verified |
| `src-doi-10-1038-s41467-022-28872-x` | 2022 | primary | corresponding | *A. thaliana* | PMC | verified |
| `src-doi-10-1016-j-devcel-2022-03-015` | 2022 | primary | senior | *A. thaliana* | PMC | verified |

## Findings

### Finding F1 — Genetics opens the pathway, but pathway stages must be separated

**Finding**  
The 2002 DCL1/CARPEL FACTORY–HEN1 work links developmental genetics to miRNA accumulation, while the later author review organizes plant-miRNA biology into transcription/processing, terminal modification and effector action. The recurrent value is not “a mutant has low miRNA,” but using the mutant as an entry point and then assigning the defect to a particular stage.

**Why it matters**  
When interrogating a new paper, a phenotype plus changed mature-miRNA abundance is underdetermined. Pri-miRNA, processing intermediates, duplex products, terminal chemistry, AGO loading and target output need separate measurements.

**Evidence**
- Source: `src-doi-10-1016-s0960-9822-02-01017-5`; senior-author team result; *A. thaliana* mutants; genetics/RNA analysis; direct; independent support not assessed in this dimension.
- Source: `src-doi-10-1016-j-febslet-2005-07-071`; sole-author review; plants with Arabidopsis emphasis; review synthesis; contextual.
- Claims: `claim-chen-a-dcl1-hen1-genetic-entry`, `claim-chen-a-stage-separated-diagnosis`.

**Attribution**  
The experimental result belongs to the team; the staged diagnostic is an agent inference from recurring publications, explicitly not a verbatim personal rule.

**Limitations**
- The 2002 terminology predates current annotation standards.
- Mutant pleiotropy can confound causal localization.

**Confidence**  
high for the component facts; medium-high for the synthesized diagnostic.

### Finding F2 — miR172/AP2 establishes a target-specific translation case

**Finding**  
The sole-author miR172/AP2 study used target-site perturbation and discordant AP2 protein/RNA behavior to support primarily translational repression in Arabidopsis flower development.

**Why it matters**  
It is a model for asking whether a target effect is cleavage, transcript destabilization or translation repression. Complementarity or expression anticorrelation alone cannot answer that question.

**Evidence**
- Source: `src-doi-10-1126-science-1088060`; sole author; *A. thaliana* flowers; genetics, transgenics, RNA/protein analyses; direct.
- Claim: `claim-chen-a-mir172-ap2-translational-repression`.

**Attribution**  
Explicit sole-author result.

**Limitations**
- The result is target-, tissue- and developmental-context specific.
- It should not be converted into a universal rule that plant miRNAs repress translation rather than cleave targets.

**Confidence**  
high.

### Finding F3 — HEN1 claims are built as a genetic–chemical–biochemical chain

**Finding**  
The HEN1 series first established terminal methylation in vivo and in vitro, then localized the modification to the terminal ribose and resolved duplex length/overhang preferences. A separate study connected loss of methylation to 3'-end uridylation.

**Why it matters**  
The sequence of evidence distinguishes enzyme requirement, chemical identity, substrate preference and protective consequence. No single assay carries the whole mechanism.

**Evidence**
- `src-doi-10-1126-science-1107130`: genetics, affinity purification, mass spectrometry and enzyme assay; corresponding-author team result; direct.
- `src-doi-10-1093-nar-gkj474`: purified-enzyme substrate panel and HPLC; corresponding-author team result; direct.
- `src-doi-10-1016-j-cub-2005-07-029`: hen1 small-RNA end analysis; final-author team result; direct.
- Claims: `claim-chen-a-hen1-terminal-methylation`, `claim-chen-a-hen1-duplex-specificity`, `claim-chen-a-methylation-protects-ends`.

**Attribution**  
Team results. The general lesson to triangulate genetic, chemical and biochemical evidence is an agent synthesis.

**Limitations**
- The measured enzyme behavior is Arabidopsis-specific unless homolog-specific evidence is supplied.
- Methylation does not establish target identity or phenotype causality.

**Confidence**  
high.

### Finding F4 — Small-RNA abundance is controlled by substrate competition and turnover

**Finding**  
The research program extends beyond production: 24-nt siRNA pathways can compete with miRNAs for HEN1 in a hypomorphic genetic context; SDN nucleases degrade mature miRNAs; and HESO1 uridylates unmethylated small RNAs in hen1 backgrounds.

**Why it matters**  
A changed mature-miRNA level can arise from processing, methylation capacity, tailing or nuclease turnover. The genotype and methylation state determine which explanation is plausible.

**Evidence**
- `src-doi-10-1093-nar-gkq348`; suppressor genetics, small-RNA profiling; direct; claim `claim-chen-a-substrate-pool-competition`.
- `src-doi-10-1126-science-1163728`; nuclease biochemistry and gene knockdown; direct; claim `claim-chen-a-sdn-turnover`.
- `src-doi-10-1016-j-cub-2012-02-052`; suppressor genetics and terminal-transferase biochemistry; direct; claim `claim-chen-a-heso1-unmethylated-substrates`.

**Attribution**  
Team results; Chen is corresponding/senior in the first two and a middle coauthor in the HESO1 paper.

**Limitations**
- HEN1 competition is not a universal mass-action law; it was exposed in particular allele/pathway combinations.
- HESO1 evidence is centered on unmethylated substrates in hen1 backgrounds.
- The 2008 SDN paper has a 2018 formal erratum (`src-doi-10-1126-science-aav2481`); quantitative or figure-level reuse must consult it.

**Confidence**  
high for bounded claims.

### Finding F5 — Target action is mode- and location-specific

**Finding**  
In the tested Arabidopsis system, AMP1 and ER-associated polysomes are required for translational repression but not the cleavage arm of miRNA action.

**Why it matters**  
“The miRNA regulates the target” is too compressed. An adequate interrogation separates AGO loading, cleavage, transcript abundance, polysome association and protein output, and records subcellular context.

**Evidence**
- Source: `src-doi-10-1016-j-cell-2013-04-005`; final-author team result; *A. thaliana*; amp1 genetics, membrane fractionation, polysome profiling and AGO1 association; direct.
- Claim: `claim-chen-a-er-translation-cleavage-separation`.

**Attribution**  
Team result; the interrogation checklist is an agent inference.

**Limitations**
- The ER result cannot be assumed for every target or plant species.
- Cleavage evidence and phenotype causality remain separate axes.

**Confidence**  
high.

### Finding F6 — Biogenesis and AGO loading can be coupled but remain distinguishable

**Finding**  
RBV affects pri-miRNA-related processing/splicing and AGO1 loading. This is evidence that one factor can influence more than one checkpoint, not a reason to collapse those checkpoints.

**Why it matters**  
Papers reporting a factor as a “miRNA biogenesis factor” should be asked which molecular intermediate changes and whether loading was directly tested.

**Evidence**
- Source: `src-doi-10-1038-s41467-022-28872-x`; shared corresponding-author team result; *A. thaliana*; genetics, sequencing, splicing, interaction and loading assays; direct.
- Claim: `claim-chen-a-rbv-coupled-checkpoints`.

**Attribution**  
Multi-institution team result.

**Limitations**
- RBV is not evidence that every processing factor controls loading.
- Bulk mature-miRNA sequencing alone would not resolve the multiple checkpoints.

**Confidence**  
high.

### Finding F7 — Mobility requires loading-state and compartment evidence

**Finding**  
The 2022 mobile-miRNA study proposes that microtubules promote non-cell-autonomous action by restricting cytoplasmic AGO1 loading, distinguishing cytoplasmic loading of mobile miRNAs from nuclear loading associated with cell-autonomous miRNAs.

**Why it matters**  
Detection of reads in a recipient cell does not establish transport mechanism, AGO engagement, target regulation or phenotype. Movement claims need cell-type, compartment and loading assays.

**Evidence**
- Source: `src-doi-10-1016-j-devcel-2022-03-015`; final-author team result; Arabidopsis roots/cell types; genetics, AGO1-IP, RNA blot and microtubule perturbation; direct.
- Claim: `claim-chen-a-mobility-loading-context`.

**Attribution**  
Team result.

**Limitations**
- The result is not a general proof for all short- or long-distance plant miRNA transport.
- Cell autonomy, mobility, AGO loading and phenotype are separate claims.

**Confidence**  
high within the tested system.

## Candidate Reasoning Models

| candidate_id | model idea | contexts | distinctive? | source_ids | disposition |
|---|---|---|---|---|---|
| `CHEN-A-M1` | Stage-separated miRNA diagnosis: transcription → processing → methylation/stability → AGO loading → action → turnover | altered abundance or phenotype | high | 2002, 2005 review, 2013 review, RBV 2022 | advance to synthesis |
| `CHEN-A-M2` | Genetic–chemical–biochemical triangulation for terminal modification | HEN1/end chemistry | high | Science 2005, Curr Biol 2005, NAR 2006 | advance to synthesis |
| `CHEN-A-M3` | Substrate-state and genotype gate for turnover claims | hen1/HESO1/SDN | high | SDN 2008, NAR 2010, HESO1 2012 | advance with erratum flag |
| `CHEN-A-M4` | Split target action by cleavage versus translation and by subcellular site | target validation | medium-high | miR172 2004, Cell 2013 | advance to synthesis |
| `CHEN-A-M5` | Movement requires compartment-specific AGO-loading evidence | mobile miRNAs | high | Dev Cell 2022 | advance with narrow scope |
| `CHEN-A-M6` | A factor may couple checkpoints; assay each checkpoint independently | RBV or pleiotropic regulators | medium | Nat Commun 2022 | merge into M1 |

## Candidate Heuristics

- IF mature miRNA abundance changes, THEN measure pri-miRNA/processing intermediates, terminal state, AGO loading and decay before naming the defect, BECAUSE several checkpoints can generate the same endpoint, UNLESS direct upstream evidence already excludes alternatives.
- IF HEN1 mechanism is claimed, THEN distinguish enzyme requirement, substrate architecture, chemical position and protective consequence, BECAUSE these are different evidentiary claims, UNLESS the paper is explicitly limited to one axis.
- IF target regulation is claimed, THEN separate cleavage, transcript reduction and translation repression, BECAUSE plant miRNAs can act by multiple modes, UNLESS direct assays show only one bounded mode.
- IF mobility is claimed, THEN require donor/recipient context plus loading or target-engagement evidence, BECAUSE recipient reads alone are not transport or functional proof, UNLESS the claim is only detection.
- IF turnover is studied in `hen1`, THEN state the unmethylated-substrate context, BECAUSE HESO1/uridylation behavior there cannot automatically describe wild type, UNLESS wild-type evidence is independently supplied.

## Contradictions and Tensions

| conflict | source A | source B | context difference | unresolved? |
|---|---|---|---|---|
| Early simplified plant-miRNA pathway versus later multi-compartment model | 2005 FEBS review | 2013 Cell; 2022 Dev Cell | historical evidence growth | no; treat as timeline expansion |
| Translational repression versus cleavage | miR172 2004; Cell 2013 | general plant target-cleavage literature not sampled here | target and assay specific | yes at target level; do not choose universally |
| Methylation protects from turnover versus SDN activity on mature miRNAs | 2005 Curr Biol | 2008 Science | substrate chemistry and nuclease sensitivity | no; methylation is protective, not absolute immortality |
| 2008 SDN report versus 2018 erratum | original report | formal erratum | correction details unavailable in this pass | partially; figure-level reuse deferred |

## Missing Evidence

- This dimension intentionally does not provide independent-laboratory replication; Agent C owns that role.
- Exact content of the 2018 Science erratum was not exposed by the accessible PubMed metadata; only existence/linkage is asserted.
- Several papers are multi-author team products. Author order/correspondence was recorded, but no claim is treated as Xuemei Chen's sole personal endorsement.
- Arabidopsis dominates the corpus; transfer to crops or non-plant taxa requires new evidence.

## Quality Self-check

- [x] Every key finding has a source ID
- [x] Author identity and role verified
- [x] Species and context recorded
- [x] Search snippets not used as experimental evidence
- [x] No unauthorized full text
- [x] No fabricated identifiers
- [x] Expert position separated from field consensus
- [x] Agent inference labeled
- [x] Conflicts preserved
