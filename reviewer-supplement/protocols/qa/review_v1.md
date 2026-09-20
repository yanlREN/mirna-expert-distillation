# MIRNA_QA_COVERAGE_INCREMENTAL_REVIEW_V1
Independently review each positional QA candidate against only its supplied
section text. Nuwa metadata is provenance and never evidence. Return exactly
the JSON keys `items` and `no_qa_reason`. Each item must contain exactly:
`label`, `reason`, `error_type`, `revised_question`,
`revised_answer`, `revised_evidence_sentence`. Use PASS, REVISE, or REJECT.
Every `reason` must be a concise non-empty string explaining the evidence
decision; never return an empty reason.
Use REVISE only when the claim is supported but wording/evidence can be
corrected from the section; all three revised fields must then be non-empty
contiguous-source corrections. PASS and REJECT require null revision fields.
If every candidate is unsupported, items may be empty only with a specific
no_qa_reason. Do not add facts, upgrade evidence, or return commentary.
