from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from api.models.campaigns_bonus import CAMPAIGNSBONUS
from api.models.rule_events import RULEEVENTS
from app import app, db




@app.route("/admin/ruleevents")
@login_required
def rule_events_html():
    rule_events = RULEEVENTS.query.all()
    return render_template('rule_events/rule_events.html', rule_events=rule_events)


@app.route("/admin/campaignsbonus")
@login_required
def campaigns_bonus_html():
    campaigns_bonus = CAMPAIGNSBONUS.query.all()
    return render_template('campaigns_bonus/campaigns_bonus.html', campaigns_bonus=campaigns_bonus)


@app.route('/addRuleEventHtml', methods=['POST'])
@login_required
def post_rule_event_html():
    id = None
    name_event = request.form.get('name_event')
    description = request.form.get('description')
    score = request.form.get('score')
    rule_description = request.form.get('rule_description')
    status = True if request.form.get('status') else False
    ruleevent = RULEEVENTS(id, name_event, description, score, rule_description, status)
    try:
        db.session.add(ruleevent)
        db.session.commit()
        flash('Event Rule register with successfully')
        return redirect(url_for('rule_events_html'))
    except:
        flash('ERROR TRY AGAIN')


@app.route('/admin/ruleevents/<int:id>/update', methods=['GET', 'POST'])
@login_required
def rule_events_update_html(id):
    ruleevent = RULEEVENTS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if ruleevent:

            ruleevent.name_event = request.form['name_event']
            ruleevent.description = request.form['description']
            ruleevent.score = request.form['score']
            ruleevent.rule_description = request.form['rule_description']
            ruleevent.status = True if request.form.get('status') else False
            db.session.commit()
            return redirect(f'/admin/ruleevents')
        return f"Employee with id = {id} Does nit exist"

    return render_template('rule_events/rule_events_edit.html', ruleevent=ruleevent)


@app.route('/admin/ruleevents/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def rule_events_delete_html(id):
    ruleevent = RULEEVENTS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if ruleevent:
            db.session.delete(ruleevent)
            db.session.commit()
            return redirect(f'/admin/ruleevents')
        return f"Employee with id = {id} Does nit exist"
    return render_template('rule_events/rule_event_delete.html', ruleevent=ruleevent)