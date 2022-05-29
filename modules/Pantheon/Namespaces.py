from flask_restx import Namespace


class NamespaceWrapper(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def expect_header(self, name, desc):
        return self.doc(params={name: {"in": "header", "description": desc}})

    def input_schema(self, schema):
        return self.expect(schema)

    def expect_url_var(self, variable, desc):
        return self.param(variable, desc)

    def output_schema(self, schema):
        return self.marshal_list_with(schema, mask='')

    def no_auth(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


user_api = NamespaceWrapper('user', description='User Management API')
group_api = NamespaceWrapper('group', description='Group Management API')
session_api = NamespaceWrapper('session', description='Session Management API')
