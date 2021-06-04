from datetime import datetime
from config.database import db


class Devices(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1028), nullable=False)
    #todo
    #hasMany = Pins
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Device %r>' % self.name
