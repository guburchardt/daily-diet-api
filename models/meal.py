from database import db
from datetime import datetime

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    data_time = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    inDiet = db.Column(db.Boolean(), nullable= False, default=True)
    