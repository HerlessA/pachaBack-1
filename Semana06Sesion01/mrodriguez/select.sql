--SELECT

SELECT * FROM ordenes;

--filter
SELECT * FROM Ordenes
WHERE idcliente  = 234
order by venta desc

SELECT * FROM Ordenes order by venta asc

--count
SELECT idenvio, count (idenvio) from Ordenes
group by idenvio


CREATE TABLE IF NOT EXISTS clientes(
	idcliente serial primary key,
    nombrecliente varchar(256) not null,
	idsegmento int not null
	idpais int not null
	idciudad int not null
	idestado int not null
	codigopostal varchar(20) not null,
	idregion int not null
	foreign key (idsegmento) references segmentos(idsegmento)
	foreign key (idpais) references paises(idpais)
	foreign key (idciudad) references ciudades(idciudad)
	foreign key (idestado) references estados(idestado)
	foreign key (idregion) references regiones(idregion)
);