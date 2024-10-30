"""
"""

# IMPORTS
from flask_session import Session


# CONFIGURE SESSIONS
def configure_sessions(app, db):
    """
    """
    app.config['SECRET_KEY'] = 'imsosleepybruh'
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    app.config['SESSION_SQLALCHEMY'] = db
    app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
    app.config['SESSION_USE_SIGNER'] = True
    Session(app)
    return
