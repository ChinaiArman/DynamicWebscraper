"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app

from services.decorators import api_key_required


# DEFINE BLUEPRINT
qna_bp = Blueprint('qna_bp', __name__)


# ROUTES
@qna_bp.route('/qna/query', methods=['GET'])
@api_key_required
def qna() -> tuple:
    """
    Query the AI server.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        # Get the URL from the request
        url = request.args.get('url')
        prompt = request.args.get('prompt')

        # Scrape the URL
        scraper = current_app.config['scraper']
        context = scraper.scrape(url)

        # Query the AI server
        llm_manager = current_app.config['llmManager']
        response = llm_manager.query(prompt, context)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
