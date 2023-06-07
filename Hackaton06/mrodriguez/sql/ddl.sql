CREATE DATABASE sv73265099
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE alumnos(
	id serial primary key,
    nombre varchar(40) not null,
    dni varchar(20) not null,
    edad int not null,
	correo varchar(40) not null
);

CREATE TABLE profesores(
	id serial primary key,
    nombre varchar(40) not null,
    dni varchar(20) not null,
    edad int not null,
	correo varchar(40) not null
);

CREATE TABLE cursos(
	id serial primary key,
    nombre varchar(50) not null
);

CREATE TABLE bimestres(
	id serial primary key,
    nombre varchar(30) not null
);

CREATE TABLE periodos(
	id serial primary key,
    denominacion varchar(20) not null,
    id_bimestre int not null,
    FOREIGN KEY(id_bimestre) references bimestres(id)
);

CREATE TABLE cursosProfesores(
	id serial primary key,
    id_curso int not null,
    id_profesor int not null,
    FOREIGN KEY(id_curso) references cursos(id),
    FOREIGN KEY(id_profesor) references profesores(id)
);

CREATE TABLE salones(
	id serial primary key,
    seccion varchar(50) not null,
    id_alumno int not null,
    id_periodo int not null,
    id_profesor int not null,
    FOREIGN KEY(id_alumno) references alumnos(id),
    FOREIGN KEY(id_periodo) references periodos(id),
    FOREIGN KEY(id_profesor) references profesores(id)
);

-- CREATE TABLE notas(
-- 	id serial primary key,
--     valor int not null,
--     id_alumno int not null,
--     id_curso int not null,
--     id_bimestre int not null,
--     FOREIGN KEY(id_alumno) references alumnos(id),
--     FOREIGN KEY(id_curso) references cursos(id),
--     FOREIGN KEY(id_bimestre) references bimestres(id)
-- );

--periodos tiene a bimestres
CREATE TABLE notas(
	id serial primary key,
    valor int not null,
    id_alumno int not null,
    id_curso int not null,
    id_periodo int not null,
    FOREIGN KEY(id_alumno) references alumnos(id),
    FOREIGN KEY(id_curso) references cursos(id),
    FOREIGN KEY(id_periodo) references periodos(id)
);