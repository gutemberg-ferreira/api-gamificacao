from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from api.models.campaigns_bonus import CAMPAIGNSBONUS
from api.models.rule_events import RULEEVENTS
from app import app, db




@app.route("/admin/ruleevents")
@login_required
def rule_events_html():
    return render_template('rule_events/rule_events.html')

@app.route("/admin/campaignsbonus")
@login_required
def campaigns_bonus_html():
    return render_template('campaigns_bonus/campaigns_bonus.html')


@app.route("/ruleevents/data")
@login_required
def data_ruleevents():
    return {'data': [rule_event.to_dict() for rule_event in RULEEVENTS.query]}

@app.route("/campaignsbonus/data")
@login_required
def data_campaignsbonus():
    return {'data': [campaignsbonus.to_dict() for campaignsbonus in CAMPAIGNSBONUS.query]}

@app.route('/addRuleEventHtml', methods=['POST'])
@login_required
def post_rule_event_html():
    id = None
    name_event =  request.form.get('name_event')
    description =  request.form.get('description')
    score =  request.form.get('score')
    rule_description =  request.form.get('rule_description')
    #status = request.json['status']
    status = True if request.form.get('status') else False
    ruleevent = RULEEVENTS(id, name_event, description, score, rule_description, status)
    try:
        db.session.add(ruleevent)
        db.session.commit()
        flash('Event Rule register with successfully')
        return redirect(url_for('rule_events_html'))
    except:
        flash('ERROR TRY AGAIN')