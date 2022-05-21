from core.Pantheon.AppFactory import ma


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class GroupSchema(ma.Schema):
    class Meta:
        fields = (
            "name",
            "uuid",
            'creation_date',
            'members'
        )


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)