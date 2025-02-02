class BaseModel:
    def to_json(self):
        return self.__dict__


class User(BaseModel):
    def __init__(self, id: int, id_waiter: int, username: str, password: str, is_admin: bool = False):
        self.id = id
        self.id_waiter = id_waiter
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        role = "Admin" if self.is_admin else "User"
        return f"<User(id={self.id}, username={self.username}, role={role})>"


class Waiter(BaseModel):
    def __init__(self, identification: int, firstname: str, lastname1: str, lastname2: str, phone: str, email: str):
        self.identification = identification
        self.firstname = firstname
        self.lastname1 = lastname1
        self.lastname2 = lastname2
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"<Waiter(identification={self.identification}, name={self.firstname} {self.lastname1} {self.lastname2})>"


class Product(BaseModel):
    def __init__(self, id: int, name: str, number: int, description: str, price: float, tax: float, image: str):
        self.id = id
        self.name = name
        self.number = number
        self.description = description
        self.price = price
        self.tax = tax
        self.image = image

    def __repr__(self):
        return f"<Product(name={self.name}, number={self.number}, price={self.price:.2f}, iva={self.tax}%)>"
