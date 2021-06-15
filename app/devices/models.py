from datetime import datetime
from config.database import db


class Devices(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pins = db.relationship('Pins', backref='devices', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Device %r>' % self.name


class Pins(db.Model):
    __tablename__ = 'pins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    assignment = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)

    def __init__(self, name, number, assignment, device_id):
        self.name = name
        self.number = number
        self.assignment = assignment
        self.device_id = device_id

    def __repr__(self):
        return '<Pin %r>' % self.name
