from flask import render_template

from api.models.rule_events import RULEEVENTS
from app import app



@app.route("/ruleevents")
def rule_events_html():
    rule_events = RULEEVENTS.query.all()
    return render_template('rule_events.html', rule_events=rule_events)