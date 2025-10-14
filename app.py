from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# sample route /api reads JSON file
@app.route('/api')
def api():
    import json
    with open('data/api_data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

# Keep /submittodoitem route for later (in master_2 branch)
if __name__ == '__main__':
    app.run(debug=True)
