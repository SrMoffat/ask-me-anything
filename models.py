from app import db
from sqlalchemy.dialects.postgresql import JSON


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(JSON)

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return '<id {}>'.format(self.id)
