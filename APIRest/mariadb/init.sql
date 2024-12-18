-- Crear base de datos
CREATE DATABASE Restaurant;
USE Restaurant;

-- Tabla CAMAREROS
CREATE TABLE Waiters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    identification VARCHAR(9) UNIQUE NOT NULL,
    firstname VARCHAR(40) NOT NULL,
    lastname1 VARCHAR(30) NOT NULL,
    lastname2 VARCHAR(30),
    phone VARCHAR(9),
    email VARCHAR(50)
);

-- Tabla CLIENTES(USUARIOS)
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idwaiter INT NOT NULL,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (idwaiter) REFERENCES Waiter(id) ON DELETE CASCADE
);

-- Tabla PRODUCTOS
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    number INT NOT NULL,
    price FLOAT NOT NULL
);
