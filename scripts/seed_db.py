import sys
sys.path.append('../')

from modules.Pantheon.Factory import app, db


with app.app_context():
    from modules.Users.Controller import UserController
    from modules.Groups.Controller import GroupController
    from modules.Sessions.Controller import SessionController

    ucon = UserController()
    gcon = GroupController()
    scon = SessionController()

    root_user = ucon.create( 'root', 'root@localhost', 'password' )
    root_group = gcon.create( 'wheel' )
    gcon.add_member( root_group, root_user )
    session = scon.create( root_user.uuid, root_user.password )
    print(session)
