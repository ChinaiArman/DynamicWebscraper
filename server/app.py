"""
"""

# IMPORTS
from flask import Flask, jsonify, request
import logging
from flask_cors import CORS
import os
from dotenv import load_dotenv

from flasgger import Swagger

from api.authentication_routes import authentication_bp
from api.service_routes import service_bp
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

    # CONFIGURE SWAGGER
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/docs/apispec.json',
                "rule_filter": lambda rule: "authentication_bp" not in rule.endpoint and "database_bp" not in rule.endpoint,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/api/docs/",
        'openapi': '3.0.1',
        'title': 'Dynamic Webscraping API',
        'version': '1.0.0',
    }
    app.config['SWAGGER'] = {
        "openapi": "3.0.1",
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [{"bearerAuth": []}]
    }
    Swagger(app, config=swagger_config)

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
        """
        Root route.
        ---
        tags:
            - Root
        responses:
            200:
                description: Hello World
        """
        return jsonify({"message": "Hello World"})
    
    @app.after_request
    def _(response):
        db = app.config['database']
        endpoint = request.endpoint
        logging.info(f"Endpoint: {endpoint}")
        if endpoint == None:
            return response
        available_endpoints = {"authentication_bp": "authenticate", "service_bp": "service", "database_bp": "database"}
        try:
            endpoint = "api/" + available_endpoints[endpoint.split(".")[0]] + "/" + endpoint.split(".")[1]
            method = request.method
            db.increment_requests(endpoint, method)
        except:
            pass
        return response

    # REGISTER BLUEPRINTS
    app.register_blueprint(authentication_bp, url_prefix='/api')
    app.register_blueprint(service_bp, url_prefix='/api')
    app.register_blueprint(database_bp, url_prefix='/api')
    return app, db
