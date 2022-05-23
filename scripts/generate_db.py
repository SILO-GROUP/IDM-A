from modules.Pantheon.Factory import app, db

import sys

sys.path.append('../')

with app.app_context():
    db.create_all()