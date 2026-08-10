import os
import json
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask import render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Existing MongoDB Connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.todo_db
collection = db.todo_items


class todo_items:
    """Helper class to manage todo items in MongoDB."""

    def __init__(self, collection):
        self.collection = collection

    def create_item(self, item_name, item_description):
        """Insert a new todo item and return the inserted id."""
        doc = {
            "itemName": item_name,
            "itemDescription": item_description
        }
        result = self.collection.insert_one(doc)
        return str(result.inserted_id)

    def get_all(self):
        """Return all todo items as a list of dicts."""
        items = []
        for doc in self.collection.find():
            doc['_id'] = str(doc.get('_id'))
            items.append(doc)
        return items

    def get_by_id(self, id_):
        """Return a single todo item by its id or None."""
        from bson.objectid import ObjectId
        try:
            doc = self.collection.find_one({"_id": ObjectId(id_)})
        except Exception:
            return None
        if doc:
            doc['_id'] = str(doc.get('_id'))
        return doc

    def update_item(self, id_, data):
        """Update fields of a todo item. Returns True if modified."""
        from bson.objectid import ObjectId
        try:
            result = self.collection.update_one({"_id": ObjectId(id_)}, {"$set": data})
        except Exception:
            return False
        return result.modified_count > 0

    def delete_item(self, id_):
        """Delete a todo item by id. Returns True if deleted."""
        from bson.objectid import ObjectId
        try:
            result = self.collection.delete_one({"_id": ObjectId(id_)})
        except Exception:
            return False
        return result.deleted_count > 0

# instantiate helper
todo_helper = todo_items(collection)

# Existing API Route
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
@app.route('/submittodoitem', methods=['GET', 'POST'])
def submit_todo():

    if request.method == 'GET':
        return "Route is working"

    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    inserted_id = todo_helper.create_item(
        item_name,
        item_desc
    )

    return jsonify({
        "message": "Todo item saved successfully",
        "id": inserted_id
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)