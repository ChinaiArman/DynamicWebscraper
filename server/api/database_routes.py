"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app


# DEFINE BLUEPRINT
database_bp = Blueprint('database_bp', __name__)


# ROUTES
@database_bp.route('/database/get-user-information', methods=['GET'])
def get_user_information():
    """
    """
    return jsonify({"message": "get user information endpoint"})

@database_bp.route('/database/get-scrape-history', methods=['GET'])
def get_scrape_history():
    """
    """
    return jsonify({"message": "get scrape history endpoint"})

@database_bp.route('/database/save-scrape', methods=['POST'])
def save_scrape():
    """
    """
    return jsonify({"message": "save scrape endpoint"})
