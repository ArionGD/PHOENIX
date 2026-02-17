# Altair — Advanced Investor Wireframes 🖼️

Wireframe layouts for the Retail and Pro investor dashboards, showing advanced features that extend beyond the casual user interface.

---

## 1. Retail Investor Dashboard — Overview (`/dashboard/`)

The Retail tier enhances the basic dashboard with performance metrics, SIP tracking, and sector breakdowns.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  RETAIL 🟡   [Avatar ▼]     │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   QUICK STATS ROW                                             │
│            │   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  Overview ●│   │Net Worth │ │ XIRR     │ │ Today    │ │ Dividend │        │
│  Portfolio │   │₹24.8L    │ │ 18.4%    │ │ +₹3,200  │ │ ₹42K/yr  │        │
│  Holdings  │   │↑ 12.3%   │ │ vs 14.2% │ │ +0.13%   │ │ Yield 2% │        │
│  SIP Track │   └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│  Dividends │                                                                │
│  Transact. │   PORTFOLIO VALUE vs NIFTY 50 BENCHMARK                       │
│  Watchlist │   ┌────────────────────────────────────────────────────────┐   │
│  Tax       │   │  ── Portfolio (Blue)    ── NIFTY 50 (Gray)            │   │
│  Goals     │   │                              ╱─·                       │   │
│  Reports   │   │                           ╱·´    ·─── (benchmark)     │   │
│  Settings  │   │              ╱──·───·──╱·´   ╱·´                      │   │
│            │   │           ╱·´           ╱·──´                          │   │
│            │   │  ·───·──·´        ·──·´                                │   │
│            │   │ Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep            │   │
│            │   │                                                        │   │
│            │   │  [ 1M ] [ 3M ] [ 6M ] [  1Y  ] [ 3Y ] [ ALL ]        │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   ┌──────────────────────┐  ┌─────────────────────────────┐   │
│            │   │  SECTOR BREAKDOWN    │  │  TOP GAINERS & LOSERS       │   │
│            │   │                      │  │                             │   │
│            │   │  ┌─────────────────┐ │  │  GAINERS                    │   │
│            │   │  │ ██ Tech    35%  │ │  │  RELIANCE  ████████  +28%  │   │
│            │   │  │ ██ Fin     22%  │ │  │  TCS       ██████    +18%  │   │
│            │   │  │ ██ Pharma  15%  │ │  │  HDFC MF   █████     +15%  │   │
│            │   │  │ ██ Energy  12%  │ │  │                             │   │
│            │   │  │ ██ FMCG     8%  │ │  │  LOSERS                    │   │
│            │   │  │ ██ Other    8%  │ │  │  INFY      ████████   -8%  │   │
│            │   │  └─────────────────┘ │  │  BPCL      █████      -5%  │   │
│            │   │                      │  │  VEDL      ████       -4%  │   │
│            │   │  ⚠ Concentration:    │  │                             │   │
│            │   │  Tech > 30%!         │  │                             │   │
│            │   └──────────────────────┘  └─────────────────────────────┘   │
│            │                                                                │
│            │   ┌────────────────────────────────────────────────────────┐   │
│            │   │  UPCOMING DIVIDEND CALENDAR                            │   │
│            │   │  ┌────────┬──────────┬──────────┬──────────┐          │   │
│            │   │  │ Asset  │ Ex-Date  │ Amount   │ Yield    │          │   │
│            │   │  ├────────┼──────────┼──────────┼──────────┤          │   │
│            │   │  │ ITC    │ Mar 10   │ ₹6.50/sh │ 3.2%    │          │   │
│            │   │  │ HDFCB  │ Mar 22   │ ₹19/sh   │ 1.1%    │          │   │
│            │   │  │ TCS    │ Apr 05   │ ₹12/sh   │ 0.8%    │          │   │
│            │   │  └────────┴──────────┴──────────┴──────────┘          │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Sidebar adds: SIP Track, Dividends, Watchlist, Reports.
- XIRR stat card shows comparison vs. NIFTY benchmark.
- Time-range selector on charts (`1M`, `3M`, `1Y`, `ALL`).
- Concentration warning banner when sector > 30%.

---

## 2. Pro Investor Dashboard — Command Center (`/dashboard/`)

