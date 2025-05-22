import os
from flask import Flask


app = Flask(__name__)

from routes import waiter_routes
from routes import product_routes


if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)