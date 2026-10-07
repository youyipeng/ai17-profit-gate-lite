# Internal benchmark summary

The internal AI-17 candidate was evaluated using 20 real, publicly posted client implementation requirements from Freelancer: 10 diagnostic cases and a separate 10-case reserve group not used for tuning before its final inference. **The final reported holdout is 10 cases, not 20 unseen cases.**

Final reserve group, baseline → AI-17:

| Measure | Baseline | AI-17 |
| --- | ---: | ---: |
| Gate risk omission (unsafe PASS/quote cases) | 2/10 | 0/10 |
| Individual risk omissions | 54/83 | 1/83 |
| Critical-risk recall | 35.4% | 98.8% |
| Runtime/maintenance omissions | 17/20 | 0/20 |
| Decision agreement with internal reference labels | 7/10 | 10/10 |
| Unsupported exact quotes | 0/10 | 0/10 |

AI-17 deterministic mathematics checks: 288/288, zero inconsistencies. The strict gate comparison 0 < 2 passed without lowering thresholds. One Stripe merchant eligibility/terms risk was omitted, while that case remained REVIEW.

This is an internal, small-sample benchmark. Labels were evidence-grounded and model-assisted; there was no independent human/external validation, independent custodian, or observed project delivery/profit outcome. The same provider and orchestrator were involved. Figures describe the internal candidate and evaluation pipeline, not a measured performance guarantee for Lite or every agent using the packaged Pro workflow. Packaging smoke checks are separate. These results do not guarantee future project outcomes. Original briefs, labels, case-level outputs, scoring details and private prompts are not distributed.
