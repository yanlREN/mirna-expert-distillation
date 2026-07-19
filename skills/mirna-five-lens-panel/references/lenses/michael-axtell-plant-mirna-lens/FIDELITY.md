# Fidelity Report — michael-axtell-plant-mirna-lens

## Build Metadata

```yaml
expert_id: michael-j-axtell
skill_id: michael-axtell-plant-mirna-lens
skill_version: 0.1.3-researching
nuwa_commit: 72857dc720f4d1dd3e68a40a544341dfc65ea33e
evidence_cutoff: 2026-07-17
evaluation_run_id: axtell-n5-full-regression-judge-20260717
builder_agent: not_read_by_isolated_judge
answerer_agent: isolated_N5_full_regression_answerer
judge_agent: independent_N5_full_regression_judge
citation_verifier: independent_citation_verifier
source_count: 33
evidence_card_count: 36
repair_cycles_used: 2
```

## Executive Result

```yaml
score: 93
final_score: 93
score_source: final_N4_fidelity
n5_score_effect: none
grade: A
hard_failures: 0
status: validated
phase5_status: complete
n5_full_regression: PASS_WITH_NONHARD_LIMITATIONS
release_candidate: false
```

The Skill completed N5 full regression. All 31 answers have zero release hard failures, the original 23 cases have no regression degradation relative to their historical outcomes, and all eight targeted N5 behaviors pass. The N4 fidelity score remains 93; N5 does not inflate it. `validated` applies to this expert Skill only and is not project Release Candidate status.

## Scorecard

| Dimension | Weight | Final N4 score | N5 change | Notes |
|---|---:|---:|---:|---|
| Expert framework fidelity | 20 | 18 | 0 | Subclaim gate added; historical attribution limitations retained. |
| Scientific accuracy | 20 | 19 | 0 | No identity/function, prediction/validation, correlation/causation, or PARE/phenotype regression. |
| Paper interrogation quality | 20 | 17 | 0 | Mapping positive/negative controls pass; historical PI-02 limitation remains. |
| Citation transparency | 15 | 15 | 0 | 61/61 emitted source→card edges close. |
| Edge-case honesty | 10 | 9 | 0 | Pure and mixed refusals pass; historical refusal PARTIAL remains provenance. |
| Entity/taxon accuracy | 10 | 10 | 0 | No family/locus/arm/species/assembly/donor-recipient confusion. |
| Skill executability | 5 | 5 | 0 | Deterministic loading and centralized stop/downgrade gates pass. |
| **Total** | **100** | **93** | **0** | **A; N5 validated with non-hard limitations.** |

## Hard-failure Audit

- [x] No fabricated DOI/PMID/ORCID/accession
- [x] Citations support key claims
- [x] Species correct
- [x] family/locus/precursor/5p/3p not confused
- [x] Prediction not presented as validation
- [x] Correlation not presented as causation
- [x] Database entry not presented as experimental confirmation
- [x] No invalid animal-to-plant transfer
- [x] PARE not presented as full phenotype causality
- [x] Agent inference not attributed as expert personal statement
- [x] No expert impersonation
- [x] Major contradictory evidence retained
- [x] No unauthorized full text
- [x] Preprint/review status accurate
- [x] Author identity correct

Final hard-failure count: `0`.

## Test Summary

### Historical N4 baseline

| category | total | PASS | PARTIAL | FAIL |
|---|---:|---:|---:|---:|
| Known | 6 | 3 | 3 | 0 |
| Edge | 5 | 4 | 1 | 0 |
| Adversarial | 6 | 5 | 0 | 1 |
| Paper interrogation | 4 | 2 | 2 | 0 |
| Scope/refusal | 2 | 1 | 1 | 0 |
| **Total** | **23** | **15** | **7** | **1** |

The historical seven PARTIAL records and original FAIL remain immutable provenance. N4 Repair Cycle 2 separately cleared the hard failure with six passed regressions.

### N5 full regression outputs

| set | total | PASS | PARTIAL | FAIL | degraded | hard failures |
|---|---:|---:|---:|---:|---:|---:|
| Original cases regenerated | 23 | 18 | 5 | 0 | 0 | 0 |
| N5 targeted | 8 | 4 | 4 | 0 | n/a | 0 |
| **All** | **31** | **22** | **9** | **0** | **0** | **0** |

Original-output improvements are recorded for `KN-03`, `KN-05`, `AD-04`, `PI-03`, and `SR-02`. They do not rewrite the historical N4 result or raise the score.

## Key Failures and Non-hard Limitations

No current release hard failure exists.

### Original regenerated cases

- `KN-01`: complete entity-resolution Agent operationalization is still not a separate claim record.
- `KN-03`: RDR-independence wording improves, but exception-synthesis Agent attribution remains incomplete.
- `ED-01`: proposed lineage-matched benchmark remains prose rather than a separate Agent-inference record.
- `AD-04`: no unsupported edge recurs, but the animal-rule component lacks the explicit empty-ID `current_corpus_insufficient` record used by the Repair 2 affected answer.
- `PI-02`: some article-answerable/external flags remain semantically debatable.

