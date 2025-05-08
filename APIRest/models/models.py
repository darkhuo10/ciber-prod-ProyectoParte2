class Waiter():
    def __init__(self, identification: str, firstname: str, lastname1: str, lastname2: str, phone: str, email: str, username: str, passwordhash: str, isadmin: bool = False):
        self.identification = identification
        self.firstname = firstname
        self.lastname1 = lastname1
        self.lastname2 = lastname2
        self.phone = phone
        self.email = email
        self.username = username
        self.passwordhash = passwordhash
        self.isadmin = isadmin
        

    def __repr__(self):
        return f"<Waiter(identification={self.identification}, name={self.firstname} {self.lastname1} {self.lastname2})>"


class Product():
    def __init__(self, name: str, number: int, description: str, price: float, tax: float, image: str):
        self.name = name
        self.number = number
        self.description = description
        self.price = price
        self.tax = tax
        self.image = image

    def __repr__(self):
        return f"<Product(name={self.name}, number={self.number}, price={self.price:.2f}, iva={self.tax}%)>"