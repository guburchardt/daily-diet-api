from flask import Flask, request, jsonify
from models.meal import Meal
from database import db
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily_diet'

db.init_app(app)

meals_id_control = 1


@app.route("/registerMeal", methods=["POST"])
def registerMeal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    data_time = data.get("data_time")
    inDiet = data.get("inDiet")
    
    if name and description and data_time and inDiet:
        meal = Meal(name=name, description=description, data_time=data_time, inDiet=InDiet)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição Cadastrada com Sucesso"}), 200

    return jsonify({"message": "Dados Incorretos"}), 400