The Pro tier transforms the dashboard into a full analytics terminal.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                             🔔  PRO 🔴   [⚙ Customize] [Avatar]  │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  NAV       │   PERFORMANCE METRICS ROW                                     │
│            │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────┐│
│  Command ● │   │NetWorth │ │ XIRR    │ │ Sharpe  │ │ Alpha   │ │ MaxDD  ││
│  Analytics │   │₹1.2Cr   │ │ 22.3%   │ │ 1.42    │ │ +4.1%   │ │ -12.8% ││
│  Risk      │   │↑ 18.7%  │ │vs Nifty │ │ Good    │ │Beating  │ │ Recov. ││
│  Holdings  │   └─────────┘ └─────────┘ └─────────┘ └─────────┘ └────────┘│
│  Lots      │                                                                │
│  SIP       │   ┌───────────────────────────┐ ┌────────────────────────────┐│
│  Dividends │   │  PORTFOLIO vs BENCHMARKS  │ │  RISK SCORE                ││
│  Watchlist │   │                           │ │                            ││
│  Transact. │   │         ·─·  Portfolio    │ │     ┌──────────────┐       ││
│  Tax +     │   │        · ╱ ·              │ │     │              │       ││
│  Reports   │   │    ·──·╱    ·             │ │     │    62 / 100  │       ││
│  Alerts    │   │   · ╱       ·─ NIFTY50    │ │     │    MODERATE  │       ││
│  Settings  │   │  ·╱    ·──·──·            │ │     │              │       ││
│            │   │ ·╱  ·──·      ·─ S&P500   │ │     └──────────────┘       ││
│            │   │  Jan  Mar  May  Jul  Sep  │ │                            ││
│            │   │                           │ │  Diversification   ████ 7  ││
│            │   │ [1M][3M][6M][1Y][3Y][MAX] │ │  Concentration     ███░ 5 ││
│            │   └───────────────────────────┘ │  Volatility        ████ 7  ││
│            │                                  │  Correlation       ██░░ 4 ││
│            │                                  └────────────────────────────┘│
│            │                                                                │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │  HOLDINGS HEATMAP (by Sector & Performance)           │   │
│            │   │                                                       │   │
│            │   │  ┌──────────────────────┐ ┌────────────┐ ┌─────────┐ │   │
│            │   │  │                      │ │            │ │         │ │   │
│            │   │  │   TECHNOLOGY  35%    │ │ FINANCE    │ │  PHARMA │ │   │
│            │   │  │   🟢 +22.4%         │ │   22%      │ │  15%    │ │   │
│            │   │  │                      │ │ 🟢 +14.1% │ │ 🔴-3.2%│ │   │
│            │   │  │  Reliance  TCS  Infy │ │ HDFC  SBI │ │  Sun    │ │   │
│            │   │  └──────────────────────┘ └────────────┘ └─────────┘ │   │
│            │   │  ┌──────────┐ ┌────────┐ ┌─────────────────┐         │   │
│            │   │  │  ENERGY  │ │  FMCG  │ │  GOLD + CRYPTO  │         │   │
│            │   │  │  12%     │ │   8%   │ │      8%          │         │   │
│            │   │  │ 🟡+2.1% │ │🟢+8.5% │ │  🟢 +15.3%      │         │   │
│            │   │  └──────────┘ └────────┘ └─────────────────┘         │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   ┌──────────────────────┐  ┌─────────────────────────────┐   │
│            │   │  P&L SUMMARY (FY)    │  │  ACTIVE ALERTS              │   │
│            │   │                      │  │                             │   │
│            │   │  Realized   +₹3.8L   │  │  ⚠ INFY hit target ₹1450  │   │
│            │   │  Unrealized +₹8.2L   │  │  ⚠ Tech sector > 30%      │   │
│            │   │  Dividends  +₹42K    │  │  🔴 Drawdown alert: -8.2%  │   │
│            │   │  Fees        -₹18K   │  │  ✅ Advance tax due Sep 15 │   │
│            │   │  ─────────────────── │  │  🟡 Goal "Home" 60% done  │   │
│            │   │  Net P&L    +₹12.4L  │  │                             │   │
│            │   └──────────────────────┘  └─────────────────────────────┘   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- 5 metric cards with Sharpe, Alpha, Max Drawdown.
- Risk Score gauge with sub-scores.
- Treemap chart for sector + performance visualization.
- P&L breakdown: Realized + Unrealized + Dividends - Fees.
- Live alerts panel.

