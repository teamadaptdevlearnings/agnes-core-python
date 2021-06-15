from datetime import datetime
from config.database import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.name

    def check_password(self, password):
        return check_password_hash(self.password, password)

