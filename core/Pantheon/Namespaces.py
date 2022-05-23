from flask_restx import Namespace

user_api = Namespace('user', description='User Management API')
group_api = Namespace('group', description='Group Management API')
session_api = Namespace('session', description='Session Management API')