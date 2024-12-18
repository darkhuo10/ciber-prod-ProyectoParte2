#import os
from flask import Flask
from models import models
from routes.user_routes import user_bp
from routes.waiter_routes import waiter_bp
from routes.product_routes import product_bp

#from variables import cargarvariables

app = Flask(__name__)
app.config.from_pyfile('config/settings.py')

  
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(waiter_bp, url_prefix='/api/waiters')
app.register_blueprint(product_bp, url_prefix='/api/products')

if __name__ == '__main__':
    #port = int(os.environ.get('PORT'))
    #host = os.environ.get('HOST')
    #app.run(host=host, port=port)
    app.run(host="0.0.0.0", port=8080)