# Blake C. Meyers N1 — Core Publications

Agent A read-only research draft. Retrieval date: 2026-07-18 (Asia/Shanghai). Evidence cutoff: 2026-07-17. All coauthored findings below are team results unless an author-written review is explicitly identified. This file does not attribute every sentence of a paper to Blake C. Meyers and does not infer private views.

## 1. Source overview

The 14-paper core set spans four connected stages of the public program:

1. **Measurement and atlas construction (2004–2007):** MPSS signature classification in Arabidopsis, deep small-RNA sequencing, mutant-guided class separation, and a rice mRNA/small-RNA atlas (`src-doi-10-1101-gr-2275604`, `src-doi-10-1126-science-1114112`, `src-doi-10-1101-gr-5530106`, `src-doi-10-1038-nbt1291`).
2. **Cleavage and secondary-siRNA inference (2008–2014):** PARE, miRNA-triggered NB-LRR phasing, explicit phasiRNA terminology, and a soybean atlas integrating small-RNA, PARE, tissue, and annotation axes (`src-doi-10-1038-nbt1417`, `src-doi-10-1101-gad-177527-111`, `src-doi-10-1105-tpc-113-114652`, `src-doi-10-1105-tpc-114-131847`).
3. **Reproductive phasiRNA staging and causal genetics (2015–2020):** staged maize anthers, the rice PMS1T locus, angiosperm-scale comparison, and maize DCL5 genetics (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1038-s41467-020-16634-6`).
4. **Spatial and mechanistic subdivision (2022–2024):** tapetum-to-meiocyte movement and a premeiotic 24-nt class with calibrated negative evidence for triggering, AGO loading, and cleavage (`src-doi-10-1111-nph-18167`, `src-doi-10-1073-pnas-2402285121`).

Of the 14 papers, 12 are original research and two are method/review framing sources. Eleven have verified open full text through PMC or the publisher; three were restricted to abstract-supported claims. No raw sequencing data were downloaded.

## 2. Core publication table

| Year | Source ID | Expert role | Species/context | Main evidentiary contribution | Boundary retained |
|---|---|---|---|---|---|
| 2004 | `src-doi-10-1101-gr-2275604` | first author | Arabidopsis MPSS libraries | Signature mapping, strand/feature classification, public browser | Platform signatures are measurements, not identities |
| 2005 | `src-doi-10-1126-science-1114112` | co-corresponding | Arabidopsis seedlings/inflorescences | Deep small-RNA transcriptome complexity | Abstract-only; historical candidates require modern re-evaluation |
| 2006 | `src-doi-10-1101-gr-5530106` | final/senior | Arabidopsis `rdr2`, `rdr6`, `dcl` mutants | Genetic and blot triangulation of small-RNA classes | Mutant enrichment can be indirect or unexplained |
| 2007 | `src-doi-10-1038-nbt1291` | final/senior | Nipponbare rice multi-library atlas | Cross-library mRNA/sRNA context and genomic clustering | Atlas association is not molecular function |
| 2008 | `src-doi-10-1038-nbt1417` | coauthor | Arabidopsis inflorescence, `xrn4` | PARE captures cleavage-product 5′ ends | Cleavage ≠ unique target ≠ phenotype causality |
| 2011 | `src-doi-10-1101-gad-177527-111` | final/senior | Medicago and potato NB-LRR networks | 22-nt miRNA triggers and phased secondary siRNAs | “Master regulator” is network/context bounded |
| 2013 | `src-doi-10-1105-tpc-113-114652` | review author | comparative plant phasiRNAs | Broader phasiRNA concept and explicit open questions | Review does not replace original evidence |
| 2014 | `src-doi-10-1105-tpc-114-131847` | corresponding | soybean tissues and PHAS loci | Integrated sRNA/PARE/phasing/tissue/annotation atlas | Predicted phasiRNA targets remain predictions |
| 2015 | `src-doi-10-1073-pnas-1418918112` | corresponding | staged maize anthers and mutants | 21-nt premeiotic vs 24-nt meiotic dynamics | Stage, cell layer, genotype are inseparable from claim |
| 2016 | `src-doi-10-1073-pnas-1619159114` | coauthor | rice young panicles, photoperiod | PMS1T mapping, perturbation, cleavage and phasiRNA chain | Downstream fertility targets remained unknown |
| 2019 | `src-doi-10-1038-s41467-019-08543-0` | co-corresponding | broad angiosperm comparison | Wide evolutionary distribution of 24-nt reproductive phasiRNAs | Broad does not mean universal; detection/assembly limits matter |
| 2020 | `src-doi-10-1038-s41467-020-16634-6` | co-corresponding | maize `dcl5`, temperature regimes | Genetic depletion, tapetal defects and conditional male sterility | One Dicer perturbation does not identify one causal phasiRNA |
| 2022 | `src-doi-10-1111-nph-18167` | coauthor | maize tapetum/meiocytes | LCM plus RNA/sRNA FISH supports mobility | Movement evidence does not establish function after arrival |
| 2024 | `src-doi-10-1073-pnas-2402285121` | co-corresponding/final | five maize lines, three teosinte taxa, rice reanalysis | Premeiotic 24-nt class and trigger/loading/cleavage tests | Negative evidence is assay- and dataset-bounded |

## 3. Recurring scientific claims

### 3.1 Measurement classes must remain biologically distinct

The early work repeatedly separates genomic placement, abundance, size class, strand, locus class, mutant dependence, and validation rather than treating all small reads as equivalent (`src-doi-10-1101-gr-2275604`, `src-doi-10-1126-science-1114112`, `src-doi-10-1101-gr-5530106`, `src-doi-10-1038-nbt1291`). This is the foundation for a candidate reasoning model: **classify the observation before assigning a small-RNA identity or function**. It recurs in Arabidopsis and rice, but the specific MPSS filters are historical and should not be copied as current miRNA criteria.

### 3.2 Cleavage is one evidence axis, not the endpoint

PARE was built to observe cleavage-product 5′ ends, moving beyond target prediction (`src-doi-10-1038-nbt1417`). Later work integrates PARE with phasing, miRNA-trigger predictions, locus genetics, transgenes, photoperiod, and fertility (`src-doi-10-1105-tpc-114-131847`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1073-pnas-2402285121`). The stable distinction is:

