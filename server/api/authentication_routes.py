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
        authenticator.verify_password(password, user.password)
        session.permanent = True
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
        verification_code = authenticator.generate_verification_code()
        user = db.create_user(email, password, name, verification_code)
        session.permanent = True
        session["user_id"] = user.id
        # TODO: SEND VERIFICATION EMAIL
        return jsonify({"message": "registration successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/reset-password/', methods=['POST'])
def reset_password():
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        verification_code = request.json.get('verification_code')
        password = authenticator.encrypt_password(request.json.get('password'))
        user = db.get_user_by_email(email)
        authenticator.verify_verification_code(verification_code, user.verification_code)
        db.update_password(user, password)
        return jsonify({"message": "password reset successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/generate-verification/', methods=['POST'])
def generate_verification():
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        user = db.get_user_by_email(email)
        verification_code = authenticator.generate_verification_code()
        db.update_verification_code(user, verification_code)
        # TODO: SEND VERIFICATION EMAIL
        return jsonify({"message": "verification code sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@authentication_bp.route('/authenticate/verify/', methods=['POST'])
def verify():
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        user_id = session.get('user_id')
        user = db.get_user_by_id(user_id)
        verification_code = request.json.get('verification_code')
        authenticator.verify_verification_code(verification_code, user.verification_code)
        api_key = authenticator.generate_api_key()
        db.verify_user(user, api_key)
        return jsonify({"message": "verification successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
