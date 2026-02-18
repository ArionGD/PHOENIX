# Git Commands & Learning Log 📚

Welcome to the learning log for the ALTAIR project. Here we track all the major setup commands used from the very beginning.

---

## 1. 🏗️ Environment Setup
These were the first steps to prepare our workspace.

1.  **`python -m venv .venv`**
    *   *What it does*: Creates a "Virtual Environment" in the `.venv` folder. This isoloates our project's libraries from the rest of the computer.
2.  **VS Code Integration**
    *   We configured `.vscode/settings.json` to automatically activate this environment every time a terminal is opened.
3.  **`python -m pip install django`**
    *   *What it does*: Downloads and installs the Django framework into our virtual environment.

---

## 2. 🛠️ Django Project Setup

1.  **`django-admin startproject config .`**
    *   *What it does*: Initializes the Django project. 
    *   `config`: This is the name we gave to the core settings folder.
    *   `.`: This tells Django to put `manage.py` in the root folder instead of making another sub-directory.

2.  **`python manage.py startapp [app_name]`**
    *   *What it does*: Creates a new Django app (module). We've used this to create:
        *   `accounts`: For user management.
        *   `core`: For global templates and layouts.
        *   `manager_dashboard`: Initialized for manager-specific views.
        *   `user_dashboard`: Initialized for regular user views.

3.  **`python manage.py makemigrations [app_name]`**
    *   *What it does*: Django reads your `models.py` and generates a "plan" (migration file) to update the database schema.

4.  **`python manage.py migrate`**
    *   *What it does*: Actually applies the migration plans to the `db.sqlite3` database file, creating your tables.

5.  **`pip freeze > requirements.txt`**
    *   *What it does*: Generates a "shopping list" of all installed libraries so the environment can be perfectly recreated on any machine.

---

## 🚀 3. Git & GitHub Sync (Step-by-Step)

Here is every command used to connect to GitHub, explained in detail:

1.  **`git init`**
    *   *What it does*: Initializes a new, empty Git repository in the current folder. It creates a hidden `.git` folder to start tracking every change you make.

2.  **`git add .`**
    *   *What it does*: Stages all files in the current directory for the next commit. It takes a "snapshot" of your current progress (excluding files in `.gitignore`).

3.  **`git commit -m "Message"`**
    *   *What it does*: Permanently records your staged changes in the local history. The message inside quotes helps you identify what was changed in this version.

4.  **`git remote add origin https://github.com/alkapandey1031986-arch/ALTAIR.git`**
    *   *What it does*: Connects your local folder to your online GitHub repository. We name this connection `origin`.

5.  **`git branch -M main`**
    *   *What it does*: Ensures your main development branch is named `main` (instead of the older `master`), following modern standards.

6.  **`git push -u origin main`**
    *   *What it does*: Uploads your local commits to GitHub. The `-u` links your local `main` branch to the GitHub `main` branch so next time you can just type `git push`.

---

## 🎨 4. Modern Frontend (T-H-A Stack)

1.  **Tailwind CSS**
    *   *Concept*: Utility-first styling. We styling components directly in HTML using classes like `bg-glass` or `flex`.
2.  **HTMX**
    *   *Concept*: Allows us to perform AJAX requests (dynamic updates without page reloads) using simple HTML attributes like `hx-get`.
3.  **Alpine.js** (Standardized)
    *   *Concept*: Used for the Portfolio "Add Asset" modal, auto-filling asset names, and handling instant calculation of "Total Amount" (Quantity x Price).

---

## 📈 5. Portfolio & Asset Management

1.  **`python manage.py startapp portfolio`**
    *   *Purpose*: Handles specialized logic for Stock and ETF tracking.
2.  **Real-Time Price Scraper**
    *   *Concept*: We use `requests` and `re` (regex) to fetch live stock prices from Google Finance. No heavy libraries like BeautifulSoup needed.
3.  **Manual Refresh Logic**
    *   *Command*: `path('refresh/', views.manual_refresh, name='refresh')`
    *   *Logic*: A dedicated view that forces a re-scrape of all prices, bypassing the cache.

---

## 📊 6. Data Visualization (Chart.js)

1.  **Multi-Dataset Line Charts**
    *   *Implementation*: Integrated two distinct lines on one graph: **Indigo** for Stocks and **Emerald** for ETFs.
2.  **Period Toggling (Monthly vs Yearly)**
    *   *Monthly*: Generates a 30-day timeline with daily "closing" calculations.
    *   *Yearly*: Generates a 12-month performance overview.
3.  **Smart Performance Simulation**
    *   *Concept*: Used **Linear Interpolation** to calculate historical points from a stock's "Buy Date" to today, added with a ±1.5% **Random Jitter** to simulate real market volatility.

---

## ⚡ 7. Performance & Optimization

1.  **5-Minute Cooldown Guard**
    *   *Logic*: `timedelta(minutes=5)`. The server only scrapes live prices if the last update was more than 5 minutes ago. This makes navigation instant while keeping data fresh.
2.  **JSON Script Tags**
    *   *Concept*: `{{ data|json_script:"id" }}`. A secure way to pass Python lists/dictionaries directly into browser JavaScript for rendering charts without syntax errors.
3.  **Symbol-Name Sync**
    *   *Concept*: Alpine.js logic in the modal that auto-populates the "Name" field once a "Symbol" (like RELIANCE) is selected, and vice-versa.

---

## 🚦 Current Project Status
- ✅ User Authentication (Login/Logout)
- ✅ Dashboard Stats (Net Worth, P/L, Savings)
- ✅ Enhanced Line Charts (Stock/ETF performance)
- ✅ Full Portfolio Analyzer (Categorized Assets)
- ✅ Real-time Price Integration (Google Finance)
