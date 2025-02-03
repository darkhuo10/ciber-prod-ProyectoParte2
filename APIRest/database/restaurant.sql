-- Crear base de datos
DROP DATABASE IF EXISTS restaurant;
CREATE DATABASE restaurant;
USE restaurant;

-- Tabla CAMAREROS
CREATE TABLE waiters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    identification CHAR(9) UNIQUE NOT NULL,
    firstname VARCHAR(40) NOT NULL,
    lastname1 VARCHAR(30) NOT NULL,
    lastname2 VARCHAR(30) NULL,
    phone VARCHAR(15),
    email VARCHAR(50) UNIQUE
);

-- Tabla USUARIOS
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_waiter INT NOT NULL,
    username VARCHAR(30) UNIQUE NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_waiter) REFERENCES waiters(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Tabla PRODUCTOS
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    number INT NOT NULL UNIQUE,
    price DECIMAL(10,2) NOT NULL,
    tax DECIMAL(5,2) NOT NULL,
    image VARCHAR(255)
);
