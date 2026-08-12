import os
import json
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(
    MONGODB_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

app = Flask(__name__)

db = client.todo_db
collection = db.todo_items

@app.route('/')
def home():
    return render_template('todo.html')

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
