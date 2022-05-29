from modules.Pantheon.Decorators import NamespaceWrapper

user_api = NamespaceWrapper("user", description="User Management API")
group_api = NamespaceWrapper("group", description="Group Management API")
session_api = NamespaceWrapper("session", description="Session Management API")
