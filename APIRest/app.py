import os
from flask import Flask
from config.vars import load_vars

app = Flask(__name__)
app.config.from_pyfile('config/settings.py')
load_vars()
  

#import rutas_upload

#import rutas_verfichero

from routes import waiter_routes
from routes import product_routes
from routes import user_routes


if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)