"""
"""

# IMPORTS
from flask import Flask, jsonify
from flask_cors import CORS

from api.authentication_routes import authentication_bp
from api.scraping_routes import scraping_bp
from api.database_routes import database_bp

from services.Database import Database
from services.Authenticator import Authenticator
from services.LLMManager import LLMManager
from services.Scraper import Scraper
from services.EmailManager import EmailManager

from db_config import db, configure_db
from logging_config import configure_logging
from session_config import configure_sessions


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
    CORS(app)

    # DATABASE CONFIGURATION
    configure_db(app)

    # LOGGING CONFIGURATION
    configure_logging(app)

    # CONFIGURE SESSIONS
    configure_sessions(app, db)

    # CONFIGURE SERVICES
    app.config['database'] = Database(db)
    app.config['authenticator'] = Authenticator()
    app.config['studentManager'] = LLMManager()
    app.config['scraper'] = Scraper()
    app.config['emailManager'] = EmailManager()

    # CONFIGURE ROUTES
    @app.route('/', methods=['GET'])
    def _():
        return jsonify({"message": "Hello World"})

    app.register_blueprint(authentication_bp, url_prefix='/api')
    app.register_blueprint(scraping_bp, url_prefix='/api')
    app.register_blueprint(database_bp, url_prefix='/api')
    return app, db
