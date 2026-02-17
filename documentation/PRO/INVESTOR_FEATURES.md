# Altair — Advanced Investor Features 📈🔬

This document expands Altair beyond personal budgeting to serve **retail investors** and **serious/professional investors**. Features are organized by user tier.

---

## User Tier System

| Tier | Profile | Key Needs |
|------|---------|-----------|
| 🟢 **Casual** | Salaried, beginner, saving goals | Basic portfolio view, tax calculator, goal tracker |
| 🟡 **Retail Investor** | Active stock market participant, SIPs, MFs | Detailed P&L, sector analysis, dividend tracking, watchlists |
| 🔴 **Pro Investor / HNI** | Serious trader, high-net-worth individual | Advanced analytics, risk metrics, multi-currency, tax harvesting, benchmarks |

> **Implementation Note**: The `UserProfile` will have an `investor_tier` field. The UI dynamically shows/hides advanced modules based on tier. All tiers share the same codebase — no separate apps needed.

---

## 1. 📊 Advanced Portfolio Analytics *(Retail + Pro)*

### 1.1 Performance Metrics Dashboard
Features beyond simple P&L:

| Metric | What It Shows | Tier |
|--------|---------------|------|
| **XIRR** (Extended IRR) | True annualized return accounting for irregular cash flows | 🟡 Retail |
| **CAGR** | Compound Annual Growth Rate for each holding | 🟡 Retail |
| **Absolute Return** | Total % gain/loss since purchase | 🟡 Retail |
| **Sharpe Ratio** | Risk-adjusted return (returns per unit of risk) | 🔴 Pro |
| **Sortino Ratio** | Like Sharpe but only penalizes downside volatility | 🔴 Pro |
| **Alpha** | Excess return vs. benchmark (e.g., NIFTY 50) | 🔴 Pro |
| **Beta** | How volatile the portfolio is vs. the market | 🔴 Pro |
| **Max Drawdown** | Largest peak-to-trough decline | 🔴 Pro |
| **Volatility (Std Dev)** | How much returns swing day-to-day | 🔴 Pro |
| **Treynor Ratio** | Excess return per unit of systematic risk | 🔴 Pro |

### 1.2 Benchmark Comparison
- Compare portfolio performance against indices:
  - NIFTY 50, SENSEX, NIFTY Bank, NIFTY IT, S&P 500.
- Overlay chart: Portfolio line vs. Benchmark line over same time period.
- Table: "Your Return" vs. "NIFTY Return" vs. "FD Return" for the same period.

### 1.3 Sector & Industry Breakdown
- **Treemap visualization**: Portfolio weight by sector, colored by performance.
- **Concentration alerts**: Warning when >25% in a single sector or >10% in a single stock.
- **Sector rotation insight**: Which sectors are overweight/underweight vs. index.

---

## 2. 📉 Risk Management *(Pro)*

### 2.1 Risk Score Dashboard
- Overall portfolio **risk score** (1–100) based on:
  - Asset diversification
  - Sector concentration
  - Volatility
  - Correlation between holdings
- Visual meter: Green (Low Risk) → Yellow → Red (High Risk).

### 2.2 Correlation Matrix
- Heatmap showing correlation between all held assets.
- Helps identify if holdings are too correlated (no real diversification).
- Example: If Reliance and ONGC are 0.85 correlated → alert.

### 2.3 Stress Testing *(Scenario Analysis)*
- "What if" scenarios:
  - Market crashes 20% → What happens to my portfolio?
  - Interest rates rise 1% → Bond impact?
  - Sector-specific crash (IT -30%) → My exposure?
- Uses historical crash data (2008, COVID 2020) as reference.

### 2.4 Drawdown Analysis
- Chart showing every peak-to-trough decline in portfolio history.
- Table: Drawdown date, magnitude, recovery time.
- Current drawdown vs. max drawdown indicator.

---

## 3. 📈 Advanced Trading Tools *(Retail + Pro)*

### 3.1 Multi-Lot Tracking (FIFO / Specific Lot)
- When selling, choose which lot to sell:
  - **FIFO**: First In, First Out (default for tax).
  - **Specific Lot**: Choose highest-cost lot (for tax harvesting).
  - **LIFO**: Last In, First Out.
- Each buy transaction becomes a separate "lot" with its own cost basis.
- Essential for accurate capital gains calculations.

### 3.2 SIP Tracker & Analyzer
- Track all SIPs (Systematic Investment Plans) across mutual funds.
- Monthly SIP calendar: What's due this month, total outflow.
- XIRR for each SIP vs. lump-sum comparison.
- SIP step-up calculator: "If I increase SIP by 10% annually, what's the impact?"

### 3.3 Dividend Management
- **Dividend Calendar**: Upcoming ex-dates and payment dates for held stocks.
- **Dividend Yield Analysis**: Yield on cost vs. current yield.
- **Dividend Growth Rate**: Year-over-year growth of dividends per stock.
- **Annual Dividend Income**: Total + projected for current FY.
- **DRIP Tracking**: Dividends reinvested vs. withdrawn.

### 3.4 Multi-Currency Support *(Pro)*
- Holdings in different currencies (INR, USD, EUR, etc.).
- Auto-conversion at current exchange rates.
- Forex gain/loss calculation on foreign holdings.
- Base currency toggle: "Show everything in INR" / "Show in USD".

### 3.5 Derivatives Tracker *(Pro / Future)*
- Track Options positions: Calls, Puts, strike price, expiry.
- Track Futures positions: Lot size, margin required.
- Greeks display: Delta, Gamma, Theta, Vega.
- P&L on expiry simulation.

---

## 4. 🏦 Advanced Tax Features *(Retail + Pro)*

