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
-- Insertar datos de prueba en la tabla de CAMAREROS (waiters)
INSERT INTO waiters (identification, firstname, lastname1, lastname2, phone, email)
VALUES
    ('123456789', 'Juan', 'Pérez', 'Gómez', '555-1234', 'juan.perez@example.com'),
    ('987654321', 'María', 'López', 'Martínez', '555-5678', 'maria.lopez@example.com'),
    ('456789123', 'Carlos', 'Fernández', 'Sánchez', '555-8765', 'carlos.fernandez@example.com');

-- Insertar datos de prueba en la tabla de USUARIOS (users)
INSERT INTO users (id_waiter, username, is_admin, password)
VALUES
    (1, 'juanperez', FALSE, 'password123'),
    (2, 'marialopez', FALSE, 'password456'),
    (3, 'adminuser', TRUE, 'adminpass123');  -- Usuario administrador

-- Insertar datos de prueba en la tabla de PRODUCTOS (products)
INSERT INTO products (name, description, number, price, tax, image)
VALUES
    ('Pizza Margarita', 'Pizza con tomate, queso mozzarella y albahaca', 1001, 8.99, 10.00, 'pizza_margarita.jpg'),
    ('Hamburguesa Clásica', 'Hamburguesa con carne de res, lechuga, tomate y cebolla', 1002, 6.50, 8.00, 'hamburguesa_clasica.jpg'),
    ('Ensalada César', 'Ensalada con lechuga, pollo, croutons y salsa César', 1003, 5.99, 7.00, 'ensalada_cesar.jpg');
