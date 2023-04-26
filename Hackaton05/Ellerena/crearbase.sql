CREATE DATABASE "SV73216398"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;



CREATE TABLE IF NOT EXISTS Regiones(
	IdRegion serial,
	Detalle varchar(50) not null,
	primary key(IdRegion)
);

CREATE TABLE IF NOT EXISTS SubCategorias(
	IdSubCategoria serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Categorias(
	IdCategoria serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Estados(
	IdEstado serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Ciudades(
	IdCiudad serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Paises(
	IdPais serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Segmentos(
	IdSegmento serial primary key,
	Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Clientes(
	IdCliente serial primary key,
	NombreCliente varchar(256) not null,
    IdSegmento int not null,
    IdPais int not null,
    IdCiudad int not null,
    IdEstado int not null,
    CodigoPostal varchar(20) not null,
    IdRegion int not null,
    Foreign key(IdSegmento) References Segmentos(IdSegmento),
    Foreign key(IdPais) References Paises(IdPais),
    Foreign key(IdCiudad) References Ciudades(IdCiudad),
    Foreign key(IdEstado) References Estados(IdEstado),
    Foreign key(IdRegion) References Regiones(IdRegion)
);

CREATE TABLE IF NOT EXISTS Productos(
    IdProduto serial primary key,
    IdCategoria int not null,
    IdSubCategoria int not null,
    NombreProducto varchar(256) not null,
    Foreign key(IdCategoria) references Categorias(IdCategoria),
    Foreign key(IdSubCategoria) references SubCategorias(IdSubCategoria)
);

CREATE TABLE IF NOT EXISTS Envios(
    IdEnvio serial primary key,
    Detalle varchar(256) not null
);

CREATE TABLE IF NOT EXISTS Ordenes(
    OrderId serial primary key,
    FechaOrden date not null,
    FechaEnvio date not null,
    IdEnvio int not null,
    IdCliente int not null,
    IdProduto int not null,
    Venta money not null,
    Cantidad int not null,
    Descuento decimal(18,2) not null,
    Total decimal(18,2) not null,
    Foreign key(IdEnvio) references Envios(IdEnvio),
    Foreign key(IdCliente) references Clientes(IdCliente),
    Foreign key(IdProduto) references Productos(IdProduto)
);