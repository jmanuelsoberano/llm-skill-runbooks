# SchemaCraft: Windows distribution lessons

Status: historical case, draft 0.1.2. Written on 2026-10-28 from the recorded 1.2/1.3 work.

## Scope and evidence limits

This case supports the [general distribution guide](distribution-guide.md).
It is an example, not a packaging specification for another application. It is not a new test
of SchemaCraft, a live Store status report, or approval to publish another product.

Source material includes SchemaCraft's public
[ADR-045](https://github.com/jmanuelsoberano/schemacraft/blob/v1.3.0/docs/architecture.md#adr-045-distribution-channels-wrap-the-same-application-and-remain-independent),
[Store preparation history](https://github.com/jmanuelsoberano/schemacraft/blob/v1.3.0/docs/microsoft-store.md),
[release checklist](https://github.com/jmanuelsoberano/schemacraft/blob/v1.3.0/docs/release-checklist.md),
[GitHub 1.3.0 release](https://github.com/jmanuelsoberano/schemacraft/releases/tag/v1.3.0)
and the maintainer's local publication records. Public documents include historical pending
states; the dated observations below distinguish later outcomes. Local evidence remains outside
this repository; it includes artifact inventories, portal readbacks and isolated app reports.
No account details, certificate material, private state or machine-specific evidence paths are
copied here. A reviewer with only the public links cannot independently reproduce every local
publication observation.

## Evidence index

These stable case identifiers map to existing local report basenames for authorized
maintainers. They are not public download links and do not make private evidence portable.
All timestamps below are UTC and correspond to 2026-10-24 in America/Mexico_City.

| ID | Local report and observation time | Supported scope |
|---|---|---|
| SC-130-PUB | `store-publication-confirmed.json`, 2026-10-25 03:21:15Z | Store submission publication completed |
| SC-130-DEL | `installed-version-readback.json`, 2026-10-25 03:13:56Z | Installed package identity, version, signing origin and executable hash |
| SC-130-APP | `app-ui-readback.json`, 2026-10-25 03:16:42Z; `restoration.json`, 03:16:59Z | Isolated About observation and state restoration |
| SC-130-EN | `store-public-english-readback.json`, 2026-10-25 03:21:15Z | Independent public English/US listing and ten matching captions |
| SC-130-ES | `store-public-spanish-readback.json`, 2026-10-25 03:22:33Z | Signed-in Spanish/Mexico observation of previous metadata |

## Recorded outcome on 2026-10-24

- Version 1.3.0 was published on GitHub and Microsoft Store. The Store-installed package
  reported 1.3.0.0, a Store signature and the same package family as the earlier 1.2 package
  (SC-130-PUB, SC-130-DEL).
- The installed executable matched the verified release payload. An isolated launch from the
  installed package displayed About Version 1.3.0, then exited; preferences and WebView state
  were restored with the recorded preference integrity check (SC-130-DEL, SC-130-APP).
- A separate browser offered Sign in and Download on the public English/US listing, with the
  new PostgreSQL description and ten captions matching the prepared gallery (SC-130-EN).
- Twenty screenshots were saved in the submission, ten per language. The last Spanish/Mexico
  readback still showed earlier metadata and one image. Public visibility of all twenty was
  not established by that observation (SC-130-ES). This is not a claim about its state on
  2026-10-28.
- The Store version transition was observed, but its automatic/manual delivery mechanism was
  not established. The isolated About test did not verify preservation of projects, connections
  or remembered credentials across an update.
- Additional Windows/environment tests were explicitly deferred. Those decisions did not turn
  unexecuted tests into passes or establish universal exceptions for later products/releases.

## Transferable lessons and application-specific choices

| Experience | Transferable rule | SchemaCraft-specific choice |
|---|---|---|
| Store support was added alongside direct distribution. | Keep channel configuration and publication outside common product behavior; enforce the boundary where possible. | A Rust core and React/Tauri host; portable and NSIS outputs; a separate MSIX packager. |
| Packaging consumed a verified release executable. | Preserve artifact provenance and verify each declared transformation. | The MSIX adapter retained the executable bytes from the published GitHub release. Another stack may need a different build/layout. |
| Store and external signing were separate concerns. | Define who signs each artifact and how trust is verified; do not embed provider dependency in the product. | Microsoft signed the Store package; external signing remained an independent integration. |
| Packaged execution introduced separate state risks. | Verify the real installed context, privileges, runtime and data behavior. Shared code is insufficient evidence. | MSIX identity, WebView2, AppData and Windows Credential Manager were relevant to this app. |
| Some tests were expensive or unavailable. | Select checks by requirements and changed risks; record bounded exceptions and their remaining coverage gaps. | The maintainer deferred named Windows/NSIS environment checks for this release. |
| Portal fields failed to save or exceeded limits. | Keep copy locally, read back saved values, and distinguish required review information from optional metadata. | Reviewer notes failed to save; an overlong capability explanation was shortened and verified. |
| Customer-visible metadata lagged publication. | Verify publication, public audience, locale-specific listing and delivered binary independently. | English/US new content was verified while Spanish/Mexico still showed prior metadata. |

## Verification discipline worth retaining

One external smoke test initially failed because its version-label matcher interpreted adjacent
rendered text incorrectly. The original failure was kept; a corrected assertion was run in a
separate report. The product binary was not changed merely to satisfy the mistaken assertion.
For future work, test the user-visible contract and investigate the cause before changing the
application or weakening an oracle.

An additional browser run was unavailable. Earlier geometry evidence was reused only after a
recorded comparison established relevant page equivalence except a footer timestamp. That was
reported as reused evidence, not a fresh browser run, and did not establish installation or
Store-update behavior. Future reuse needs its own applicability argument and must respect any
tool/security restrictions.

## Applying the case to another application

Start with the new product's goals and current architecture. Do not copy SchemaCraft's package
identity, minimum Windows version, project format, runtime choice, capability declarations,
licensing decision, test counts or exact build scripts as defaults.

An Electron application may need a different runtime/package layout; a .NET application may
choose a different deployment mode. Those are decisions to investigate, not conclusions of
this case. The reusable outcomes are explicit channel contracts, traceable artifacts,
proportionate verification, protected test state and narrowly stated evidence.

## Document history

| Date | Version | Change |
|---|---|---|
| 2026-10-28 | 0.1.0 draft | Initial sanitized case; dated observations and remaining gaps kept separate. |
| 2026-10-28 | 0.1.1 draft | Add stable evidence identifiers and dated report mapping without private paths or contents. |
| 2026-10-28 | 0.1.2 draft | Move the case into the standalone skill reference folder; keep historical evidence optional. |
