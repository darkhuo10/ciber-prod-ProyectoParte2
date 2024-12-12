from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idwaiter = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, idwaiter, username, password):
        self.idwaiter = idwaiter
        self.username = username
        self.password = password


class Waiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(9), unique=True, nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname1 = db.Column(db.String(30), nullable=False)
    lastname2 = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(9), nullable=True)
    email = db.Column(db.String(50), nullable=True)

    def __init__(self, identification, firstname, lastname1, lastname2=None, phone=None, email=None):
        self.identification = identification
        self.firstname = firstname
        self.lastname1 = lastname1
        self.lastname2 = lastname2
        self.phone = phone
        self.email = email


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    number = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description=None, number=0, price=0.0):
        self.name = name
        self.number = number
        self.description = description
        self.price = price
