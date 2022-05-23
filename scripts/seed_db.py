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