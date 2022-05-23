import sys
sys.path.append('../')

from modules.Pantheon.Factory import app, db

with app.app_context():
    db.create_all()