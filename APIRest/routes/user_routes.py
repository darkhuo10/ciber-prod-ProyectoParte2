from __main__ import app
from flask import jsonify

@app.route('/prueba', methods=['GET'])
def test():
    return jsonify({"message": "hello world"}), 200
