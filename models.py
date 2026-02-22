from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    personality = db.Column(db.String(50))
    language = db.Column(db.String(50))
    user_message = db.Column(db.Text)
    ai_reply = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)