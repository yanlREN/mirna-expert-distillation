# Query Plan — Hailing Jin

```yaml
expert_id: hailing-jin
skill_id: hailing-jin-cross-kingdom-rna-lens
phase: N1
target_unique_sources: 25-40
hard_max_unique_sources: 45
independent_validation_or_critique_minimum: 6
evidence_cutoff: 2026-07-17
identity_metadata_retrieval_date: 2026-07-18
identity_anchor_required: true
minimum_matching_identity_anchors: 2
jin_h_standalone_key: forbidden
h_jin_standalone_key: forbidden
hailing_jin_standalone_key: insufficient
raw_sequencing_data: forbidden
local_model: forbidden
unauthorized_fulltext: forbidden
```

## Identity inclusion gate

The project-wide mechanism-evidence cutoff is `2026-07-17`. Identity and current-affiliation pages retrieved on `2026-07-18` are used only for author disambiguation and must not introduce post-cutoff scientific claims.

Every expert-attributed source must match at least two date-appropriate anchors: canonical full name; verified ORCID `0000-0001-5778-5193`; UCR/John Innes/UC Berkeley affiliation or email; plant small-RNA, plant-immunity, or plant-pathogen topic; recurring verified coauthors; and authoritative PubMed/publisher metadata. Record author position and corresponding/contribution role separately.

`Jin H`, `H Jin`, and the exact full name by themselves are not inclusion keys. A distinct Hailing Jin works in a Vanderbilt biomedical/oncology network. Exclude those records and all non-plant namesakes unless two independent anchors resolve them to the locked UCR expert.

## Discovery queries

Use combinations, then inspect authoritative metadata rather than accepting search snippets:

- `"Hailing Jin" UCR small RNA plant pathogen`
- `"Hailing Jin" hailingj@ucr.edu`
- `"Hailing Jin" 0000-0001-5778-5193`
- PubMed full-name search constrained by UCR/plant/pathogen terms and date
- DOI/title lookups for verified recurring coauthors: Qiang Cai, Baoye He, Lulu Qiao, Arne Weiberg, Ming Wang, Huan Wang, Rachael Hamby, and Chien-Yu Huang
- Historical searches constrained to John Innes Centre/Cathie Martin or UC Berkeley Plant Gene Expression Center/Barbara Baker
- Independent-replication and methodological-critique searches that exclude Jin-lab and close collaborator networks
- Per-source correction/retraction/expression-of-concern searches in PubMed, Crossref/publisher records, and official notices

## Six-dimension routing priorities

1. Core publications: early plant-immunity/small-RNA work; cross-kingdom RNA claims; extracellular-vesicle/RNA-trafficking studies; recent disease-control work. Record team roles and publication status.
2. Talks and public academic responses: prefer official seminar recordings/pages, author-written reviews/perspectives, and transcript-bearing sources; use biography text for scope only.
3. Scientific reasoning DNA: extract only patterns reproduced across at least two independently verified research contexts.
4. Independent validation and critique: collect at least six sources outside the Jin laboratory, explicitly including negative, conflicting, contamination/mapping, extracellular-vesicle, uptake, and causal-transport critiques where available.
5. Experimental decisions: trace donor-release-transport-uptake-effector-target-phenotype claims while keeping contamination, mixed tissue, species assignment, and mapping ambiguity explicit.
6. Timeline: separate the 1996-2004 training/transition period, UCR faculty continuity from 2004, emergence of cross-kingdom RNA claims, extracellular-vesicle work, and current application-oriented scope.

## Source hierarchy

Prioritize original research, methods papers, official database/method documentation, PubMed/PMC metadata, publisher version-of-record pages, official correction/retraction notices, and independent primary studies. Official UCR/NAS pages support identity and timeline only. Author-written reviews and perspectives can support public framing but cannot replace original experimental evidence. Talks lacking transcripts support public scope only.

## High-risk safeguards

- Do not infer interspecies transfer from mapped reads alone.
- Do not equate extracellular-vesicle enrichment with vesicle-mediated delivery.
- Keep donor origin, release, transport, recipient uptake, effector loading, target action, and phenotype causality as separate claims.
- Require species-unique sequence/mapping logic and contamination/mixed-tissue controls where relevant.
- Keep predicted targeting, molecular target directness, and disease-phenotype causality separate.
- Do not label every cross-species small RNA a miRNA; preserve miRNA/siRNA and locus/precursor/mature/arm/sequence distinctions.
- Do not treat same-laboratory repetition or close collaborators as independent validation.
- Do not download raw sequencing data, unauthorized full text, PDFs for redistribution, or any model weights.
- Record unresolved conflicts rather than forcing consensus.

## N1 stop/escalation rule

A single inaccessible page or paper is not fatal; replace it or downgrade the claim. Stop for identity only if the exact author cannot be resolved after the two-anchor rule and date-appropriate affiliation/coauthor checks. The N0.5 audit found no such fatal issue, so N1 may proceed.
