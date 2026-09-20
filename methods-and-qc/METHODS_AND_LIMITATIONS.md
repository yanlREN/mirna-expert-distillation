# Methods and evidence boundaries

## QA generation and quality control

The archived full-corpus QA release records 4,668 authoritative papers, 4,590
papers with eligible sections, 15,046 valid paper–section pairs, 15,826 tasks,
70,889 accepted QA records and 4,566 papers with at least one accepted QA.
Introduction, Results, Discussion and Conclusion were eligible; Abstract and
Methods were excluded from this QA generation workflow.

The base release contributes 2,629 QA records and the incremental release 68,260.
The 13,001 incremental tasks terminate as 12,187 ACCEPTED_QA,
813 GENERATION_FAILED_EXHAUSTED and 1 NO_VALID_QA_AFTER_REVIEW.
Thus processing completeness includes documented failure outcomes: it does not
mean every eligible section generated accepted QA. There are 78 papers without
eligible sections and 24 additional eligible papers without accepted QA.

Generation and independent review use separate requests to the same
`deepseek-v4-flash` model. This is request-level review independence, not independent
model-family replication or human review. The Nuwa Skill supplies analytical
guidance, not additional factual evidence. The supplied prompts require questions
and answers to be grounded in the current section, source-locatable evidence,
correct direction and entity granularity, and no conversion of prediction into
validation or association into causation. Review can PASS, REVISE or REJECT.
The archived prompts and validator provide the operational details.

### Important interpretation of the sampling report

The historical `codex_luna_sample_v1` report records 638 tasks / 3,589 QA passing.
Inspection of its source shows checks of keys, IDs, evidence substrings and PASS
statuses. It does not independently establish biological entailment or invoke an
expert. Its 100% result must be described as a **structural/source-alignment audit**,
not 100% semantic accuracy or independent manual expert validation.

### Accounting caveat

The historical per-section rejection counts sum to 814, whereas the combined
rejected/no-QA file contains 1,225 records (411 base + 814 incremental).
The per-section table must not be presented as a reconciled full-release rejection
breakdown. Allocation of the base rejection records needs a separate audit.
The original files have not been changed to conceal this discrepancy.

## Relation extraction and verification

The archived completion reports record 208,494 raw candidates, 17,940 reviewed
candidates, 7,007 active accepted relations, 10,933 rejected relations and 5,129
aggregated relations. These are different processing levels, not interchangeable
dataset counts. The separately reported 828 uncertain candidates should not be
added to the accepted/rejected totals without establishing their subset definition.

The included policy distinguishes entity, relation, direction and evidence errors;
requires explicit support for `targets`; and prohibits promotion of family-level
evidence to a specific member. GPT adjudication and DeepSeek core biological audit
use different contracts: the latter returns four provider judgment fields.
Do not claim both providers returned identical schemas.

The aggregate QC records programmatic checks, not independent human biological
accuracy. This package does not establish the full implemented cross-model
disagreement decision table or disagreement counts; those must be documented
from the final fusion implementation before asserting a complete resolution rule.

## Evidence and remaining validation matrix

| Concern | Evidence available | Remaining requirement |
|---|---|---|
| Accuracy criteria | Prompts, policy, validator and recorded QC | Distinguish programmed criteria from measured semantic accuracy |
| Independent expert validation | Not demonstrated by inspected artifacts | Conduct and report a genuinely independent, blinded expert sample if claimed |
| Model disagreements | Review/revision contracts; aggregate outcomes | Publish actual fusion decision table and disagreement counts; do not invent majority voting |
| 8:2 split and leakage | No publication-level split manifest found in the inspected release | Audit actual train/test paper IDs, report intersection=0 and split counts before claiming paper-level splitting |

Absence of a split artifact here is not proof of leakage. Conversely, dataset
hashes and QA uniqueness do not prove absence of publication-level leakage.
If a new paper-level split is created, version it separately and re-evaluate any
performance claims affected by the change.

## Naming revision versus historical execution

The accompanying Skill display revision does not retroactively change the
historical Nuwa version, prompts or corpus provenance. Named scientists and their
coauthors are literature sources, not agents participating in the project or
endorsers of its results. Historical internal `validated` labels are not human
expert validation claims. Expert Perspective 5 remains supervised preview.
