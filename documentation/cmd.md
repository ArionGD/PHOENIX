# 🛠️ ALTAIR Command Reference

This document lists all the essential, unique, and powerful commands used in the active development of the **ALTAIR** financial platform. Use this as your "cheat sheet" when working on the project.

---

## 🏗️ Architecture: Why Django?
ALTAIR is built on **Django**, a high-level Python web framework. We chose it for four strategic reasons:

1.  **Batteries Included**: It comes with a built-in **Admin Panel**, **User Authentication**, and **ORM** (Object-Relational Mapper) out of the box. This lets us focus on building financial logic instead of reinventing the wheel.
2.  **Bank-Grade Security**: Django provides default protection against critical vulnerabilities like **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Cross-Site Request Forgery (CSRF)**—essential for a fintech application handling sensitive user portfolios.
3.  **Rapid Development (MTV)**: Its **Model-Template-View** architecture separates data (Models), logic (Views), and user interface (Templates), allowing us to ship complex features (like the Transaction Ledger) cleanly and quickly.
4.  **Scalability**: Trusted by giants like **Instagram** and **Pinterest**, effectively handling high-traffic loads as our user base grows.

---

## ⚡ Core Django Development

The most frequently used commands for daily development.

### 1. Server Management
Run the local development server.
```bash
python manage.py runserver
```
Run on a specific port (e.g., 8080) to avoid conflicts.
```bash
python manage.py runserver 8080
```

### 2. Database & Migrations
Create new migration files based on changes to `models.py`.
```bash
python manage.py makemigrations
```
Apply migrations to update the database schema.
```bash
python manage.py migrate
```
**Advanced Migration Control:**
Drop a specific app's tables and reset its migration history (Use with caution!).
```bash
python manage.py migrate transactions zero
```
Print the SQL that a migration will execute (for debugging).
```bash
python manage.py sqlmigrate portfolio 0001
```

### 3. Superuser & Auth
Create a new admin account with full access to the Django Admin panel.
```bash
python manage.py createsuperuser
```
Change a user's password via CLI.
```bash
python manage.py changepassword <username>
```

### 4. Interactive Shell
Open a Python shell with all Django settings and models pre-loaded. Perfect for testing queries or debugging logic quickly.
```bash
python manage.py shell
```
*Example usage inside shell:*
```python
from portfolio.models import Holding
Holding.objects.filter(symbol='RELIANCE').update(quantity=10)
```

### 5. System Checks
Check your project for common errors/warnings.
```bash
python manage.py check
```
Verify which apps and migrations are applied.
```bash
python manage.py showmigrations
```

---

## 📦 Dependency Management
We use a virtual environment (`.venv`) to keep our project isolated.

### Virtual Environment (PowerShell)
Activate the environment (Run this every time you open a new terminal).
```powershell
.venv\Scripts\Activate.ps1
```
Deactivate the environment.
```powershell
deactivate
```

### Pip Commands
Install dependencies from `requirements.txt`.
```bash
pip install -r requirements.txt
```
Save currently installed libraries to `requirements.txt`.
```bash
pip freeze > requirements.txt
```

---

## 📂 Project Structure & Apps
Commands to create new components.

Create a new Django app (e.g., `transactions`).
```bash
python manage.py startapp transactions
```
**Best Practice:** After creating an app, always register it in `config/settings.py` under `INSTALLED_APPS`.

---

## 🧪 Testing & Code Quality
Run all automated tests.
```bash
python manage.py test
```
Run tests for a specific app.
```bash
python manage.py test portfolio
```

---

## 🔧 Advanced / Edge-Case Commands
Unique commands used during ALTAIR's development to solve specific issues.

### Inspecting Database Columns
Verify if a specific column exists in the breakdown of a table (using Python one-liner).
```bash
python -c "import django; import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); from django.db import connection; print([c.name for c in connection.introspection.get_table_description(connection.cursor(), 'transactions_transaction')])"
```

### Debugging App Configuration
Check if an app configuration is properly loaded by Django.
```bash
python -c "import django; import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); from django.apps import apps; print([a.name for a in apps.get_app_configs()])"
```

### Locating Template Files
Find exactly where Django is resolving a template file from.
```bash
python -c "import django; import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); from django.template.loader import get_template; print(get_template('transactions/transactions.html').origin.name)"
```

### Analyzing Project Size (PowerShell)
Count lines of code and file sizes excluding `.venv` and `.git`.
```powershell
$files = Get-ChildItem -Recurse -File -Include *.py,*.html,*.css,*.js,*.md -Exclude ".venv*",".git*" -ErrorAction SilentlyContinue; $stats = $files | Group-Object Extension | Select-Object Name, Count, @{Name="SizeKB"; Expression={($_.Group | Measure-Object -Property Length -Sum).Sum / 1KB}}, @{Name="Lines"; Expression={ ($_.Group | Get-Content | Measure-Object -Line).Lines } }; $stats | Format-Table -AutoSize
```

---

## 🎨 Frontend & Static Files
Generate static files for production (CSS/JS/Images).
```bash
python manage.py collectstatic
```

---

## 🔍 Git Version Control
Syncing your local code with the GitHub repository.

Check status of changes.
```bash
git status
```
Stage all changes.
```bash
git add .
```
Commit changes with a message.
```bash
git commit -m "Your concise message here"
```
Push to the main branch.
```bash
git push origin main
```
View commit history (compact).
```bash
git log --oneline -5
```

---

## 🎨 Django Template Syntax
Common patterns used in our HTML templates (`.html` files) to create dynamic pages.

