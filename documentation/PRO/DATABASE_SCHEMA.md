# Altair — Database Schema & Models 🗃️

This document defines every Django model, its fields, and relationships across all apps.

---

## 1. Accounts App (`accounts/`)

### `CustomUser` *(Already Implemented)*
Extends Django's `AbstractUser`.

| Field       | Type         | Details                                |
|-------------|--------------|----------------------------------------|
| `username`  | CharField    | Inherited from AbstractUser            |
| `email`     | EmailField   | Inherited from AbstractUser            |
| `password`  | CharField    | Inherited (hashed automatically)       |
| `role`      | CharField    | Choices: `manager`, `user`             |
| `first_name`| CharField    | Inherited                              |
| `last_name` | CharField    | Inherited                              |

### `UserProfile` *(New)*
Extended profile information linked 1:1 with `CustomUser`.

| Field            | Type          | Details                                   |
|------------------|---------------|-------------------------------------------|
| `user`           | OneToOneField | Links to `CustomUser`                     |
| `phone`          | CharField     | Optional phone number                     |
| `date_of_birth`  | DateField     | For age-based tax calculations            |
| `pan_number`     | CharField     | Indian PAN (for tax features), encrypted  |
| `profile_picture`| ImageField    | Optional avatar                           |
| `currency`       | CharField     | Preferred currency (INR, USD, EUR)        |
| `investor_tier`  | CharField     | Choices: `casual`, `retail`, `pro`        |
| `created_at`     | DateTimeField | Auto-set on creation                      |
| `updated_at`     | DateTimeField | Auto-set on every save                    |

---

## 2. Portfolio App (`portfolio/`)

### `Account`
A financial account container (e.g., "Zerodha Demat", "HDFC Savings", "Crypto Wallet").

| Field          | Type           | Details                                     |
|----------------|----------------|---------------------------------------------|
| `user`         | ForeignKey     | Links to `CustomUser`                       |
| `name`         | CharField      | e.g., "Zerodha Demat Account"               |
| `account_type` | CharField      | Choices: `demat`, `savings`, `fd`, `ppf`, `crypto`, `other` |
| `institution`  | CharField      | e.g., "Zerodha", "HDFC Bank"                |
| `balance`      | DecimalField   | Current balance (auto-calculated or manual) |
| `is_active`    | BooleanField   | Soft delete                                 |
| `created_at`   | DateTimeField  | Auto-set                                    |

### `Asset`
An individual financial instrument or holding.

| Field            | Type           | Details                                        |
|------------------|----------------|------------------------------------------------|
| `account`        | ForeignKey     | Links to `Account`                             |
| `name`           | CharField      | e.g., "Reliance Industries", "Bitcoin"         |
| `ticker`         | CharField      | e.g., "RELIANCE.NS", "BTC"                    |
| `asset_type`     | CharField      | Choices: `stock`, `mutual_fund`, `bond`, `fd`, `crypto`, `gold`, `real_estate`, `cash` |
| `quantity`       | DecimalField   | Number of units held                           |
| `avg_buy_price`  | DecimalField   | Average purchase price per unit                |
| `current_price`  | DecimalField   | Latest market price (manual or API-updated)    |
| `sector`         | CharField      | e.g., "Technology", "Finance" (optional)       |
| `purchase_date`  | DateField      | Date of first purchase                         |
| `currency`       | CharField      | Choices: `INR`, `USD`, `EUR` (default: INR)    |
| `notes`          | TextField      | Optional notes                                 |

**Computed Properties (not stored, calculated in Python):**
- `current_value` = `quantity × current_price`
- `invested_value` = `quantity × avg_buy_price`
- `profit_loss` = `current_value - invested_value`
- `return_pct` = `(profit_loss / invested_value) × 100`

### `InvestmentLot` *(Pro — Multi-Lot Tracking)*
Individual purchase lots for FIFO/Specific Lot tax calculations.

| Field          | Type          | Details                            |
|----------------|---------------|------------------------------------|
| `asset`        | ForeignKey    | Links to `Asset`                   |
| `quantity`     | DecimalField  | Units in this lot                  |
| `buy_price`    | DecimalField  | Purchase price per unit            |
| `buy_date`     | DateField     | Purchase date                      |
| `remaining_qty`| DecimalField  | Units not yet sold from this lot   |
| `is_closed`    | BooleanField  | All units in lot have been sold    |

### `AssetSnapshot` *(For historical tracking)*
Daily/weekly snapshot of portfolio value for chart generation.

