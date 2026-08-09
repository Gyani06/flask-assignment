import os
import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api')
def get_data():
    here = os.path.dirname(__file__)
    path = os.path.join(here, 'data.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)