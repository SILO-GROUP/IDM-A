from flask_restx import Namespace


class NamespaceWrapper(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # tell swagger to expect a header
    def expect_header(self, name, desc):
        return self.doc(params={name: {"in": "header", "description": desc}})

    # tell swagger to expect a URI param
    def expect_url_var(self, variable, desc):
        return self.param( variable, desc )

    # define the structure of the input for the api
    def input_schema(self, schema):
        return self.expect( schema )

    # define the structure of the output for the api
    def output_schema(self, schema):
        return self.marshal_list_with( schema, mask='' )

    # indicate to swagger ui that no session is needed
    def no_session_required(self, func):
        return self.doc(security=None)(func)


user_api = NamespaceWrapper('user', description='User Management API')
group_api = NamespaceWrapper('group', description='Group Management API')
session_api = NamespaceWrapper('session', description='Session Management API')