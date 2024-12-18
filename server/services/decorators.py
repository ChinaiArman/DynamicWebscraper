"""
decorators.py
This module contains decorators for the DynamicWebscraper application.

Disclaimer
----------
This file was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
from functools import wraps
from flask import session, jsonify, request, current_app
import os
import json


# CONSTANTS
with open(os.getenv('USER_STRINGS_FILEPATH'), 'r') as file:
    USER_STRINGS = json.load(file)


# DECORATORS
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
    """
    @wraps(func)
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
        """
        if "user_id" in session:
            db = current_app.config['database']
            db.increment_total_requests(db.get_user_by_id(session.get('user_id')))
            return func(*args, **kwargs)
        else:
            return jsonify({"error": USER_STRINGS['decorators']['login']}), 401
    return wrapper


def api_key_required(func: callable) -> callable:
    """
    A decorator to require an API key for a route.

    Args
    ----
    func (callable): The function to decorate.

    Returns
    -------
    wrapper (callable): The decorated function.

    Disclaimer
    ----------
    This function was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    @wraps(func)
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
        """
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        api_key = request.headers.get('Authorization')
        try:
            if api_key:
                if api_key.startswith("Bearer "):
                    api_key = api_key.split(" ")[1]
                user = db.get_user_by_api_key(api_key)
                is_reset_available = authenticator.is_scrape_available(user)
                if is_reset_available:
                    db.reset_requests(user)
                if user.requests_available > 0:
                    db.decrement_requests_available(user)
                db.increment_total_requests(user)
                return func(*args, **kwargs)
            else:
                raise Exception(USER_STRINGS['decorators']['api'])
        except Exception as e:
            return jsonify({"error": str(e)}), 401
    return wrapper

def admin_required(func: callable) -> callable:
    """
    A decorator to require an admin user for a route.

    Args
    ----
    func (callable): The function to decorate.

    Returns
    -------
    wrapper (callable): The decorated function.

    Disclaimer
    ----------
    This function was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        """
        """
        if "user_id" in session:
            db = current_app.config['database']
            user = db.get_user_by_id(session.get('user_id'))
            if user.is_admin:
                db.increment_total_requests(user)
                return func(*args, **kwargs)
            else:
                return jsonify({"error": USER_STRINGS['decorators']['admin']}), 401
        else:
            return jsonify({"error": USER_STRINGS['decorators']['login']}), 401
    return wrapper