| Field         | Type          | Details                        |
|---------------|---------------|--------------------------------|
| `user`        | ForeignKey    | Links to `CustomUser`          |
| `date`        | DateField     | Snapshot date                  |
| `total_value` | DecimalField  | Total portfolio value on date  |

---

## 2b. SIP Tracking *(Retail + Pro)*

### `SIPPlan`
Active Systematic Investment Plans.

| Field             | Type          | Details                              |
|-------------------|---------------|--------------------------------------|
| `user`            | ForeignKey    | Links to `CustomUser`                |
| `asset`           | ForeignKey    | Links to `Asset` (mutual fund)       |
| `monthly_amount`  | DecimalField  | Monthly SIP contribution             |
| `sip_date`        | IntegerField  | Day of month (1–28)                  |
| `start_date`      | DateField     | SIP start date                       |
| `step_up_pct`     | DecimalField  | Annual step-up percentage (optional) |
| `is_active`       | BooleanField  | Whether SIP is currently active      |
| `total_invested`  | DecimalField  | Cumulative amount invested via SIP   |
| `created_at`      | DateTimeField | Auto-set                             |

---

## 2c. Risk & Analytics *(Pro)*

### `RiskSnapshot`
Periodic snapshot of portfolio risk metrics.

| Field            | Type          | Details                               |
|------------------|---------------|---------------------------------------|
| `user`           | ForeignKey    | Links to `CustomUser`                 |
| `date`           | DateField     | Snapshot date                         |
| `risk_score`     | IntegerField  | Overall score (1–100)                 |
| `sharpe_ratio`   | DecimalField  | Risk-adjusted return                  |
| `sortino_ratio`  | DecimalField  | Downside risk-adjusted return         |
| `alpha`          | DecimalField  | Excess return vs benchmark            |
| `beta`           | DecimalField  | Systematic risk vs market             |
| `max_drawdown`   | DecimalField  | Largest peak-to-trough decline (%)    |
| `volatility`     | DecimalField  | Standard deviation of returns         |

### `AlertRule` *(Retail + Pro)*
User-configured alert triggers.

| Field           | Type          | Details                                      |
|-----------------|---------------|----------------------------------------------|
| `user`          | ForeignKey    | Links to `CustomUser`                        |
| `alert_type`    | CharField     | Choices: `price`, `drift`, `goal`, `dividend`, `tax`, `drawdown` |
| `asset`         | ForeignKey    | Links to `Asset` (nullable)                  |
| `threshold`     | DecimalField  | Trigger value (price, %, etc.)               |
| `direction`     | CharField     | Choices: `above`, `below`                    |
| `is_active`     | BooleanField  | Whether alert is enabled                     |
| `last_triggered`| DateTimeField | Last time this alert fired                   |

### `Report` *(Pro)*
Generated report metadata.

| Field          | Type          | Details                                 |
|----------------|---------------|-----------------------------------------|
| `user`         | ForeignKey    | Links to `CustomUser`                   |
| `report_type`  | CharField     | Choices: `holdings`, `performance`, `pnl`, `capital_gains`, `dividend`, `tax_summary` |
| `format`       | CharField     | Choices: `pdf`, `csv`                   |
| `date_from`    | DateField     | Report start date                       |
| `date_to`      | DateField     | Report end date                         |
| `file_path`    | CharField     | Path to generated file                  |
| `created_at`   | DateTimeField | Auto-set                                |


---

## 3. Tracker App (`tracker/`)

### `Transaction`
Every financial event: buy, sell, dividend, deposit, withdrawal.

| Field            | Type           | Details                                       |
|------------------|----------------|-----------------------------------------------|
| `user`           | ForeignKey     | Links to `CustomUser`                         |
| `asset`          | ForeignKey     | Links to `Asset` (nullable for cash txns)     |
| `account`        | ForeignKey     | Links to `Account`                            |
| `transaction_type` | CharField    | Choices: `buy`, `sell`, `dividend`, `deposit`, `withdrawal`, `sip` |
| `quantity`       | DecimalField   | Number of units                               |
| `price_per_unit` | DecimalField   | Price at time of transaction                  |
| `total_amount`   | DecimalField   | `quantity × price_per_unit` (or manual)       |
| `fees`           | DecimalField   | Brokerage, STT, GST etc.                     |
| `date`           | DateField      | Transaction date                              |
| `notes`          | TextField      | Optional description                          |
| `created_at`     | DateTimeField  | Auto-set                                      |

