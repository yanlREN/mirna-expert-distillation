# Security

[English](SECURITY.md) | [中文](SECURITY_ZH.md)

## Package capabilities

The installable Skill ZIP contains Markdown, YAML, and JSONL files only. It
contains no scripts, executables, network connectors, automatic file-writing
logic, or account credentials. By itself, it does not download data, call
third-party APIs, or train models.

The repository also contains historical quality-checking reference code under
`methods-and-qc/reference-code/`. Those files are not included in the
installable Skill ZIP and do not run automatically when the Skill is installed.

The model service, network access, logging, and permissions used at runtime are
determined by the user's WorkBuddy configuration and are not controlled by this
repository.

## Before installation

1. Download from a trusted repository or GitHub Release.
2. Verify the ZIP and Skill files against `CHECKSUMS.sha256`.
3. Confirm that the archive contains only the expected `.md`, `.yaml`, and
   `.jsonl` files.
4. Confirm that `SKILL.md` still prohibits researcher impersonation and retains
   the `supervised_preview` status of Expert Perspective 5.
5. Use Ask mode for the first run and grant no unnecessary filesystem or system permissions.

## Data privacy

Do not submit patient identifiers, unpublished experimental data, passwords,
API keys, institutional subscription credentials, restricted paper full text,
or other sensitive material to an untrusted model service. Before analyzing
unpublished research, confirm that the selected WorkBuddy model and applicable
organizational policy permit that data processing.

## Reporting security issues

Include the package version, file hash, WorkBuddy version, reproduction steps,
observed behavior, and expected behavior. Do not post credentials, private data,
or copyrighted full text in a public issue.
