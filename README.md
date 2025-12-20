# Secure Flask Auth System
_[Matthew 7:24-25](https://biblia.com/bible/niv/matthew/7/24-25)_

A simple, robust and secure Full-Stack web application built with Python and Flask. This project demonstrates core backend principles including database persistence, password security, and session management.

## Features
- **Secure Authentication**: Password hashing using `pbkdf2:sha256` via Werkzeug.
- **Session Management**: Protected routes (Dashboard) that require a valid login.
- **Database Persistence**: SQLite database integrated with Flask-SQLAlchemy.
- **Modern UI**: Styled with Tailwind CSS for a professional look and feel.
- **Robust Error Handling**: Custom 404 "Not Found" page and flash messaging for user feedback.

## Tech Stack
- **Backend**: Python, Flask
- **Database**: SQLite, Flask-SQLAlchemy
- **Frontend**: HTML5, Tailwind CSS
- **Security**: Werkzeug Security Helpers

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AwaniCaleb/python-backend
   cd python-backend

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Initialize the Database**: Run these commands in your terminal:
    ```python
    python
    >>> from app import app, db
    >>> with app.app_context():
    ...     db.create_all()
    >>> exit()

5. **Run the App**:
    ```bash
    flask run

## Project Structure

* `app.py`: Main application logic, models, and routes.
* `instance/`: Contains the SQLite `project.db` file.
* `templates/`: Jinja2 HTML templates (Login, Dashboard, 404, and other shi).

---

### `requirements.txt`
GitHub and deployment platforms use this file to know which libraries to install. You can generate this automatically by running `pip freeze > requirements.txt` in your terminal (which is what I did btw), or just create a file with this content (basically):

```text
Flask
Flask-SQLAlchemy
Werkzeug
