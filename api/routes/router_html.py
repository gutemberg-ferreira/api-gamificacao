from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from werkzeug.security import generate_password_hash
from faker import Faker
import datetime
from flask_login import login_required, current_user
from api.models.campaigns_bonus import CAMPAIGNSBONUS
from api.models.listen_events import LISTENEVENTS
from api.models.rule_events import RULEEVENTS
from api.models.users import USERS
from app import app, db


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/dashrank")
@login_required
def dash_rank():
    fake = Faker('pt_BR')
    return render_template('dashboard.html', utc_dt=datetime.datetime.utcnow(), allRanking=get_all_ranking(), cont=0, faker=fake, name=current_user.name)


def get_all_ranking():
    query = db.select(
        [LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).order_by(desc('Overall_Score')).group_by(LISTENEVENTS.user_id)
    listen_event = db.engine.execute(query).fetchall()
    return [dict(row) for row in listen_event]


@app.route("/admin/ruleevents")
@login_required
def rule_events_html():
    rule_events = RULEEVENTS.query.all()
    return render_template('rule_events/rule_events.html', rule_events=rule_events)


@app.route('/admin/addRuleEventHtml', methods=['POST'])
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


@app.route("/admin/campaignsbonus")
@login_required
def campaigns_bonus_html():
    campaigns_bonus = CAMPAIGNSBONUS.query.all()
    rule_events = RULEEVENTS.query.all()
    return render_template('campaigns_bonus/campaigns_bonus.html', campaigns_bonus=campaigns_bonus, rule_events=rule_events)


@app.route('/admin/addCampaignsBonusHtml', methods=['POST'])
@login_required
def post_campaigns_bonus_html():
    id = None
    name = request.form.get('name')
    date_begin = request.form.get('date_begin')
    date_end = request.form.get('date_end')
    bonus = request.form.get('bonus')
    community_id = request.form.get('community_id')
    event_ids = request.form['event_ids']
    status = True if request.form.get('status') else False
    campaigns_bonus = CAMPAIGNSBONUS(id, name, date_begin, date_end, bonus, community_id, event_ids, status)
    try:
        db.session.add(campaigns_bonus)
        db.session.commit()
        flash('Campaigns Bonus register with successfully')
        return redirect(f'/admin/campaignsbonus')
    except:
        flash('ERROR TRY AGAIN')


@app.route('/admin/campaignsbonus/<int:id>/update', methods=['GET', 'POST'])
@login_required
def campaigns_bonus_update_html(id):
    campaigns_bonus = CAMPAIGNSBONUS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if campaigns_bonus:
            campaigns_bonus.name = request.form['name']
            campaigns_bonus.date_begin = request.form['date_begin']
            campaigns_bonus.date_end = request.form['date_end']
            campaigns_bonus.bonus = request.form['bonus']
            campaigns_bonus.community_id = request.form['community_id']
            campaigns_bonus.event_ids = request.form['event_ids']
            campaigns_bonus.status = True if request.form.get('status') else False
            db.session.commit()
            return redirect(f'/admin/campaignsbonus')
        return f"Employee with id = {id} Does nit exist"

    return render_template('campaigns_bonus/campaigns_bonus_edit.html', campaigns_bonus=campaigns_bonus)


@app.route('/admin/campaignsbonus/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def campaigns_bonus_delete_html(id):
    campaigns_bonus = CAMPAIGNSBONUS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if campaigns_bonus:
            db.session.delete(campaigns_bonus)
            db.session.commit()
            return redirect(f'/admin/campaignsbonus')
        return f"Employee with id = {id} Does nit exist"
    return render_template('campaigns_bonus/campaigns_bonus_delete.html', campaigns_bonus=campaigns_bonus)


@app.route("/admin/users")
@login_required
def users_html():
    users = USERS.query.all()
    return render_template('users/users.html', users=users)


@app.route('/admin/addUsersHtml', methods=['POST'])
@login_required
def post_users_html():
    id = None
    username = request.form.get('username')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    users = USERS(id, username, name, email, password)
    try:
        db.session.add(users)
        db.session.commit()
        flash('User register with successfully')
        return redirect(f'/admin/users')
    except:
        flash('ERROR TRY AGAIN')


@app.route('/admin/users/<int:id>/update', methods=['GET', 'POST'])
@login_required
def users_update_html(id):
    users = USERS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            users.username = request.form.get('username')
            users.name = request.form.get('name')
            users.email = request.form.get('email')
            users.password = generate_password_hash(request.form.get('password'))
            db.session.commit()
            return redirect(f'/admin/users')
        return f"Employee with id = {id} Does nit exist"

    return render_template('users/users_edit.html', users=users)


@app.route('/admin/users/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def users_delete_html(id):
    users = USERS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect(f'/admin/users')
        return f"Employee with id = {id} Does nit exist"
    return render_template('users/users_delete.html', users=users)

@app.route('/admin/users/<int:id>/changepass', methods=['GET', 'POST'])
@login_required
def users_change_pass_html(id):
    users = USERS.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            users.password = generate_password_hash(request.form.get('password'))
            db.session.commit()
            return redirect(f'/admin/users')
        return f"Employee with id = {id} Does nit exist"
    return render_template('users/user_change_pass.html', users=users)