# Flask Todo Manager 🚀

A simple, lightweight, and dynamic Todo application built using the **Flask** web framework. This project was created to explore full-stack development with Python, database management with SQLAlchemy, and dynamic templating with Jinja2.

## ✨ Features (Version 2.0 Updates)
- **Full CRUD Operations:** You can now Create, Read, **Update**, and **Delete** your tasks!
- **Template Inheritance:** The frontend has been refactored to use a `Base.html` layout, making the code much cleaner and easier to manage.
- **View Tasks:** All tasks are displayed in a clean, responsive table.
- **Real-time Updates:** Uses a local SQLite database to persist your data.
- **Responsive Design:** Styled with **Bootstrap 5** for a modern look.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Frontend:** HTML5, Jinja2, Bootstrap 5, CSS
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
<div align="center">

# 🚀 QuickTask Web

**A Sleek, Modern, & High-Performance Todo Manager Built with Flask**

[![Python Version](https://img.shields.io/badge/Python-3.14+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-latest-black.svg?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3.svg?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)

[Features](#-key-features) •
[Installation](#%EF%B8%8F-installation-guide) •
[Usage](#-how-to-use) •
[Architecture](#-project-architecture)

---

</div>

## 🌟 About The Project

**QuickTask Web** is a beautifully designed, full-stack web application that helps you organize your daily life. Designed with a **minimalist, premium dark theme**, it provides a distraction-free environment to manage your workflow. 

It was built from the ground up to demonstrate mastery of Python backend architecture (Flask/SQLAlchemy) paired with a responsive, glassmorphic frontend (Jinja2/Bootstrap/Custom CSS).

---

## ✨ Key Features

<details>
<summary><b>🛠 Full CRUD Operations</b> (Click to expand)</summary>
Create, Read, Update, and Delete your tasks seamlessly without page reloads interrupting your flow.
</details>

<details>
<summary><b>🎨 Premium Dark Aesthetics</b> (Click to expand)</summary>
A custom-built dark mode featuring glassmorphism, soft drop-shadows, hover micro-animations, and the modern 'Inter' typeface.
</details>

<details>
<summary><b>🏷️ Smart Categorization</b> (Click to expand)</summary>
Assign tags to your tasks: <code>General</code>, <code>Music</code>, <code>Study</code>, <code>Finance</code>, <code>Work</code>, <code>Watchlist</code>, and <code>Shopping</code>.
</details>

<details>
<summary><b>🔍 Instant Filtering</b> (Click to expand)</summary>
Use the interactive navigation bar dropdown to instantly filter your task list by specific categories.
</details>

---

## 📸 Sneak Peek
*(Replace this section with a screenshot of your beautiful dark-themed app!)*
> Example: `![App Screenshot](link-to-your-image.png)`

---

## ⚙️ Installation Guide

Follow these simple steps to get a local copy up and running.

### 1. Clone the Repository
```bash
git clone https://github.com/SouravEmpire07/QuickTask-Web.git
cd QuickTask-Web
```

### 2. Set Up Your Environment
We highly recommend using a virtual environment to keep dependencies clean.
```bash
# Create the environment
python3 -m venv .flenv

# Activate it (Mac/Linux)
source .flenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Before running the app for the first time, you need to create the SQLite database structure.
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 5. Launch the App! 🚀
```bash
python app.py
```
> Open your browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🏗 Project Architecture

Here is how the project is structured to maintain clean, scalable code:

```text
.
├── app.py              # Main Flask application logic (Routes & DB Models)
├── templates/
│   ├── Base.html       # Master layout template (Jinja2)
│   ├── index.html      # Homepage and Todo list view
│   └── update.html     # Form page for updating existing Todos
├── instance/
│   └── my_todo.db      # SQLite database file (created after init)
├── requirements.txt    # List of project dependencies
└── .gitignore          # Files to exclude from Git
📦 QuickTask-Web
 ┣ 📂 instance/            # 🗄️ Auto-generated SQLite Database (my_todo.db)
 ┣ 📂 static/
 ┃ ┗ 📜 style.css          # 🎨 Custom dark theme, animations, and typography
 ┣ 📂 templates/           # 🖼️ Frontend Jinja2 Views
 ┃ ┣ 📜 Base.html          # Master layout (Navbar, CSS/JS links)
 ┃ ┣ 📜 index.html         # Homepage dashboard (Add task, Table View)
 ┃ ┗ 📜 update.html        # Task editing interface
 ┣ 📜 app.py               # 🧠 Core Backend Logic (Routing & SQLAlchemy Models)
 ┣ 📜 requirements.txt     # 📦 Project dependencies
 ┗ 📜 README.md            # 📖 You are here!
```

---
*Created by [Sourav](https://github.com/YOUR_USERNAME)*

<div align="center">
  <b>Built with ❤️ by <a href="https://github.com/SouravEmpire07">Sourav</a></b>
  <br><br>
  <i>If you found this project helpful, please consider giving it a ⭐!</i>
</div>
