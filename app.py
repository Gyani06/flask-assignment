import os
import json
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Existing MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todo_items

# Existing API Route
@app.route('/api')
def get_data():
    here = os.path.dirname(__file__)
    path = os.path.join(here, 'data.json')

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return jsonify(data)

# New Route for master_2 Branch
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({
        "message": "Todo item saved successfully"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)