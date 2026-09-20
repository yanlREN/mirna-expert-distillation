# Adjudication Policy

## Evidence boundary

Use only the supplied evidence sentence and candidate tuple. Do not infer from unstated full-text context or outside biological knowledge.

## Labels

- `CORRECT`: exact entities, relation, direction, and specificity are supported.
- `WRONG_ENTITY`: a candidate entity is invalid or not the stated entity.
- `WRONG_RELATION`: entities are present but the proposed relation is wrong.
- `WRONG_DIRECTION`: evidence supports the reverse direction.
- `INSUFFICIENT_EVIDENCE`: the sentence does not establish the exact candidate.
- `UNCERTAIN`: the evidence cannot be adjudicated reliably.

## Specificity

Allowed values are `DIRECT`, `FAMILY_LEVEL`, `GROUP_LEVEL`, and `AMBIGUOUS`. Family/group evidence cannot validate a specific member unless that member is explicitly supported.

## Relation scope

Allowed values are `molecular`, `expression`, and `phenotype`.

## Target directness

`targets` is accepted only when the evidence explicitly identifies the target relationship or reports direct validation, such as luciferase, degradome, 5′ RACE, cleavage, or direct binding. Transcript reduction without direct target evidence may support `represses`. Prediction or correlation alone is `INSUFFICIENT_EVIDENCE`.

## Direction

Condition–miRNA evidence is normalized as `miRNA responds_to condition`. Do not accept a reversed tuple unless the supplied evidence explicitly supports that direction and the submitted relation permits it.

## Recommended relation sentinel

The frozen and exclusive no-applicable-relation value is `NOT_APPLICABLE`. `NONE`, empty strings, nulls, and alternative spellings are invalid.

