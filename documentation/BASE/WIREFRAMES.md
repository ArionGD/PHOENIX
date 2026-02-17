# Altair — Wireframe Designs 🎨

Page-by-page layout blueprints for every major screen in the application.

---

## 1. Landing Page (`/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                          Home   Portfolio   Tax   Advisor   [Login] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                                                                             │
│               Financial Intelligence, Reimagined.                           │
│                                                                             │
│       Altair is your all-in-one assistant for tax optimization,             │
│       portfolio analysis, and intelligent goal tracking.                    │
│                                                                             │
│              [ Get Started Free ]    [ Learn More ]                         │
│                                                                             │
├────────────────────────┬────────────────────────┬───────────────────────────┤
│  ┌──────────────────┐  │  ┌──────────────────┐  │  ┌──────────────────────┐ │
│  │   📈              │  │  │   ⚖️              │  │  │   🎯                 │ │
│  │                   │  │  │                   │  │  │                      │ │
│  │  Portfolio         │  │  │  Tax Calculator   │  │  │  Goal Tracker        │ │
│  │  Analyzer          │  │  │                   │  │  │                      │ │
│  │                   │  │  │  Optimize taxes    │  │  │  Set milestones      │ │
│  │  Deep dive into   │  │  │  and minimize      │  │  │  and track your      │ │
│  │  your assets...   │  │  │  liabilities...    │  │  │  progress...         │ │
│  │                   │  │  │                   │  │  │                      │ │
│  │  Explore →        │  │  │  Calculate →       │  │  │  Set Goal →          │ │
│  └──────────────────┘  │  └──────────────────┘  │  └──────────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│  ALTAIR         Product    Company                                          │
│  AI-powered     Analyzer   About Us          © 2026 Altair Finance.         │
│  finance.       Tracker    Privacy                                          │
│                 Advisor    Terms                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Dark gradient background (`#0d1117` → `#161b22`).
- Hero text uses gradient fill (`white` → `#00d4ff`).
- Feature cards use glassmorphism (`bg-white/5`, `backdrop-blur`, `border-white/10`).
- Hover: cards lift up with shadow.

---

## 2. Login Page (`/accounts/login/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                                        [Home]      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                        ┌─────────────────────────────┐                      │
│                        │                              │                      │
│                        │       Welcome Back 👋       │                      │
│                        │                              │                      │
│                        │   Username or Email          │                      │
│                        │   ┌──────────────────────┐   │                      │
│                        │   │                      │   │                      │
│                        │   └──────────────────────┘   │                      │
│                        │                              │                      │
│                        │   Password                   │                      │
│                        │   ┌──────────────────────┐   │                      │
│                        │   │                      │   │                      │
│                        │   └──────────────────────┘   │                      │
│                        │                              │                      │
│                        │   ☐ Remember me              │                      │
│                        │                              │                      │
│                        │    [ Sign In →→→→→→→ ]       │                      │
│                        │                              │                      │
│                        │   Don't have an account?     │                      │
│                        │   Register here              │                      │
│                        │                              │                      │
│                        └─────────────────────────────┘                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Centered glass card on dark background.
- Gradient button for "Sign In".
- Subtle radial glow behind the card.

---

