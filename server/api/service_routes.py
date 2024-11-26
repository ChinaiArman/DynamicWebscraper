"""
service_routes.py
This module contains the service routes for the DynamicWebscraper application.

Disclaimer
----------
The swagger documentation was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app

from services.decorators import api_key_required


# DEFINE BLUEPRINT
service_bp = Blueprint('service_bp', __name__)


# ROUTES
@service_bp.route('/service/register', methods=['POST'])
def register() -> tuple:
    """
    Register a New User
    ---
    tags:
      - Registration
    requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  description: "The email address of the user to register."
                password:
                  type: string
                  description: "The password for the user's account."
    responses:
      200:
        description: Successfully registered user and sent verification email.
        content:
          application/json:
            schema:
              type: object
              properties:
                userInfo:
                  type: object
                  description: The user information.
                message:
                  type: string
                  description: Confirmation message about email verification.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email_manager = current_app.config['emailManager']
        email = request.json.get('email')
        authenticator.validate_email(email)
        password = authenticator.encrypt_password(request.json.get('password'))
        verification_code = authenticator.generate_one_time_code()
        user = db.create_user(email, password, verification_code)
        db.increment_total_requests(user)
        email_manager.send_verification_email(email, user.email, verification_code)
        return jsonify({"userInfo": user.to_dict(), "message": "Check email for verification code"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/verify/<int:user_id>', methods=['POST'])
def verify(user_id) -> tuple:
    """
    Verify User Account
    ---
    tags:
      - Registration
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
        description: The unique ID of the user to verify.
    requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - verification_code
              properties:
                verification_code:
                  type: string
                  description: "The verification code sent to the user's email."
    responses:
      200:
        description: Verification successful, user account activated.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Confirmation message indicating successful verification.
      401:
        description: Unauthorized. Verification failed due to invalid code or other issues.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        user = db.get_user_by_id(user_id)
        verification_code = request.json.get('verification_code')
        authenticator.verify_code(verification_code, user.verification_code)
        api_key = authenticator.generate_api_key()
        db.verify_user(user, api_key)
        return jsonify({"message": "verification successful", "api_key": api_key}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@service_bp.route('/service/query', methods=['GET'])
@api_key_required
def query() -> tuple:
    """
    Service Query Endpoint.
    ---
    tags:
      - AI Service
    security:
      - bearerAuth: []
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
                  type: object
                  description: The AI-generated response to the query.
                warning:
                  type: string
                  description: Warning message about remaining requests.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        db.create_scrape(user.id, url, prompt, str(response))

        # if user.requests_available > 0, add a warning to the response
        if user.requests_available <= 0:
            response = {
                "result": response,
                "warning": "You have 0 requests remaining."
            }
        else:
            response = {
                "result": response
            }

        # Return the response
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/user-info', methods=['GET'])
@api_key_required
def user_info() -> tuple:
    """
    Retrieve User Information
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    responses:
      200:
        description: Successfully retrieved user information.
        content:
          application/json:
            schema:
              type: object
              properties:
                user:
                  type: object
                  description: The user information.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/update-user-info', methods=['PATCH'])
@api_key_required
def update_user_info() -> tuple:
    """
    Update User Information
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                  description: "The new email address for the user."
                password:
                  type: string
                  description: "The new password for the user's account."
    responses:
      200:
        description: Successfully updated user information.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Confirmation message indicating successful update.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        email = request.json.get('email')
        password = request.json.get('password')
        if email:
            db.update_email(user, email)
        if password:
            authenticator = current_app.config['authenticator']
            password = authenticator.hash_password(password)
            db.update_password(user, password)
        return jsonify({'message': 'User info updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/delete-user', methods=['DELETE'])
@api_key_required
def delete_user() -> tuple:
    """
    Delete User Account
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    responses:
      200:
        description: Successfully deleted user account.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Confirmation message indicating successful deletion.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        db.delete_user(user.id)
        return jsonify({'message': 'User deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@service_bp.route('/service/query-history', methods=['GET'])
@api_key_required
def query_history() -> tuple:
    """
    Get Query History
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    responses:
      200:
        description: Successfully retrieved query history.
        content:
          application/json:
            schema:
              type: object
              properties:
                scrapes:
                  type: array
                  items:
                    type: object
                    description: The scrape information.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        scrapes = db.get_scrapes_by_user_id(user.id)
        return jsonify({"scrapes": [scrape.to_dict() for scrape in scrapes]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/query-history/<int:scrape_id>', methods=['GET'])
@api_key_required
def query_history_by_id(scrape_id: int) -> tuple:
    """
    Get Query History by ID
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    parameters:
      - name: scrape_id
        in: path
        required: true
        schema:
          type: integer
        description: The unique ID of the scrape to retrieve.
    responses:
      200:
        description: Successfully retrieved query history by ID.
        content:
          application/json:
            schema:
              type: object
              properties:
                scrape:
                  type: object
                  description: The scrape information.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        scrape = db.get_scrape_by_id(scrape_id)
        if scrape.user_id != user.id:
            return jsonify({'error': 'Scrape not found'}), 400
        return jsonify(scrape.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@service_bp.route('/service/query-history/<int:scrape_id>', methods=['DELETE'])
@api_key_required
def delete_query_history(scrape_id: int) -> tuple:
    """
    Delete Query History by ID
    ---
    tags:
      - User Information
    security:
      - bearerAuth: []
    parameters:
      - name: scrape_id
        in: path
        required: true
        schema:
          type: integer
        description: The unique ID of the scrape to delete.
    responses:
      200:
        description: Successfully deleted query history by ID.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Confirmation message indicating successful deletion.
      400:
        description: Bad request due to missing data or other errors.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message explaining what went wrong.
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
        api_key = request.headers.get('Authorization')
        if api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
        db = current_app.config['database']
        user = db.get_user_by_api_key(api_key)
        scrape = db.get_scrape_by_id(scrape_id)
        if scrape.user_id != user.id:
            return jsonify({'error': 'Scrape not found'}), 400
        db.delete_scrape(scrape_id)
        return jsonify({'message': 'Scrape deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
