"""
db_config.py
This module contains the configuration for the MYSQL database connection.
"""

# IMPORTS
from flask_sqlalchemy import SQLAlchemy
import ssl
import os
from dotenv import load_dotenv


# ENVIRONMENT VARIABLES
load_dotenv()
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_SSL_CERT = os.getenv('DB_SSL_CERT')


# INIT DATABASE
db = SQLAlchemy()


# CONFIGURE DATABASE
def configure_db(app) -> None:
    """
    Configure the MYSQL database connection.

    Args
    ----
    app (Flask): The Flask application instance.

    Returns
    -------
    None

    Disclaimer
    ----------
    This function was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(cadata=DB_SSL_CERT)  # Load the CA certificate from the string

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "connect_args": {
            "ssl": ssl_context  # Pass the SSL context directly
        }
    }
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return
