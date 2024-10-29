"""
"""

# IMPORTS
from flask import Flask, jsonify, request, g
import time
from flask_cors import CORS
from dotenv import load_dotenv
import os

from logging_config import configure_logging

from api.authentication_routes import authentication_bp
from api.scraping_routes import scraping_bp
from api.database_routes import database_bp

from services.Database import Database
from services.Authenticator import Authenticator
from services.LLMManager import LLMManager
from services.Scraper import Scraper
from services.EmailManager import EmailManager

from db_config import db, configure_db


# ENVIRONMENT VARIABLES
load_dotenv()
PORT = os.getenv('PORT', 5000)


# FLASK CONFIGURATION
app = Flask(__name__)
CORS(app)


# DATABASE CONFIGURATION
configure_db(app)


# LOGGING CONFIGURATION
configure_logging(app)
@app.before_request
def log_request():
    g.start_time = time.time()
    app.logger.info(f"Incoming request Request: {request.method} {request.path}")

@app.after_request
def log_response(response):
    execution_time = time.time() - g.start_time
    app.logger.info(f"Completed request: {request.method} {request.path} "f"with status {response.status_code} in {execution_time:.4f}s")
    return response

@app.teardown_request
def log_request_teardown(error=None):
    if error is not None:
        app.logger.error(f"An error occurred: {error}")


# CONFIGURE SERVICES
app.config['database'] = Database(db)
app.config['authenticator'] = Authenticator()
app.config['studentManager'] = LLMManager()
app.config['scraper'] = Scraper()
app.config['emailManager'] = EmailManager()


# ROUTES
@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Hello World"})

app.register_blueprint(authentication_bp, url_prefix='/api')
app.register_blueprint(scraping_bp, url_prefix='/api')
app.register_blueprint(database_bp, url_prefix='/api')


# MAIN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
