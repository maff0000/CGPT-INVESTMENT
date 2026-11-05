# G0-PROVIDER-001 — Massive onboarding and manual credential-free validation
**Later status — G0-EBOT-002 (2026-11-05):** A separate private E-Bot v0.1 implementation was independently accepted and an initial five-call market-data sample was **operator-reported successful**. This document preserves original onboarding/setup instructions, not current access status. [Dated acceptance](../research/decisions/2026-11-05-ebot-private-acceptance.md). D1 licence, D3 second-source and full G0 approval remain OPEN.
**Decision:** 2026-11-05 Europe/London | **Provider candidate:** Massive Stocks Basic for a **private manual G0 trial only** | **Connection status:** USER ACCOUNT/AUTH NOT VERIFIED, no live API test completed.

## What is and is not approved
- Massive is the **first provider for a controlled trial**, not yet the final licensed canonical feed. Start with **free Stocks Basic ($0/month)** if the account and permitted usage qualify; **no paid upgrade** is authorised by this project decision.
- No new agents, broker connectors, automatic scanning, unattended scripts or trading authority. A small one-shot [manual read-only smoke test](../research/validation/g0_massive_readonly_probe.py) is provided solely for D1–D4 provider acceptance.
- Provider account creation, API token issuance and acceptance of the vendor licence **require the account holder's explicit action**; they have not been completed through this chat. **NEVER put credentials in public GitHub, ChatGPT messages, screenshots or shell history.**
- Vendor licences: Massive [redistribution guidance](https://massive.com/knowledge-base/article/how-can-i-redistribute-massives-market-data) says an individual subscription covers own research; publishing price tables/charts or passing underlying data to anyone else normally requires separate commercial rights. Even derived signals can require clarification. The public repo should therefore store **only non-sensitive process decisions and metadata**, no Massive raw bars or price tables until written data rights verified. **Commercial hosted-agent use must be separately cleared with Massive.**

## Source-backed entitlements to check
| Feature | Basic according to provider | Limitation |
|---|---|---|
| US stock EOD market-wide OHLCV | Yes, [grouped daily](https://massive.com/docs/rest/stocks/aggregates/daily-market-summary), one request per completed day | **Prior trading day available after midnight US Eastern on next calendar day**, NOT at 16:00 ET same evening: [official timing](https://massive.com/knowledge-base/article/on-the-free-basic-plan-when-can-i-pull-the-previous-trading-days-data) |
| History | **2 years**, [Stocks pricing](https://massive.com/stocks) | Enough for ~260 completed days and SMA200; exact corporate-action coverage must be checked |
| Rate limit | **5 requests/minute** | One test run is 5 GETs; do not immediately repeat |
| Ticker OHLCV ranges | Yes, [custom stock bars](https://massive.com/docs/rest/stocks/aggregates/custom-bars) | API aggregates are **split-adjusted by default but NOT dividend-adjusted**: [official answer](https://massive.com/knowledge-base/article/is-massives-stock-data-adjusted-for-splits-or-dividends) |
| Company accounts and forward valuation metrics | **Not included in Basic** | Use issuer/SEC primary data and separately sourced analyst estimates for fundamental research |
| ChatGPT app/MCP option | Provider [ChatGPT OAuth setup](https://massive.com/docs/ai-tools/clients/chatgpt) | Optional. Not a substitute for point-in-time source archive; access/entitlements must first be verified |

## Account-holder setup (one-time)
1. Open [Massive Stocks signup](https://massive.com/stocks); choose **Stocks Basic / Free**. Review the individual-use terms for the actual planned private manual research.
2. Use [Massive dashboard API keys](https://massive.com/dashboard/keys) to generate/view a key **locally** after authenticating. API supports [Authorization: Bearer](https://massive.com/docs/rest) instead of a query-string key; bearer header avoids placing the token in URL history and proxy request logs.
3. On a trusted **private workstation** with Python 3, obtain the repository's [manual probe](../research/validation/g0_massive_readonly_probe.py). Run it in an interactive terminal, for a historical **completed** US session:
    python3 research/validation/g0_massive_readonly_probe.py --date 2026-11-04 --from-date 2025-08-01
4. Enter the API key at the **hidden prompt**. The probe makes at most 5 **read-only** calls: one grouped US-market daily request and historical 1-day bars for XOM, LIN, EQIX and SPY. It prints statuses/counts and time boundaries **only**; it does not save provider-derived price data or the key.
5. **Report only redacted/summary diagnostics**: HTTP success/failure, market grouped count, 260+ completed bars for each sample, dates, and any provider restrictions. Do not paste the key or any raw vendor data into GitHub or chat. A 401 signals bad/missing credentials; a 403 can mean plan entitlement or attempting current-day data on Basic; a 429 can mean >5/min.
6. Verify a second independent data source under its own rights. Then apply [G0-DATA-002](g0-price-tolerance-and-provider-trial.md): **absolute EOD close delta <=$1.00 PRICE_OK**, >$1 PRICE_CHECK; **pivot straddle** triggers separate SIGNAL_AMBIGUOUS; split, currency or trading-date mismatch triggers DATA_MISMATCH.

This probe is **a data availability/access smoke test**, not a calculation of SMA50/200, volume contraction, adjusted dividends, base validity or data-source commercial rights. Passing the probe cannot close G0.

## Security and operational requirements
- A dedicated **read-only research credential** if Massive supports per-key scoping; otherwise recognise the key is generic read entitlement and protect it by OS/user access control. No secrets in Git, issue trackers or chat.
- Do not commit a dot-env, shell history, curl URL with apiKey, or complete market-wide JSON responses. If a key is exposed, revoke it in the provider dashboard and create a new one.
- Run source validation locally only after accepting account terms. The probe consumes exactly 5 requests if successful. If other processes share a key/account quota, they may have used the rate limit already.
- Provider acceptance states: **SETUP NEEDED → ACCESS VERIFIED → DATA QUALITY VERIFIED → LICENCE APPROVED → CANONICAL ACCEPTED**. Current status is **SETUP NEEDED**; only pricing/API capability and public rules are VERIFIED from docs.
- As future design separates public research and private accounts, Massive should only be the OHLCV/market-data source. Financials, issuer earnings and macro inputs still need their existing vetted providers. Massive is **not a broker**.

## Next acceptance after user setup
**D1:** verify account entitlement and licence for private research, storage and any onward use. **D2:** successful real response for grouped Nov4 date. **D3:** compare vendor close/adjustment conventions using G0-DATA-002 rule. **D4:** verify 260+ bars and actual SMA/contraction calculations with manual charts. **D5:** contemporaneous Finviz A/B/C evidence. **D6:** independent source reconciliation signoff and G0 rule freeze. **G1 only after explicit G0 approval.**

Reference: [price tolerance and candidate provider plan](g0-price-tolerance-and-provider-trial.md), [G0 source governance](g0-data-integrity-and-valuation-rules.md), [decision](../research/decisions/2026-11-05-massive-onboarding-selection.md), [current status](../CURRENT-STATE.md).
