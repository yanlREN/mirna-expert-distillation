# miRNA Five-Lens Scientific Panel for WorkBuddy

[English](README.md) | [中文](README_ZH.md)

A five-perspective research-analysis Skill for questions involving miRNAs,
plant small RNAs, RNA silencing, and cross-kingdom RNA. It applies five public
research frameworks to the same question while preserving each perspective's
focus, evidence boundary, disagreements, and follow-up questions.

> **Release status: GitHub public candidate / prerelease.** Perspectives 1–4
> retain historical project-internal `validated` status, which is not human
> expert confirmation. Perspective 5 remains `supervised_preview` and has not
> passed the formal release gate. These labels must remain visible in use and
> redistribution.

## Literature basis and role names

This is a literature-guided analysis Skill; five separate expert models were
not trained. Personal names are used only for source attribution. The five
perspectives are primarily informed by public work from Axtell, Chen, Meyers,
Carrington, Jin, their coauthors, and relevant independent groups. See the
[literature attribution](skills/mirna-five-lens-panel/references/literature-attribution.md).
The project does not claim that the named researchers reviewed or endorsed the
tool. Automated perspectives do not constitute human expert validation.

## What it does

- Analyzes scientific questions, abstracts, results passages, figure legends,
  and research proposals.
- Separately identifies each perspective's assumptions, evidentiary ceiling,
  missing controls, and follow-up questions.
- Distinguishes miRNA identity, direct target evidence, and phenotypic causality.
- Distinguishes family, MIR gene family, locus, precursor, mature sequence,
  5p/3p, isomiR, sequence, and database-record entity levels.
- Audits cross-kingdom RNA claims edge by edge: origin → release/carrier →
  stability → intact uptake → effector access → direct target action → phenotype.
- Summarizes shared conclusions, complementary concerns, unresolved differences,
  and the evidence most likely to change the conclusion.

It does not train models, include model weights, download raw sequencing data,
or impersonate any researcher.

## Perspective status

| Perspective | Primary focus | Status |
|---|---|---|
| Expert Perspective 1 | miRNA identity, annotation rigor, miRNA/siRNA classification, and entity level | `validated` |
| Expert Perspective 2 | plant miRNA biogenesis, processing, methylation, AGO loading, and lifecycle | `validated` |
| Expert Perspective 3 | small-RNA omics, PARE/degradome, PHAS/phasiRNA, and reproducibility | `validated` |
| Expert Perspective 4 | DCL/RDR/AGO, tasiRNA, viral suppressors, and RNA-silencing pathways | `validated` |
| Expert Perspective 5 | plant–pathogen cross-kingdom RNA, carriers/uptake, recipient pathways, and causal chains | `supervised_preview` |

`supervised_preview` does not mean “a fifth validated expert.” Perspective 5
still has four completeness regressions in the independent N5 regression set;
the panel therefore preserves its status, evidence cutoff, and edge-specific
stopping points.

## Repository layout

```text
.
├── README.md                       # English (default)
├── README_ZH.md                    # Chinese
├── LICENSE
├── NOTICE.md
├── RELEASE-MANIFEST.yaml
├── CHECKSUMS.sha256
├── docs/
├── methods-and-qc/
├── skills/
│   └── mirna-five-lens-panel/       # self-contained WorkBuddy Skill
├── dist/
│   └── mirna-five-lens-panel-workbuddy.zip
└── third-party-licenses/
    └── NUWA-MIT.txt
```

All five perspectives are embedded in the panel. Ordinary users should install
only `mirna-five-lens-panel`, rather than enabling five separate copies.

## Install in WorkBuddy

### Option 1: upload through the interface

1. Download `mirna-five-lens-panel-workbuddy.zip` from the GitHub Release.
2. Verify it against `CHECKSUMS.sha256`.
3. In WorkBuddy, open Skills → Installed → Add Skill → Upload Skill.
4. Select the ZIP and wait for the import to finish.
5. Create a task; **Ask** mode is recommended for the first run.
6. Select `mirna-five-lens-panel` in the input area and enter the question.

WorkBuddy documentation describes importing local skills and recommends
reviewing a third-party Skill's source, permissions, and scripts before use:

- [WorkBuddy skill management](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
- [Creating a task and selecting a skill](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

### Option 2: manual copy

Copy the complete `skills/mirna-five-lens-panel` directory to the user Skills
directory:

```text
Windows: C:\Users\<username>\.workbuddy\skills\mirna-five-lens-panel
macOS/Linux: ~/.workbuddy/skills/mirna-five-lens-panel
```

Completely exit and restart WorkBuddy. If your WorkBuddy version shows a
different local Skills directory, use the location displayed by that version.
See [the installation guide](docs/INSTALL-WORKBUDDY.md) for troubleshooting.

## Minimal prompt

```text
Use the five-perspective scientific panel to analyze the following material:

[Paste a question, abstract, results passage, or figure legend]

For Expert Perspectives 1–5, separately report:
1. applicability;
2. primary concerns;
3. the strongest conclusion supported by the current evidence;
4. evidence gaps;
5. the 2–4 most useful follow-up questions.

Then summarize common ground, complementary concerns, disagreements that must
remain explicit, and the next evidence most likely to change the conclusion.
Do not decide scientific truth by majority vote. Mark Perspective 5 as
supervised_preview.
```

Additional templates are available in [docs/USAGE.md](docs/USAGE.md).

## Scientific and identity boundaries

- Outputs are agent applications of public research frameworks, not statements
  by the named researchers and not evidence of their current views or endorsement.
- Agreement among perspectives is not evidence from independent laboratories;
  scientific truth must not be decided by voting.
- Database inclusion, predicted hairpins, target predictions, PARE peaks, and
  inverse expression each have a limited evidentiary ceiling.
- Judgments on new material default to `agent_inference`; use
  `documented_framework` only when the cited source actually supports the claim.
- The evidence cutoff is **2026-07-17**. Later publications, corrections, or
  retractions require renewed source verification.
- The Skill does not replace reading the source papers, statistical review,
  experimental validation, clinical judgment, or domain peer review.

See [scientific limitations](docs/SCIENTIFIC-LIMITATIONS.md).

## Security

The candidate Skill package contains no executable scripts, binaries, account
credentials, network connectors, or automatic file-writing logic. It contains
Markdown, YAML, and JSONL instructions, metadata, structured evidence summaries,
and lawful links. How user input is processed still depends on the selected
WorkBuddy model, permissions, and privacy settings.

Review third-party Skill contents and SHA-256 values before installation. Do not
send unpublished data, patient information, passwords, institutional credentials,
or restricted full text to an untrusted model service. See [SECURITY.md](SECURITY.md).

## Validation status

- The panel and all five embedded perspectives pass Skill structure validation.
- JSONL records parse successfully and referenced local files are present.
- The package contains no PDFs, raw sequencing data, model weights, caches, or credentials.
- ZIP contents and SHA-256 values were regenerated and verified.
- The authoritative project state remains `partial_release_candidate`; this
  repository does not promote Perspective 5 to `validated`.

See [docs/VALIDATION.md](docs/VALIDATION.md) for the exact scope and limitations.

## Methods and quality-control materials

The [methods and quality-control directory](methods-and-qc/README.md) separates
archived reports, reproducible methods evidence, and validation/split audits
that remain outstanding. A programmatic PASS is not presented as biological accuracy.

## Before redistributing

1. Distribute the complete repository, not `SKILL.md` alone.
2. Mark the first GitHub Release as **Pre-release**, not production-ready.
3. Attach `dist/mirna-five-lens-panel-workbuddy.zip` and `CHECKSUMS.sha256`.
4. Preserve `LICENSE`, `NOTICE.md`, `RELEASE-MANIFEST.yaml`, and the
   `supervised_preview` label for Perspective 5.
5. Do not add paper PDFs, caches, raw sequencing data, model files, or credentials.

See [GitHub publishing guidance](docs/GITHUB-PUBLISHING.md).

## License and attribution

Original instructions, documentation, and structured code materials in this
candidate are provided under the [MIT License](LICENSE). The upstream Nuwa MIT
license is preserved in [third-party-licenses/NUWA-MIT.txt](third-party-licenses/NUWA-MIT.txt).
Papers, databases, and third-party websites remain the property of their respective
rightsholders; this repository does not redistribute paper full text.

See [NOTICE.md](NOTICE.md) for attribution and non-endorsement details.