### 4.1 Tax Loss Harvesting
- Identify holdings currently at a loss.
- Suggest selling to book losses → offset against gains.
- Show potential tax saved.
- **Wash sale alert**: Flag if repurchased within 30 days.

### 4.2 Multi-Year Tax History
- Tax summary across financial years (FY 2023-24, 2024-25, 2025-26).
- Compare tax paid year-over-year.
- Trend chart: Tax liability over time.

### 4.3 Advance Tax Calculator *(Pro)*
- For investors with income beyond salary (capital gains, dividends).
- Calculates quarterly advance tax installment schedule.
- Due dates: Jun 15, Sep 15, Dec 15, Mar 15.
- Interest on late payment calculator (234B/234C).

### 4.4 Comprehensive Capital Gains Report
- Grandfathered gains (equity purchased before Jan 31, 2018).
- Separate treatment for: Listed equity, Unlisted equity, Debt MFs, Property, Gold.
- STT-paid vs. Non-STT implications.
- Export-ready format for filing ITR.

---

## 5. 📊 Advanced Reporting *(Retail + Pro)*

### 5.1 Customizable Dashboards
- Users can add/remove/reorder dashboard widgets.
- Available widgets: Net Worth, Asset Allocation, Returns Chart, Recent Txns, Top Gainers, Top Losers, Dividend Income, Goals, Risk Score.
- Drag-and-drop layout (Alpine.js-powered).

### 5.2 P&L Statement (Detailed)
- Realized P&L: From completed sell transactions.
- Unrealized P&L: Current holdings vs. buy price.
- Fee-adjusted returns: Deducting all brokerage, STT, GST, stamp duty.
- Daily / Weekly / Monthly / Yearly views.
- Filterable by: Account, Asset Type, Sector, Date Range.

### 5.3 Portfolio Reports (Export)
| Report | Format | Contents |
|--------|--------|----------|
| Holdings Report | PDF / CSV | All assets with current values |
| Transaction Statement | PDF / CSV | Full transaction history |
| Capital Gains Statement | PDF | STCG + LTCG breakdown for ITR |
| Dividend Statement | PDF / CSV | All dividends received in FY |
| Tax Summary | PDF | Complete tax estimation + regime comparison |
| Performance Report | PDF | Returns, benchmarks, risk metrics |

### 5.4 Alerts & Notifications *(Retail + Pro)*
| Alert Type | Description | Tier |
|------------|-------------|------|
| Price Alert | Asset reaches target buy/sell price | 🟡 Retail |
| Portfolio Drift | Allocation drifts >5% from target | 🔴 Pro |
| Goal Deadline | Goal target date is approaching | 🟢 Casual |
| Dividend Alert | Upcoming ex-dividend date for held stocks | 🟡 Retail |
| Tax Deadline | Advance tax installment due date | 🔴 Pro |
| Concentration Warning | Single asset exceeds 10% of portfolio | 🔴 Pro |
| Drawdown Alert | Portfolio drops >10% from peak | 🔴 Pro |

---

## 6. 🤖 AI Advisor Enhancements *(Pro / Future)*

### 6.1 Portfolio Rebalancing Suggestions
- Define target allocation (e.g., 60% Equity, 20% Debt, 10% Gold, 10% Cash).
- System calculates current drift and suggests trades to rebalance.
- "Buy ₹50K of Gold ETF, Sell ₹30K of IT stocks" — actionable suggestions.

### 6.2 Investment Style Analysis
- Classify user as: Growth, Value, Balanced, Aggressive, Conservative.
- Based on actual holdings, not just a questionnaire.
- Suggest adjustments based on age, risk tolerance, and market conditions.

### 6.3 Peer Comparison *(Anonymized)*
- "Your portfolio returned 18% this year. Average Altair user returned 14%."
- Ranking percentile: "You're in the top 20% of investors on this platform."
- Completely anonymized — no personal data shared.

### 6.4 Smart Tax Planning
- AI-driven year-end tax planning:
  - "Book losses worth ₹50K before March 31 to offset ₹1.2L STCG."
  - "Invest ₹20K more in ELSS to max out 80C."
  - "Switch to New Regime — it saves ₹18K for your profile."

---

## 7. Feature Matrix Summary

| Feature | 🟢 Casual | 🟡 Retail | 🔴 Pro |
|---------|-----------|-----------|--------|
| Basic Portfolio View | ✅ | ✅ | ✅ |
| Asset Allocation Pie | ✅ | ✅ | ✅ |
| Simple P&L | ✅ | ✅ | ✅ |
| Tax Calculator | ✅ | ✅ | ✅ |
| Goal Tracking | ✅ | ✅ | ✅ |
| XIRR / CAGR | ❌ | ✅ | ✅ |
| Sector Analytics | ❌ | ✅ | ✅ |
| Dividend Dashboard | ❌ | ✅ | ✅ |
| SIP Analyzer | ❌ | ✅ | ✅ |
| Watchlist with Alerts | ❌ | ✅ | ✅ |
| Transaction Filters & Export | ❌ | ✅ | ✅ |
| Benchmark Comparison | ❌ | ❌ | ✅ |
| Risk Score & Correlation | ❌ | ❌ | ✅ |
| Sharpe / Alpha / Beta | ❌ | ❌ | ✅ |
| Stress Testing | ❌ | ❌ | ✅ |
| Tax Harvesting | ❌ | ❌ | ✅ |
| Multi-Lot Tracking | ❌ | ❌ | ✅ |
| Multi-Currency | ❌ | ❌ | ✅ |
| Custom Dashboards | ❌ | ❌ | ✅ |
| Advance Tax Calculator | ❌ | ❌ | ✅ |
| AI Rebalancing | ❌ | ❌ | ✅ |
| Derivatives Tracker | ❌ | ❌ | 🔮 Future |