---

## 3. Advanced Holdings & Lot Tracking (`/portfolio/holdings/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  PRO 🔴   [Avatar ▼]        │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   Holdings                  [ Filter ▼ ] [ Export CSV ] 📊    │
│            │                                                                │
│  ...       │   ┌───────────────────────────────────────────────────────┐   │
│  Holdings● │   │ Asset     Ticker   Qty  Avg₹   Curr₹  P/L     XIRR  │   │
│  ...       │   ├───────────────────────────────────────────────────────┤   │
│            │   │ Reliance  RELI    150  2400   2720  🟢+13.3  🟢22%  │   │
│            │   │  ├ Lot 1: 50 @ ₹2200 (Jan 24)    🟢 +23.6%         │   │
│            │   │  ├ Lot 2: 50 @ ₹2500 (May 24)    🟢 +8.8%          │   │
│            │   │  └ Lot 3: 50 @ ₹2500 (Nov 24)    🟢 +8.8%          │   │
│            │   │                                                       │   │
│            │   │ TCS       TCS      80  3800   4100  🟢+7.9   🟢14%  │   │
│            │   │  ├ Lot 1: 30 @ ₹3600 (Feb 24)    🟢 +13.8%         │   │
│            │   │  └ Lot 2: 50 @ ₹3920 (Aug 24)    🟢 +4.5%          │   │
│            │   │                                                       │   │
│            │   │ Infosys   INFY    200  1500   1390  🔴-7.3   🔴-10% │   │
│            │   │  └ Lot 1: 200 @ ₹1500 (Mar 24)   🔴 -7.3%          │   │
│            │   │  └─ 🏷️ Tax Harvest Candidate: Book ₹22K loss        │   │
│            │   │                                                       │   │
│            │   │ HDFC Gold  GOLD    500   58     64   🟢+10.3  🟢12%  │   │
│            │   │ Bitcoin    BTC    0.15   42L    52L   🟢+23.8  🟢34%  │   │
│            │   │                                                       │   │
│            │   │ Sort by: [Name] [Value ▼] [Return] [XIRR] [Sector]   │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   SELL MODAL (when "Sell" clicked on a holding)               │
│            │   ┌────────────────────────────────────────────┐              │
│            │   │  Sell Reliance Industries                  │              │
│            │   │                                            │              │
│            │   │  Sell Method:                              │              │
│            │   │  (●) FIFO  ( ) Specific Lot  ( ) LIFO     │              │
│            │   │                                            │              │
│            │   │  Quantity:  ┌──────────┐  / 150 available  │              │
│            │   │             │ 50       │                    │              │
│            │   │             └──────────┘                    │              │
│            │   │  Price:     ┌──────────┐                   │              │
│            │   │             │ ₹2720    │                    │              │
│            │   │             └──────────┘                    │              │
│            │   │                                            │              │
│            │   │  ── Tax Impact Preview ──                  │              │
│            │   │  Lot 1 (FIFO): 50 × (2720 - 2200) = +₹26K │              │
│            │   │  Holding: 11 months → STCG @ 15%           │              │
│            │   │  Estimated Tax: ₹3,900                     │              │
│            │   │                                            │              │
│            │   │  [ Cancel ]              [ Confirm Sell ]  │              │
│            │   └────────────────────────────────────────────┘              │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Expandable rows show individual lots per asset.
- Tax harvest candidates are auto-flagged (holdings at loss).
- Sell modal shows FIFO/Specific Lot/LIFO choice.
- Tax impact preview before confirming a sale.

---

