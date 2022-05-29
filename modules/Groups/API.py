from flask_restx import Resource
from flask import request, g

from modules.Groups.APIModels import GroupFields, GroupCreateFields, GroupMemberModifyFields
from modules.Pantheon.Namespaces import group_api as api
from modules.Groups.Controller import group_controller
from modules.Groups.ViewSchemas import group_schema, groups_schema
from modules.Groups.Decorators import *
from modules.Sessions.Decorators import *


@api.route('/all')
class Groups(Resource):
    @session_required
    @api.output_schema(GroupFields)
    def get(self):
        '''List all groups.'''
        groups = group_controller.get_all()
        if groups is None:
            return 'No groups found.', 404

        return groups_schema.dump(groups)


@api.route('/create')
class Group(Resource):
    @api.doc('create_group')
    @api.expect(GroupCreateFields)
    @api.response( 201, 'Group created.' )
    @api.response( 400, 'Failed to create group.' )
    def post( self ):
        '''Create a group.'''
        new_group = group_controller.create(
            name=request.json['name']
        )

        if new_group is None:
            return 'Failed to create group.', 400

        return group_schema.dump(new_group), 201


@api.route('/uuid/<uuid>')
@api.param('uuid', 'The group UUID.')
@api.response( 404, 'Group not found.' )
class Group(Resource):
    @api.doc('get_group_uuid')
    def get(self, group_uuid ):
        '''Get group details by group UUID.'''
        group = group_controller.get_uuid(uuid=group_uuid)
        if group is None:
            return 'Group not found.', 404
        return group_schema.dump(group)

    def put( self, group_uuid ):
        '''Rename a group.'''
        group = group_controller.get_uuid(uuid=group_uuid)
        if group is None:
            return 'Group not found.', 404

        result = group_controller.update(group, request.json['name'])
        if result is None:
            return 'Failed to update group.', 400

        return group_schema.dump( result )

    @api.param('uuid', 'The group UUID.')
    @api.doc( 'delete_group_uuid' )
    @api.response(404, 'Group not found.')
    @api.response(401, 'Group not empty.')
    def delete(self, uuid ):
        '''Delete an empty group.'''
        group = group_controller.get_uuid(uuid=uuid)
        if group is None:
            return 'Group not found.', 404

        if len(group.members) > 0:
            return 'Refused to delete non-empty group. ', 401


@api.route('/name/<name>')
@api.param('name', 'The group name.')
@api.response( 404, 'Group not found.' )
class Group(Resource):
    @api.doc('get_group_byname')
    def get(self, name ):
        '''Get group details by group name.'''
        group = group_controller.get_name(name=name)
        if group is None:
            return 'Group not found.', 404

        return group_schema.dump(group)


@api.route('/uuid/<uuid>/members')
@api.param('uuid', 'The group UUID.')
@api.response( 404, 'Group not found.' )
class Group(Resource):
    @api.doc('add_user_to_group')
    @api.expect(GroupMemberModifyFields)
    def put(self, uuid ):
        '''Add a user to a group.'''
        group = group_controller.get_uuid(uuid=uuid)
        if group is None:
            return 'Group not found.', 404

        ucon = UserController()
        user = ucon.get_uuid( uuid=request.json['uuid'] )

        if user is None:
            return 'User not found.', 401

        result = group_controller.add_member(group=group, user=user)
        if result is None:
            return 'Failed to append group.', 400
        return group_schema.dump(result), 201

    @api.doc('remove_user_from_group')
    @api.expect(GroupMemberModifyFields)
    @api.response(404, 'Group not found.')
    @api.response(401, 'User not in group.')
    def delete( self, uuid ):
        '''Remove a user from a group.'''
        group = group_controller.get_uuid(uuid=uuid)
        if group is None:
            return 'Group not found.', 404

        ucon = UserController()
        user = ucon.get_uuid( uuid=request.json['uuid'] )

        if user is None:
            return 'User not found.', 401

        if user.suid not in group.members:
            return 'User is not in that group.', 404

        result = group_controller.remove_member(group, user)
        if result is None:
            return 'Failed to remove user from group.', 400
        return group_schema.dump( result ), 200