```text
predicted complementarity
≠ cleavage signal
≠ phased-product biogenesis
≠ target uniqueness
≠ organismal phenotype causality
```

### 3.3 Phasing requires trigger/register/precursor context

The NB-LRR, soybean and reproductive studies examine a candidate PHAS locus through precursor identity, trigger evidence, phase register, product size, tissue/stage, and sometimes genetic dependence (`src-doi-10-1101-gad-177527-111`, `src-doi-10-1105-tpc-114-131847`, `src-doi-10-1073-pnas-1418918112`). A cluster of reads or a predicted trigger is insufficient alone. The 2024 Zea study is especially informative because it does not force premeiotic 24-nt loci into the canonical miR2275-trigger model when trigger, AGO18-loading and cleavage evidence are largely absent (`src-doi-10-1073-pnas-2402285121`).

### 3.4 Stage and cell type are causal interpretation variables

The maize program uses sequential anther lengths, mutant cell-layer defects, laser-capture microdissection and spatial FISH to distinguish where precursors arise, where products accumulate, and when different size classes peak (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1038-s41467-020-16634-6`, `src-doi-10-1111-nph-18167`). Stage is not decorative metadata: an apparent absence or mechanistic contradiction may reflect sampling before or after the relevant burst.

### 3.5 Evolutionary transfer requires explicit presence/absence evidence

The 2013 review and 2019/2024 comparative papers show that Arabidopsis is not a universal template, and that trigger, Dicer, locus count, precursor architecture and product timing vary across lineages (`src-doi-10-1105-tpc-113-114652`, `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1073-pnas-2402285121`). “Broadly present” must preserve verified absences, uncertain absences, assembly quality and stage sampling.

## 4. Recurring methods and controls

| Question | Preferred triangulation seen in corpus | Key controls/boundaries | Sources |
|---|---|---|---|
| Is a read/locus reproducible and interpretable? | abundance + genomic mapping + strand/feature class + library context | multi-mapping, platform restriction sites, low abundance | `src-doi-10-1101-gr-2275604`, `src-doi-10-1038-nbt1291` |
| Is a candidate small RNA tied to a pathway? | wild type vs `rdr`/`dcl` mutants + blot/sequence profile | indirect mutant effects; unexplained enrichment | `src-doi-10-1101-gr-5530106` |
| Is cleavage supported? | PARE/nanoPARE + expected site + abundance/category context | random decay, transcript abundance, assay sensitivity | `src-doi-10-1038-nbt1417`, `src-doi-10-1073-pnas-2402285121` |
| Is a PHAS locus credible? | trigger test + phase statistics/register + precursor annotation + reproducible staged accumulation | predicted triggers are not cleavage; clustering is not phasing | `src-doi-10-1101-gad-177527-111`, `src-doi-10-1105-tpc-114-131847` |
| Is a reproductive pattern localized? | precise staging + mutants + in situ/LCM/FISH | anther length transfer across species; cell non-autonomy | `src-doi-10-1073-pnas-1418918112`, `src-doi-10-1111-nph-18167` |
| Is fertility causality supported? | multiple alleles/transgenes + molecular depletion + anatomy + environmental/genetic controls | pathway-gene perturbation does not identify one effector | `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6` |
| Is a pathway conserved? | genomes + expressed sRNA + precursor/trigger/Dicer inventories + matched stage | assembly and sampling false negatives | `src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1073-pnas-2402285121` |

## 5. Candidate reasoning models (for later N2 testing, not synthesis)

### Candidate A — Measurement-to-mechanism ladder

Start with what the assay directly observes, then promote only through independent axes: mapped reads → locus/precursor → pathway dependence → cleavage/target action → genetic or intervention-based phenotype. This recurs in early atlases, PARE, soybean, PMS1T and DCL5 contexts (`src-doi-10-1101-gr-2275604`, `src-doi-10-1038-nbt1417`, `src-doi-10-1105-tpc-114-131847`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`). Failure condition: the model becomes generic unless N2 retains its small-RNA-specific axes and examples.

