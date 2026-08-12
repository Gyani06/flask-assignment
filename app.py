import os
import json
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from pymongo import MongoClient
from dotenv import load_dotenv
import certify

app = Flask(__name__, template_folder='template')

#Load environment variables from .env file
load_dotenv()

# Existing MongoDB Connection
# MongoDB Connection
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

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
# MongoDB code here

    return jsonify({
        "message": "Todo item received successfully"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
