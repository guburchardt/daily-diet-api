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
    
    if name and description:
        meal = Meal(name=name, description=description, data_time=data_time, inDiet=inDiet)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição Cadastrada com Sucesso"}), 200

    return jsonify({"message": "Dados Incorretos"}), 400

@app.route("/getAllMeals", methods=["GET"])
def getAllMeals():
    meals = Meal.query.all()

    meals_list = []
    for meal in meals:
        meals_list.append({
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "data_time": meal.data_time.strftime("%Y-%m-%d %H:%M:%S"),
            "inDiet": meal.inDiet
        })
    
    return jsonify({
        "meals": meals_list,
        "total": len(meals_list)
    }), 200        

@app.route("/getMealById/<int:id>", methods=["GET"])
def getMealById(id):
    meal = Meal.query.get(id)

    if meal:
        return jsonify({
            "message": "Refeição Encontrada",
            "meal": {
                "id": meal.id,
                "name": meal.name,
                "description": meal.description,
                "data_time": meal.data_time.strftime("%Y-%m-%d %H:%M:%S"),
                "inDiet": meal.inDiet
            }
        }), 200
    
    return jsonify({"message": "Refeição Não Encontrada"}), 404

@app.route("/updateMeal/<int:id>", methods=["PUT"])
def updateMeal(id):
    meal = Meal.query.get(id)

    if meal:
        data = request.json

        if "name" in data:
            meal.name = data["name"]
        if "description" in data:
            meal.description = data["description"]
        if "inDiet" in data:
            meal.inDiet = data["inDiet"]

        try:
            db.session.commit()
            return jsonify({
                "message": "Refeição atualizada com sucesso",
                "meal": {
                    "id": meal.id,
                    "name": meal.name,
                    "description": meal.description,
                    "data_time": meal.data_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "inDiet": meal.inDiet                    
                }
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "message": "Erro ao atualizar refeição",
                "error": str(e)
            }), 500
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/deleteMeal/<int:id>", methods=["DELETE"])
def deleteMeal(id):
    meal = Meal.query.get(id)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": f"Refeição {id} deletada com sucesso"}), 200
    
    return jsonify({"message": "Não foi possível encontrar essa refeição"})




if __name__ == "__main__":
    app.run(debug=True)