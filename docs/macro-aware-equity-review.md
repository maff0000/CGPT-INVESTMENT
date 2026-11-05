# MACRO-PROSPECTIVE-001 — In-time macro-aware equity research
**Adopted:** 2026-11-05 (Europe/London). **Status:** requirements for manual prospective validation, not a working trading system.

## Decision
**Forward-only observations and review are the primary validation method.** Conventional mechanical retrospective strategy backtesting is **deferred and OPTIONAL**, not a prerequisite or a substitute for current conditions. Retain historical price/valuation and company operating records **for context only**. Do not optimise current rules by hindsight or imply that a historical anecdote establishes predictive alpha.

A chart has no economic context in isolation. Each researched opportunity needs a *dated macro/regime evidence packet*, the sector/industry transmission mechanism, firm-specific economics and an explicit assessment of what is **already priced in**. **Observed market signals** come first; **interpretation** and **hypothesis** are different fields. Never translate an unverified geopolitical claim, a confident election prediction or today's headlines into a presumed price effect.

Crucially, prospective manual reviews also have limitations: a short run in one macro regime cannot establish a lasting edge. Preserve all no-signal days, failed trades that were never taken, rejected candidates and missed winners. Use independent reviewers and prospective future outcomes before any research-agent automation gate.

## Macro dashboard — minimum decision-time observations
| Pillar | Observable evidence to capture | Why it could matter | Interpretation guard |
|---|---|---|---|
| **Interest rates, yield curve and real yields** | US 2yr/10yr nominal yields, 10yr TIPS real yield, yield-curve slope, changes 1w/1m/3m; UK rates/FX only where exposure relevant | Discount rates, financing cost, refinancing and equity-duration sensitivity | Rising yields may reflect growth, inflation or fiscal risk; sign of effect **not fixed** |
| **Inflation and central banks** | Latest CPI/PCE and original release time, upcoming FOMC/BLS dates, policy expectations (market-implied if reliable), revisions | Demand, costs, margins, valuation, surprise risk | CPI "latest" must respect release vintage and availability; distinguish expectation vs outcome |
| **Energy and industrial commodities** | Brent/WTI level, 1w/1m trend, gas/copper and relevant inputs, inventories or outages with source | Energy producer margins vs airline/chemical costs; industrial capacity and project spend | A price spike can benefit one industry and damage another, and may already be reflected in equities |
| **Credit, liquidity and FX** | Investment-grade/high-yield spreads or reliable proxies, dollar index, volatility measures, funding availability | Balance-sheet distress, cyclicality, capital cost, FX translation | Credit spreads/volatility are regime clues, not guaranteed sell signals |
| **Growth, labour and consumption** | Latest employment and activity data, consumer spending, manufacturing/services surveys and publication timestamps | Cyclical demand, earnings revisions and policy response | Lagged/revised data do not establish current firm economics without corroboration |
| **Geopolitical and trade shocks** | Verified wars/conflicts, sanctions, supply-route disruption, tariffs, export restrictions, announced policy changes | Physical shortages, logistics, capex, security exposure and sector dispersion | Report only supported facts; label disputed assertions, duration unknown and alternate scenario |
| **Political/regulatory calendar** | Election dates and confirmed results, enacted vs proposed tax/trade/industrial policies, litigation, sector rules | Business model, cash flows, regulated returns, market uncertainty | **Election expectation ≠ enacted policy**; no assumed automatic bullish/bearish effect |
| **Physical capacity and shortages** | Semiconductors, grid transformers, power, labour, shipping, refined fuels, data-centre cooling and other industry-specific bottlenecks | Prices, project timing, competitive advantage, orders and margins | Source availability and resolution dates; shortage claims need evidence, not AI-sector narratives |
| **Market structure/leadership** | S&P 500 and relevant sector 1w/1m/3m, participation/breadth, concentration, realised volatility | Distinguish narrow rallies from broad participation and market resilience | Do not overfit a market-regime switch to a single indicator |

**Not all pillars require daily prose.** Standard daily brief = 4–8 material *changes* and their business effects; weekly full review refreshes the dashboard. Mark irrelevant/no material change instead of padding and prioritise exposures of live candidates. Avoid falsely precise numeric macro composite scores before validation.

