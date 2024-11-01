"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app

from services.decorators import api_key_required


# DEFINE BLUEPRINT
scraping_bp = Blueprint('scraping_bp', __name__)


# ROUTES
@scraping_bp.route('/scrape/', methods=['GET'])
@api_key_required
def scrape():
    """
    """
    return jsonify({"message": "scrape endpoint"})
