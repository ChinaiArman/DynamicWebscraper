"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app


# DEFINE BLUEPRINT
scraping_bp = Blueprint('scraping_bp', __name__)


# ROUTES
@scraping_bp.route('/scrape/', methods=['GET'])
def scrape():
    """
    """
    return jsonify({"message": "scrape endpoint"})