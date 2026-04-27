# Flask Todo Manager 🚀

A simple, lightweight, and dynamic Todo application built using the **Flask** web framework. This project was created to explore full-stack development with Python, database management with SQLAlchemy, and dynamic templating with Jinja2.

## ✨ Features
- **Create Tasks:** Add new todos with a title and description.
- **View Tasks:** All tasks are displayed in a clean, responsive table.
- **Real-time Updates:** Uses a local SQLite database to persist your data.
- **Responsive Design:** Styled with **Bootstrap 5** for a modern look.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Frontend:** HTML5, Jinja2, Bootstrap 5
- **Environment:** Python Virtual Environment (venv)

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```python
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   >>> exit()
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be live at `http://127.0.0.1:5000`

## 📁 Project Structure
```text
.
├── app.py              # Main Flask application logic
├── templates/
│   └── index.html      # Main UI template (Jinja2)
├── instance/
│   └── my_todo.db      # SQLite database file (created after init)
├── requirements.txt    # List of project dependencies
└── .gitignore          # Files to exclude from Git
```

---
*Created by [Sourav](https://github.com/YOUR_USERNAME)*
