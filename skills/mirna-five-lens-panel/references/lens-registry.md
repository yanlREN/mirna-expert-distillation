# Five-Lens Runtime Registry

Use this fixed registry for the WorkBuddy GitHub public-candidate panel.

| Order | Lens ID | Runtime status | Primary responsibility |
|---:|---|---|---|
| 1 | `michael-axtell-plant-mirna-lens` | `validated` | Plant miRNA identity, annotation, processing precision, locus/family logic |
| 2 | `xuemei-chen-plant-mirna-lens` | `validated` | Plant miRNA biogenesis, lifecycle, loading, movement, turnover and development |
| 3 | `blake-meyers-plant-small-rna-lens` | `validated` | Small-RNA omics, PARE/degradome, PHAS/phasiRNA and experimental design |
| 4 | `james-carrington-rna-silencing-lens` | `validated` | RNA-silencing pathways, DCL/RDR/AGO, tasiRNA and antiviral mechanisms |
| 5 | `hailing-jin-cross-kingdom-rna-lens` | `supervised_preview` | Cross-kingdom RNA, extracellular carriers, recipient action and deployment maturity |

The Jin source package retains `status: needs_review`. The panel's
`supervised_preview` status permits prerelease, supervised use with additional
runtime guardrails; it is not a release-gate override and must remain visible
in redistributed copies and outputs.

Do not activate:

- `david-bartel-mirna-mechanism-lens` — excluded from this preview because its
  release-hard failures remain scientifically material.
- `mirna-evidence-auditor` — excluded as an executable Skill because its
  aggregate veto behavior did not pass the release gate. Apply the panel's
  explicit scientific boundaries instead, without representing them as an
  Auditor result.
- `mirna-expert-router` — not needed for the default five-view panel; the panel
  evaluates applicability itself and never routes by vote.

Evidence cutoff: `2026-07-17`. Verify later or time-sensitive facts against
current primary sources when retrieval is available.
