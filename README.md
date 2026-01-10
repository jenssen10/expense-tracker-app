# expense-tracker-app

# Expense Tracker (Python + SQLite)

A command-line expense tracker built with **Python** and **SQLite** that allows users to record, manage, and analyze personal expenses. The application supports full CRUD operations, category-based filtering, and monthly expense summaries using SQL queries.

This project demonstrates practical backend development skills, including database design, data persistence, and structured application logic.

---

## 🚀 Features

* ➕ Add new expenses
* 📄 View all recorded expenses
* 🗂️ Filter expenses by category
* ✏️ Edit existing expenses
* 🗑️ Delete expenses
* 📊 View monthly expense summaries
* 💾 Persistent storage using SQLite

---

## 🛠️ Technologies Used

* **Python 3**
* **SQLite (sqlite3 module)**
* **SQL**
* Command-Line Interface (CLI)

---

## 📁 Project Structure

```
expense_tracker/
│
├── expense_tracker.py   # Main application logic
└── expenses.db          # SQLite database (auto-created)
```

---

## 🗄️ Database Schema

The application uses a single SQLite table:

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    amount REAL,
    category TEXT,
    description TEXT
);
```

---

## ▶️ How to Run the Application

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Run the program

```bash
python expense_tracker.py
```

The database file (`expenses.db`) will be created automatically on first run.

---

## 📌 Usage Overview

When the program starts, you will see a menu with the following options:

```
1. Add Expense
2. View Expenses
3. Filter by Category
4. Edit Expense
5. Delete Expense
6. Monthly Summary
7. Exit
```

Follow the prompts to interact with the expense tracker.

---

## 📊 Monthly Summary

The monthly summary feature uses SQL date filtering:

```
YYYY-MM
```

Example:

```
2026-01
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* CRUD operations with SQLite
* SQL queries and aggregations
* Data persistence
* CLI application design
* Separation of concerns in Python

---

## 📄 Resume Description

> Developed a Python-based expense tracker using SQLite with full CRUD functionality, category filtering, and monthly expense aggregation via SQL queries.

---

## 🔮 Future Improvements

* 📈 Data visualization with Matplotlib
* 🖥️ GUI version using Tkinter
* 🌐 Web version using Flask
* 🔐 User authentication
* 📤 Export reports to CSV or PDF

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**Jenssen Honore**
Aspiring Software Developer
