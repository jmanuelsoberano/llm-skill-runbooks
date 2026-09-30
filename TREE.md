# Árbol del repositorio

Snapshot de archivos fuente del catálogo.

```text
llm-skill-runbooks/
├── conventions
│   ├── evaluation-guide.md
│   ├── markdown-output-guide.md
│   ├── naming.md
│   ├── prompt-style-guide.md
│   ├── skill-contracts.md
│   └── versioning.md
├── playbooks
│   ├── how-to-add-new-skill.md
│   ├── how-to-improve-with-llm.md
│   ├── how-to-run-evals.md
│   ├── migrate-existing-skills.md
│   ├── prompt-review-process.md
│   └── use-and-install-agent-skills.md
├── references
│   └── prompt-engineering-sources.md
├── schemas
│   ├── agent-skill.schema.json
│   ├── skill.schema.json
│   └── test-case.schema.json
├── scripts
│   └── validate_repo.py
├── skills
│   ├── evidence-guided-development
│   │   ├── agents
│   │   │   └── openai.yaml
│   │   ├── assets
│   │   │   └── system-context-template.md
│   │   ├── evals
│   │   │   ├── cases.md
│   │   │   └── checklist.md
│   │   ├── examples
│   │   │   ├── sample-input.md
│   │   │   └── sample-output.md
│   │   ├── references
│   │   │   ├── architecture-and-performance.md
│   │   │   ├── code-changes.md
│   │   │   ├── data-changes.md
│   │   │   ├── oreilly.md
│   │   │   └── requirements-and-docs.md
│   │   ├── changelog.md
│   │   ├── input.schema.md
│   │   ├── output.schema.md
│   │   ├── prompt.full.md
│   │   └── SKILL.md
│   ├── meeting-transcript-analysis
│   │   ├── adapters
│   │   │   ├── chatgpt.md
│   │   │   ├── claude.md
│   │   │   ├── copilot.md
│   │   │   ├── gemini.md
│   │   │   └── generic-llm.md
│   │   ├── evals
│   │   │   ├── agent-cases.md
│   │   │   ├── checklist.md
│   │   │   ├── evaluator.prompt.md
│   │   │   ├── rubric.md
│   │   │   └── test-cases.yaml
│   │   ├── examples
│   │   │   ├── example-ambiguous-transcript.txt
│   │   │   ├── example-analysis-output.md
│   │   │   └── example-teams-transcript.txt
│   │   ├── changelog.md
│   │   ├── input.schema.md
│   │   ├── output.schema.md
│   │   ├── prompt.chunked-long-transcript.md
│   │   ├── prompt.file-input.md
│   │   ├── prompt.full.md
│   │   ├── prompt.multi-transcript.md
│   │   ├── prompt.quick.md
│   │   └── SKILL.md
│   ├── repository-initialization
│   │   ├── evals
│   │   │   ├── agent-cases.md
│   │   │   └── checklist.md
│   │   ├── examples
│   │   │   ├── app-framework-native-example.md
│   │   │   ├── app-monorepo-workspace-example.md
│   │   │   ├── app-repo-example.md
│   │   │   ├── app-single-src-layered-example.md
│   │   │   ├── app-split-frontend-backend-example.md
│   │   │   ├── code-repo-example.md
│   │   │   ├── docs-repo-example.md
│   │   │   ├── testing-by-structure-pattern-example.md
│   │   │   └── testing-profiles-example.md
│   │   ├── templates
│   │   │   ├── CHANGELOG.md
│   │   │   ├── DECISIONS.md
│   │   │   ├── GITIGNORE.md
│   │   │   ├── LLM_GUIDE.md
│   │   │   ├── PROJECT_CONTEXT.md
│   │   │   ├── README.repo.md
│   │   │   ├── STRUCTURE.md
│   │   │   ├── TEST_STRATEGY.md
│   │   │   └── TODO.md
│   │   ├── changelog.md
│   │   ├── input.schema.md
│   │   ├── output.schema.md
│   │   ├── prompt.file-input.md
│   │   ├── prompt.full.md
│   │   ├── prompt.quick.md
│   │   └── SKILL.md
│   ├── repository-issue-generator
│   │   ├── evals
│   │   │   ├── agent-cases.md
│   │   │   └── checklist.md
│   │   ├── examples
│   │   │   ├── input-from-meeting-analysis.md
│   │   │   └── output-issues.md
│   │   ├── changelog.md
│   │   ├── input.schema.md
│   │   ├── output.schema.md
│   │   ├── prompt.full.md
│   │   └── SKILL.md
│   └── technical-requirements-extractor
│       ├── evals
│       │   ├── agent-cases.md
│       │   └── checklist.md
│       ├── changelog.md
│       ├── input.schema.md
│       ├── output.schema.md
│       ├── prompt.full.md
│       └── SKILL.md
├── templates
│   ├── adapter-template.md
│   ├── changelog-template.md
│   ├── eval-template.md
│   ├── prompt-template.md
│   └── skill-template.md
├── tests
│   └── test_validate_repo.py
├── workflows
│   ├── meeting-to-documentation.md
│   ├── meeting-to-repository-followup.md
│   └── multi-meeting-program-tracker.md
├── .gitignore
├── AGENTS.md
├── LICENSE.md
├── README.md
├── registry.yaml
├── requirements-dev.txt
└── TREE.md
```


## Ampliación de investigación — 2026-09-29

- research-suite.json: manifiesto de 20 paquetes (18 principales y 2 integraciones).
- references/evidence-contract.md: fuente canónica de evidencia compartida.
- scripts/manage_research_suite.py: sincronización, comprobación, empaquetado e instalación.
- tests/test_research_suite.py: integridad, conflictos, recuperación y portabilidad.
- playbooks/research-suite.md y workflows/engineering-research.md: uso y composición.
- Las nuevas carpetas de skills se enumeran en registry.yaml y README.md.
