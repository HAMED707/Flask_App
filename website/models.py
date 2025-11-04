from . import db

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(50))
    email=db.Column(db.String(150))
    password=db.Column(db.Integer)
 