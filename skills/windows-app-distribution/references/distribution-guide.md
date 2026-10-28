# Windows application distribution guide

Status: draft. Version: 0.1.2. Last source review: 2026-10-28.

## Purpose and scope

Prepare a Windows application for Microsoft Store and independently distributed releases,
starting during design and returning to the relevant checks as the product changes. The
procedure applies across frameworks; it does not prescribe Tauri, .NET, Electron, a portable
executable, MSIX, or a particular installer or signing provider.

This is the canonical human-readable reference for
[windows-app-distribution](../SKILL.md). The method itself creates no account, installs no
tooling, changes no certificate trust, and authorizes no external action. The optional
[SchemaCraft case](schemacraft-case.md) separates observed experience from recommendations.

## Start early; apply only the relevant phase

| Phase | Focus | Reviewable result |
|---|---|---|
| Design | Channels, identity, privileges, data ownership and updates | A distribution decision record |
| First working application | Test packaging feasibility before feature completion | An installed, runnable prototype |
| Development | Maintain channel boundaries and applicable checks | Repeatable builds and automated guards |
| Release candidate | Verify the actual deliverables and changed risks | An artifact inventory and acceptance record |
| Submission and publication | Prepare the listing and execute approved external actions | Submission identity and publication evidence |
| Customer delivery | Check availability and the delivered version | A customer-route verification record |

An existing application starts with a gap assessment, not a mandatory restart of every phase.

## 1. Establish the application-specific context

Read the repository instructions, architecture, release workflow and previous decisions. Record:

- Product owner, audience, supported Windows versions, architectures, frameworks and runtimes.
- Required distribution channels, supported offline behavior, price and intended markets.
- Publisher-account eligibility and applicable policies for this product type; an existing
  account for one application is not proof of eligibility for every future product [M5].
- Actual installation format and update owner for each channel; first release or upgrade.
- Stable application/package identity, publisher information and versioning rules. Obtain real
  Store identity from the product's own Partner Center entry; do not copy another app's values.
- Privileges, capabilities, services, drivers, external integrations and file associations.
- Ownership and effective locations of preferences, projects, credentials, caches and logs.
- Licensing, dependency notices, privacy/support information and any unresolved constraints.

If monetized, distinguish application purchases, in-app purchases and subscriptions. Record
the entitlement authority per channel, offline/outage behavior and any intended cross-channel
portability. Verify the current Store commerce rules for that model before implementation [M5];
supporting another channel does not automatically make purchases transferable.

Reuse confirmed decisions and authorization. Ask only questions that change the result, one
product decision at a time when needed. Keep personal account data, private keys, credentials
and production fixtures out of reusable documentation. Mark unknown facts explicitly.

## 2. Preserve the distribution boundary

Keep product behavior separate from packaging, signing, publication and channel configuration.
Required Store integrations, if any, should have explicit interfaces and an alternative policy
for other channels. Do not duplicate business rules for each installer.

Build direct-download outputs without Store credentials when independent distribution is a
requirement. Decide explicitly how updates and data behave when channels coexist or change.
Shared application code does not establish shared physical state or compatible credentials.
For MSIX, check the declared runtime/trust model and applicable Windows data behavior rather
than assuming that every packaged app is virtualized [M2].

Select packaging after examining the application. Reusing a verified executable may be a good
option; another framework may require a different layout or build. Record the reason and the
verification contract instead of forcing SchemaCraft's packaging recipe onto every project.

## 3. Define signing and artifact provenance per channel

For each output, identify who signs it, how the customer establishes trust, and who handles
updates and certificate renewal. Keep provider credentials in the appropriate secret store,
outside product code and public configuration.

Microsoft re-signs MSIX/AppX packages during Store publication after certification; their Store
submission does not require purchasing a CA-trusted certificate. For EXE/MSI Store submissions,
Microsoft does not re-sign the installer: the publisher must Authenticode-sign it with a valid
code-signing certificate before submission. Store signing does not provide a reusable
certificate for direct downloads [M1]. Verify the requirements for external distribution and
the chosen signing service separately.

Record the chain from source commit to build, signing, packaging, publication and delivery.
For every transformation retain the version, tool version, input/output identity and hashes.
Signing can change file bytes: compare hashes at the correct stage. Require byte identity only
where the declared transformation promises it. Also verify signature trust, expected publisher
and package identity where applicable; a checksum alone does not establish authenticity.

