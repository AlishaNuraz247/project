from application import db # import the sqlalchemy object (db) created for our app

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(30), nullable=False) 
    owner = db.Column(db.String(30), nullable=False)
    Notes = db.Column (db.String(60), nullable=False)
