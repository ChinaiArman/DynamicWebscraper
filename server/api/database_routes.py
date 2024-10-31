"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session


# DEFINE BLUEPRINT
database_bp = Blueprint('database_bp', __name__)


# LOGIN DECORATOR
def login_required(func):
    """
    """
    def wrapper(*args, **kwargs):
        """
        """
        if "user_id" in session:
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "login required"}), 401
    wrapper.__name__ = func.__name__
    return wrapper


# ROUTES
@database_bp.route('/database/get-user-information/', methods=['GET'])
@login_required
def get_user_information():
    """
    """
    return jsonify({"message": "get user information endpoint"})

@database_bp.route('/database/get-scrape-history/', methods=['GET'])
@login_required
def get_scrape_history():
    """
    """
    return jsonify({"message": "get scrape history endpoint"})

@database_bp.route('/database/save-scrape/', methods=['POST'])
@login_required
def save_scrape():
    """
    """
    return jsonify({"message": "save scrape endpoint"})
