"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app


# DEFINE BLUEPRINT
scraping_bp = Blueprint('scraping_bp', __name__)


# API KEY DECORATOR
def api_key_required(func):
    def wrapper(*args, **kwargs):
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