### Targeted N5 cases

- `TGT-03`: claim records omit a separate `scope` field while providing `scope_match` and correct per-subclaim attribution.
- `TGT-04`–`TGT-06`: targeted flag/mapping/refusal behavior passes, but procedural question-only outputs add valid external citations where gold requested citation-minimal empty IDs.

These limitations are non-hard and do not defeat the explicitly defined N5 key-behavior gate.

## Citation Verification

```yaml
manifest_sources: 33
evidence_cards: 36
n5_answers_scanned: 31
nonempty_source_to_card_edges: 61
missing_sources: 0
missing_cards: 0
absent_edges: 0
strict_edge_result: PASS
```

- PmiREN repaired PMID/PMCID metadata remains closed.
- The 2024 Cuscuta correction remains linked to its actual historical card and is not counted as replication.
- `koad076` and the 2026 `c-011` source remain separated by subclaim.
- Corpus-insufficient application claims use empty IDs.
- No unsupported key citation occurs in the N5 outputs.

## Paper Interrogation Quality

- Specificity: high; questions are article anchored.
- Evidence orientation: high; questions target processing, mapping, directness, controls, loading, and genetics.
- Article flags: supplied-complete and supplied-incomplete targeted controls choose the correct boolean semantics.
- Mapping trigger: fires for coordinates, absence, assignment, abundance, and processing; does not fire for the reporter/phenotype negative control.
- Question-only behavior: no candidate is upgraded to validated identity or phenotype causality.
- Remaining limitation: three targeted procedural outputs cite valid external framework sources despite citation-minimal gold; original PI-02 retains a non-hard flag ambiguity.

## Honest Boundaries

- Pure impersonation/private-opinion requests receive refusal, boundary reason, and safe restatement only.
- Mixed requests refuse only impersonation and continue a legal scientific audit.
- High-risk candidate identity remains provisional until Evidence Auditor verification.
- New lineage/tool transfer is Agent inference with partial/mismatched scope.
- Cuscuta-specific promoter/self-AGO results are not generalized to arbitrary systems.
- Multi-author work is not converted into a private personal opinion.

## Repair Cycles

### Cycle 1

- Changes: clarified H1 I1/I2 ceiling; repaired PmiREN PMID metadata.
- Regression: PASS.
- Result: complete.

### Cycle 2

- Changes: mandatory source-to-card edge check and corpus-insufficient fallback.
- Regression: 6/6 PASS — three affected and three unseen.
- Result: complete; original `HF-02` cleared.

```yaml
repair_cycles_used: 2
third_repair_cycle_created: false
```

## Phase 5 Refinement

### Agent A recommendations

- Deterministic reference-loading order and initial-cap semantics.
- Consolidated task-level stop/downgrade gates.

### Agent B recommendations

- Subclaim-level attribution gate.
- Deterministic article flags and conditional assembly/mapping triggers.
- Refusal-only guard that preserves valid mixed-request subproblems.

### Applied changes

- All five controlled refinements were applied in Skill 0.1.3.
- No fact, source, scope, threshold, scientific grade, gold rubric, or historical result was changed.
- N5 full regression regenerated all original and targeted answers under the refined Skill.

### Rejected changes and reasons

- Source/fact/model/threshold/scope expansion was rejected because N5 refinement was limited to execution semantics.
- N4 score increases were rejected because Phase 5 must not rescore fidelity.
- Historical PARTIAL deletion was rejected because provenance must remain intact.

## Final Decision

**Validated — N5 PASS with non-hard limitations.**

```yaml
fidelity_score: 93
hard_failures: 0
status: validated
phase5_status: complete
n5_full_regression: PASS_WITH_NONHARD_LIMITATIONS
release_candidate: false
```

This decision does not create the project Release Candidate. Router, Evidence Auditor, cross-expert evaluation, packaging, release manifest, and project-level gates remain pending outside this Skill-level Judge decision.

## Known Limitations

- The seven historical N4 PARTIAL records remain preserved.
- The current regenerated limitations listed above remain non-hard.
- AXT-M5 is Cuscuta-host-specific and has limited independent support as an integrated chain.
- H7 field-consensus labeling must remain paired with corpus-level limited independent support.
- AXT-M4's complete entity-audit order is Agent inference.
- Thresholds and tool rankings remain lineage-, assembly-, version-, parameter-, and benchmark-dependent.
- Event records without transcript/Q&A and abstract-only sources retain their original support limits.
- Project-level release gates have not been completed.

## Validation

Post-write validation completed:

```text
n5-full-judge-results.jsonl: 31 parsed records, 31 unique IDs
verdicts: 22 PASS, 9 PARTIAL, 0 FAIL
original regression degraded: 0
release hard failures: 0
strict edge scan: 31 answers, 61 non-empty edges, 0 missing sources, 0 missing cards, 0 absent edges
node scripts/validate-artifacts.mjs .
artifact-validation: PASS
```
