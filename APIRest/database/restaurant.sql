-- Crear base de datos
DROP DATABASE IF EXISTS restaurant;
CREATE DATABASE restaurant;
CREATE USER 'user'@'%' IDENTIFIED BY 'user+123';
GRANT ALL PRIVILEGES ON restaurant.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE restaurant;

-- Tabla PRODUCTOS
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    number INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    tax INT NOT NULL
);


CREATE TABLE users(
	username VARCHAR(100) NOT NULL PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    role VARCHAR(100) NOT NULL,
    activity VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    last_login DATE,
    block_date DATE,
    login_errors INTEGER,
    change_passwd BOOLEAN
);
INSERT INTO `users` (`username`, `passwd`, `role`,`activity`, `email`,`login_errors`,`last_login`) 
VALUES ('prueba','$2b$10$pkQRT4kV1j6nag3/z90R9u2pLCDo8Eyyp0KGk2Sr9.D6H48/17QZK', 'admin', 'active','test@test.com', 0, '2022-03-01 00:00');


-- Insertar datos de prueba en la tabla de PRODUCTOS (products)
INSERT INTO products (name, description, number, price, tax) VALUES
    ('Pizza Margarita', 'Pizza con tomate, queso mozzarella y albahaca', 8, 8.99, 21),
    ('Hamburguesa Clásica', 'Hamburguesa con carne de res, lechuga, tomate y cebolla', 6, 6.50, 21),
    ('Ensalada César', 'Ensalada con lechuga, pollo, croutons y salsa César', 6, 5.99, 21);
