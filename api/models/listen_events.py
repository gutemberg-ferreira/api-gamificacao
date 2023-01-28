from app import db, ma
from api.models.rule_events import RULEEVENTS


class LISTENEVENTS(db.Model):
    __tablename__ = 'LISTENEVENTS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    event_id = db.Column(db.ForeignKey('RULEEVENTS.id'), nullable=False)
    event = db.relationship('RULEEVENTS')

    def __init__(self, id, user_id, event_date, event_id):
        self.id = id
        self.user_id = user_id
        self.event_date = event_date
        self.event_id = event_id


class ListenEventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'event_date', 'event_id')


listenEvent_schema = ListenEventSchema()
listenEvents_schema = ListenEventSchema(strict=True, many=True)
