from app import db
from dataclasses import dataclass


@dataclass
class Competition(db.Model):
    
    __tablename__ = 'competitions'
    id =db.Column('id',db.Integer, primary_key=True)
    category = db.Column('category', db.String(255))
    discipline = db.Column('discipline', db.String(255))
    start_date = db.Column('start date', db.Date)
    end_date = db.Column('end date', db.Date)
    team_event = db.Column('team event', db.Boolean)
    winner = db.Column('password', db.String(255))      