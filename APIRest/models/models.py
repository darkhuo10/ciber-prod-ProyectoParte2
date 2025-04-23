class User():
    def __init__(self, id_waiter, username, password, is_admin = False):
        self.id_waiter = id_waiter
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        role = "Admin" if self.is_admin else "User"
        return f"<User(id={self.id}, username={self.username}, role={role})>"


class Waiter():
    def __init__(self, identification, firstname, lastname1, lastname2, phone, email):
        self.identification = identification
        self.firstname = firstname
        self.lastname1 = lastname1
        self.lastname2 = lastname2
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"<Waiter(identification={self.identification}, name={self.firstname} {self.lastname1} {self.lastname2})>"


class Product():
    def __init__(self, name, number, description, price, tax, image):
        self.name = name
        self.number = number
        self.description = description
        self.price = price
        self.tax = tax
        self.image = image

    def __repr__(self):
        return f"<Product(name={self.name}, number={self.number}, price={self.price:.2f}, iva={self.tax}%)>"
