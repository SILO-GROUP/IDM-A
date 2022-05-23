from modules.Users.Controller import UserController
from modules.Groups.Controller import GroupController
from modules.Sessions.Controller import SessionController
from modules.Pantheon.Factory import app

import sys

sys.path.append('../')

ucon = UserController()
gcon = GroupController()
scon = SessionController()

with app.app_context():
    root_user = ucon.create( 'root', 'root@localhost', 'password' )
    root_group = gcon.create( 'wheel' )
    gcon.add_member( root_group, root_user )
    session = scon.create( root_user.uuid, root_user.password )
    print(session)