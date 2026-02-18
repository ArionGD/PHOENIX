# ALTAIR — Portfolio Management Gap Analysis Report 📊
**Date:** 18 February 2026  
**Prepared by:** Antigravity (AI Engineering Assistant)  
**Project Status:** Active Development

---

## 🔍 Executive Summary

ALTAIR currently has a solid foundation: user authentication, a live portfolio tracker for Stocks and ETFs, a real-time price scraper, and a performance chart with Monthly/Yearly views. However, compared to industry-standard portfolio management platforms like **Zerodha Kite**, **Groww**, and **ET Money**, there are significant gaps across data depth, user experience, and financial intelligence features.

This report categorizes every missing feature by priority and estimated complexity.

---

## ✅ What We Have (Current State)

| Feature | Status |
|---|---|
| User Login / Logout | ✅ Done |
| Role-based Access (User, Manager, Superuser) | ✅ Done |
| Dashboard Overview (Net Worth, P/L) | ✅ Done |
| Portfolio — Add Stock / ETF | ✅ Done |
| Separate Stock & ETF Sections | ✅ Done |
| Live Price Scraping (Google Finance) | ✅ Done |
| 5-Minute Auto-Refresh Cooldown | ✅ Done |
| Manual Refresh Button | ✅ Done |
| Monthly / Yearly Performance Chart | ✅ Done |
| Symbol ↔ Name Auto-fill in Modal | ✅ Done |

---

## 🚨 Priority 1 — Critical Gaps (Build These Next)

These are features that users expect from *any* portfolio tracker. Their absence makes the app feel incomplete.

### 1.1 — Transaction History & Ledger
**What's missing:** There is no way to record or view past buy/sell transactions. Currently, a holding is a single static entry.  
**Why it matters:** Users need to track when they bought, when they sold, and at what price. This is the backbone of any portfolio app.  
**What to build:**
- A `Transaction` model with fields: `holding`, `type` (Buy/Sell), `quantity`, `price`, `date`.
- A "Transactions" page listing all buys and sells in a table.
- Ability to "sell" a holding (reduce quantity or close position).

---

### 1.2 — Delete / Edit Holdings
**What's missing:** Once a holding is added, there is no way to edit the quantity/price or delete it from the UI.  
**Why it matters:** Users make mistakes. Without edit/delete, they are stuck with wrong data forever.  
**What to build:**
- An "Edit" button on each holding row that opens a pre-filled modal.
- A "Delete" button with a confirmation prompt.

---

### 1.3 — Asset Expansion (More Stocks & ETFs)
**What's missing:** The curated list has only 5 assets (3 stocks, 2 ETFs). This is far too restrictive.  
**Why it matters:** A user with a real portfolio cannot use this app if their stocks aren't listed.  
**What to build:**
- Expand `NSE_STOCKS` to include the top 50 NSE stocks (Nifty 50 list).
- Add a broader ETF list (NIFTYBEES, BANKBEES, JUNIORBEES, etc.).
- Or better: allow users to type any valid NSE symbol and validate it by attempting a live price fetch.

---

### 1.4 — Profit/Loss on Sell (Realized P/L)
**What's missing:** The app only shows "Unrealized P/L" (current value vs. buy price). There is no concept of "Realized P/L" (profit actually booked from a sale).  
**Why it matters:** Investors need to know what they've actually earned, not just what they're sitting on.  
**What to build:**
- Track `realized_profit_loss` on the `Transaction` model when a sell is recorded.
- Show a "Realized P/L" card on the dashboard.

---

## ⚠️ Priority 2 — Important Gaps (Build Soon)

These features significantly improve the quality and usefulness of the app.

### 2.1 — Tax Calculator Page
**What's missing:** The wireframe (`WIREFRAMES.md`) has a full Tax Calculator design, but it has not been implemented.  
**Why it matters:** Tax optimization is listed as a core feature of ALTAIR in the landing page copy. It's a major differentiator.  
**What to build:**
- Old vs. New Tax Regime comparison calculator.
- Input fields for: Gross Income, 80C, 80D, HRA deductions.
- Auto-calculate STCG (Short-Term Capital Gains Tax at 15%) and LTCG (Long-Term at 10%) from the transaction history.

---

### 2.2 — Goals / Financial Milestones Page
**What's missing:** The Goals page is fully designed in wireframes but not implemented.  
**Why it matters:** Goal tracking is a key engagement feature that keeps users returning to the app.  
**What to build:**
- A `Goal` model: `name`, `target_amount`, `saved_amount`, `deadline`, `priority`.
- Progress bars showing % completion.
- A "Top Goals" widget on the main dashboard.

---

### 2.3 — Asset Allocation Doughnut Chart
**What's missing:** The dashboard wireframe shows a Doughnut/Pie chart for asset allocation (Stocks %, ETFs %, etc.), but this is not implemented.  
**Why it matters:** A visual breakdown of allocation is one of the most-used features in portfolio apps. It gives users an instant snapshot of their risk exposure.  
**What to build:**
- A Chart.js Doughnut chart on the dashboard showing the % split between Stocks and ETFs.
- Color-coded segments (Indigo for Stocks, Emerald for ETFs).

---

### 2.4 — Portfolio Search & Filter
**What's missing:** There is no way to search or filter holdings on the portfolio page.  
**Why it matters:** As the portfolio grows, users need to quickly find a specific stock.  
**What to build:**
- A search input above the holdings table that filters rows in real-time using Alpine.js.
- Filter buttons: "All", "Profit", "Loss", "Stocks", "ETFs".

