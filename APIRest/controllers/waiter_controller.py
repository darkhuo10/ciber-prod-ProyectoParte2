from flask import request, jsonify
from models import models

# Create a new waiter
def create_waiter():
    data = request.get_json()
    identification = data.get('identification')
    firstname = data.get('firstname')
    lastname1 = data.get('lastname1')
    lastname2 = data.get('lastname2', None)
    phone = data.get('phone', None)
    email = data.get('email', None)

    new_waiter = Waiter(identification=identification, firstname=firstname, lastname1=lastname1,
                        lastname2=lastname2, phone=phone, email=email)

    db.session.add(new_waiter)
    db.session.commit()

    return jsonify({"message": "Waiter created", "id": new_waiter.id}), 201


# Get a list of all waiters
def get_all_waiters():
    waiters = Waiter.query.all()
    waiters_list = [{"id": waiter.id, "identification": waiter.identification, "firstname": waiter.firstname,
                     "lastname1": waiter.lastname1, "lastname2": waiter.lastname2, "phone": waiter.phone, "email": waiter.email} for waiter in waiters]
    return jsonify(waiters_list), 200


# Get a single waiter by id
def get_waiter(id):
    waiter = Waiter.query.get(id)
    if not waiter:
        return jsonify({"message": "Waiter not found"}), 404
    
    waiter_data = {"id": waiter.id, "identification": waiter.identification, "firstname": waiter.firstname,
                   "lastname1": waiter.lastname1, "lastname2": waiter.lastname2, "phone": waiter.phone, "email": waiter.email}
    return jsonify(waiter_data), 200


# Update a waiter by id
def update_waiter(id):
    data = request.get_json()
    waiter = Waiter.query.get(id)
    if not waiter:
        return jsonify({"message": "Waiter not found"}), 404
    
    waiter.identification = data.get('identification', waiter.identification)
    waiter.firstname = data.get('firstname', waiter.firstname)
    waiter.lastname1 = data.get('lastname1', waiter.lastname1)
    waiter.lastname2 = data.get('lastname2', waiter.lastname2)
    waiter.phone = data.get('phone', waiter.phone)
    waiter.email = data.get('email', waiter.email)

    db.session.commit()
    
    return jsonify({"message": "Waiter updated"}), 200


# Delete a waiter by id
def delete_waiter(id):
    waiter = Waiter.query.get(id)
    if not waiter:
        return jsonify({"message": "Waiter not found"}), 404
    
    db.session.delete(waiter)
    db.session.commit()
    
    return jsonify({"message": "Waiter deleted"}), 200
