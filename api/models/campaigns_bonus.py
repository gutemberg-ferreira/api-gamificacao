from app import db, ma


class CAMPAIGNSBONUS(db.Model):
    __tablename__ = 'CAMPAIGNSBONUS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date_begin = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    bonus = db.Column(db.Integer, nullable=False)
    community_id = db.Column(db.Integer, nullable=False)
    event_ids = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, name, date_begin, date_end, bonus, community_id, event_ids, status):
        self.id = id
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        self.bonus = bonus
        self.community_id = community_id
        self.event_ids = event_ids
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_begin': self.date_begin,
            'date_end': self.date_end,
            'bonus': self.bonus,
            'community_id': self.community_id,
            'event_ids': self.event_ids,
            'status': self.status,
        }

class CampaignsBonusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'date_begin', 'date_end', 'bonus', 'community_id', 'event_ids', 'status')


CampaignsBonus_schema = CampaignsBonusSchema()
CampaignsBonusS_schema = CampaignsBonusSchema(strict=True, many=True)
