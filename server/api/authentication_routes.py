"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import login_required, admin_required


# DEFINE BLUEPRINT
authentication_bp = Blueprint('authentication_bp', __name__)


# ROUTES
@authentication_bp.route('/authenticate/login/', methods=['POST'])
def login() -> tuple:
    """
    Login a user.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        password = request.json.get('password')
        user = db.get_user_by_email(email)
        authenticator.verify_password(password, user.password)
        session.permanent = True
        session["user_id"] = user.id
        return jsonify({"message": "login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/logout/', methods=['POST'])
@login_required
def logout() -> tuple:
    """
    Logout a user.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        session.clear()
        return jsonify({"message": "logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/register/', methods=['PUT'])
def register() -> tuple:
    """
    Register a user.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email_manager = current_app.config['emailManager']
        email = request.json.get('email')
        password = authenticator.encrypt_password(request.json.get('password'))
        verification_code = authenticator.generate_one_time_code()
        user = db.create_user(email, password, verification_code)
        session.permanent = True
        session["user_id"] = user.id
        email_manager.send_verification_email(email, user.username, verification_code)
        return jsonify({"message": "registration successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/reset-password/', methods=['POST'])
def reset_password() -> tuple:
    """
    Reset a user's password.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        reset_code = request.json.get('reset_code')
        password = authenticator.encrypt_password(request.json.get('password'))
        user = db.get_user_by_email(email)
        authenticator.verify_code(reset_code, user.reset_code)
        db.update_password(user, password)
        return jsonify({"message": "password reset successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/request-password-reset/', methods=['POST'])
def request_password_reset() -> tuple:
    """
    Request a password reset.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email_manager = current_app.config['emailManager']
        email = request.json.get('email')
        user = db.get_user_by_email(email)
        reset_code = authenticator.generate_one_time_code()
        db.update_reset_code(user, reset_code)
        email_manager.forgot_password_email(email, reset_code)
        return jsonify({"message": "reset code sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/verify/', methods=['POST'])
@login_required
def verify() -> tuple:
    """
    Verify a user.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        user_id = session.get('user_id')
        user = db.get_user_by_id(user_id)
        verification_code = request.json.get('verification_code')
        authenticator.verify_code(verification_code, user.verification_code)
        api_key = authenticator.generate_api_key()
        db.verify_user(user, api_key)
        return jsonify({"message": "verification successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/reset-api-key/', methods=['POST'])
@login_required
def reset_api_key() -> tuple:
    """
    Reset a user's API key.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        user_id = session.get('user_id')
        user = db.get_user_by_id(user_id)
        api_key = authenticator.generate_api_key()
        db.reset_api_key(user, api_key)
        return jsonify({"message": "API key reset successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/is-admin/', methods=['GET'])
@admin_required
def is_admin() -> tuple:
    """
    Check if a user is an admin.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    return jsonify({"message": "user is an admin"}), 200

@authentication_bp.route('/authenticate/is-verified/', methods=['GET'])
@login_required
def is_verified() -> tuple:
    """
    Check if a user is verified.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    # check if user is verified
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        user = db.get_user_by_id(user_id)
        if user.is_verified:
            return jsonify({"message": "user is verified"}), 200
        else:
            return jsonify({"error": "user is not verified"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@authentication_bp.route('/authenticate/is-logged-in/', methods=['GET'])
@login_required
def is_logged_in() -> tuple:
    """
    Check if a user is logged in.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    return jsonify({"message": "user is logged in"}), 200

@authentication_bp.route('/authenticate/delete-account/', methods=['DELETE'])
@login_required
def delete_account() -> tuple:
    """
    Delete a user's account.

    Args
    ----
    None

    Returns
    -------
    response (tuple): The response tuple containing the response data and status code.
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        db.delete_user(user_id)
        session.clear()
        return jsonify({"message": "account deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    