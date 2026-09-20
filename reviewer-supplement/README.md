# Reviewer evidence supplement — release candidate

Prepared 2026-09-20 from archived project reports. This is a documentation and
reproducibility supplement, not a new corpus release or an independent human
validation. Historical reports are preserved verbatim; their status names must
be interpreted with the limitations below.

## Contents

- `source-reports/qa/`: recorded coverage, generation, quality and sampling reports,
  release manifest, and deterministic sampling results.
- `source-reports/relations/`: recorded extraction, lineage, completion audit and QC.
- `protocols/qa/`: generation, independent review, revision and Nuwa application prompts.
- `protocols/relations/`: evidence adjudication policy, DeepSeek prompt and schemas.
- `reference-code/`: historical QA validator and structural sampling audit.
- [Methods, limits and reviewer questions](METHODS_AND_LIMITATIONS.md).
- `SOURCE_INVENTORY.json`: SHA256 of each copied source artifact.

The repository-level CHECKSUMS.sha256 covers this supplement. Dataset hashes in
the historical release manifest are recorded provenance, not a claim that all
large datasets were revalidated during this documentation-only preparation.

## What this supports

The files document evidence-only prompts, executable structural checks, corpus
coverage and release accounting. They do **not** demonstrate independent expert
accuracy, absence of semantic errors, or a publication-disjoint training/test split.
Those require additional evidence before being asserted in a reviewer response.

## Publication boundary

No credentials, raw API responses, paper full texts, per-record QA datasets or
Gold/human annotations are included in this supplement. Third-party literature
and model outputs are not relicensed by the repository MIT license. Existing
citations, authorship and third-party notices remain applicable. Review the
underlying licenses separately before uploading full datasets.

中文说明：本补充包用于展示实际方法和审计证据，不可称为人工专家验证。
展示名称改为“专家视角1–5”；研究者姓名仅保留在文献来源与引用中。
Skill是文献框架整理的指令包，不是五个独立训练的专家模型。
