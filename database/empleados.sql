CREATE DATABASE IF NOT EXISTS brewery;
USE brewery;

CREATE TABLE empleado(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255),
    correo VARCHAR(255),
    foto VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE usuario(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    pass TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE cerveza(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    keywords VARCHAR(255) NOT NULL,
    precio INT NOT NULL,
    descripcion TEXT,
    ibu INT,
    alcohol INT,
    foto_birra VARCHAR(255),
    foto_tapa VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE categoria(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    tipo VARCHAR(255),
    PRIMARY KEY(id)
);

INSERT INTO cerveza (nombre, keywords, precio, descripcion, ibu, alcohol, foto_birra, foto_tapa) VALUES
("Black Horse Ale - Carling O'Keefe", "DORADA/SUAVE/FRESCA/FRUTADA", 450, "Existen muchas cervezas doradas y refrescantes. Pero frutadas y con destellos finales de lúpulo, sólo hay un estilo: la legendaria Black Horse Ale. En Brewery rescatamos la antigua receta de la cerveza favorita de los bebedores en Toronto, Canada, y la honramos desde 1983. En nuestra cocina, su legado sigue intacto.", 22, 5, "botella-black-horde.jpg", "tapa-black-horse.png"),

INSERT INTO cerveza (nombre, keywords, precio, descripcion, ibu, alcohol, foto_birra, foto_tapa) VALUES
("Branding Ale - Carling O'Keefe", "LUPULADA/TURBIA/SEDOSA", 700, "Este tipo de cervezas artesanales se fermentan a temperaturas superiores a las de las Lager (hasta los 25ºC). Son muy aromáticas, dulces, con cuerpo y generalmente con sabor muy marcado.", 25, 4, "botella-branding-ale.jpg", "tapa-branding-ale.png")

INSERT INTO empleado (nombre, correo, foto) VALUES
("Mario", "mario@email.com", "fotodemario.png");

SELECT * FROM empleado;