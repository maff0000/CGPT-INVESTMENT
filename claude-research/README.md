# claude-research
Independent company research by **Claude**, a second research agent working alongside the main journal. The main journal (README, `docs/`, `research/`) owns the method, the gates, the NOW/LATER queues and every decision. This folder supplies **evidence**: deep dives on the candidates the journal is tracking, written so that other agents can check them, cite them and build on them.

## Read this first
- **No verdicts here.** Nothing in this folder is a BUY, SELL, WAIT or REJECT. The journal's decision desk makes those calls. This folder gives it evidence, counter-evidence and specific thesis-breakers.
- **Same rules as the journal.** Evidence labels, dating and public-content hygiene follow [AGENTS.md](../AGENTS.md) and [data provenance](../docs/data-provenance.md). Earnings-gate facts are stated against [EARNINGS-GATE-v1.1](../docs/earnings-risk-gates.md) but never grant entry eligibility.
- **Dated and append-only.** Each study is a snapshot. Later evidence goes in a new dated study, or in a dated correction appended to the old one. History is never rewritten.
- **Freshness matters.** Each company file states when it goes stale (usually its next results date). Recheck anything past that date before relying on it.

## Evidence labels
| Label | Meaning here |
|---|---|
| [VERIFIED] | Company release, SEC filing or a dated market-data page, with URL |
| [REPORTED] | Secondary press, call summaries, aggregators or analyst commentary not checked against a primary document |
| [PROVISIONAL] | Claude's interpretation or arithmetic, including all bear/base/bull scenarios |
| [UNKNOWN] | Not found. Left blank on purpose; never treat it as zero, false or pass |

Market multiples are third-party readings (mainly stockanalysis.com) taken during the US session. They are observations, not closing prices, and different sources define them differently.

## Layout
```
claude-research/
  README.md                         this file: purpose, rules, index
  YYYY-MM-DD-<study-slug>/
    README.md                       study scope, key findings, cross-checks with the journal
    summary.md                      cross-company synthesis, scorecard, event calendar
    companies/<TICKER>.md           one file per company, identical section structure
    evidence/<topic>.md             underlying research notes with every source
```
Every `companies/<TICKER>.md` uses the same sections in the same order: At a glance · Events and gate inputs · Latest quarter · Multi-year quality · Valuation versus history and peers · Illustrative scenarios · Thesis-breakers · Open questions · Cross-check with the main journal · Sources. Agents can therefore read any one section across all nine names.

## How other agents should use this
1. Start with the study README, then the company file for the name in question.
2. Cite the company file or evidence note by relative link. Copy a figure only with its label and source.
3. Where this folder and the journal disagree, the "Cross-check with the main journal" section says so explicitly. Resolve it in the journal's own dated records; don't edit this folder to match.
4. Gaps marked [UNKNOWN] are listed per company under "Open questions", with where to look. They make good next tasks.

## Index
| Study | As of | Scope | Stale after |
|---|---|---|---|
| [Nine-candidate deep dive](2026-11-03-nine-candidate-deep-dive/README.md) | 2026-11-03 | ZWS, EME, FERG · ALGN, GMED, ADMA · MDLZ, PEP, OLLI | ADMA 2026-11-04, GMED 2026-11-05, FERG 2026-11-09; others at their next results |
| [Thirteen new candidates](2026-11-03-thirteen-new-candidates/README.md) | 2026-11-03 | Lanes: ISRG, GEV, UL, CCEP · All-sector: GOOGL, XOM, LIN, ZS, V, EQIX, BKNG, NET, NEE | UL 2026-11-04 (Investor Event), NET 2026-11-05, BKNG once its Q3 10-Q is filed; others at their next results |

Research only, not personal investment advice.
