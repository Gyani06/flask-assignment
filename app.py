import os
import json
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__, template_folder='template')

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
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    print("POST /submittodoitem received")

    item_name = request.form.get('itemName')
    item_id = request.form.get('itemID')
    item_uuid = request.form.get('itemUUID')
    item_hash = request.form.get('itemHash')
    item_description = request.form.get('itemDescription')

    print("Item Name:", item_name)
    print("Item ID:", item_id)
    print("Item UUID:", item_uuid)
    print("Item Hash:", item_hash)

    inserted_id = collection.insert_one({
        "itemName": item_name,
        "itemID": item_id,
        "itemUUID": item_uuid,
        "itemHash": item_hash,
        "itemDescription": item_description
    }).inserted_id

    return jsonify({
        "message": "Todo item saved successfully",
        "id": str(inserted_id)
    })

# MongoDB code here

    return jsonify({
        "message": "Todo item received successfully"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
