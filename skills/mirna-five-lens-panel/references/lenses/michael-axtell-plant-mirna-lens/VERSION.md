# Version — Michael J. Axtell Plant miRNA Lens

```yaml
skill_id: michael-axtell-plant-mirna-lens
version: 0.1.3
status: validated
created_at: 2026-07-17T17:42:00+08:00
updated_at: 2026-07-17T21:16:00+08:00
evidence_cutoff: 2026-07-17
nuwa_commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
source_count: 33
evidence_card_count: 36
fidelity_score: 93
build_phase: N5
validation_status: validated
known_limitations:
  - AXT-M5 is specific to the Cuscuta-host research program; its integrated chain and the 2026 AGO-loading result have limited independent-laboratory support.
  - AXT-H7 may use field_consensus only together with corpus-level independent_support limited; that label cannot upgrade a specific paper's causal grade.
  - AXT-M4 entity hygiene and the complete operational sequence are agent_inference, not an expert quotation.
  - Numerical thresholds and tool rankings remain lineage-, dataset-, version-, parameter-, assembly-, and benchmark-dependent.
  - Three event records have no transcript, slides, or Q&A; they support scope only.
  - Three abstract-only sources do not support unobserved full-text experimental details.
```

## N3 changes

- Replaced the N0.5 placeholder with an executable, non-impersonating Scientific Expert Lens.
- Implemented all 15 required sections, five gated models (`AXT-M1`–`AXT-M5`), eight compact heuristics, miRNA entity/evidence safeguards, and the Paper Interrogation Protocol.
- Required every key runtime claim to report directness, independent support, scope match, knowledge status, source IDs, and claim IDs.
- Added a manifest-only core-source index and preserved every N2.5 limitation.

## N4 repair cycle 1

- Split AXT-H1's evidence ceiling so database/expression/similarity/prediction-only evidence is at most I1, while I2 additionally requires a plausible precursor/hairpin or incomplete processing evidence.
- This wording-only repair responds to the independent Scientific Review; it adds no fact or source and does not lower any evidence threshold.
- Citation verification supplied the already-existing PubMed mapping for the PmiREN core source (`PMID 31602478`); the manifest/core index metadata were completed without changing the supported claim.

## N4 repair cycle 2

- Added a mandatory source-to-card edge check before runtime citation emission.
- When a source is not present in the evidence array of a cited claim card, the runtime must omit that binding and label the subclaim `current corpus insufficient` / `agent_inference` with no independent support.
- This repair addressed the N4 hard citation-edge failure and adds no source or scientific claim. Six regression cases passed: three affected and three unseen; strict-edge hard failures are now zero.

## Verification state

- N2 synthesis: PASS.
- N2.5 independent gate: PASS_WITH_LIMITATIONS; N3 allowed.
- N3 structural/project validation: recorded in `reports/phase-3-build.md`.
- N4 scientific, citation, and benchmark validation: PASS, final score 93/100, hard failures 0, two repair cycles used.
- N5 dual-Agent refinement and full regression: PASS; 31 cases, 0 degraded original cases, 0 release hard failures.
- Status `validated` applies only to this expert Skill; it is not a project Release Candidate.

## N5 controlled refinements

- Clarified deterministic reference loading and consolidated existing stop/downgrade gates.
- Required subclaim-level attribution, deterministic paper-evidence flags, and triggered assembly/mapping questions.
- Added a refusal-only guard that still permits independently valid mixed-request subproblems.
- No fact, source, scope, evidence threshold, gold rubric, or historical PARTIAL record was changed. Full regression passed; the N4 score remains 93/100.
