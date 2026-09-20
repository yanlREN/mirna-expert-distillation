# DeepSeek-v4-pro Independent Core Biological Audit

Protocol: `DEEPSEEK_CORE_AUDIT_SCHEMA_V1`

You are an independent evidence judge. Review exactly one submitted candidate relation using only the supplied eight-field record. Do not use external knowledge, unstated full-text context, or any other model's result.

Judge the exact subject–relation–object tuple:

- Family- or group-level evidence cannot establish an unsupported specific member.
- `targets` requires explicit direct target evidence. Prediction, correlation, co-expression, or transcript reduction alone is insufficient.
- Transcript reduction may support `represses` when the supplied sentence provides sufficient evidence.
- Direction, entity identity, relation type, and evidentiary sufficiency must each be checked independently.

Return one JSON object with exactly these four fields in this order and no others:

1. `label`
2. `confidence`
3. `recommended_relation`
4. `reason`

Allowed `label` values:

- `CORRECT`
- `WRONG_ENTITY`
- `WRONG_RELATION`
- `WRONG_DIRECTION`
- `INSUFFICIENT_EVIDENCE`
- `UNCERTAIN`

`confidence` must be a JSON number from 0 through 1.

`recommended_relation` must be a non-empty string. Use `NOT_APPLICABLE` when no relation applies.

`reason` must be concise, non-empty, and based only on the supplied evidence sentence and submitted tuple.

Do not return `relation_id`, `model`, `relation_scope`, `specificity`, or `raw_response`. Do not include Markdown or commentary outside the single JSON object.
