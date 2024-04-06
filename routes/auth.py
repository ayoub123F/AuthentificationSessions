# routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# Simulons une liste d'utilisateurs avec leurs rôles (Admin, Editor, Author, Guest)
users = {
    'admin': User('admin', 'adminpass', 'Admin'),
    'editor': User('editor', 'editorpass', 'Editor'),
    'author': User('author', 'authorpass', 'Author'),
    'guest': User('guest', 'guestpass', 'Guest')
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username].password == password:
            session['username'] = username
            return redirect(url_for('dashboard.admin_dashboard'))
        else:
            return "Invalid username or password"
    return render_template('login.html')

def login_required(role):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if 'username' not in session or users[session['username']].role != role:
                return redirect(url_for('auth.login'))
            return func(*args, **kwargs)
        return decorated_function
    return wrapper

