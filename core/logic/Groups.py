from core.Pantheon.AppFactory import *
from core.ViewSchemas.Group import group_schema, groups_schema
from core.DatabaseModels.Group import GroupModel
from sqlalchemy import exc
# data validation happens _here_
# input sanitization happens here, too.


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

    def get_uuid( self, uuid ):
        group = db.session.query(GroupModel).filter_by( uuid=uuid ).first()
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