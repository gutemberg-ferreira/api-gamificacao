from app import db, ma


class RULEEVENTS(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_event = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    rule_description = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, id, name_event, description, score, rule_description, status):
        self.id = id
        self.name_event = name_event
        self.description = description
        self.score = score
        self.rule_description = rule_description
        self.status = status

class RuleEventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name_event', 'description', 'score', 'rule_description', 'status')


ruleEvent_schema = RuleEventSchema()
ruleEvents_schema = RuleEventSchema(strict=True, many=True)
