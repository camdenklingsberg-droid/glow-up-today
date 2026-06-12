from ..extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    xp = db.Column(db.Integer, default=0)
    streak = db.Column(db.Integer, default=0)

    last_login = db.Column(db.String(20), default="")
    completed = db.Column(db.Text, default="")

    plan_type = db.Column(db.String(10), default="free")
