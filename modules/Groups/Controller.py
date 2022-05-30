from modules.Groups.DatabaseModels import GroupModel
from modules.Pantheon.Factory import db
from sqlalchemy import exc


class GroupController:
    def __init__(self):
        pass

    def get_all(self):
        groups = GroupModel.query.all()
        if groups is None:
            return None
        return groups

    def get_id(self, id):
        group = GroupModel.query.get(id)
        if group is None:
            return None
        return group

    def get_name( self, name ):
        group = db.session.query(GroupModel).filter_by(name=name).first()
        if group is None:
            return None
        return group

    def get_guid(self, guid):
        group = db.session.query(GroupModel).filter_by(guid=guid).first()
        if group is None:
            return None
        return group

    def create( self, name ):
        try:
            group = GroupModel(name=name)
            db.session.add(group)

            db.session.commit()
            return group
        except exc.IntegrityError:
            return None

    def update( self, group, name=None ):
        if group is None:
            return None
        try:
            if name is not None:
                group['name'] = name
            db.session.commit()
            return group
        except exc.IntegrityError:
            return None

    def add_member(self, group, user ):
        try:
            group.members.append(user)
            db.session.commit()
            return group
        except exc.IntegrityError:
            return None

    def remove_member(self, group, user ):
        try:
            group.members.remove( user )
            db.session.commit()
            return group
        except exc.IntegrityError:
            return None

    def user_is_in_group( self, user, group ):
        if group.guid in [entry.guid for entry in user.groups]:
            return True
        else:
            return False


group_controller = GroupController()