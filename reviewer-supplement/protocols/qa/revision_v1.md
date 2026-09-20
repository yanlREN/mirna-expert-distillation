# MIRNA_QA_COVERAGE_INCREMENTAL_REVISION_V1
Revise only the supplied positional QA candidates using the supplied frozen
section text. Preserve the scientific claim and evidence strength; use no
outside knowledge. Return exactly JSON keys `items` and `no_qa_reason`.
Each item has exactly `qa_type`, `question`, `answer`,
`evidence_sentence`; evidence must be a contiguous source substring. An
empty items array is allowed only with a specific no_qa_reason. Do not return
identity fields, Markdown, or commentary.
