import sys

sys.path.append('../')

with app.app_context():
    db.create_all()