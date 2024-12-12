#import os
from flask import Flask
from models import models

#from variables import cargarvariables

app = Flask(__name__)
app.config.from_pyfile('config/settings.py')

  
from routes import user_routes, waiter_routes
app.register_blueprint(waiter_bp, url_prefix='/waiters')

if __name__ == '__main__':
    #port = int(os.environ.get('PORT'))
    #host = os.environ.get('HOST')
    #app.run(host=host, port=port)
    app.run(host="0.0.0.0", port=8080)