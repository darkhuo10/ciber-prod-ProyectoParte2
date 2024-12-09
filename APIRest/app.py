#import os
from flask import Flask
from flask import jsonify

#from variables import cargarvariables

app = Flask(__name__)
#app.config.from_pyfile('config/settings.py')

  
from routes import user_routes

#import waiter_routes

#import product_routes


#@app.route('/prueba', methods=['GET'])
#def test():
#    return jsonify({"message": "hello world"}), 200

if __name__ == '__main__':
    #port = int(os.environ.get('PORT'))
    #host = os.environ.get('HOST')
    #app.run(host=host, port=port)
    app.run(host="0.0.0.0", port=8080)