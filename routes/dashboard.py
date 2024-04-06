# routes/dashboard.py
from flask import Blueprint, session
from routes.auth import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required('Admin')
def admin_dashboard():
    return "Admin Dashboard - All user management actions allowed"

@dashboard_bp.route('/profile')
@login_required('Guest')
def guest_profile():
    return f"Guest Profile - Viewing and editing allowed for user: {session['username']}"
