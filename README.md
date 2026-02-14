# 💰 Expense Tracker App

A simple and elegant web application for tracking personal expenses, built with Flask and SQLite.

## ✨ Features

- **Add Expenses**: Quickly log expenses with amount, category, and description
- **View All Expenses**: See all your expenses in a clean, organized table
- **Monthly Summary**: Get detailed breakdowns of spending by month
- **Visual Analytics**: Interactive charts showing spending patterns by category
- **Category Breakdown**: See exactly where your money is going
- **Responsive Design**: Works great on desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jenssen10/expense-tracker-app.git
   cd expense-tracker-app
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   
   Navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
expense-tracker-app/
├── app.py                 # Main Flask application
├── expenses.db            # SQLite database (auto-created)
├── templates/
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page (add/view expenses)
│   ├── summary.html      # Monthly summary page
│   └── charts.html       # Analytics and charts page
└── README.md
```

## 🎯 Usage

### Adding an Expense

1. Go to the home page
2. Fill in the expense form:
   - **Amount**: Enter the cost
   - **Category**: Choose from predefined categories (Food, Transport, Entertainment, etc.)
   - **Description**: Add a brief note
3. Click "Add Expense"

### Viewing Monthly Summary

1. Click "Monthly Summary" in the navigation
2. Select a month from the date picker
3. View total spending and category breakdown

### Analyzing with Charts

1. Click "Charts" in the navigation
2. Select a month to visualize
3. See:
   - Doughnut chart showing expense distribution by category
   - Bar chart showing total monthly spending
   - Summary statistics (total, count, average)

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js
- **Template Engine**: Jinja2

## 📊 API Endpoints

The app includes a RESTful API for programmatic access:

- `GET /api/expenses` - Get all expenses
- `POST /api/expenses` - Add new expense
- `PUT /api/expenses/<id>` - Update expense
- `DELETE /api/expenses/<id>` - Delete expense
- `GET /api/summary/<month>` - Get monthly summary (format: YYYY-MM)
- `GET /api/summary/<month>/by-category` - Get category breakdown

## 🎨 Categories

- 🍔 Food
- 🚗 Transport
- 🎬 Entertainment
- 🛍️ Shopping
- 💡 Bills
- 🏥 Health
- 📦 Other

## 🔮 Future Enhancements

- [ ] User authentication and multiple user support
- [ ] Budget limits and alerts
- [ ] Expense editing functionality
- [ ] Export data to CSV/Excel
- [ ] Receipt upload and storage
- [ ] Recurring expenses
- [ ] Multi-currency support
- [ ] Mobile app

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Jenssen**
- GitHub: [@jenssen10](https://github.com/jenssen10)

## 🙏 Acknowledgments

- Built with Flask
- Charts powered by Chart.js
- Icons from emoji unicode

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