Published artifacts are immutable. A product correction produces a new version; preserve
earlier artifacts and evidence. Preparing a package does not submit or publish it.

Define recovery before releasing: retain previous artifacts, preserve update identity, and
check the channel's version ordering and data-migration compatibility. Reoffering an older
Store package to new customers does not downgrade users who already received the faulty
version; those installations need a suitable higher-version fix [M1]. Do not promise a rollback
that the channel or the saved data format cannot support.

## 4. Turn architectural decisions into executable checks

Choose checks that match the actual repository and channel contract. Candidate assertions are:

- A direct-download build succeeds without Store-specific secrets or configuration.
- Product modules cannot import distribution tooling; required integrations stay behind their
  documented interfaces. Use the stack's dependency/import checks rather than guessed layers.
- Production packaging rejects missing identity, inconsistent versions and unsupported inputs.
- The final package inventory contains the declared files and no secrets or development data.
- A package that promises unchanged payload preserves its expected file hashes after extraction.
- CI reports which checks ran and fails on violated contracts.

Select tools and thresholds from the application, not this guide. Documentation or a skill can
describe a boundary; only implemented checks can enforce its automatable parts. Keep runtime
and human acceptance separate from static validation.

For each protected rule, record its owning decision, implementing check/command, failure
condition and CI job (or manual owner). Mark a proposed check as not implemented until it
actually enforces the rule. A green job that never selected the relevant check is not evidence
that the rule passed.

## 5. Build a proportionate acceptance plan

Classify what changed before selecting tests:

| Change | Verification focus |
|---|---|
| First release or application/payload change | Changed product risks, delivered artifact, activation and the applicable update path |
| Packaging, identity, signing, runtime or capability change | Trust, installation, permissions and state behavior, even if product source is unchanged |
| Listing-only change with unchanged artifacts | Saved metadata, submission identity and public content; justify reuse of binary evidence |
| Internal documentation change | Document accuracy, links and consistency; channel execution only if a distribution contract also changes |

A listing-only change that adds a compatibility or feature claim needs evidence for that
claim. Do not manufacture a new package version or repeat installation solely because text or
images changed; record the listing revision/submission separately from the unchanged package.

Assign each scenario a reason: a current channel requirement, changed behavior, a known failure,
or a material risk. Select environments that can test that reason. A VM or clean Windows
installation is useful for isolation and prerequisite risks, but is not an automatic condition
for every release. Read the current channel requirements, including applicable certification
tools, before deciding what is mandatory [M1].

| Risk | Example observation |
|---|---|
| Installation and activation | Intended user scope and privileges; launch through the actual channel |
| Runtime dependencies | Startup with required runtimes; actionable behavior when a prerequisite is absent |
| Updates and persistence | A real previous-version update with synthetic settings, projects and remembered test credentials |
| Coexistence and removal | Supported channels coexist; uninstall preserves externally owned user files |
| Product behavior | Representative critical workflows under the packaged identity |
| Usability and localization | Supported window sizes, scaling, keyboard use, languages and themes |
| Privacy and support | Defined diagnostic contents, retention, consent and sharing behavior |

Prepare opaque backups and isolate existing user preferences/profiles before a maintainer's
test session. Use synthetic files and disposable accounts. Confirm process exit before
restoration, verify integrity and retain recovery material. Identify actual packaged data
locations; protecting only the unpackaged path may leave state unprotected.

An isolated fresh-profile launch does not prove upgrade preservation. An SQL login does not
prove Windows authentication. Installing a development package does not prove Store delivery.
Use similarly narrow claims for other applications.

Record each scenario as passed, failed, not run, not applicable with rationale, or explicitly
deferred. A project-level deferral requires the maintainer's decision, risk and follow-up;
it cannot waive a Store requirement. Reuse prior evidence only with a documented applicability
argument. An identical build is not enough when identity, environment or state changed.

## 6. Prepare the listing and submission

Keep descriptions, privacy/support/license URLs, reviewer instructions and release notes in
versioned source. Match package languages and listing locales. Capture real supported
features with synthetic data, check captions and cropping, and use current Store image rules
instead of permanent hard-coded limits [M3].

Explain required privileges/capabilities accurately and within the portal's current limits.
If essential features need external services or accounts, arrange an authorized, disposable
review path. Never expose production access or put credentials in public listing text [M4].

