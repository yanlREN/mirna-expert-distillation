# MIRNA_QA_COVERAGE_INCREMENTAL_GENERATION_V1
Generate section-grounded QA candidates using only the supplied frozen section
text. The supplied Nuwa five-lens information points are design aids only and
never evidence. Do not use outside knowledge, relation status, or other model
outputs. Return exactly the JSON keys `items` and `no_qa_reason`. Each item
must contain exactly these keys in order: `qa_type`, `question`, `answer`,
`evidence_sentence`. QA types are RELATION_FACT, EVIDENCE, CONTEXT,
RESULT_PHENOTYPE, and CONCLUSION_SIGNIFICANCE. For introduction return
between 1 and 4 items inclusive; for results return between 3 and 10 items
inclusive; for discussion return between 1 and 5 items inclusive; for
conclusion return between 1 and 3 items inclusive. Do not exceed the maximum
for the section type. If no defensible QA can be supported, return an empty
items array and a specific non-empty `no_qa_reason`; otherwise
`no_qa_reason` must be null. Every `evidence_sentence` must be copied
character-for-character as a contiguous substring of the supplied section
text, including punctuation, capitalization, spacing, and parenthetical text.
Preserve prediction/association versus validation/causation, entity direction
and family/member level. Do not return Markdown, identity fields, or
commentary.
