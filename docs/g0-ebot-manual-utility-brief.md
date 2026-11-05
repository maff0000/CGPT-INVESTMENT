# G0-EBOT-001 — GrokBot build brief: manually invoked E-Bot v0.1
**Authorised scope:** 2026-11-05 (Europe/London) | **Delivery status:** brief only, NOT yet built or connected. **Project priority:** manual G0 data validation before research automation.

**Naming/status update — 2026-11-05:** The correct project name is **E-Bot** (not E_Bot/E_BOT). The user reports **GrokBot's build is IN PROGRESS**, with a report expected when complete. The build, its tests and any Massive connection have **not yet been independently verified**. Historical file paths and the proposed `e_bot` CLI command remain unchanged until the implementer confirms the actual interface.

## Task for GrokBot — paste this as the build instruction

You are GrokBot, the bounded **implementer** of a small private tool named **E-Bot**.

### Objective
Build a minimal **human-invoked, read-only market-data task runner** so a human operator can give E-Bot narrowly scoped prompts and have it execute predefined Massive market-data validation checks. This is **G0 test tooling**, NOT the autonomous equity discovery or investing platform. **No autonomous running, trading, stock picks or scheduled jobs.**

### Read-only authoritative research reference
First review the latest GitHub main of **maff0000/CGPT-INVESTMENT**, starting with:
- README.md; AGENTS.md; CURRENT-STATE.md
- docs/g0-massive-onboarding.md; docs/g0-price-tolerance-and-provider-trial.md
- research/validation/g0_massive_readonly_probe.py
- docs/research-process-validation-charter.md; docs/macro-aware-equity-review.md
- docs/g0-data-integrity-and-valuation-rules.md
- This brief at docs/g0-ebot-manual-utility-brief.md.

Treat the public repository as **read-only documentation/source reference**, never as a place to store the E-Bot program, market-data extracts, API tokens or future private investment records. You may reuse the existing, bounded Python probe **after reviewing its behaviour and tests**, rather than duplicating it. Check current HEAD before using any quoted rules.

### Build location and resource restrictions
Inspect the currently approved development workspace for any pre-existing E-Bot project. If found, report what exists and preserve it. If absent, create a dedicated **private/local, nonproduction E-Bot workspace** that the operator can inspect; do not assume authority to SSH to production, create new remote GitHub repositories or deploy services. Keep code and config isolated from FOUNDRY, ForgeV2, trading execution hosts and the public CGPT-INVESTMENT repo. Use minimal standard-library Python and a simple CLI. No Docker, UI, message bus, database, orchestration framework, new cloud service or generic AI-agent platform in v0.1.

### v0.1 task interface
Provide an explicit, human-invoked command/task interface:
- `e_bot help` — list exactly allowed tasks and display operational constraints.
- `e_bot run massive-smoke --session 2026-11-04 --from-date 2025-08-01` — one-shot, read-only Massive connectivity and EOD-history test.
- `e_bot prompt "Check Massive connectivity and 260+ daily bars for XOM, LIN, EQIX, SPY as at 2026-11-04"` — map the bounded prompt to that **same allowlisted task** and display the interpreted task before execution. Unsupported, ambiguous, malicious or unrecognised prompts must **reject without any external call**.

You may adjust CLI spelling for implementation simplicity, but supply equivalent concrete invocations and test each. A flexible natural-language AI interpreter is **not required** at v0.1; a deterministic allowlisted phrase/intent parser is preferable. **NEVER** let free-text prompts become shell commands, arbitrary Python, URLs, file paths, modifications or an unbounded request generator.

### Allowed Massive tests only
1. One read-only **US grouped-daily OHLCV** request for an explicitly supplied **completed, accessible historical trading session** (US Eastern market calendar), no current-day data under Basic.
2. Four read-only historical daily range requests for `XOM`, `LIN`, `EQIX`, `SPY` covering at least **260 completed sessions**, if plan permits.
3. Validate responses: API status, requested/returned session, symbol identity, count of daily records, duplicate timestamps, missing and malformed OHLCV, ordering, and returned source adjustment convention. Distinguish provider 401, 403, 429 and other problems; never silently retry 403 or 429 in a loop.
4. Return a **compact redacted summary** with source date, UTC retrieval timestamp, per-symbol bar count, earliest/latest returned session, validation issues and PASS/HOLD/FAIL. Do not print raw bars, full market-wide responses, keys, request URLs containing keys or vendor data licensed for private use only.
5. **Do not claim** current Finviz A/B/C pass, exact chart/breakout pattern, 10/40 contraction success, final company valuations, approved investments or live market access unless a separate authorised task actually verifies them. G0 stays OPEN.
6. For future independent price reconciliation, retain the documented **same USD instrument/session/adjustment `<= $1.00 PRICE_OK, > $1.00 PRICE_CHECK`** rule; signal/pivot straddle is separate **SIGNAL_AMBIGUOUS**. With only one vendor tested, report `SECOND_SOURCE_NOT_TESTED`, never fabricate a comparison.

