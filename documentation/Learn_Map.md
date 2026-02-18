# 🗺️ Altair Finance: Learning Map & Deep Dive

This guide explains how the **Altair Finance** codebase is structured and how the different layers (HTML, CSS, JS, and Python) work together to create a premium dashboard experience.

---

## 🏗️ 1. Project Architecture

The project is built using **Django**, a high-level Python web framework. It is divided into three main "apps":

1.  **`accounts/`**: Handles user login, registration, and the Custom User Model (which allows us to use email or roles).
2.  **`core/`**: Contains the public landing page (Home) and shared components.
3.  **`dashboard/`** (or `user_dashboard/`): This is the "Command Center" where users see their financials, graphs, and transaction history.

---

## 🛣️ 2. The "Request Journey" (How it Works)

When you click on **"/dashboard/"**, here is what happens behind the scenes:

1.  **URL Dispatcher (`urls.py`)**: Django looks at the URL and says, "This belongs to the Dashboard View."
2.  **Authentication Control**: The `@login_required` decorator checks if you are logged in. If not, it redirects you to the login page.
3.  **The View (`views.py`)**: The Python code runs logic (like calculating your net worth or fetching recent transactions) and sends it to the template.
4.  **Template Rendering (`.html`)**: Django combines the Python data with your HTML to create the final page.

---

## 🎨 3. The Tech Stack (Frontend)

We used a modern, "Premium" stack to make the UI feel fast and smooth:

-   **Tailwind CSS**: Instead of writing thousands of lines of custom CSS, we use utility classes (like `bg-white`, `rounded-2xl`, `shadow-sm`) directly in the HTML. This makes the design extremely consistent.
-   **Lucide Icons**: A clean, lightweight icon library used for all sidebar and card icons.
-   **Chart.js**: The powerful engine behind the "Transactions Overview" graph. It handles the animations, tooltip hover effects, and drawing the lines.
-   **Alpine.js**: A tiny JavaScript framework used for simple UI effects, like hiding/showing the "Upgrade Pro" banner.

---

## 🧱 4. Template Inheritance (The "Lego" System)

To keep the code clean, we use a system called **Template Inheritance**:

-   **`base.html` / `user_base.html`**: These are the "parent" frames. They contain the sidebar, the top header, and the background. They stay the same on every page.
-   **`user_db.html`**: This is the "child" page. It only contains the content *inside* the main area. It "plugs into" the parent frame using `{% block content %}`.

---

## 📊 5. Financial Mock Data

Currently, the numbers in the dashboard (like ₹24,80,000) are **placeholders** for demonstration. In the next phase of development, we will connect these to a real database so they update whenever a user adds a new transaction.

---

## 💡 How to read this code?

If you want to understand how a specific feature works:
1.  Open **`views.py`** to see the logic.
2.  Open the corresponding **`.html`** file to see how it's styled.
3.  Check the **`<script>`** tags at the bottom of the HTML to see any interactive behavior.

🚀 **Happy Coding!**
