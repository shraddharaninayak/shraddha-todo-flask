from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Moon_30:Moon1530@shraddhatodo.atapwkn.mongodb.net/?retryWrites=true&w=majority&appName=Shraddhatodo")
client = MongoClient(MONGO_URI)
db = client["shraddha_todo_db"]
todos = db["todos"]

@app.route("/")
def home():
    return render_template("index.html")
# @app.route('/', methods=['GET'])
# def home():
#     return "Flask is running!"
@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = request.get_json(force=True)  # Flask expects JSON
    if not data:
        return jsonify({"status":"error", "message":"No JSON received"}), 400

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    res = todos.insert_one(item)
    return jsonify({"status":"success", "id": str(res.inserted_id)})


if __name__ == "__main__":
    app.run(debug=True)