## 3. User Dashboard — Overview (`/dashboard/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                              🔔   [Avatar ▼]      │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   STAT CARDS ROW                                              │
│            │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  Overview ●│   │ Net Worth │  │ Invested  │  │ Returns  │  │ Assets   │     │
│  Portfolio │   │ ₹12.4L   │  │ ₹10.2L   │  │ +₹2.2L   │  │ 18       │     │
│  Transact. │   │ ↑ 4.2%   │  │          │  │ +21.5%   │  │          │     │
│  Tax       │   └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│  Goals     │                                                                │
│  Settings  │   PORTFOLIO VALUE OVER TIME                                   │
│            │   ┌────────────────────────────────────────────────────────┐   │
│            │   │                              ╱─·                       │   │
│            │   │                           ╱·´                          │   │
│            │   │              ╱──·───·──╱·´                             │   │
│            │   │           ╱·´                                          │   │
│            │   │  ·───·──·´                                             │   │
│            │   │ Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep            │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   ┌──────────────────────┐  ┌─────────────────────────────┐   │
│            │   │  ASSET ALLOCATION    │  │  RECENT TRANSACTIONS        │   │
│            │   │                      │  │                             │   │
│            │   │     ┌────┐           │  │  RELIANCE  Buy   +50  ₹1.2L│   │
│            │   │    ╱Stocks╲          │  │  TCS       Sell  -20  ₹0.8L│   │
│            │   │   │  45%   │         │  │  HDFC MF   SIP   +10  ₹5K │   │
│            │   │    ╲Bonds ╱          │  │  Bitcoin   Buy   +0.1 ₹4K │   │
│            │   │     └─MF──┘          │  │  Infosys   Div   --   ₹800│   │
│            │   │                      │  │                             │   │
│            │   │  🟦 Stocks  45%      │  │  [ View All → ]             │   │
│            │   │  🟩 MF     30%      │  │                             │   │
│            │   │  🟨 FD     15%      │  └─────────────────────────────┘   │
│            │   │  🟧 Crypto 10%      │                                    │
│            │   └──────────────────────┘  ┌─────────────────────────────┐   │
│            │                              │  TOP GOALS                  │   │
│            │                              │  Retirement ████████░░  80% │   │
│            │                              │  Home       ████░░░░░░  40% │   │
│            │                              │  Vacation   ██░░░░░░░░  20% │   │
│            │                              └─────────────────────────────┘   │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance Assistant                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Sidebar: dark glass panel, active item highlighted with `altair-primary` left border.
- Stat cards: glass cards with large number + trend indicator.
- Charts: Chart.js with dark theme, cyan accent lines.
- Responsive: sidebar collapses to hamburger on mobile.

---

## 4. Portfolio Page (`/portfolio/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                              🔔   [Avatar ▼]      │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   My Portfolio                            [ + Add Account ]   │
│            │                                                                │
│  Overview  │   ACCOUNT CARDS                                               │
│  Portfolio●│   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  │
│  Transact. │   │ 📈 Zerodha     │  │ 🏦 HDFC Savings│  │ ₿ Crypto      │  │
│  Tax       │   │ Demat Account  │  │ Savings Account│  │ Wallet         │  │
│  Goals     │   │                │  │                │  │                │  │
│  Settings  │   │ ₹8,42,000     │  │ ₹2,15,000     │  │ ₹1,83,000     │  │
│            │   │ 12 holdings   │  │ 1 holding      │  │ 3 holdings    │  │
│            │   │ [View →]      │  │ [View →]      │  │ [View →]      │  │
│            │   └────────────────┘  └────────────────┘  └────────────────┘  │
│            │                                                                │
│            │   ALL HOLDINGS                                [ Search 🔍 ]   │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │ Asset         Ticker    Qty    Avg₹   Curr₹   P/L %  │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │ Reliance      RELIANCE  50     2400   2680   🟢+11.7 │   │
│            │   │ TCS           TCS       30     3800   3950   🟢+3.9  │   │
│            │   │ Infosys       INFY      100    1500   1420   🔴-5.3  │   │
│            │   │ HDFC MF       HDFCMF    200    45     52     🟢+15.5 │   │
│            │   │ Bitcoin       BTC       0.05   45L    48L    🟢+6.6  │   │
│            │   │ Ethereum      ETH       1.2    2.1L   2.3L   🟢+9.5  │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │   [ ← Prev ]                         [ Next → ]   Page 1/3   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance Assistant                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Account cards are glass cards with an icon, name, total value, and holding count.
- Holdings table has alternating subtle row backgrounds.
- Green/Red color coding for profit/loss.
- "Add Account" opens an HTMX-powered slide-in modal.

---

