#import os
from flask import Flask
#from variables import cargarvariables

app = Flask(__name__)
app.config.from_pyfile('settings.py')

  
import user_routes

import waiter_routes

import product_routes


if __name__ == '__main__':
    #port = int(os.environ.get('PORT'))
    #host = os.environ.get('HOST')
    #app.run(host=host, port=port)
    app.run(host="0.0.0.0", port=8080)