import sys
sys.path.append('../')

from modules.Pantheon.Factory import app, db


with app.app_context():
    from modules.Users.Controller import UserController
    from modules.Groups.Controller import GroupController
    from modules.Sessions.Controller import SessionController

    user_controller = UserController()
    group_controller = GroupController()
    session_controller = SessionController()

    root_user = user_controller.create('root', 'root@localhost', 'password')
    root_group = group_controller.create('wheel')
    x = group_controller.add_member(root_group, root_user)
    root_session = session_controller.create(root_user.uuid, root_user.password)
    print(root_session)

    normal_user = user_controller.create('test_user', 'test@localhost', 'password')
    normal_group = group_controller.create('dummies')
    x = group_controller.add_member(normal_group, normal_user)
    normal_session = session_controller.create(normal_user.uuid, normal_user.password)
    print(normal_session)