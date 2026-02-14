
import sqlite3
from datetime import datetime

DB_NAME = "expenses.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (date, amount, category, description)
        VALUES (?, ?, ?, ?)
    """, (date, amount, category, description))

    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")


def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    conn.close()

    if not expenses:
        print("No expenses found.")
        return

    print("\nID | Date | Amount | Category | Description")
    print("-" * 55)

    for exp in expenses:
        print(f"{exp[0]} | {exp[1]} | ${exp[2]:.2f} | {exp[3]} | {exp[4]}")


def filter_by_category():
    category = input("Enter category: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?",
        (category,)
    )

    expenses = cursor.fetchall()
    conn.close()

    if not expenses:
        print("No expenses found for this category.")
        return

    for exp in expenses:
        print(f"{exp[0]} | {exp[1]} | ${exp[2]:.2f} | {exp[3]} | {exp[4]}")


def edit_expense():
    view_expenses()
    expense_id = input("Enter expense ID to edit: ")

    amount = float(input("New Amount: "))
    category = input("New Category: ")
    description = input("New Description: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, expense_id))

    conn.commit()
    conn.close()
    print("✏️ Expense updated successfully!")


def delete_expense():
    view_expenses()
    expense_id = input("Enter expense ID to delete: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()
    print("🗑️ Expense deleted successfully!")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
    """, (month,))

    total = cursor.fetchone()[0]
    conn.close()

    if total:
        print(f"📊 Total expenses for {month}: ${total:.2f}")
    else:
        print(f"No expenses found for {month}.")


def main():
    create_table()

    while True:
        print("\nExpense Tracker (SQLite)")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Monthly Summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
