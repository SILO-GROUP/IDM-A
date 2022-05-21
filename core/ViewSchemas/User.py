from core.Pantheon.AppFactory import ma


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "uuid",
            'creation_date',
            'email_verified',
            'identity_verified',
            'creation_date',
            'active',
            'groups'
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)