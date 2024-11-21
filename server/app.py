"""
"""

# IMPORTS
from flask import Flask, jsonify, request
import logging
from flask_cors import CORS
import os
from dotenv import load_dotenv

from api.authentication_routes import authentication_bp
from api.qna_routes import qna_bp
from api.database_routes import database_bp

from services.Database import Database
from services.Authenticator import Authenticator
from services.LLMManager import LLMManager
from services.Scraper import Scraper
from services.EmailManager import EmailManager

from db_config import db, configure_db
from session_config import configure_sessions


# CONSTANTS
load_dotenv()
CLIENT_URL = os.getenv('CLIENT_URL')


# CREATE APP
def create_app() -> Flask:
    """
    Create the Flask application instance.

    Args
    ----
    None

    Returns
    -------
    app (Flask): The Flask application instance.
    """
    # FLASK CONFIGURATION
    app = Flask(__name__)
    CORS(app, supports_credentials=True) #, resources={r"/api/*": {"origins": CLIENT_URL, "allow_headers": ["Content-Type"]}}

    # DATABASE CONFIGURATION
    configure_db(app)

    # CONFIGURE SESSIONS
    configure_sessions(app, db)

    # CONFIGURE SERVICES
    app.config['database'] = Database(db)
    app.config['authenticator'] = Authenticator()
    app.config['llmManager'] = LLMManager()
    app.config['scraper'] = Scraper()
    app.config['emailManager'] = EmailManager(
        email_address=os.getenv('EMAIL_ADDRESS'),
        email_password=os.getenv('EMAIL_PASSWORD'),
        client_url=os.getenv('CLIENT_URL')
    )

    # ROUTES
    @app.route('/', methods=['GET'])
    def _():
        return jsonify({"message": "Hello World"})
    
    # RESPONSE HEADERS
    # @app.after_request
    # def _(response):
    #     response.headers['Access-Control-Allow-Origin'] = CLIENT_URL
    #     response.headers['Access-Control-Allow-Credentials'] = 'true'
    #     response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    #     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
    #     # Handle OPTIONS request directly
    #     if request.method == 'OPTIONS':
    #         response.status_code = 200
    #     return response
    
    @app.after_request
    def _(response):
        # increment the count for the endpoint requested in the database
        db = app.config['database']
        endpoint = request.endpoint
        # convert the bp to the endpoint
        logging.info(f"Endpoint: {endpoint}")
        if endpoint == None:
            return response
        available_endpoints = {"authentication_bp": "authenticate", "qna_bp": "qna", "database_bp": "database"}
        try:
            endpoint = "api/" + available_endpoints[endpoint.split(".")[0]] + "/" + endpoint.split(".")[1]
            method = request.method
            db.increment_requests(endpoint, method)
        except:
            pass
        return response

    # REGISTER BLUEPRINTS
    app.register_blueprint(authentication_bp, url_prefix='/api')
    app.register_blueprint(qna_bp, url_prefix='/api')
    app.register_blueprint(database_bp, url_prefix='/api')
    return app, db