### `Watchlist`
Stocks/assets the user wants to monitor but hasn't purchased yet.

| Field          | Type          | Details                           |
|----------------|---------------|-----------------------------------|
| `user`         | ForeignKey    | Links to `CustomUser`             |
| `name`         | CharField     | e.g., "TCS"                       |
| `ticker`       | CharField     | e.g., "TCS.NS"                    |
| `target_price` | DecimalField  | Alert when price reaches this     |
| `notes`        | TextField     | Why they're watching it           |
| `added_at`     | DateTimeField | Auto-set                          |

---

## 4. Tax App (`tax/`)

### `TaxProfile`
User-specific tax configuration for a financial year.

| Field               | Type           | Details                                     |
|---------------------|----------------|---------------------------------------------|
| `user`              | ForeignKey     | Links to `CustomUser`                       |
| `financial_year`    | CharField      | e.g., "2025-26"                             |
| `regime`            | CharField      | Choices: `old`, `new`                       |
| `gross_income`      | DecimalField   | Total annual income                         |
| `hra_exemption`     | DecimalField   | House Rent Allowance exemption              |
| `section_80c`       | DecimalField   | Investments under 80C (max 1.5L)            |
| `section_80d`       | DecimalField   | Health insurance premium                    |
| `other_deductions`  | DecimalField   | 80G, 80E, NPS, etc.                        |
| `created_at`        | DateTimeField  | Auto-set                                    |

**Computed Properties:**
- `taxable_income` = `gross_income - all_deductions`
- `estimated_tax` = calculated via slab logic
- `effective_rate` = `estimated_tax / gross_income × 100`

### `CapitalGain`
Capital gains from selling assets (auto-generated from transactions).

| Field             | Type          | Details                                  |
|-------------------|---------------|------------------------------------------|
| `user`            | ForeignKey    | Links to `CustomUser`                    |
| `asset`           | ForeignKey    | Links to `Asset`                         |
| `transaction`     | ForeignKey    | Links to sell `Transaction`              |
| `buy_price`       | DecimalField  | Original purchase price                  |
| `sell_price`      | DecimalField  | Sale price                               |
| `quantity`        | DecimalField  | Units sold                               |
| `gain_type`       | CharField     | Choices: `stcg`, `ltcg`                  |
| `gain_amount`     | DecimalField  | `(sell_price - buy_price) × quantity`    |
| `holding_period`  | IntegerField  | Days between buy and sell                |
| `financial_year`  | CharField     | e.g., "2025-26"                          |

---

## 5. Goals App (`goals/`)

### `FinancialGoal`

| Field             | Type           | Details                                    |
|-------------------|----------------|--------------------------------------------|
| `user`            | ForeignKey     | Links to `CustomUser`                      |
| `name`            | CharField      | e.g., "Retirement Fund", "Dream Home"      |
| `target_amount`   | DecimalField   | The amount needed                          |
| `current_amount`  | DecimalField   | How much saved so far                      |
| `deadline`        | DateField      | Target completion date                     |
| `priority`        | CharField      | Choices: `high`, `medium`, `low`           |
| `category`        | CharField      | Choices: `retirement`, `home`, `education`, `travel`, `emergency`, `other` |
| `monthly_contribution` | DecimalField | Planned monthly saving toward goal      |
| `is_completed`    | BooleanField   | Auto-set when `current_amount >= target`   |
| `created_at`      | DateTimeField  | Auto-set                                   |

**Computed Properties:**
- `progress_pct` = `(current_amount / target_amount) × 100`
- `remaining` = `target_amount - current_amount`
- `months_to_goal` = `remaining / monthly_contribution`

---

## 6. Entity Relationship Diagram

```
CustomUser ──┬── 1:1 ── UserProfile (investor_tier: casual/retail/pro)
             │
             ├── 1:N ── Account ── 1:N ── Asset ── 1:N ── Transaction
             │                              │                │
             │                              ├── 1:N ── InvestmentLot
             │                              │                │
             │                              └── 1:N ── CapitalGain
             │
             ├── 1:N ── SIPPlan
             ├── 1:N ── Watchlist
             ├── 1:N ── AlertRule
             ├── 1:N ── TaxProfile
             ├── 1:N ── FinancialGoal
             ├── 1:N ── AssetSnapshot
             ├── 1:N ── RiskSnapshot
             └── 1:N ── Report
```

