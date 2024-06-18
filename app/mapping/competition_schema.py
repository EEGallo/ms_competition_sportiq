from app.models.competition import Competition
from marshmallow import fields, Schema, post_load

class CompetitionSchema(Schema):
    id = fields.Integer(dump_only=True)
    category = fields.Str(required=True)
    discipline = fields.Str(required=True)
    start_date = fields.Date(required=True, format='%Y-%m-%d')
    end_date = fields.Date(required=True, format='%Y-%m-%d')
    team_event = fields.Bool(required=True)
    winner = fields.Str(required=False)
    data = fields.Dict(required=False)

    @post_load
    def make_user(self, data, **kwargs):
        return Competition(**data)