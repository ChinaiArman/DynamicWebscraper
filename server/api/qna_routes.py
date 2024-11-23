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
    QnA Query Endpoint
    ---
    tags:
      - QnA
    security:
      - BearerAuth: []  # This is the security definition being used
    parameters:
      - name: url
        in: query
        required: true
        schema:
          type: string
        description: The URL of the content to scrape.
      - name: prompt
        in: query
        required: true
        schema:
          type: string
        description: The prompt or question to query the AI server with.
    responses:
      200:
        description: Successful response containing the AI-generated answer.
        content:
          application/json:
            schema:
              type: object
              properties:
                result:
                  type: string
                  description: The AI-generated response to the query.
      400:
        description: Error response due to a bad request or exception.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: The error message explaining the failure.
      401:
        description: Unauthorized. No valid Bearer Token provided.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining the lack of authorization.
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

        # Get user information from API key
        api_key = request.headers.get('Authorization').split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        db.create_scrape(user.id, url, prompt, str(response))

        # Return the response
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
