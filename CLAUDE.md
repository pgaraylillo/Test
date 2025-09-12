# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a Flask-based blog application with user authentication, blog post management, and commenting functionality. The application is structured for deployment and includes production dependencies like gunicorn and PostgreSQL support.

## Development Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt
# or on macOS
pip3 install -r requirements.txt
```

### Running the Application
```bash
# Development server
python main.py
# Runs on http://localhost:5000 with debug=True (port 5000 is default)
# The app is configured to run on host="0.0.0.0" for deployment compatibility
```

### Production Deployment
The app is configured for production deployment with:
- Gunicorn WSGI server (included in requirements.txt)
- PostgreSQL support via psycopg2-binary
- Environment variable configuration for secrets
- Procfile configured for Heroku deployment (`web: gunicorn main:app`)

## Architecture

### Core Components
- **main.py**: Main Flask application with all routes and database models
- **forms.py**: WTForms definitions for all user input forms
- **templates/**: Jinja2 templates for all pages
- **static/**: Static assets (CSS, JS, images)
- **instance/**: Contains SQLite database file (posts.db)

### Database Models
The application uses SQLAlchemy with three main models:
1. **User**: Handles authentication and user management
2. **BlogPost**: Blog posts with author relationships  
3. **Comment**: Comments with relationships to both users and posts

### Key Features
- User registration and authentication with Flask-Login
- Admin-only post creation/editing/deletion (user ID 1 is admin)
- Rich text editing with CKEditor for blog posts and comments
- Gravatar integration for user avatars
- Bootstrap 5 for responsive design

### Environment Variables
- `FLASK_KEY`: Secret key for Flask sessions
- `DB_URI`: Database connection string (defaults to SQLite if not set)

### Important Notes
- Admin functionality is restricted to user with ID 1 (first registered user becomes admin)
- The `@admin_only` decorator in main.py:118 enforces admin-only routes
- Database tables are auto-created on first run via `db.create_all()`
- The app supports both SQLite (development) and PostgreSQL (production)
- User passwords are hashed using PBKDF2 with SHA-256
- Edit post route (line 242) is missing the `@admin_only` decorator