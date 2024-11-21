"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import login_required, admin_required

# DEFINE BLUEPRINT
database_bp = Blueprint('database_bp', __name__)


# ROUTES
@database_bp.route('/database/get-user-information/', methods=['GET'])
@login_required
def get_user_information() -> tuple:
    """
    Get user information.

    Args
    ----
    None

    Returns
    -------
    tuple: The user information and status code.
    """
    try:
        db = current_app.config['database']
        user_id = session["user_id"]
        user = db.get_user_by_id(user_id).to_dict()
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@database_bp.route('/database/get-scrape-history/', methods=['GET'])
@login_required
def get_scrape_history() -> tuple:
    """
    Get scrape history.

    Args
    ----
    None

    Returns
    -------
    tuple: The scrape history and status code.
    """
    try:
        db = current_app.config['database']
        user_id = session["user_id"]
        scrapes = db.get_scrapes_by_user_id(user_id)
        return jsonify({"scrapes": [scrape.to_dict() for scrape in scrapes]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@database_bp.route('/database/change-name/', methods=['POST'])
@login_required
def change_name() -> tuple:
    """
    Change the name of the user.

    Args
    ----
    None

    Returns
    -------
    tuple: The response and status code.
    """
    try:
        db = current_app.config['database']
        user_id = session["user_id"]
        name = request.json.get('name')
        user = db.get_user_by_id(user_id)
        db.update_user(user, name)
        return jsonify({"message": "name changed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@database_bp.route('/database/get-all-users/', methods=['POST'])
@admin_required
def get_all_users() -> tuple:
    """
    Get all users.

    Args
    ----
    None

    Returns
    -------
    tuple: The users and status code.
    """
    try:
        db = current_app.config['database']
        users = db.get_all_users()
        return jsonify({"users": [user.to_dict() for user in users]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@database_bp.route('/database/get-endpoint-usage/', methods=['GET'])
@admin_required
def get_endpoint_usage() -> tuple:
    """
    Get the endpoint usage.

    Args
    ----
    None

    Returns
    -------
    tuple: The endpoint usage and status code.
    """
    try:
        db = current_app.config['database']
        endpoint_usage = db.get_endpoint_usage()
        return jsonify({"endpoint_usage": endpoint_usage}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400