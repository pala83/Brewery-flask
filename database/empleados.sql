CREATE DATABASE IF NOT EXISTS empleados;
USE empleados;

CREATE TABLE empleado(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255),
    correo VARCHAR(255),
    foto VARCHAR(255),
    PRIMARY KEY(id)
);

INSERT INTO empleado (nombre, correo, foto) VALUES
("Mario", "mario@email.com", "fotodemario.png");

SELECT * FROM empleado;