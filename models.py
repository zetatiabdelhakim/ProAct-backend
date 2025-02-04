from datetime import datetime
from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    major = db.Column(db.String(120), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'gender': self.gender,
            'major': self.major,
            'level': self.level
        }

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    problem = db.Column(db.String(200), nullable=False)
    solution = db.Column(db.String(200), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'problem': self.problem,
            'solution': self.solution
        }
