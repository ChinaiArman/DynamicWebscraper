"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session


# DEFINE BLUEPRINT
authentication_bp = Blueprint('authentication_bp', __name__)


# ROUTES
@authentication_bp.route('/authenticate/login/', methods=['POST'])
def login():
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        password = request.json.get('password')
        user = db.get_user_by_email(email)
        authenticator.verify_password(user, password)
        session["user_id"] = user.id
        return jsonify({"message": "login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/logout/', methods=['POST'])
def logout():
    """
    """
    try:
        session.clear()
        return jsonify({"message": "logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/register/', methods=['POST'])
def register():
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        password = authenticator.encrypt_password(request.json.get('password'))
        name = request.json.get('name')
        api_key = authenticator.generate_api_key()
        reset_code = authenticator.generate_reset_code()
        user = db.create_user(email, password, name, api_key, reset_code)
        session["user_id"] = user.id
        return jsonify({"message": "registration successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/reset-password/', methods=['POST'])
def reset_password():
    """
    """
    return jsonify({"message": "reset password endpoint"})

@authentication_bp.route('/authenticate/verify/', methods=['POST'])
def verify():
    """
    """
    return jsonify({"message": "verify endpoint"})
