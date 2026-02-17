# Altair — Feature Specifications 📋

Detailed breakdown of every feature, organized by app and user story.

---

## 1. 🔐 Authentication & Accounts

### 1.1 User Registration
- **As a** new user, **I want to** create an account **so that** I can access the finance tools.
- Fields: Username, Email, Password, Confirm Password.
- After registration, user is assigned `role = 'user'` by default.
- Redirect to User Dashboard after successful signup.

### 1.2 Login / Logout
- Standard Django auth login with email/username + password.
- "Remember Me" functionality (session duration).
- Logout clears session and redirects to home page.

### 1.3 Profile Management
- View and edit: Name, Phone, Date of Birth, PAN, Currency preference.
- Upload profile picture.
- Change password flow.

### 1.4 Role-Based Routing
- After login, check `user.role`:
  - `'manager'` → Redirect to `/manager/`
  - `'user'` → Redirect to `/dashboard/`
  - `is_superuser` → Can access `/admin/`

---

## 2. 📊 User Dashboard (`/dashboard/`)

### 2.1 Overview Page
- **Net Worth Card**: Total value of all accounts combined.
- **Quick Stats Row**: Total Invested, Total Returns, Return %, Number of Assets.
- **Portfolio Value Chart**: Line chart showing portfolio value over time (from `AssetSnapshot`).
- **Asset Allocation Pie**: Donut chart showing distribution by `asset_type`.
- **Recent Transactions**: Last 5 transactions with link to full list.
- **Goal Progress**: Mini progress bars for top 3 goals.

### 2.2 Sidebar Navigation
- Overview
- Portfolio
- Transactions
- Tax Calculator
- Goals
- Settings

---

## 3. 💼 Portfolio Management (`/portfolio/`)

### 3.1 Portfolio Dashboard
- **All Accounts List**: Cards for each financial account (Demat, Savings, etc.).
- Each card shows: Account name, Institution, Balance, Number of holdings.
- Click to expand → shows all assets in that account.

### 3.2 Add/Edit Account
- Form: Name, Type (dropdown), Institution, Initial Balance.
- HTMX-powered modal form (no page reload).

### 3.3 Add/Edit Asset
- Form: Asset name, Ticker, Type, Quantity, Avg Buy Price, Current Price, Sector.
- Auto-compute: Current Value, P&L, Return %.
- HTMX-powered inline editing.

### 3.4 Asset Detail View
- Full information card for a single asset.
- Transaction history for that specific asset.
- Price trend chart (if snapshot data available).

### 3.5 Asset Allocation Analysis
- **By Type**: Pie chart (Stocks vs Mutual Funds vs FDs vs Crypto etc.).
- **By Sector**: Bar chart (Tech, Finance, Healthcare, etc.).
- **Concentration Risk**: Warning if any single asset > 30% of portfolio.

### 3.6 Performance Summary
- Table showing: Asset, Invested, Current, P/L, Return %, Weight in Portfolio.
- Sortable columns. Color-coded green (profit) / red (loss).

---

## 4. 📈 Transaction Tracker (`/tracker/`)

### 4.1 Transaction List
- Paginated table: Date, Asset, Type (Buy/Sell/Dividend), Qty, Price, Total, Fees.
- Filter by: Date range, Account, Asset, Transaction type.
- Search by asset name or notes.

### 4.2 Add Transaction
- HTMX modal form.
- Fields: Account (dropdown), Asset (dropdown/autocomplete), Type, Quantity, Price, Fees, Date, Notes.
- On "Sell" type → auto-trigger Capital Gains calculation.
- On "Buy" type → update asset quantity and avg_buy_price.

### 4.3 Transaction Detail
- Full details of a single transaction.
- Edit / Delete (soft delete) actions.

### 4.4 Dividend Tracker
- Filtered view showing only dividend transactions.
- Summary: Total dividends received this FY, Monthly dividend income.
- Projected annual dividend income.

### 4.5 Watchlist
- List of assets being monitored (not yet purchased).
- Fields: Name, Ticker, Target Price, Notes.
- Quick action: "Buy" button → pre-fills Add Transaction form.

---

## 5. 🏦 Tax Calculator (`/tax/`)

### 5.1 Tax Profile Setup
- Form: Financial Year, Tax Regime (Old/New), Gross Income.
- Deductions section (only for Old Regime):
  - 80C: PPF, ELSS, LIC, etc. (max ₹1,50,000)
  - 80D: Medical insurance
  - Other: HRA, 80G, 80E, NPS

### 5.2 Tax Estimation Result
- **Summary Card**: Gross Income, Total Deductions, Taxable Income, Tax Payable.
- **Breakdown**: Tax per slab (5%, 10%, 15%, 20%, 30%).
- **Comparison Table**: Old Regime vs New Regime side-by-side.
- **Recommendation**: Which regime saves more, with exact ₹ difference.

### 5.3 Capital Gains Report
- Auto-calculated from sell transactions.
- Separate tables for STCG (< 1 year) and LTCG (> 1 year).
- Tax on STCG: 15% (equities), slab rate (others).
- Tax on LTCG: 10% above ₹1 lakh (equities).
- Total capital gains tax.

### 5.4 Tax Saving Suggestions
- How much of 80C limit is utilized → remaining capacity.
- Suggested instruments: ELSS, PPF, NPS, etc.
- If in New Regime → show potential savings if switched to Old (and vice versa).

---

## 6. 🎯 Goal Tracking (`/goals/`)

### 6.1 Goals List
- Cards for each goal: Name, Target, Progress %, Deadline, Priority badge.
- Color-coded by priority (High = red, Medium = amber, Low = green).
- Completed goals shown in a separate "Achieved" section.

### 6.2 Add/Edit Goal
- Form: Name, Category, Target Amount, Deadline, Priority, Monthly Contribution.
- HTMX modal form.

### 6.3 Goal Detail
- Large progress ring / bar.
- Stats: Target, Saved so far, Remaining, Monthly contribution, Projected completion.
- "Add Contribution" button → quick form to add savings.

### 6.4 Projected Timeline
- Simple calculation: `remaining / monthly_contribution = months`.
- Visual: "At current rate, you'll reach your goal by [date]."
- Warning if projected date is after deadline.

---

## 7. 👔 Manager Dashboard (`/manager/`)

### 7.1 Manager Overview
- **Total Users Card**: Number of managed users.
- **Aggregate Stats**: Combined portfolio value of all users, Avg return %.
- **Activity Feed**: Recent transactions across all users.

### 7.2 User Management
- Table: Username, Email, Role, Portfolio Value, Last Active.
- Click user → view their portfolio/dashboard as read-only.
- Action: Change user role, Deactivate account.

### 7.3 System Reports
- Aggregate asset allocation across all users.
- Top performing assets across the platform.
- Export data to CSV.

---

## 8. 🏠 Public Pages (Core App)

### 8.1 Landing Page (`/`)
- Hero section with tagline.
- Feature cards (Portfolio, Tax, Goals).
- CTA: "Get Started" → Register page.

### 8.2 About / Contact (Optional, Phase 2)
- Static marketing pages.