### Massive access and security
- **Do not request the API key in this GrokBot conversation**, prompts, GitHub, issues, tests or logs. After code passes offline tests, the human operator will enter/configure the key locally on the chosen test host using a **hidden terminal prompt** or an existing protected local secrets facility. No credentials embedded in source or persisted to public repo, output or task history. If using a local secret file for repeated manual runs, restrict it to the operating user (0600), outside repository; do not access or echo it in agent-readable output.
- Use Massive's documented REST API over HTTPS. The verified source in the reference repository uses `https://api.massive.com`, `Authorization: Bearer`, grouped daily and ticker custom bar routes; verify endpoints/entitlements against official docs before use.
- Respect the Basic tier's **5 requests per minute**. The specified successful smoke run uses a maximum of **five GET calls**, once per manual invocation. If interrupted partway through, do not auto-repeat a complete five-call batch; report what was completed. Basic only serves the session after **midnight America/New_York the following day**.
- Split-adjusted bars are not automatically dividend-adjusted. Record these conventions. Respect data supplier rights: avoid uploading vendor raw feeds to any AI model or redistributing in the public GitHub project. Human must verify individual vs business/commercial licence suitability before progressing beyond private trial.
- Do not add broker APIs, trading capability, position/account records, private portfolio settings or key-bearing outgoing messages.

### Tests and acceptance before real key
- All tests **offline** using fixtures/mock HTTP responses; never depend on or expose a real API key in unit tests.
- Prove help/allowed prompt/unknown prompt rejection and absence of arbitrary shell execution.
- Verify endpoint path/session construction, local time/Basic plan cutoff, 5-calls-per-minute cap, timeout/error handling, partial result reporting and accidental secret redaction.
- Test exactly **$1.00 = PRICE_OK** and **$1.01 = PRICE_CHECK** (for a future two-source task), with a pivot straddle separately blocking breakout confirmation.
- Confirm that a missing key returns a safe **SETUP_NEEDED** state, not a crash or dummy success.
- Deliver documented local launch commands, safe key setup instructions and a clear operator procedure.

### STOP / report back
Stop after code exists and **offline tests pass**. **Do not activate a real API key or make Massive requests until the human operator explicitly installs the key and asks for the test.**

Report:
- Actual E-Bot workspace and repository/branch/commit if created, paths changed, tests run and precise PASS/FAIL results.
- Manual `e_bot` commands and how the user safely supplies the key.
- Confirm no scheduler, daemon, broker integration, unreviewed external libraries, API calls, secrets, public-repo changes, other-host modifications or autonomous investment logic.
- Open risks: provider commercial licence, chart data quality, rate limits and what still blocks G0.
- No tasks beyond these requirements. Escalate architectural ambiguity rather than broadening scope.

**Acceptance rule:** An explicit bounded manual EOD probe that refuses unsafe/unrecognised prompts, keeps keys isolated, produces valid summary diagnostics and passes offline tests. A finished agent framework, a dashboard or investment suggestion is **not** an acceptable substitute for the small v0.1 deliverable.

## Authority distinction
The project still blocks automated equity research, stock recommendations, autonomous trade execution and broker code until G0–G3. This brief explicitly permits **only creation and offline testing of the narrow manual G0 provider-data tool**, with a later separate human invocation for a credentialed live data test. It does not permit new data rights or final canonical source selection.

## State
**GrokBot dispatch pending.** No E-Bot workspace, tested implementation, account configuration or authenticated Massive response verified by this public document. The operator will separately provide local API access. Recovery: read this brief, [Massive onboarding](g0-massive-onboarding.md), [G0 source tolerance](g0-price-tolerance-and-provider-trial.md) and [CURRENT-STATE](../CURRENT-STATE.md).
