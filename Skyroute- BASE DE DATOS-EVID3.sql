CREATE DATABASE skyroute;

Use skyroute;


create table clientes (Id_cliente INT);

alter table clientes add column nombre varchar(50);
alter table clientes add column DNI INT;
alter table clientes add column email varchar (50);

alter table clientes drop column Id_cliente;
alter table clientes add column id_cliente INT PRIMARY KEY NOT NULL auto_increment;

describe clientes;

insert into clientes (nombre, dni, email) values 
('Juan Perez', 45234543, 'juan_perez@ispc.com.ar'), 
('Maria Molina', 47262833, 'maria_molina@ispc.com.ar'), 
('Rosa Sanchez', 42356345, 'rosa_sanchez@ispc.com.ar'),
('Ramiro lopez', 5836292, 'ramiro_lopez@ispc.com.ar'), 
('Jonathan gigena', 48262829, 'jona_gige@ispc.com.ar'),
 ('Griselda Luduena', 31827343, 'gri_ludu@ispc.com.ar');


-- Con la siguiente sentencia, podemos ver el listado de clientes

SELECT * from clientes;

 
 CREATE TABLE Destino (id_destino INT PRIMARY KEY NOT NULL auto_increment);
 
alter table Destino add column Pais varchar (15),
alter table Destino add column Ciudad varchar (15),
alter table Destino add column Precio float;

Describe Destino;

Insert into Destino (Pais, Ciudad, Precio) values
('Alemania', 'Frankfurt', 653500.00),
('Argentina', 'Buenos Aires', 72934.00),
('Argentina', 'Córdoba', 32283.00),
('Peru', 'Lima', 836283.00),
('Uruguay', 'Punta de Este', 83722.00),
('Francia', 'París', 300000.00),
('Japón','Tokio', 3840.00),
('México','Cancún', 1440.00),
('Italia','Roma', 2520.00);


Select * from Destino;
 
CREATE TABLE Venta (
    id_venta INT PRIMARY KEY NOT NULL auto_increment,
    fecha DATE NOT NULL,
    estado_venta BOOLEAN NOT NULL DEFAULT TRUE,
    id_cliente INT,
    id_destino INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES Destinos(id_destino)
);
Describe venta;

INSERT INTO venta (fecha, id_cliente, id_destino) VALUES
('2025-01-15', 1, 4),
('2025-03-22', 3, 7),
('2025-07-09', 2, 10),
('2025-10-30', 6, 1),
('2025-12-05', 5, 6),
('2026-02-18', 4, 2),
('2026-04-10', 2, 9),
('2026-06-25', 1, 3),
('2026-09-03', 3, 5),
('2026-11-14', 6, 8);
 
 select * from venta;

-- Con siguiente sentencia, podemos ver las ventas realizadas en determinada fecha.
 
 SELECT *
FROM venta
WHERE fecha = '2025-01-15';

-- Con la siguiente sentencia, podemos filtrar la ultima vente por cliente

SELECT v.id_cliente, c.nombre, v.id_venta, v.fecha
FROM venta v
JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE v.fecha = (
    SELECT MAX(v2.fecha)
    FROM venta v2
    WHERE v2.id_cliente = v.id_cliente
);

-- En la siguiente sentencia, podemos buscar los Paises que empiecen con "S"

SELECT *
FROM destino
WHERE Pais OR Ciudad LIKE 'S%';

-- Con la siguiente sentencia, podemos ver cuantas ventas se realizaron por pais

SELECT d.pais, COUNT(*) AS total_ventas
FROM venta v
JOIN destino d ON v.id_destino = d.id_destino
GROUP BY d.pais
ORDER BY total_ventas DESC;
 