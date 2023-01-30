from app import db, ma


class CAMPAIGNSBONUS(db.Model):
    __tablename__ = 'CAMPAIGNSBONUS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_begin = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    bonus = db.Column(db.Integer, nullable=False)
    community_id = db.Column(db.Integer, nullable=False)
    event_ids = db.Column(db.String(300), nullable=False)

    def __init__(self, id, date_begin, date_end, bonus, community_id, event_ids):
        self.id = id
        self.date_begin = date_begin
        self.date_end = date_end
        self.bonus = bonus
        self.community_id = community_id
        self.event_ids = event_ids


class CampaignsBonusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_begin', 'date_end', 'bonus', 'community_id', 'event_ids')


CampaignsBonus_schema = CampaignsBonusSchema()
CampaignsBonusS_schema = CampaignsBonusSchema(strict=True, many=True)
