from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import os

# Mongo connection (local or Atlas)
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
client = MongoClient(MONGO_URI)
db = client['shraddha_todo_db']
todos = db['todos']

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = request.get_json()
    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    res = todos.insert_one(item)
    return jsonify({"status":"success", "id": str(res.inserted_id)})