Read saved fields back after reopening the page; entering text or selecting files is not proof
of persistence. On portal failure, preserve the draft and error, make bounded attempts based on
new evidence, then escalate. Distinguish optional metadata from information reviewers need to
exercise the product. Skipping optional notes requires a recorded decision and a viable review
path; it is not safe merely because a field is labeled optional [M4].

If a required field or essential reviewer access/instructions cannot be saved or provided
through an authorized, functional alternative, mark submission preparation blocked. Record
the missing prerequisite, error/evidence, next action and owner; resolve and verify that
prerequisite before sending the submission.

Confirm the chosen audience, price, markets and publication timing. A manual publication hold
is available for MSIX submissions [M4]; it is a choice, not a universal requirement. Apply user
authorization and the client's action policies to submission, publication, account, payment and
certificate operations. Resolve required confirmations against a concrete prepared result.

## 7. Verify publication and customer delivery separately

Maintain separate observations for package prepared, uploaded/validated, submitted, certified,
ready to publish, publishing, published, publicly discoverable and delivered version. These
are evidence milestones, not promises about the exact portal labels for every application.

After the approved publication action:

1. Record the portal's completed publication state and the exact submission/package version.
2. Open the public listing outside the publisher session; confirm the intended audience can
   reach the product and acquisition action. Check the relevant locale/market and new content.
3. For a first release or changed deliverable, obtain or update through the actual customer
   route. Verify the installed version, expected
   identity and signing origin, and compare payload hashes where the contract permits.
4. Exercise the real-app workflows selected for the changed risks using the agreed state
   protection. Record delivery, startup and persistence as distinct results. For listing-only
   changes, reuse applicable artifact/runtime evidence with its identity and rationale instead
   of automatically requiring a new download, installation or app session.
5. If a regional listing remains stale, record that scope and time without claiming every
   locale is updated. Do not infer a new-version delivery from a pre-existing public link.

Schedule later checks only when requested. A published release record is a dated observation,
not a live status monitor.

## Release record and completion criteria

Each application/version keeps its own record with: decision references, source commit, artifact
versions and hashes, signing/packaging chain, environments, executed checks and evidence,
failures and deferrals, submission/publication events, public readbacks and installed-version
proof. Keep historical observations intact and label corrections or superseding evidence.
Protect non-public evidence separately and use sanitized summaries in shared documentation.

The preparation is ready for review when the chosen channels remain independently usable,
applicable required checks pass, material exceptions are explicit, privacy/licensing/listing
inputs are reviewed, and remaining external actions have clear ownership. Publication and
customer delivery are complete only to the extent demonstrated by their own observations.

## Reuse and maintenance

The skill first inspects the new project, selects its phase and relevant reference sections,
and reuses the project's evidence. Its evaluation cases cover different stacks, an existing
release, listing-only work and a blocked portal flow. Written cases alone are not passed tests.

This file is the single canonical guide. Repository playbook links point here; the complete
skill folder carries the guide and optional historical case. An installed copy does not need
a neighboring repository, a SchemaCraft checkout or private publication records.

Review volatile requirements before each submission. Record source URL, review date and the
relevant format/channel. Revisit this guide after a new incident, a changed channel contract
or a discovered gap; do not turn one product's workaround into a universal rule.

## Official references

Reviewed on 2026-10-28. The citations establish platform behavior; the workflow and proposed
checks above are recommendations, not a claim that another application passed them.

- **M1:** [Microsoft Store package and signing requirements](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msix/app-package-requirements).
- **M2:** [Packaged desktop app behavior](https://learn.microsoft.com/en-us/windows/msix/desktop/desktop-to-uwp-behind-the-scenes).
- **M3:** [Store screenshots and images](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msix/screenshots-and-images).
- **M4:** [Submission options, reviewer information and publication holds](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msix/manage-submission-options).
- **M5:** [Microsoft Store policies, including financial transactions and account types](https://learn.microsoft.com/en-us/windows/apps/publish/store-policies).

## Document history

| Date | Version | Change |
|---|---|---|
| 2026-10-28 | 0.1.0 draft | Initial cross-framework guide, separate SchemaCraft case and future-skill boundary. |
| 2026-10-28 | 0.1.1 draft | Clarify change-scoped verification, essential-review blockers, EXE/MSI signing, recovery, entitlements and enforceable checks. |
| 2026-10-28 | 0.1.2 draft | Relocate the canonical guide into the standalone skill package; preserve repository forwarding links. |
