# Altair — Development Roadmap 🗺️

Step-by-step phased implementation plan. Each phase is designed to be a working, deployable increment.

---

## Phase 0: Foundation ✅ (COMPLETED)

| # | Task                                         | Status |
|---|----------------------------------------------|--------|
| 1 | Create virtual environment & install Django   | ✅ Done |
| 2 | `django-admin startproject config .`          | ✅ Done |
| 3 | Create `accounts` app with CustomUser model   | ✅ Done |
| 4 | Define roles: Manager, User                   | ✅ Done |
| 5 | Run migrations & create sample users          | ✅ Done |
| 6 | Create `core` app with base templates         | ✅ Done |
| 7 | Integrate Tailwind CSS, HTMX, Alpine.js       | ✅ Done |
| 8 | Design landing page (hero + feature cards)     | ✅ Done |
| 9 | Initialize `manager_dashboard` & `user_dashboard` apps | ✅ Done |
| 10| Push to GitHub                                | ✅ Done |

---

## Phase 1: Authentication & Dashboards

*Goal: Users can register, log in, and see a role-based dashboard.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Build registration page (`/accounts/signup/`)               | accounts           |
| 2 | Build login page (`/accounts/login/`)                       | accounts           |
| 3 | Implement logout flow                                       | accounts           |
| 4 | Create `UserProfile` model + migration                      | accounts           |
| 5 | Build profile edit page                                     | accounts           |
| 6 | Create `@role_required` decorator                           | accounts           |
| 7 | Design User Dashboard sidebar layout                        | user_dashboard     |
| 8 | Build User Dashboard overview (placeholder cards)           | user_dashboard     |
| 9 | Design Manager Dashboard layout                             | manager_dashboard  |
| 10| Build Manager Dashboard overview (placeholder cards)        | manager_dashboard  |
| 11| Implement role-based redirect after login                   | accounts           |

**Deliverable**: Users can register, log in, and land on their respective dashboards.

---

## Phase 2: Portfolio Management

*Goal: Users can create financial accounts, add assets, and view their portfolio.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Create `portfolio` app                                      | portfolio          |
| 2 | Define `Account` model + migration                          | portfolio          |
| 3 | Define `Asset` model + migration                            | portfolio          |
| 4 | Build "My Accounts" page with account cards                 | portfolio          |
| 5 | Build "Add Account" HTMX modal form                        | portfolio          |
| 6 | Build "Add Asset" form (linked to an account)               | portfolio          |
| 7 | Build asset detail view                                     | portfolio          |
| 8 | Portfolio dashboard: asset allocation pie chart (Chart.js)  | portfolio          |
| 9 | Portfolio dashboard: performance summary table              | portfolio          |
| 10| Create `AssetSnapshot` model for historical tracking        | portfolio          |

**Deliverable**: A working portfolio tracker where users can manage accounts and assets.

---

## Phase 3: Transaction Tracker

*Goal: Users can log all buy/sell/dividend transactions and track history.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Create `tracker` app                                        | tracker            |
| 2 | Define `Transaction` model + migration                      | tracker            |
| 3 | Define `Watchlist` model + migration                        | tracker            |
| 4 | Build transaction list page (with filters & search)         | tracker            |
| 5 | Build "Add Transaction" HTMX modal                         | tracker            |
| 6 | Auto-update asset quantity on buy/sell                       | tracker            |
| 7 | Build dividend tracker view                                 | tracker            |
| 8 | Build watchlist page                                        | tracker            |
| 9 | Link transactions to User Dashboard overview                | user_dashboard     |

**Deliverable**: Full transaction logging with auto-updated portfolio figures.

---

## Phase 4: Tax Calculator

*Goal: Users can estimate income tax and view capital gains.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Create `tax` app                                            | tax                |
| 2 | Define `TaxProfile` model + migration                       | tax                |
| 3 | Define `CapitalGain` model + migration                      | tax                |
| 4 | Implement Indian tax slab logic (Old & New regime)          | tax                |
| 5 | Build tax profile setup form                                | tax                |
| 6 | Build tax estimation result page                            | tax                |
| 7 | Build Old vs New regime comparison table                    | tax                |
| 8 | Auto-generate capital gains from sell transactions          | 
tax + tracker      |
| 9 | Build capital gains report page (STCG + LTCG)              | tax                |
| 10| Tax saving suggestions                                      | tax                |

**Deliverable**: Working tax calculator with regime comparison and capital gains tracking.

---

## Phase 5: Goal Tracking

