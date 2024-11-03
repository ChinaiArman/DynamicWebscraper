"""
"""

# IMPORTS
from app import create_app


# CREATE APP
app, db = create_app()


# MAIN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