### Stable primary reference locations
- [US Federal Reserve release calendar](https://www.federalreserve.gov/data/releaseschedule.htm) and [real TIPS/yield framework](https://www.federalreserve.gov/data/tips-yield-curve-and-inflation-compensation.htm).
- [US Bureau of Labor Statistics schedule](https://www.bls.gov/schedule/) for economic data announcements and [CPI calendar](https://www.bls.gov/schedule/news_release/cpi.htm).
- [US Energy Information Administration short-term energy outlook](https://www.eia.gov/outlooks/steo/) for oil, energy forecasts, supply disruptions and **forecast vintage**.
- [Federal Reserve Bank of St Louis FRED release calendar](https://fred.stlouisfed.org/releases/calendar) and [ALFRED vintage data documentation](https://fred.stlouisfed.org/docs/api/fred/alfred.html) for what was actually published or later revised.
- Sources for conflicts/policy must be issuer/government/official agency or cross-checked credible reporting; a search snippet is not independent confirmation. Recheck publication date, event date, report vintage and later correction. **No source here represents a locked live market quote.**

## The five-step causal test for each material macro factor
1. **Observation:** what happened and when, with value/unit, publication and retrieval time, verified source, expected versus actual (if available), and uncertainty.
2. **Transmission:** how could this alter *this company's* unit economics, revenue, margins, debt cost, capex or valuation, through which operating segment? Could it operate in the opposite direction?
3. **Exposure:** what proportion of business is genuinely exposed, with credible evidence and horizon (days/weeks vs quarters/years)? No generic "AI beneficiary" or "war stock" shortcut.
4. **Market expectations:** what is already expected or reflected in share price, earnings estimates, bond/commodity futures or peer moves? State unknown when difficult; don't imply a macro forecast is unpriced.
5. **Decision consequence:** **TAILWIND / HEADWIND / MIXED / IMMATERIAL / UNKNOWN**, conviction and evidence strength, scenario if wrong, monitoring trigger and how it affects valuation/entry decision. A macro tailwind alone NEVER overrides company fundamentals, event blackouts or portfolio downside.

## Event/regime journal — prospective, not hindsight
Before candidate committee review freeze a **timestamped macro snapshot**: rates/real rates, energy, credit/liquidity, FX, growth/inflation, material geopolitical/trade facts, upcoming verified risk calendar, sector leadership, observed vs forecast changes, and company-specific transmission. If **nothing material changed**, record NO CHANGE with source/cutoff. Don't keep rewriting a historical entry based on revised macro statistics; append a new observation.

Maintain company scenario cases (base/upside/downside). Example mechanisms:
- **Oil shock:** upstream producers may see higher realised prices; transportation and chemicals higher fuel/feedstock costs; demand destruction or hedging can offset either.
- **Yield shock:** highly valued long-duration equities can de-rate; leveraged real estate can face higher refinancing costs; insurers/banks may have offsetting asset yield and credit effects.
- **Trade conflict or physical bottleneck:** local suppliers may benefit from reshoring while import-dependent firms suffer; timing and contract terms determine whether margins change.
- **Election or major geopolitical shock:** record the announced/confirmed event; treat future government or military actions as *conditional scenarios*, not facts.

## G0–G4 proof alignment
- **G0 specification freeze:** include agreed dashboard fields, available sources, time-cuts, macro-to-sector mapping, relevance classification and exposure/expectations test. Preserve old Finviz A/B/C and chart-stage rules as a baseline. **Do not require a backtest**.
- **G1 manual reproducibility:** for each completed US session create the macro sheet **before** independent company decision. Blind second reviewer can challenge causal claims. Check >=95% evidence completeness and 100% hard event-gate compliance as provisional acceptance criteria, including macro review.
- **G2 prospective utility:** record after-decision 5/20/60-session behaviour of all candidates, plus sector/market baselines, costs and misses. Compare decisions *with* meaningful macro overlay vs a **predeclared macro-blind baseline using identical candidates**; both observed outcomes and false macro vetoes matter. This is a **forward-only** study, not retroactive parameter fitting.
- **G3 independent forward replication:** repeat in *additional future windows and differing observed regimes*, using a fresh/blind reviewer. A separate past-regime backtest is **NOT mandatory**, though historical episodes can be used to ask stress-test questions and identify unknowns.
- **G4 evidence-gated permission:** research automation remains BLOCKED until G0–G3 are accepted and a separate bounded permission is given. Do not interpret G1 manual agreement or a single successful trade as proof of future alpha.

## Learning objectives
Was the company economics assessment accurate? Was the macro catalyst material and anticipated or already priced in? Did an election/shock surprise change the thesis? Did we correctly distinguish macro noise from a genuine regime change? Would we have done better with **no macro adjustment**? Record failures equally with successes, keep counterfactuals and uncertainty, and never imply that a small sample has statistical significance.

Related: [validation charter](research-process-validation-charter.md), [prospective protocol](research-validation-protocol.md), [manual worksheet](../templates/manual-equity-validation-review.md), [decision](../research/decisions/2026-11-05-macro-aware-forward-validation.md).