### 1. Structure & Inheritance
The "skeleton" of our pages.
```django
<!-- Extend the base layout -->
{% extends "user_dashboard/user_base.html" %}

<!-- Load static file library -->
{% load static %}

<!-- Define content for a specific block -->
{% block title %}Altair — Portfolio{% endblock %}

{% block content %}
    <!-- Page content goes here -->
{% endblock %}
```

### 2. Logic & Loops
Controlling what gets shown.
```django
<!-- If / Else Condition -->
{% if holding.profit_loss >= 0 %}
    <span class="text-green-500">Profit</span>
{% else %}
    <span class="text-red-500">Loss</span>
{% endif %}

<!-- For Loop with Empty State -->
{% for holding in holdings %}
    <tr>
        <td>{{ holding.symbol }}</td>
        <td>{{ holding.quantity }}</td>
    </tr>
{% empty %}
    <tr>
        <td colspan="2">No holdings found.</td>
    </tr>
{% endfor %}
```

### 3. Data Formatting (Filters)
Formatting numbers and dates on the fly.
```django
<!-- Format as currency (2 decimal places) -->
₹{{ holding.current_price|floatformat:2 }}

<!-- Format date (e.g., "18 Feb 2026") -->
{{ holding.purchase_date|date:"d M Y" }}

<!-- Escape text for use in JavaScript -->
'{{ holding.name|escapejs }}'

<!-- Access first character (e.g., for avatars) -->
{{ holding.symbol.0 }}
```

### 4. URLs & Links
Connecting pages without hardcoding paths.
```django
<!-- constant link to a named URL -->
<a href="{% url 'portfolio:add_asset' %}">Add Asset</a>

<!-- Link with an argument (ID/PK) -->
<a href="{% url 'portfolio:edit_asset' holding.pk %}">Edit</a>

<!-- Link to a static asset (image/css/js) -->
<img src="{% static 'img/logo.jpg' %}" alt="Logo">
```

### 5. Deployment & Security
Essential tags for forms and security.
```django
<!-- Security token (MUST be inside every POST form) -->
{% csrf_token %}
```

---

## 🐍 Backend Development (MTV)
Core Python patterns for Models, Templates, and Views.

### 1. Models (`models.py`)
Defining the data structure. We prioritize `DecimalField` for all financial data to avoid floating-point errors.

```python
from django.db import models
from django.conf import settings

class Transaction(models.Model):
    # Link to the user (One-to-Many)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Financial data (ALWAYS use DecimalField)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Text & Dates
    symbol = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_at = models.DateTimeField(auto_now=True)      # Update every save

    # Meta options
    class Meta:
        ordering = ['-created_at']  # Newest first

    # String representation (for Admin panel)
    def __str__(self):
        return f"{self.symbol} ({self.quantity})"
```

### 2. Views (`views.py`)
Handling logic and requests. We typically use **Function-Based Views (FBVs)** for clarity.

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# 1. Protect view (User must be logged in)
@login_required
def dashboard(request):
    # 2. Fetch data (filtered by logged-in user)
    holdings = Holding.objects.filter(user=request.user)
    
    # 3. Calculate context data
    total_value = sum(h.market_value() for h in holdings)
    
    # 4. Render template with context
    context = {'holdings': holdings, 'total': total_value}
    return render(request, 'dashboard/index.html', context)

# Handling Form Submissions (POST)
def add_transaction(request):
    if request.method == 'POST':
        # logic to save data...
        return redirect('dashboard')  # Redirect after success
    return render(request, 'add_txn.html')

# API Endpoints (for JavaScript/AJAX)
def get_live_price(request):
    data = {'symbol': 'BTC', 'price': 45000.50}
    return JsonResponse(data)
```

### 3. URLs (`urls.py`)
Routing requests to views.

**Project Level (`config/urls.py`)**:
```python
from django.urls import path, include

urlpatterns = [
    # Delegate to app-specific URL confs
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('dashboard/', include('user_dashboard.urls')),
]
```

**App Level (`portfolio/urls.py`)**:
```python
from django.urls import path
from . import views

# key for namespacing (e.g., {% url 'portfolio:detail' pk=1 %})
app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    # Dynamic URL parameter (Integer Primary Key)
    path('edit/<int:pk>/', views.edit_holding, name='edit'),
]
```

---

## 📂 File Anatomy
A guide to the standard Python files you'll find in this project.

### Project Root
*   **`manage.py`**: The command-line utility for administrative tasks (running server, migrations, etc.). **Do not edit this.**

### Configuration (`config/`)
*   **`settings.py`**: The central brain. Contains DB config, installed apps, static file paths, and security keys.
*   **`urls.py`**: The "Table of Contents" for the website. Routes incoming web requests to the correct app.
*   **`wsgi.py` / `asgi.py`**: Entry points for web servers (like Gunicorn/Daphne) to serve the project in production.

### App Structure (e.g., `portfolio/`)
Every app (folder) generally contains these files:

*   **`models.py`**: The Database Schema. Defines tables (Classes) and columns (Fields).
*   **`views.py`**: The Logic Layer. Functions that fetch data from models and pass it to templates.
*   **`urls.py`**: App-specific routing. Matches URL patterns to view functions.
*   **`admin.py`**: Configuration for the built-in Django Admin interface. Register models here to manage them easily.
*   **`apps.py`**: App metadata (name, readable name). Rarely edited.
*   **`tests.py`**: Unit tests. Code that checks if your other code is working correctly.
*   **`migrations/`**: A folder containing the history of database changes. **Do not edit these files manually.**