## 4. Risk Analysis Dashboard (`/dashboard/risk/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  PRO 🔴   [Avatar ▼]        │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   Risk Analysis                                     [Export]  │
│            │                                                                │
│  ...       │   RISK OVERVIEW                                               │
│  Risk    ● │   ┌──────────────────────────────────────────────────────┐    │
│  ...       │   │                                                      │    │
│            │   │  Overall Risk Score      RISK BREAKDOWN              │    │
│            │   │                                                      │    │
│            │   │     ╭─────────╮          Diversification   ████████░ │    │
│            │   │    ╱           ╲         Concentration     ██████░░░ │    │
│            │   │   │     62      │        Volatility        ███████░░ │    │
│            │   │   │   MODERATE  │        Liquidity         █████████ │    │
│            │   │    ╲           ╱         Correlation       █████░░░░ │    │
│            │   │     ╰─────────╯         Drawdown Risk     ██████░░░ │    │
│            │   │                                                      │    │
│            │   └──────────────────────────────────────────────────────┘    │
│            │                                                                │
│            │   ASSET CORRELATION MATRIX                                     │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │         RELI   TCS   INFY   HDFC   BTC   GOLD       │   │
│            │   │  RELI    1.0   0.65  0.58   0.42   0.12  0.08       │   │
│            │   │  TCS    0.65   1.0   ■0.88  0.38   0.15  0.05       │   │
│            │   │  INFY   0.58  ■0.88  1.0    0.35   0.10  0.03       │   │
│            │   │  HDFC   0.42   0.38  0.35   1.0    0.08  0.12       │   │
│            │   │  BTC    0.12   0.15  0.10   0.08   1.0   0.25       │   │
│            │   │  GOLD   0.08   0.05  0.03   0.12   0.25  1.0        │   │
│            │   │                                                       │   │
│            │   │  ■ = High Correlation (>0.80) — Reduces diversification │ │
│            │   │  Legend: 🟢 <0.3  🟡 0.3-0.6  🟠 0.6-0.8  🔴 >0.8   │ │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   STRESS TESTING — SCENARIO ANALYSIS                          │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │  Scenario              Portfolio Impact    Recovery   │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │  Market Crash (-20%)   -₹4.96L  (-20.0%)  ~8 months │   │
│            │   │  2008-style (-52%)     -₹12.9L  (-52.0%)  ~24 months│   │
│            │   │  COVID Crash (-38%)    -₹9.4L   (-38.0%)  ~6 months │   │
│            │   │  IT Sector Crash(-30%) -₹2.8L   (-11.2%)  ~5 months │   │
│            │   │  Rate Hike (+2%)       -₹1.2L   (-4.8%)   ~3 months │   │
│            │   │  Crypto Crash (-60%)   -₹0.9L   (-3.6%)   ~12 months│   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   DRAWDOWN HISTORY                                            │
│            │   ┌────────────────────────────────────────────────────────┐  │
│            │   │  0% ──────·─────·──·───────────·──────────────────── │  │
│            │   │          ╲    ╱         ╲    ╱                        │  │
│            │   │  -5%      ╲  ╱           ╲  ╱                        │  │
│            │   │           ╲╱             ╲╱                           │  │
│            │   │  -10%    ·               ·                            │  │
│            │   │         (-8.2%)        (-12.8% MAX)                   │  │
│            │   │  -15% ──────────────────────────────────────────────  │  │
│            │   │   Mar 24   Jun 24   Sep 24   Dec 24   Mar 25         │  │
│            │   └────────────────────────────────────────────────────────┘  │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. SIP Tracker & Analyzer (`/dashboard/sip/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  RETAIL 🟡   [Avatar ▼]     │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   SIP Tracker                              [ + Add SIP ]      │
│            │                                                                │
│  ...       │   MONTHLY OVERVIEW — February 2026                            │
│  SIP     ● │   ┌──────────────────────────────────────────────────────┐    │
│  ...       │   │  Total Monthly SIP:  ₹45,000                        │    │
│            │   │  SIPs This Month:     4 / 4 completed  ✅            │    │
│            │   │  Total SIP Invested:  ₹12,60,000 (since start)      │    │
│            │   │  Current Value:       ₹15,30,000                    │    │
│            │   │  SIP Returns (XIRR):  16.8%                         │    │
│            │   └──────────────────────────────────────────────────────┘    │
│            │                                                                │
│            │   ACTIVE SIPs                                                  │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │ Fund Name        Monthly  Start     XIRR    Status   │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │ HDFC Flexi Cap   ₹15,000  Jan '24   🟢18.2%  Active │   │
│            │   │ Axis Bluechip    ₹10,000  Mar '24   🟢14.5%  Active │   │
│            │   │ PPFAS Flexi      ₹10,000  Jun '24   🟢20.1%  Active │   │
│            │   │ Nippon Gold ETF  ₹ 5,000  Sep '24   🟢12.3%  Active │   │
│            │   │ Quant Small Cap  ₹ 5,000  Nov '24   🟡 8.1%  Active │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   SIP vs LUMP SUM COMPARISON                                  │
│            │   ┌────────────────────────────────────────────────────────┐  │
│            │   │  For HDFC Flexi Cap (₹15K/mo since Jan '24):          │  │
│            │   │                                                        │  │
│            │   │  Strategy       Invested    Value     Return           │  │
│            │   │  SIP            ₹3,90,000   ₹4,61,000   +18.2%        │  │
│            │   │  Lump Sum       ₹3,90,000   ₹4,45,000   +14.1%        │  │
│            │   │                                                        │  │
│            │   │  ✅ SIP outperformed Lump Sum by ₹16,000 (+4.1%)      │  │
│            │   └────────────────────────────────────────────────────────┘  │
│            │                                                                │
│            │   SIP STEP-UP CALCULATOR                                      │
│            │   ┌────────────────────────────────────────────────────────┐  │
│            │   │  Current SIP: ₹15,000/mo    Step-Up: [ 10 ]% annually │  │
│            │   │  Expected Return: [ 12 ]%   Duration: [ 20 ] years    │  │
│            │   │                                                        │  │
│            │   │  Without Step-Up:   ₹1.49 Cr                          │  │
│            │   │  With 10% Step-Up:  ₹3.04 Cr   (🟢 +₹1.55 Cr more!) │  │
│            │   │                                                        │  │
│            │   │  [ Calculate ]                                         │  │
│            │   └────────────────────────────────────────────────────────┘  │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Advanced Tax — Tax Harvesting & Advance Tax (`/tax/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  PRO 🔴   [Avatar ▼]        │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   Tax Center                                                  │
│            │                                                                │
│  ...       │   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  Tax +   ● │   │ STCG     │ │ LTCG     │ │ Tax Saved│ │ Advance  │       │
│  ...       │   │ ₹52,000  │ │ ₹1,80,000│ │ ₹22,000  │ │ Due: Sep │       │
│            │   │ Tax: ₹7.8K│ │Tax:₹8,000│ │via Harv. │ │ ₹42,500  │       │
│            │   └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│            │                                                                │
│            │   TAX LOSS HARVESTING OPPORTUNITIES                           │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │  Holdings currently at a LOSS that can be sold to     │   │
│            │   │  offset gains and reduce your tax bill:               │   │
│            │   │                                                       │   │
│            │   │  Asset    Loss     Gain Offset  Tax Saved   Action    │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │  INFY    -₹22,000  vs STCG     ₹3,300     [Harvest] │   │
│            │   │  BPCL    -₹8,500   vs STCG     ₹1,275     [Harvest] │   │
│            │   │  VEDL    -₹5,200   vs STCG     ₹780       [Harvest] │   │
│            │   │                                                       │   │
│            │   │  ⚠ Total Potential Tax Saved: ₹5,355                 │   │
│            │   │  ⚠ Wash Sale Rule: Don't repurchase within 30 days   │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   ADVANCE TAX SCHEDULE (FY 2025-26)                           │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │                                                       │   │
│            │   │  Quarter      Due Date    % Due    Amount    Status   │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │  Q1           Jun 15      15%      ₹12,750  ✅ Paid  │   │
│            │   │  Q2           Sep 15      45%      ₹38,250  ⏳ Due   │   │
│            │   │  Q3           Dec 15      75%      ₹63,750  ⬜ Future│   │
│            │   │  Q4           Mar 15      100%     ₹85,000  ⬜ Future│   │
│            │   │                                                       │   │
│            │   │  💡 Interest on late payment (234C): ₹0 (on track)   │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   MULTI-YEAR TAX TREND                                        │
│            │   ┌────────────────────────────────────────────────────────┐  │
│            │   │  ₹1L │          ┌───┐                                  │  │
│            │   │      │  ┌───┐   │   │  ┌───┐                           │  │
│            │   │  ₹50K│  │'23│   │'24│  │'25│                           │  │
│            │   │      │  │₹62K   │₹85K  │₹78K  ← Lower (harvesting!)  │  │
│            │   │  ₹0  │  └───┘   └───┘  └───┘                           │  │
│            │   │       FY 23-24  FY 24-25  FY 25-26 (est.)             │  │
│            │   └────────────────────────────────────────────────────────┘  │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Reports & Export Center (`/dashboard/reports/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                    🔔  PRO 🔴   [Avatar ▼]        │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   Reports Center                                              │
│            │                                                                │
│  ...       │   GENERATE REPORT                                             │
│  Reports ● │   ┌───────────────────────────────────────────────────────┐   │
│  ...       │   │                                                       │   │
│            │   │  ┌───────────────┐  ┌───────────────┐  ┌────────────┐│   │
│            │   │  │ 📄 Holdings   │  │ 📊 Performance│  │ 💰 P&L     ││   │
│            │   │  │   Report      │  │    Report      │  │  Statement ││   │
│            │   │  │               │  │                │  │            ││   │
│            │   │  │ All assets,   │  │ Returns, XIRR, │  │ Realized + ││   │
│            │   │  │ values, lots  │  │ benchmarks,    │  │ Unrealized ││   │
│            │   │  │               │  │ risk metrics   │  │ per asset  ││   │
│            │   │  │ [PDF]  [CSV]  │  │ [PDF]  [CSV]   │  │ [PDF][CSV] ││   │
│            │   │  └───────────────┘  └───────────────┘  └────────────┘│   │
│            │   │                                                       │   │
│            │   │  ┌───────────────┐  ┌───────────────┐  ┌────────────┐│   │
│            │   │  │ 🏦 Capital    │  │ 💸 Dividend   │  │ 📈 Tax     ││   │
│            │   │  │   Gains       │  │   Statement   │  │  Summary   ││   │
│            │   │  │               │  │                │  │            ││   │
│            │   │  │ STCG + LTCG   │  │ All dividends  │  │ Full tax   ││   │
│            │   │  │ ITR-ready     │  │ by asset, date │  │ breakdown  ││   │
│            │   │  │               │  │                │  │ + regime   ││   │
│            │   │  │ [PDF]  [CSV]  │  │ [PDF]  [CSV]   │  │ [PDF][CSV] ││   │
│            │   │  └───────────────┘  └───────────────┘  └────────────┘│   │
│            │   │                                                       │   │
│            │   │  Date Range:  ┌──────────┐  to  ┌──────────┐         │   │
│            │   │               │ 01-04-25 │      │ 31-03-26 │         │   │
│            │   │               └──────────┘      └──────────┘         │   │
│            │   │                                                       │   │
│            │   │  Financial Year: [ FY 2025-26 ▼ ]                    │   │
│            │   │                                                       │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   RECENT DOWNLOADS                                            │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │  📄 Holdings_Report_Feb2026.pdf      3 hrs ago  [↓]  │   │
│            │   │  📊 Capital_Gains_FY2025-26.csv      2 days ago [↓]  │   │
│            │   │  📈 Tax_Summary_FY2025-26.pdf        5 days ago [↓]  │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Sidebar Comparison Across Tiers

| Sidebar Item | 🟢 Casual | 🟡 Retail | 🔴 Pro |
|-------------|-----------|-----------|--------|
| Overview | ✅ | ✅ | ✅ (as "Command Center") |
| Portfolio | ✅ | ✅ | ✅ |
| Holdings | — | — | ✅ (with Lot tracking) |
| SIP Tracker | — | ✅ | ✅ |
| Dividends | — | ✅ | ✅ |
| Analytics | — | — | ✅ (Sharpe, Alpha, Beta) |
| Risk | — | — | ✅ (Score, Correlation, Stress) |
| Transactions | ✅ | ✅ | ✅ |
| Watchlist | — | ✅ | ✅ (with Alerts) |
| Tax | ✅ | ✅ | ✅ (+ Harvesting, Advance) |
| Goals | ✅ | ✅ | ✅ |
| Reports | — | — | ✅ (PDF/CSV Export) |
| Alerts | — | — | ✅ |
| Settings | ✅ | ✅ | ✅ |

