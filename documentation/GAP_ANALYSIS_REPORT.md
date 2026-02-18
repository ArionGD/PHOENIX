## ✅ What We Have (Current State — Updated 18 Feb)

| Feature | Status |
|---|---|
| User Login / Logout | ✅ Done |
| Dashboard Overview (Net Worth, P/L) | ✅ Done |
| Portfolio — Add Stock / ETF / **Crypto** / **Index Funds** | ✅ Done |
| Live Price Scraping (Google Finance / Yahoo / Crypto) | ✅ Done |
| **Initial Investment tracking** (Historical Cost Basis) | ✅ Done |
| **Asset Allocation Doughnut Chart** (Live Distribution) | ✅ Done |
| Performance Timeline (Monthly / Yearly Views) | ✅ Done |
| Symbol ↔ Name Auto-fill in Modal | ✅ Done |
| 5-Minute Auto-Refresh Cooldown | ✅ Done |

---

## 🚨 Priority 1 — The Final Core Gaps (Next Steps)

With the multi-asset foundation now complete (Stocks, ETFs, Crypto, Index Funds), we must focus on the "Ledge & Intel" layer.

### 1.1 — Transaction Ledger & Average Buy Price
**Goal:** Instead of just "current holdings", we need a full `Transaction` history (Buy/Sell/Dividend).
- **Step 1:** Implement "Weighted Average Cost" logic. If a user adds NIFTYBEES twice at different prices, ALTAIR must auto-calculate the single average buy price.
- **Step 2:** Create a "Ledger" view where users can see exactly when and where they deployed capital.

### 1.2 — 'Book Profit/Loss' (Sell & Clear Position)
**Goal:** Enable users to close positions and track actual earnings.
- **Step 3:** Add a "Checkmark" or "Dollar" icon in the holdings table for **"Book Profit/Loss"**.
- **Step 4:** When clicked, it should allow the user to enter the "Sell Price" and "Sell Quantity".
- **Step 5:** Move that profit to a "Realized Profit" bucket and reduce the holding quantity (or delete if 100% sold).

### 1.3 — Expand Asset List & Smart Validation
**Goal:** Move beyond the curated list.
- **Step 6:** Allow users to type *any* valid NSE symbol. Validation occurs by attempting a live price fetch.
- **Step 7:** Add support for Mutual Funds (Direct/Regular) via manual entry or NAV scraping.

To move ALTAIR from a "Tracker" to an "Advisor", we need these high-intelligence features.

### 0.1 — Drawdown & Risk Analysis
- **Target:** Calculate the "Max Drawdown" (the biggest drop from peak value) for each asset.
- **Impact:** Shows the user if their portfolio is too volatile.

### 0.2 — AI-Driven Rebalancing Alerts
- **Target:** If "Crypto" grows to 50% of the portfolio (exceeding a user-set limit), ALTAIR should flash a "High Risk Alert" and suggest rebalancing.
- **Action:** Add "Target Allocation" settings for each asset class.

### 0.3 — Portfolio "Stress Test"
- **Target:** Simulate the portfolio performance against 100 historical "Crash" scenarios (2008, 2020, 1929).
- **Action:** Integrate a simulation engine that uses historical volatility to project 10-year growth probabilities.

---

## 🌟 Priority 3 — Market-Leading Features (Competitor Benchmarking)

To compete with apps like **Groww**, **Indmoney**, and **Empower**, we need these industry-standard "Pro" features:

### 3.1 — Benchmarking (Portfolio vs. Market)
- **Feature:** A chart overlaying your Portfolio growth against the **Nifty 50** or **S&P 500**.
- **Value:** Tells the user if they are actually beating the market or if they'd be better off in a simple index fund.

### 3.2 — Sector & Industry Exposure
- **Feature:** A breakdown of holdings by sector (e.g., IT: 40%, Banking: 20%, Pharma: 10%).
- **Value:** Prevents over-concentration in a single industry.

### 3.3 — Tax-Loss Harvesting Alerts
- **Feature:** ALTAIR identifies assets currently in loss that can be sold to "offset" realized capital gains, reducing the user's tax bill.
- **Value:** A major "Wealth Management" feature that saves users actual money.

### 3.4 — Hidden Fee & Expense Ratio Tracker
- **Feature:** Analyze ETFs and Mutual Funds to show the "Expense Ratio".
- **Value:** Alerts users if they are losing too much money to fund management fees over 10-20 years.

### 3.5 — Family Portfolio (Multi-Account)
- **Feature:** Allow users to switch between "My Portfolio" and "Family Portfolio" (aggregation of spouse/children accounts).
- **Value:** High retention for long-term wealth builders.

### 3.6 — AI Market Explainer
- **Feature:** Use a LLM (like Gemini) to summarize *why* the portfolio is up/down today based on global news (e.g., "The Fed rate hike impacted your Tech holdings").

### 2.1 — Tax-Smart Analytics
- **Target:** Flag assets held for >1 year as "Long Term" (LTCG) and <1 year as "Short Term" (STCG) to show the tax impact of selling *before* the user clicks delete.

### 2.2 — Digital Gold & Fixed Assets
- **Target:** Add "Fixed Deposits" and "Digital Gold" as manual entry assets to complete the user's Total Net Worth picture.

---

## �️ Updated Roadmap & Build Order

```
Phase 1: Intel & History (Next)
  → 1.1 Transaction Ledger & Weighted Averaging
  → 1.2 Realized Profit Tracking
  → Edit/Delete functionality for all 4 asset types

Phase 2: Risk & Discipline (Soon)
  → 0.1 Drawdown Tracking (Volatility metrics)
  → 0.2 Target Allocation & Rebalancing Alerts
  → Search/Filter for Holdings

Phase 3: Sophistication (Horizon)
  → 0.3 Portfolio Stress Testing (Monte Carlo)
  → 2.1 Tax-Smart Flags (LTCG/STCG)
  → SIP Simulation for Index Funds

Phase 4: Platform Maturity
  → Manager Dashboard (Multi-user analytics)
  → Mobile Responsive Refactoring
  → Data Export (CSV/PDF for Tax filing)
```

---

## 📊 Summary Scorecard (Revision 2)

| Category | Current Score | Target Score |
|---|---|---|
| Core Portfolio Tracking | 9 / 10 | 10 / 10 |
| Transaction Management | 2 / 10 | 9 / 10 |
| Data Visualization | 7 / 10 | 10 / 10 |
| Financial Intelligence (Risk/Simulation) | 0 / 10 | 9 / 10 |
| Asset Coverage (Equity/Crypto/Index) | 8 / 10 | 10 / 10 |
| **Overall** | **26 / 50** | **48 / 50** |

*Report updated by Antigravity on 18 Feb 2026, following the successful integration of Multi-Asset support and Initial Investment tracking.*
