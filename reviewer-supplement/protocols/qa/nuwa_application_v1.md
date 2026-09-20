# MIRNA_QA_COVERAGE_NUWA_APPLICATION_V1
Apply the frozen Nuwa miRNA five-lens panel to the supplied section only. Nuwa
metadata is a candidate-design aid, never an evidence source. Do not use
outside knowledge, relation-extraction state, or any other model output.
Return one JSON object with exactly the keys `information_points` and
`no_qa_reason`. Each information point must use exactly these keys in order:
`information_point_id`, `content`, `suggested_qa_type`,
`candidate_question`, `candidate_answer`, `candidate_evidence`,
`risk_flags`, `lens_trace`. The runner assigns the final identity fields;
do not emit paper_id, section_id, model, or hashes. The five allowed
suggested_qa_type values are RELATION_FACT, EVIDENCE, CONTEXT,
RESULT_PHENOTYPE, and CONCLUSION_SIGNIFICANCE. Every candidate_evidence must
be copied character-for-character from the supplied section text, including
punctuation, capitalization, spacing, and any parenthetical text; never
paraphrase or normalize the quote. Before returning, verify every
`candidate_evidence` value is an exact contiguous substring of the input.
If an information point cannot supply such an exact quote, omit that point.
Keep points concise
and non-duplicative. `risk_flags` must be an array of unique non-empty strings
(use [] when there are no flags), and `lens_trace` must be a non-empty array
of unique non-empty strings (one or more applicable Nuwa lens labels). If the
section contains no defensible information point
for these QA types, return an empty array and a specific non-empty
no_qa_reason; otherwise return null for no_qa_reason. Do not return Markdown or
commentary.
