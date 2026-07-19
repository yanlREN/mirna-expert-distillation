# Query Plan — Inactive Scaffold

Identity anchors: ORCID `0000-0003-3572-129X`, Donald Danforth Plant Science
Center, historical Oregon State/WSU affiliations, plant RNA silencing, virus-host
interactions, and verified coauthor networks. N1 will cover six dimensions with
25-40 unique lawful sources and no raw sequencing data.
# Query Plan — James C. Carrington

```yaml
expert_id: james-c-carrington
skill_id: james-carrington-rna-silencing-lens
phase: N1
distillation_tier: standard
target_unique_sources: 25-40
hard_max_unique_sources: 45
target_evidence_cards: 30-60
evidence_cutoff: 2026-07-17
identity_anchor_required: true
verified_orcid: 0000-0003-3572-129X
carrington_jc_standalone_key: forbidden
current_affiliation: Donald Danforth Plant Science Center
current_title: Member; Past President & CEO
raw_sequencing_data: forbidden
local_model: forbidden
unauthorized_fulltext: forbidden
```

## Identity and inclusion anchors

For every Carrington-authored publication, combine at least two identity anchors: verified ORCID, canonical full name, Oregon State/Washington State/Danforth affiliation, plant RNA-silencing topic, stable coauthor network, or authoritative publication metadata. `Carrington JC`, `J C Carrington`, and `James Carrington` alone are never sufficient inclusion keys. Record author role and team attribution separately. The current Danforth profile governs the date-corrected title; older pages describing him as current President are historical records only.

## Six-dimension routing

- Research Agent A: core publications and scientific claims; research timeline and changes.
- Research Agent B: recurring reasoning patterns; experimental decisions, controls, stops, and failure modes.
- Research Agent C: public academic talks and institutional statements; independent validation, critique, conflict, and limits.

Each agent writes only its isolated cache directory. The main process performs DOI/PMID/URL deduplication, source-ID remapping, support-edge checking, and the authoritative merge.

## Priority research themes

1. Plant antiviral RNA silencing and viral suppressors, including HC-Pro, with host–virus–construct–tissue boundaries preserved.
2. DCL, AGO, RDR and related pathway specialization, redundancy, and genetic interaction, without importing animal Drosha–DGCR8 assumptions.
3. Endogenous plant small-RNA biogenesis and action, with miRNA, tasiRNA, phasiRNA, hc-siRNA and virus-derived siRNA kept distinct.
4. Evidence ladders from small-RNA accumulation and reporter effects through genetics, biochemical interaction, direct target evidence and phenotype causality.
5. Viral perturbation as a mechanistic probe, with pleiotropy, suppressor dosage, developmental effects and infection context treated as alternative explanations.
6. Historical changes from gene-for-gene plant virology to small-RNA pathway dissection, systems genetics, network architecture and crop/virus applications.

## Source hierarchy and search families

Prefer original papers, official database records, PubMed/PMC, Crossref/publisher metadata, author-written reviews, official institutional academic pages and independent laboratory studies. Searches combine the verified identity anchors with topic terms such as `RNA silencing`, `antiviral`, `HC-Pro`, `DCL`, `AGO`, `RDR`, `microRNA`, `tasiRNA`, `virus-derived siRNA`, `Arabidopsis`, `Turnip mosaic virus`, and dated institutional affiliations. Citation networks may discover candidates, but final metadata must be checked against S1–S4 sources.

## Scientific safeguards

- Separate small-RNA identity, direct target evidence and phenotype causality.
- Do not treat predicted hairpins, target predictions, expression anticorrelation, database entries or sequencing abundance as complete causal proof.
- Do not treat degradome/PARE cleavage as sufficient phenotype causality.
- Preserve species, genotype, tissue, developmental stage, virus strain, construct, treatment and assembly scope.
- Count independent support by laboratory/coauthor network and method, not by paper count.
- Use talks without transcripts only for dated topic scope; do not reconstruct a persona or characteristic live voice.
- Represent coauthored results as team findings and new-question answers as Agent inference from public research frameworks.
- Record conflicts and non-replication instead of forcing consensus.
- Never download raw sequencing data, bypass access controls, or store copyrighted PDFs in release artifacts.
