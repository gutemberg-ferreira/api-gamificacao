from flask import jsonify, request, render_template
import datetime
from faker import Faker
from sqlalchemy import desc

from api.models.listen_events import LISTENEVENTS
from app import app, db



@app.route("/dashrank")
def dash_rank():
    fake = Faker('pt_BR')
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(), allRanking=get_all_ranking(), cont=0, faker=fake)

@app.route('/about/')
def about():
    return render_template('about.html')


def get_all_ranking():
    query = db.select(
        [LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).order_by(desc('Overall_Score')).group_by(LISTENEVENTS.user_id)
    listen_event = db.engine.execute(query).fetchall()
    return [dict(row) for row in listen_event]