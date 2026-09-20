# Contributing

[English](CONTRIBUTING.md) | [中文](CONTRIBUTING_ZH.md)

## Scope

This public candidate is fixed as a five-perspective panel. Ordinary
contributions must not add, replace, or merge perspectives, or promote Expert
Perspective 5 from `supervised_preview` to `validated`. Personal names are used
only for literature attribution, not as simulated speaking roles.

## Accepted contributions

- Repair broken links or bibliographic metadata errors.
- Add corrections, errata, retractions, or independent counterevidence.
- Correct miRNA family/locus/arm/species/assembly confusion.
- Improve WorkBuddy installation compatibility and accessibility guidance.
- Add evaluation cases that expose overinterpretation.
- Repair reference closure, JSONL structure, or checksum problems.

## Requirements for scientific changes

Any pull request that changes an evidentiary ceiling should provide:

1. a link to the original paper, methods standard, or official database documentation;
2. a DOI, PMID, PMCID, or stable URL;
3. the applicable species, tissue, treatment, genotype, strain, assembly, and assay scope;
4. the directness, independence, and limitations of the evidence;
5. affected claim/source IDs; and
6. corresponding regression tests.

Prediction must not be described as validation, expression correlation as
causation, PARE/degradome evidence as a complete phenotypic causal chain, or
database inclusion as experimental confirmation.

## Prohibited contributions

- Paper PDFs, unauthorized full text, or long copyrighted quotations.
- Raw sequencing data, model weights, local LLMs, or training environments.
- Private communications, unpublished personal views, or researcher impersonation.
- Unsourced DOI, PMID, ORCID, or accession identifiers.
- Changes that pass a component by deleting tests or weakening standards.