*Goal: Users can set financial goals and track progress.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Create `goals` app                                          | goals              |
| 2 | Define `FinancialGoal` model + migration                    | goals              |
| 3 | Build goals list page with progress cards                   | goals              |
| 4 | Build "Add Goal" HTMX modal form                           | goals              |
| 5 | Build goal detail page (progress ring + stats)              | goals              |
| 6 | Implement projected timeline calculation                    | goals              |
| 7 | Link top goals to User Dashboard overview                   | user_dashboard     |

**Deliverable**: Complete goal tracking system with projections.

---

## Phase 6: Manager Features

*Goal: Managers can view all user data and generate reports.*

| # | Task                                                        | App               |
|---|-------------------------------------------------------------|--------------------|
| 1 | Build user management table                                 | manager_dashboard  |
| 2 | Implement "view user as read-only" feature                  | manager_dashboard  |
| 3 | Aggregate stats across all users                            | manager_dashboard  |
| 4 | Build system reports page                                   | manager_dashboard  |
| 5 | CSV export for reports                                      | manager_dashboard  |

**Deliverable**: Manager can oversee all users and export data.

---

## Phase 7: Polish & Production (Future)

| # | Task                                              |
|---|---------------------------------------------------|
| 1 | Full responsive design audit                       |
| 2 | Dark/Light mode toggle                             |
| 3 | Email notifications (goal deadlines, big drops)    |
| 4 | API integration (Yahoo Finance for live prices)    |
| 5 | PostgreSQL migration for production                |
| 6 | Deploy to PythonAnywhere / Railway / DigitalOcean  |

---

## Phase 8: Retail Investor Features 🟡

*Goal: Serve active stock market participants with SIP tracking, dividends, and sector analysis.*

| # | Task                                                          | App               |
|---|---------------------------------------------------------------|--------------------|
| 1 | Add `investor_tier` field to `UserProfile`                    | accounts           |
| 2 | Implement tier-based sidebar (show/hide nav items per tier)   | user_dashboard     |
| 3 | Build SIP Tracker page (active SIPs, calendar, XIRR)         | portfolio          |
| 4 | Define `SIPPlan` model + migration                            | portfolio          |
| 5 | Build SIP step-up calculator                                  | portfolio          |
| 6 | Build Dividend Dashboard (calendar, yield, DRIP tracking)     | tracker            |
| 7 | Implement XIRR and CAGR calculations for holdings            | portfolio          |
| 8 | Build sector breakdown treemap + concentration alerts         | portfolio          |
| 9 | Build Top Gainers / Top Losers widget                         | user_dashboard     |
| 10| Define `AlertRule` model + price alert system                 | tracker            |
| 11| Add time-range selector to all charts (1M, 3M, 1Y, ALL)      | portfolio          |

**Deliverable**: Enhanced dashboard for retail investors with SIP tracking, dividends, and sector analysis.

---

## Phase 9: Pro Investor Features 🔴

*Goal: Professional-grade analytics, risk management, tax harvesting, and report generation.*

| # | Task                                                          | App               |
|---|---------------------------------------------------------------|--------------------|
| 1 | Define `InvestmentLot` model + migration                      | portfolio          |
| 2 | Implement multi-lot tracking (FIFO, Specific Lot, LIFO)       | portfolio          |
| 3 | Build sell modal with tax impact preview                       | portfolio          |
| 4 | Define `RiskSnapshot` model + migration                       | portfolio          |
| 5 | Implement Sharpe, Sortino, Alpha, Beta, Max Drawdown calcs    | portfolio          |
| 6 | Build Risk Analysis page (score, correlation matrix, stress)  | user_dashboard     |
| 7 | Implement benchmark comparison (NIFTY 50, S&P 500 overlay)    | portfolio          |
| 8 | Build Tax Loss Harvesting page + wash sale alerts             | tax                |
| 9 | Implement Advance Tax Calculator (quarterly schedule)          | tax                |
| 10| Build multi-year tax trend chart                               | tax                |
| 11| Define `Report` model + report generation engine              | user_dashboard     |
| 12| Build Reports Center (PDF/CSV for all report types)           | user_dashboard     |
| 13| Implement customizable dashboard (drag-and-drop widgets)       | user_dashboard     |
| 14| Multi-currency support + forex gain/loss                       | portfolio          |

**Deliverable**: Full pro-grade analytics terminal with risk management, tax optimization, and exportable reports.

---

## Phase 10: AI Advisor (Future) 🤖

| # | Task                                                          |
|---|---------------------------------------------------------------|
| 1 | Portfolio rebalancing suggestions based on target allocation   |
| 2 | Investment style classification (Growth/Value/Balanced)        |
| 3 | Smart year-end tax planning recommendations                   |
| 4 | Peer comparison (anonymized percentile ranking)                |
| 5 | Derivatives tracker (Options, Futures, Greeks)                 |

