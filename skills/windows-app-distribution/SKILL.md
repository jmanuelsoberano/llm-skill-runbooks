---
name: windows-app-distribution
description: "Plan, implement or verify distribution of Windows applications through Microsoft Store and direct-download channels. Use for early packaging decisions, release preparation, signing boundaries, listing updates or customer-delivery verification; adapt to the project's stack and changed risks."
metadata:
  id: "distribution.windows.app"
  version: "0.1.0"
  status: "experimental"
---

# Windows application distribution

Prepare the requested distribution outcome while preserving the application's architecture,
chosen channels and the user's scope. A listing edit, first release and identity change need
different work.

1. Read [input.schema.md](input.schema.md), [prompt.full.md](prompt.full.md) and
   [output.schema.md](output.schema.md). Use available project context before asking questions.
2. Read only the relevant sections of the
   [canonical guide](references/distribution-guide.md):
   - Design or first packaging: sections 1-2.
   - Signing, provenance or CI boundaries: sections 3-4.
   - Changed-risk verification: section 5.
   - Listings, submission or delivery: sections 6-7.
   - Evidence reuse or completion: Release record and completion criteria.
3. Recheck current official requirements when a version-sensitive decision depends on them.
   Prefer existing tooling and access. If unavailable, identify the unresolved requirement;
   do not invent current policies or claim execution.

The [SchemaCraft case](references/schemacraft-case.md) is optional background. Its identity,
framework, scripts, private records and accepted deferrals are not defaults for a new app.

For maintenance only, use [evals/checklist.md](evals/checklist.md),
[evals/cases.md](evals/cases.md), the [example input](examples/sample-input.md),
[example output](examples/sample-output.md) and [changelog.md](changelog.md).
Example results and evaluation expectations are not facts about the user's project.
