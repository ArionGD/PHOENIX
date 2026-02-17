# Altair — System Architecture 🏗️

This document describes the high-level system architecture of the Altair Finance Assistant.

---

## 1. Application Map

The project is organized into distinct Django apps, each responsible for a single domain:

```
ALTAIR/
├── config/              → Project settings, root URL routing, WSGI/ASGI
├── accounts/            → Authentication, roles, user profiles
├── core/                → Shared templates (base, header, footer), home page
├── manager_dashboard/   → Manager-only views: user management, system reports
├── user_dashboard/      → User's personal finance command center
├── portfolio/           → [NEW] Asset management, accounts, holdings
├── tracker/             → [NEW] Transactions, buy/sell logs, dividend tracking
├── tax/                 → [NEW] Tax estimation engine, capital gains, deductions
├── goals/               → [NEW] Financial goal setting & progress tracking
├── advisor/             → [FUTURE] AI-powered financial suggestions
└── XDOCX/              → Documentation (excluded from Git)
```

---

## 2. Technology Stack

| Layer          | Technology                | Purpose                                        |
|----------------|---------------------------|------------------------------------------------|
| **Backend**    | Django 5.x (Python 3.12)  | Server-side logic, ORM, auth                   |
| **Frontend**   | Tailwind CSS              | Utility-first responsive styling               |
| **Interactivity** | HTMX                  | AJAX-driven partial page updates (no SPA)      |
| **Reactivity** | Alpine.js                 | Lightweight client-side interactions            |
| **Database**   | SQLite (Dev) / PostgreSQL | Relational data storage                        |
| **Charts**     | Chart.js                  | Portfolio pie charts, line graphs, bar charts   |
| **Auth**       | Django Auth + CustomUser  | Role-based access (Manager / User)             |

---

## 3. Request Flow (How a Page Loads)

```
Browser → Django URL Router → View Function → Template (extends base.html)
                                    ↓
                              Database (ORM)
                                    ↓
                          HTML Response (with Tailwind + HTMX)
```

For HTMX-powered interactions (e.g., adding a transaction without page reload):

```
User clicks "Add" → HTMX sends POST to /tracker/add/ → Django View processes
    → Returns HTML fragment → HTMX swaps it into the DOM (no full reload)
```

---

## 4. Role-Based Access Control (RBAC)

| Role      | Access Level                                                     |
|-----------|------------------------------------------------------------------|
| **Admin** | Full Django admin panel, all data, user management               |
| **Manager** | Manager Dashboard: view all users' portfolios, generate reports |
| **User**  | User Dashboard: personal portfolio, transactions, tax, goals     |

Access is enforced via:
- `@login_required` decorator on all dashboard views.
- Custom `@role_required('manager')` decorator for manager-only pages.
- Django's built-in `is_superuser` for admin access.

---

## 5. Template Inheritance Strategy

```
core/base.html                    ← Global shell (head, scripts, header, footer)
  ├── core/home.html              ← Public landing page
  ├── accounts/login.html         ← Auth pages
  ├── user_dashboard/base.html    ← User dashboard layout (sidebar + content)
  │     ├── user_dashboard/overview.html
  │     ├── portfolio/dashboard.html
  │     ├── tracker/transactions.html
  │     ├── tax/calculator.html
  │     └── goals/list.html
  └── manager_dashboard/base.html ← Manager dashboard layout
        ├── manager_dashboard/overview.html
        └── manager_dashboard/users.html
```

---

## 6. URL Namespace Strategy

| URL Prefix            | App                 | Example Routes                    |
|-----------------------|---------------------|-----------------------------------|
| `/`                   | core                | Home page                         |
| `/accounts/`          | accounts            | `/login/`, `/logout/`, `/signup/` |
| `/dashboard/`         | user_dashboard      | `/dashboard/`, `/dashboard/settings/` |
| `/manager/`           | manager_dashboard   | `/manager/`, `/manager/users/`    |
| `/portfolio/`         | portfolio           | `/portfolio/`, `/portfolio/add/`  |
| `/tracker/`           | tracker             | `/tracker/`, `/tracker/add/`      |
| `/tax/`               | tax                 | `/tax/`, `/tax/calculate/`        |
| `/goals/`             | goals               | `/goals/`, `/goals/new/`          |
| `/admin/`             | Django Admin         | Built-in admin panel              |

