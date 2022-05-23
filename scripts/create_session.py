import sys
sys.path.append('../')

from modules.Pantheon.Factory import app, db


with app.app_context():
    from modules.Users.Controller import UserController
    from modules.Sessions.Controller import SessionController

    ucon = UserController()
    scon = SessionController()

    root_user = ucon.get_username( 'root' )
    if root_user is None:
        print( "Failed to find the root user." )
        exit(1)
    session = scon.create( root_user.uuid, root_user.password )
    print(session)