## 5. Tax Calculator Page (`/tax/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                              🔔   [Avatar ▼]      │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   Tax Calculator                                              │
│            │                                                                │
│  Overview  │   ┌─────────────────────────────┐  ┌─────────────────────────┐│
│  Portfolio │   │  TAX PROFILE SETUP          │  │  ESTIMATION RESULT      ││
│  Transact. │   │                             │  │                         ││
│  Tax     ● │   │  Financial Year             │  │  Gross Income  ₹15,00L ││
│  Goals     │   │  ┌─────────────────────┐    │  │  Deductions    ₹ 2,50L ││
│  Settings  │   │  │  2025-26        ▼   │    │  │  Taxable       ₹12,50L ││
│            │   │  └─────────────────────┘    │  │  ─────────────────────  ││
│            │   │                             │  │  Estimated Tax ₹1,87,500││
│            │   │  Tax Regime                 │  │  Effective Rate   12.5% ││
│            │   │  ┌─────────┐ ┌──────────┐  │  │                         ││
│            │   │  │  ● Old  │ │  ○ New   │  │  │  ✅ Old Regime saves    ││
│            │   │  └─────────┘ └──────────┘  │  │     ₹25,000 more!       ││
│            │   │                             │  │                         ││
│            │   │  Gross Annual Income        │  └─────────────────────────┘│
│            │   │  ┌─────────────────────┐    │                             │
│            │   │  │  ₹ 15,00,000        │    │                             │
│            │   │  └─────────────────────┘    │                             │
│            │   │                             │                             │
│            │   │  ── Deductions (Old) ──     │                             │
│            │   │  80C  ┌──────────────┐      │                             │
│            │   │       │ ₹ 1,50,000   │      │                             │
│            │   │       └──────────────┘      │                             │
│            │   │  80D  ┌──────────────┐      │                             │
│            │   │       │ ₹ 25,000     │      │                             │
│            │   │       └──────────────┘      │                             │
│            │   │  HRA  ┌──────────────┐      │                             │
│            │   │       │ ₹ 75,000     │      │                             │
│            │   │       └──────────────┘      │                             │
│            │   │                             │                             │
│            │   │  [ Calculate Tax →→→ ]      │                             │
│            │   └─────────────────────────────┘                             │
│            │                                                                │
│            │   REGIME COMPARISON                                           │
│            │   ┌───────────────────────────────────────────────────────┐   │
│            │   │  Slab             Old Regime      New Regime          │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │  Up to ₹2.5L     NIL             NIL                 │   │
│            │   │  ₹2.5L - 5L      ₹12,500         ₹12,500            │   │
│            │   │  ₹5L - 7.5L      ₹25,000         ₹25,000            │   │
│            │   │  ₹7.5L - 10L     ₹50,000         ₹37,500            │   │
│            │   │  ₹10L - 12.5L    ₹50,000         ₹50,000            │   │
│            │   │  ₹12.5L - 15L    ₹37,500         ₹62,500            │   │
│            │   ├───────────────────────────────────────────────────────┤   │
│            │   │  TOTAL           ₹1,75,000  ✅   ₹2,00,000          │   │
│            │   └───────────────────────────────────────────────────────┘   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance Assistant                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Goals Page (`/goals/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                                              🔔   [Avatar ▼]      │
├────────────┬────────────────────────────────────────────────────────────────┤
│            │                                                                │
│  SIDEBAR   │   My Goals                                  [ + New Goal ]    │
│            │                                                                │
│  Overview  │   ACTIVE GOALS                                                │
│  Portfolio │   ┌────────────────────────────────────────────────────────┐   │
│  Transact. │   │  🏠 Dream Home                          Priority: 🔴  │   │
│  Tax       │   │  Target: ₹50,00,000     Saved: ₹20,00,000            │   │
│  Goals   ● │   │  ████████████████░░░░░░░░░░░░░░░░░░░░░░  40%         │   │
│  Settings  │   │  Monthly: ₹50K   •   Projected: Dec 2028   [View →]  │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │   ┌────────────────────────────────────────────────────────┐   │
│            │   │  ✈️  Europe Vacation                     Priority: 🟡  │   │
│            │   │  Target: ₹5,00,000      Saved: ₹1,50,000             │   │
│            │   │  ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  30%        │   │
│            │   │  Monthly: ₹25K   •   Projected: Jun 2027   [View →]  │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │   ┌────────────────────────────────────────────────────────┐   │
│            │   │  🚨 Emergency Fund                      Priority: 🔴  │   │
│            │   │  Target: ₹3,00,000      Saved: ₹2,70,000             │   │
│            │   │  ██████████████████████████████████████░░  90%        │   │
│            │   │  Monthly: ₹15K   •   Projected: Mar 2026   [View →]  │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            │   ── ACHIEVED ✅ ──────────────────────────────────────────   │
│            │   ┌────────────────────────────────────────────────────────┐   │
│            │   │  📱 New Laptop          ₹1,20,000   ████████████ 100% │   │
│            │   └────────────────────────────────────────────────────────┘   │
│            │                                                                │
├────────────┴────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance Assistant                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Manager Dashboard (`/manager/`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALTAIR                               👔 Manager Panel   [Avatar ▼]       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   AGGREGATE STATS                                                          │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐    │
│   │  Total Users      │  │  Combined Value   │  │  Avg. Return         │    │
│   │  24               │  │  ₹4.2 Cr          │  │  +14.2%              │    │
│   │  ↑ 3 new this mo. │  │  ↑ 8.5% this qtr │  │                      │    │
│   └──────────────────┘  └──────────────────┘  └──────────────────────┘    │
│                                                                             │
│   ALL USERS                                     [ Search 🔍 ] [ Export CSV]│
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Username   Email              Role     Portfolio    Last Active     │  │
│   ├─────────────────────────────────────────────────────────────────────┤  │
│   │ rahul      rahul@mail.com     User     ₹12.4L      2 hrs ago   👁 │  │
│   │ priya      priya@mail.com     User     ₹8.7L       1 day ago   👁 │  │
│   │ amit       amit@mail.com      Manager  ₹15.2L      Online      👁 │  │
│   │ sneha      sneha@mail.com     User     ₹3.1L       3 days ago  👁 │  │
│   │ vikram     vikram@mail.com    User     ₹22.8L      5 hrs ago   👁 │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│   [ ← Prev ]                                     [ Next → ]   Page 1/5   │
│                                                                             │
│   ┌──────────────────────────────┐  ┌──────────────────────────────────┐  │
│   │  PLATFORM ASSET DISTRIBUTION │  │  TOP PERFORMING ASSETS           │  │
│   │                              │  │                                  │  │
│   │     ┌────┐                   │  │  Reliance   ████████████  +28%  │  │
│   │    ╱Stocks╲                  │  │  HDFC MF    ██████████    +22%  │  │
│   │   │  52%   │                 │  │  TCS        █████████     +18%  │  │
│   │    ╲Bonds ╱                  │  │  Gold ETF   ████████      +15%  │  │
│   │     └─MF──┘                  │  │  Bitcoin    ██████        +12%  │  │
│   │                              │  │                                  │  │
│   └──────────────────────────────┘  └──────────────────────────────────┘  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  © 2026 Altair Finance Assistant                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design Notes:**
- Full-width layout (no sidebar) since manager has fewer pages.
- "👁 View" button opens a read-only view of that user's dashboard.
- CSV Export button for compliance/reporting.

---

## 8. Design System Summary

### Color Palette
| Token            | Hex       | Usage                        |
|------------------|-----------|------------------------------|
| `altair-bg`      | `#0d1117` | Page background              |
| `altair-card`    | `#161b22` | Card / sidebar backgrounds   |
| `altair-primary` | `#00d4ff` | Accent, links, active states |
| `altair-accent`  | `#7000ff` | Secondary gradients          |
| `green`          | `#2ea043` | Profit, success              |
| `red`            | `#f85149` | Loss, warning                |
| `amber`          | `#d29922` | Medium priority              |

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: 600-700 weight
- **Body**: 400 weight
- **Monospace numbers**: Tabular nums for financial data alignment

### Component Library
| Component    | Tech            | Description                           |
|--------------|-----------------|---------------------------------------|
| Glass Card   | Tailwind + CSS  | `bg-white/5 backdrop-blur border`     |
| Modal Form   | HTMX            | Slide-in form, no page reload         |
| Data Table   | Tailwind        | Sortable, paginated, color-coded rows |
| Sidebar      | Alpine.js       | Collapsible nav, active state         |
| Charts       | Chart.js        | Pie, line, bar with dark theme        |
| Progress Bar | Tailwind        | Color-coded by % completion           |
| Buttons      | Tailwind        | Gradient primary, outline secondary   |
| Alerts       | Tailwind        | Success/Warning/Error banners         |

