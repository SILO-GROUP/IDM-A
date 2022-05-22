import sys

sys.path.append('../')

from app import *
from core.logic.Users import *
from core.logic.Groups import *

ucon = UserController()
gcon = GroupController()

with app.app_context():
    root_user = ucon.create( 'root', 'root@localhost', 'password' )
    root_group = gcon.create( 'wheel' )
    gcon.add_member( root_group, root_user )