# Altair: Complete Financial Assistant 🚀

Altair is designed to be a comprehensive financial hub, providing users with tools to track, analyze, and optimize their financial lives.

## 🌟 Core Modules & Features

### 1. 📊 Portfolio Analyzer
- **Dashboard**: Real-time overview of net worth.
- **Asset Allocation**: Breakdown of Stocks, Bonds, Cash, Real Estate, and Crypto.
- **Risk Assessment**: Analyze portfolio volatility and diversification.
- **Performance Tracking**: Time-weighted and money-weighted returns.

### 2. 📈 Investment Tracker
- **Transaction History**: Track every buy/sell/dividend event.
- **Dividends Tracker**: Forecast upcoming dividend income.
- **Watchlist**: Monitor potential investment opportunities.
- **API Integration**: (Future) Connect to brokers or market data APIs (e.g., Yahoo Finance).

### 3. 🏦 Tax Calculator & Optimizer
- **Income Tax Estimation**: Based on regional rules (e.g., India's Old vs. New regime).
- **Capital Gains Tracker**: Automatic calculation of Short-Term and Long-Term Capital Gains (STCG/LTCG).
- **Tax-Saving Recommendations**: Suggest investments (e.g., 80C, 80D) to minimize liability.

### 4. 🤖 AI Financial Advisor
- **Spending Analysis**: Analyze transaction patterns to suggest budget cuts.
- **Portfolio Rebalancing**: AI suggestions to realign with target allocation.
- **Goal-Based Advice**: "What if" scenarios for retirement or major purchases.

### 5. 🎯 Goal Tracking
- **Defined Goals**: Retirement planning, Home purchase, Vacation fund.
- **Progress Tracking**: Visual indicators of how close you are to your goals.
- **Projected Completion**: Estimating when a goal will be met based on current savings rate.

---

## 🛠 Technology Stack
- **Backend**: Django (Python)
- **Frontend**: **Tailwind CSS** (Styling), **HTMX** (Interactivity), **Alpine.js** (Reactive UI)
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Optimization**: SEO-friendly, Server-side rendering (SSR).

---

## 📅 Roadmap (Phase 1)

1.  **Project Setup**: Django project creation, custom user models, and theme setup.
2.  **Portfolio Core**: Database models for Accounts, Assets, and Transactions.
3.  **Basic Tracking**: Dashboard with asset allocation pie charts.
4.  **Tax Engine**: Logic implementation for basic income tax calculations.


---

## 📁 App Architecture
- `accounts`: User authentication, profiles, and roles.
- `core`: Shared templates (base, header, footer), home page.
- `manager_dashboard`: Manager-only views and reports.
- `user_dashboard`: User's personal finance command center.
- `portfolio`: *(Phase 2)* Asset management, accounts, holdings.
- `tracker`: *(Phase 3)* Transactions, buy/sell logs, dividends.
- `tax`: *(Phase 4)* Tax estimation engine, capital gains.
- `goals`: *(Phase 5)* Financial goal setting & progress.
- `advisor`: *(Phase 7)* AI-powered suggestions.

---

## 📚 Documentation Index
All detailed planning documents are available in the `XDOCX/` folder:

| Document | Description |
|----------|-------------|
| `ARCHITECTURE.md` | System architecture, tech stack, RBAC, URL strategy |
| `DATABASE_SCHEMA.md` | All models, fields, relationships, ERD |
| `FEATURES.md` | Detailed feature specs with user stories |
| `INVESTOR_FEATURES.md` | Advanced features for Retail & Pro investors (3-tier system) |
| `INVESTOR_WIREFRAMES.md` | Wireframes for advanced investor dashboards |
| `DEVELOPMENT_ROADMAP.md` | 7-phase implementation plan with tasks |
| `WIREFRAMES.md` | ASCII wireframes for every major page + design system |
| `learn.md` | Command history and learning log |
