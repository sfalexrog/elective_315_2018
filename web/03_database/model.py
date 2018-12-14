from app import db

class Message(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    sender = db.Column(db.String(80))
    contents = db.Column(db.Text)
