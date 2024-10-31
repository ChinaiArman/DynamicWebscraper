"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app


# DEFINE BLUEPRINT
scraping_bp = Blueprint('scraping_bp', __name__)


# API KEY DECORATOR
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
        if api_key and api_key.startswith("Bearer "):
            try:
                api_key = api_key.split(" ")[1]
                user = db.get_user_by_api_key(api_key)
                authenticator.is_scrape_available(user)
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401
    wrapper.__name__ = func.__name__
    return wrapper


# ROUTES
@scraping_bp.route('/scrape/', methods=['GET'])
@api_key_required
def scrape():
    """
    """
    return jsonify({"message": "scrape endpoint"})
