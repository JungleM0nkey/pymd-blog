from app import app
from app import db, login
from datetime import datetime
from time import time
from pytz import timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt

tz = timezone('EST')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String)

    def __repr__(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True)
    title = db.Column(db.String(), index=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    text = db.Column(db.String(), index=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))