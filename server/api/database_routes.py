"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session


# DEFINE BLUEPRINT
database_bp = Blueprint('database_bp', __name__)


# LOGIN DECORATOR
def login_required(func: callable) -> callable:
    """
    A decorator to require login for a route.

    Args
    ----
    func (callable): The function to decorate.

    Returns
    -------
    wrapper (callable): The decorated function.

    Disclaimer
    ----------
    This function was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.

    Author: ``@ChinaiArman``
    """
    def wrapper(*args, **kwargs) -> callable:
        """
        The wrapper function for the decorator.

        Args
        ----
        *args: The arguments for the function.
        **kwargs: The keyword arguments for the function.

        Returns
        -------
        func(*args, **kwargs): The decorated function.

        Disclaimer
        ----------
        This function was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.

        Author: ``@ChinaiArman``
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
def get_user_information() -> tuple:
    """
    Get user information.

    Args
    ----
    None

    Returns
    -------
    tuple: The user information and status code.

    Author: ``@ChinaiArman``
    """
    try:
        db = current_app.config['database']
        user_id = session["user_id"]
        user = db.get_user_by_id(user_id)
        return jsonify({"user": user.to_dict()}), 200
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

    Author: ``@ChinaiArman``
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

    Author: ``@ChinaiArman``
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
