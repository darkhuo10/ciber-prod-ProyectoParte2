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
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(50) UNIQUE,
    username VARCHAR(30) UNIQUE NOT NULL,
    isadmin BOOLEAN DEFAULT FALSE,
    password VARCHAR(100) NOT NULL,
    lastaccess DATE,
    loginerror INTEGER
);

-- Tabla PRODUCTOS
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    number INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    tax INT NOT NULL
);
-- Insertar datos de prueba en la tabla de CAMAREROS (waiters)
INSERT INTO waiters (identification, firstname, lastname1, lastname2, phone, email, username, isadmin, password, loginerror) VALUES
    ('987654321', 'nombre', 'ap1', 'ap2', '555-5678', 'admin@example.com', 'adminuser', TRUE, '$2b$10$bmRewuyQ57fOW3v9YHQuZe8TpqUA5BBC7D864QpY/DJLXSKbP.W7i', 0);

-- Insertar datos de prueba en la tabla de PRODUCTOS (products)
INSERT INTO products (name, description, number, price, tax) VALUES
    ('Pizza Margarita', 'Pizza con tomate, queso mozzarella y albahaca', 8, 8.99, 21),
    ('Hamburguesa Clásica', 'Hamburguesa con carne de res, lechuga, tomate y cebolla', 6, 6.50, 21),
    ('Ensalada César', 'Ensalada con lechuga, pollo, croutons y salsa César', 6, 5.99, 21);
