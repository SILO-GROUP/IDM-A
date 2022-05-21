import sys

sys.path.append('../')

from app import *
from core.DatabaseModels.User import *
from core.DatabaseModels.Group import *
from core.DatabaseModels.UserGroupAssociations import *

with app.app_context():
    db.create_all()