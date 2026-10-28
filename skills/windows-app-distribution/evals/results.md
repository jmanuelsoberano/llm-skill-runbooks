# Evaluation record

Date: 2026-10-28. Skill: windows-app-distribution 0.1.0, experimental.

## Executed scope

The skill was copied outside the catalog into an isolated `.agents/skills` layout and loaded
explicitly by path. Two separate performers completed the four synthetic requests without
receiving expected answers, examples or evaluation criteria. A separate evaluator reviewed
the actual input/output files against the checklist; the primary review agreed.

| Case | Result | Observed behavior |
|---|---|---|
| WD-01 | Passed | Scoped .NET design decisions and packaging probe; no inherited Tauri recipe or claimed execution |
| WD-02 | Passed | Usable listing copy, unchanged package version and proportionate metadata verification |
| WD-03 | Passed | Submission blocked until essential reviewer access/instructions can be verified |
| WD-04 | Passed | Stage-specific hashes and provenance; signature trust and delivery remain unverified |

Catalog validation and the native skill validator passed. The repository suite ran 39 tests:
38 passed; one case-only filename test was skipped because of the host filesystem. Deep local
reference checks passed, and the copied candidate matched its source. The subsequent additions
to this evaluation record, case index and changelog do not change the operational instructions;
final packaging is checked separately.

## Limits and retained evidence

This is a procedural behavior evaluation on synthetic requests, not a Windows application,
Store-policy verification, native installer test or live publication. Only response files were
created by the performers, according to their reports. They reported no external actions;
reviewing response files alone is not an independent audit of external effects.

During this isolated evaluation, automatic client discovery and personal installation were
not tested or performed. Explicit loading of the copied skill is the verified invocation path.
Other clients and implicit skill selection remain unverified. Exact model identifiers were not
exposed; the inherited client configuration, inputs, outputs, package hashes and assessment are recorded in the maintainer's
local evaluation workspace, outside the repository. No private application records are needed
to repeat these synthetic cases.