### Candidate B — Stage × cell × genotype matrix

Before interpreting reproductive phasiRNA abundance, require matched anther stage, cell layer, genotype and species; use spatial assays and developmental mutants to distinguish production, accumulation and mobility (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1111-nph-18167`). Failure condition: numeric anther-length thresholds are transferred across species.

### Candidate C — Canonical-pathway exception audit

Test a canonical trigger/Dicer/AGO/cleavage model, but treat well-supported missing components or alternate architectures as evidence to subdivide the class, not as noise (`src-doi-10-1038-s41467-019-08543-0`, `src-doi-10-1073-pnas-2402285121`). Failure condition: nondetection is converted into universal absence without sensitivity and stage analysis.

### Candidate D — Comparative presence/absence with ascertainment controls

Transfer a pathway across lineages only after evaluating genome quality, appropriate reproductive stage, precursor and trigger detectability, Dicer complement and reproducible phased products (`src-doi-10-1105-tpc-113-114652`, `src-doi-10-1038-s41467-019-08543-0`). Failure condition: a missing annotation is equated with biological loss.

## 6. Historical changes

- **2004–2007:** emphasis on building measurement and visualization systems for genome-scale transcripts and small RNAs (`src-doi-10-1101-gr-2275604`, `src-doi-10-1038-nbt1291`).
- **2008:** target analysis shifts from computational pairing alone toward direct sequencing of cleavage-product ends (`src-doi-10-1038-nbt1417`).
- **2011–2014:** “tasiRNA” expands to a broader phasiRNA concept involving many coding and noncoding sources across non-Arabidopsis species (`src-doi-10-1101-gad-177527-111`, `src-doi-10-1105-tpc-113-114652`, `src-doi-10-1105-tpc-114-131847`).
- **2015–2020:** reproductive phasiRNA research becomes explicitly spatiotemporal, comparative and genetic, moving from abundance patterns toward male-fertility causality (`src-doi-10-1073-pnas-1418918112`, `src-doi-10-1073-pnas-1619159114`, `src-doi-10-1038-s41467-020-16634-6`).
- **2022–2024:** production site, mobility and mechanistic subclasses are separated; negative evidence is used to refine rather than erase the pathway model (`src-doi-10-1111-nph-18167`, `src-doi-10-1073-pnas-2402285121`).

## 7. Gaps and cautions

1. Most core studies are Meyers-team or close-collaboration results; independent validation belongs to Agent C and must not be inferred here.
2. The authorized full text was unavailable for three papers; claims from them were limited to abstracts (`src-doi-10-1126-science-1114112`, `src-doi-10-1038-nbt1291`, `src-doi-10-1038-nbt1417`, with publisher-open status checked separately).
3. PARE/nanoPARE evidence supports cleavage but is not equivalent to full phenotype causality.
4. A PHAS locus, its precursor, a particular phased product, its trigger miRNA, and its downstream target are separate entities.
5. “21-nt” and “24-nt reproductive phasiRNA” labels do not guarantee identical trigger, Dicer, AGO, timing or function across lineages.
6. The 2024 paper’s negative statements are mostly probabilistic and assay-bounded; they should remain “not detected/likely absent in sampled contexts,” not absolute biochemical impossibilities (`src-doi-10-1073-pnas-2402285121`).
7. PubMed/PMC/publisher records displayed no correction, retraction or expression-of-concern notices for the 14 papers at retrieval. A dedicated Citation Verifier must still recheck every identifier and current publication status.
