from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DataTime(), nullable=False)
    inDiet = db.Column(db.Boolean(), nullable= False, default=True)
    