---

### 2.5 — Average Buy Price (Multiple Buys)
**What's missing:** If a user buys the same stock twice at different prices, the app creates two separate rows instead of averaging them.  
**Why it matters:** In real investing, users "average down" or "average up". The app should show a single row per symbol with a weighted average buy price.  
**What to build:**
- Logic to detect if a symbol already exists for the user.
- If it does, update the quantity and recalculate the weighted average purchase price.

---

## 💡 Priority 3 — Advanced Features (Future Roadmap)

These are "power user" features that would make ALTAIR competitive with professional tools.

### 3.1 — Dividend Tracking
Track dividends received from stocks and ETFs. Show total dividend income on the dashboard.

### 3.2 — SIP (Systematic Investment Plan) Simulator
Allow users to set up a recurring monthly investment amount for a stock/ETF and simulate the returns over time using the historical interpolation engine we already built.

### 3.3 — Portfolio Export (CSV / PDF)
Allow users to download their full portfolio and transaction history as a CSV or PDF report. This is essential for tax filing.

### 3.4 — Price Alerts / Notifications
Allow users to set a target price for a stock (e.g., "Alert me when RELIANCE hits ₹3000"). The system checks on each refresh and shows a notification badge.

### 3.5 — Manager Dashboard (Full Implementation)
The Manager Dashboard wireframe is designed but not implemented. It should show:
- Aggregate stats across all users.
- A user table with portfolio values.
- Platform-wide asset distribution charts.

### 3.6 — Mobile Responsive Design
The current layout uses a fixed `ml-64` sidebar that breaks on mobile screens. A collapsible hamburger menu and responsive table design are needed.

### 3.7 — Real Historical Data (yfinance)
Replace the current linear interpolation simulation with actual historical data using the `yfinance` Python library. This would give users a true picture of their portfolio's past performance.

---

## 📊 Summary Scorecard

| Category | Current Score | Target Score |
|---|---|---|
| Core Portfolio Tracking | 6 / 10 | 10 / 10 |
| Transaction Management | 1 / 10 | 9 / 10 |
| Data Visualization | 5 / 10 | 9 / 10 |
| Tax & Financial Planning | 0 / 10 | 8 / 10 |
| Goal Tracking | 0 / 10 | 8 / 10 |
| User Experience (UX) | 6 / 10 | 9 / 10 |
| Asset Coverage | 2 / 10 | 8 / 10 |
| **Overall** | **20 / 70** | **61 / 70** |

---

## 🗺️ Recommended Build Order

```
Phase 1 (Immediate):
  → 1.2 Edit / Delete Holdings
  → 1.1 Transaction History Model
  → 1.3 Expand Asset List (Nifty 50)

Phase 2 (Next Sprint):
  → 2.5 Average Buy Price Logic
  → 2.3 Doughnut Chart (Asset Allocation)
  → 2.4 Portfolio Search & Filter

Phase 3 (Core Features):
  → 2.1 Tax Calculator Page
  → 2.2 Goals Page
  → 1.4 Realized P/L Tracking

Phase 4 (Advanced):
  → 3.7 Real Historical Data (yfinance)
  → 3.1 Dividend Tracking
  → 3.5 Manager Dashboard
  → 3.6 Mobile Responsive Design
```

---

*This report was auto-generated by Antigravity based on a full analysis of the ALTAIR codebase, wireframes, and documentation as of 18 Feb 2026.*

---

📊 ALTAIR Gap Analysis — Key Findings
🚨 Priority 1 — Critical (Build These Next)
Gap	Impact - No Transaction History - Users can't track buys/sells. This is the backbone of any portfolio app.
No Edit / Delete Holdings	Users are stuck with wrong data forever.
Only 5 Assets Available	Real users can't use the app if their stocks aren't listed.
No Realized P/L	App only shows unrealized gains, not actual booked profits.
⚠️ Priority 2 — Important (Build Soon)
Tax Calculator	Fully designed in wireframes but not built. Core differentiator.
💡 Priority 3 — Advanced (Future Roadmap)
SIP Simulator
Dividend Tracking
Price Alerts
CSV/PDF Export
Manager Dashboard (fully designed, not built)
📊 Overall Score
Current: 20/70 → Target: 61/70

🗺️ Recommended Build Order
Phase 1 → Edit/Delete Holdings + Transaction Model + Expand Asset List
Phase 2 → Average Buy Price + Doughnut Chart + Search/Filter
Phase 3 → Tax Calculator + Goals Page + Realized P/L
Phase 4 → yfinance + Dividends + Manager Dashboard

Which phase would you like to start with? 🚀

---

To transform ALTAIR into a truly comprehensive wealth management platform, we can expand beyond just Stocks and ETFs. Based on modern financial trends and your current "₹" (INR) focused layout, here are the major asset types we can add:



3. 🛡️ Low-Risk/Fixed Income
Fixed Deposits (FD): Traditional savings with a fixed interest rate.
Provident Funds (PPF/EPF): Essential for Indian retirement tracking.
Bonds: Government or Corporate bonds (Debt market).
Implementation: These usually have a "fixed" annual return (e.g., 7.1% for PPF), so we can auto-calculate their growth without needing a live scraper.
4. 🟡 Digital Gold & Commodities
Why: Gold is a traditional "hedge" against market crashes.
Data Source: Live gold spot prices are easily available.
Impact: Adds a "Safe Haven" category to the portfolio.

---