# Simple_Quotes_CRUD

A very simple, web-based CRUD (Create, Read, Update, Delete) application built with Django. This project allows users to manage a personal collection of quotes, providing a clean interface to store and reflect on meaningful snippets of text.

🚀 Features
Create: Add new quotes with an author name.
Read: View a list of all saved quotes on a central dashboard.
Update: Edit existing quotes or update the author details.
Delete: Remove quotes from the database with a single click.
Persistent Storage: Uses SQLite to ensure your quotes are saved locally.

🛠️ Tech Stack
Framework: Django(Python)
Database: SQLite (Default)
Frontend: HTML5, CSS3 (Django Templates)

📋 Prerequisites
Before running this project, ensure you have the following installed:
Python 3.8 or higher
pip (Python package manager)

⚙️ Installation & Setup
1. Clone the repository - git clone https://github.com/shruti838/simple-quotes-project.gi
                          cd simple-quotes-project
2. Create a Virtual Environment - python -m venv venv
                                  venv\Scripts\activate

3. Install Dependencies - pip install django
   
4. Run Database Migrations - python manage.py makemigrations
                              python manage.py migrate
   
5. Start the Development Server - http://127.0.0.1:8000
