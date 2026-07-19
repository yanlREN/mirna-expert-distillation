# Version - Xuemei Chen Plant miRNA Lens

```yaml
skill_id: xuemei-chen-plant-mirna-lens
version: 0.1.2
status: validated
created_at: 2026-07-17T21:18:00+08:00
updated_at: 2026-07-18T01:51:00+08:00
evidence_cutoff: 2026-07-17
nuwa_commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
source_count: 35
evidence_card_count: 38
fidelity_score: 96
build_phase: N5
validation_status: N5_full_regression_passed
known_limitations:
  - The corpus is dominated by Arabidopsis thaliana; transfer requires entity-, system-, AGO-, and assay-level revalidation.
  - CHEN-M1, CHEN-M2, and parts of CHEN-M3 are Agent operationalizations, not named frameworks authored by Xuemei Chen or independently tested complete protocols.
  - Mobility evidence includes one shared collaboration cluster, and the microtubule-loading mechanism is restricted to the tested Arabidopsis root miR165/166 context.
  - Public event records lack transcripts and support scope only, not mechanistic detail or personal voice.
  - The SDN erratum's figure-level and quantitative impact remain unclosed; AAR2 affected-panel reuse must follow the verified correction boundary and corrected online version.
  - Abstract-bounded records cannot support unobserved assay details.
  - Multi-author findings are team results and cannot be phrased as current personal endorsement.
```

## N5 pre-regression changes

- N4 passed at 93/100 with zero hard failures; citation and benchmark support-edge rechecks passed.
- Added subclaim-local stop/auditor fields, transfer and correction state, unique-source/independent-group accounting, and deterministic team attribution.
- Split catalytic capacity, in-vivo access, endogenous substrate effect, and turnover flux/rate; added random-degradation alternatives and correction-sensitive paper provenance questions.
- N5 full regression passed: 31 tests, 28 PASS, 3 PARTIAL, 0 FAIL; original tests degraded 0 and improved 5; hard failures 0.
- Promoted locally to `validated`; this does not mark the project as a Release Candidate or authorize public release.
