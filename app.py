from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import sqlite3
from contextlib import contextmanager

app = Flask(__name__)

# Database file
DATABASE = 'expenses.db'


# ========================================
# DATABASE SETUP
# ========================================
def init_db():
    """Initialize the database with the expenses table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database initialized!")


def connect_db():
    """Connect to the SQLite database"""
    return sqlite3.connect(DATABASE)


@contextmanager
def get_db():
    """Context manager for database connections"""
    conn = connect_db()
    try:
        yield conn
    finally:
        conn.close()


# ========================================
# WEB ROUTES (HTML Pages)
# ========================================
@app.route('/')
def index():
    """Home page - show all expenses"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        expenses = cursor.fetchall()
    
    return render_template('index.html', expenses=expenses)


@app.route('/summary')
def summary():
    """Monthly summary page"""
    return render_template('summary.html')


@app.route('/charts')
def charts():
    """Charts and analytics page"""
    return render_template('charts.html')


@app.route('/add', methods=['POST'])
def add_expense():
    """Add a new expense from the web form"""
    amount = request.form.get('amount')
    category = request.form.get('category')
    description = request.form.get('description')
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (date, amount, category, description)
            VALUES (?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d"),
            amount,
            category,
            description
        ))
        conn.commit()
    
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_expense(id):
    """Delete an expense"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
        conn.commit()
    
    return redirect(url_for('index'))


# ========================================
# API ROUTES (JSON)
# ========================================
@app.route("/api/expenses", methods=["GET"])
def api_get_expenses():
    """Get all expenses as JSON"""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
            rows = cursor.fetchall()

        expenses = [
            {
                "id": r[0],
                "date": r[1],
                "amount": float(r[2]),
                "category": r[3],
                "description": r[4]
            } for r in rows
        ]

        return jsonify(expenses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/expenses", methods=["POST"])
def api_add_expense():
    """Add a new expense via API"""
    data = request.json
    
    # Validate required fields
    required_fields = ["amount", "category", "description"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Validate amount is positive number
    try:
        amount = float(data["amount"])
        if amount <= 0:
            return jsonify({"error": "Amount must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount format"}), 400

    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (date, amount, category, description)
                VALUES (?, ?, ?, ?)
            """, (
                datetime.now().strftime("%Y-%m-%d"),
                amount,
                data["category"],
                data["description"]
            ))
            conn.commit()
            expense_id = cursor.lastrowid

        return jsonify({
            "message": "Expense added",
            "id": expense_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/expenses/<int:id>", methods=["PUT"])
def api_update_expense(id):
    """Update an existing expense"""
    data = request.json
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Check if expense exists
            cursor.execute("SELECT id FROM expenses WHERE id=?", (id,))
            if not cursor.fetchone():
                return jsonify({"error": "Expense not found"}), 404
            
            cursor.execute("""
                UPDATE expenses
                SET amount=?, category=?, description=?
                WHERE id=?
            """, (data["amount"], data["category"], data["description"], id))
            
            conn.commit()

        return jsonify({"message": "Expense updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/expenses/<int:id>", methods=["DELETE"])
def api_delete_expense(id):
    """Delete an expense via API"""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Check if exists before deleting
            cursor.execute("SELECT id FROM expenses WHERE id=?", (id,))
            if not cursor.fetchone():
                return jsonify({"error": "Expense not found"}), 404
            
            cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
            conn.commit()

        return jsonify({"message": "Expense deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/summary/<month>")
def api_monthly_summary(month):
    """Get monthly summary"""
    # Validate month format (YYYY-MM)
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return jsonify({"error": "Invalid month format. Use YYYY-MM"}), 400

    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(amount), COUNT(*)
                FROM expenses
                WHERE strftime('%Y-%m', date) = ?
            """, (month,))
            result = cursor.fetchone()
            total = result[0] or 0
            count = result[1] or 0

        return jsonify({
            "month": month,
            "total": float(total),
            "count": count
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/summary/<month>/by-category")
def api_category_breakdown(month):
    """Get category breakdown for a specific month"""
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return jsonify({"error": "Invalid month format. Use YYYY-MM"}), 400

    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT category, SUM(amount) as total, COUNT(*) as count
                FROM expenses
                WHERE strftime('%Y-%m', date) = ?
                GROUP BY category
                ORDER BY total DESC
            """, (month,))
            rows = cursor.fetchall()

        breakdown = [
            {
                "category": r[0],
                "total": float(r[1]),
                "count": r[2]
            } for r in rows
        ]

        return jsonify({
            "month": month,
            "categories": breakdown
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ========================================
# RUN THE APP
# ========================================
if __name__ == '__main__':
    print("🚀 Starting Expense Tracker...")
    init_db()  # Initialize database on startup
    print("📊 Server running at http://127.0.0.1:5000")
    print("Press CTRL+C to stop")
    app.run(debug=True, port=5000)
