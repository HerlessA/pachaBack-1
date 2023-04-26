-- Database: a1703782

-- DROP DATABASE IF EXISTS a1703782;

CREATE DATABASE a1703782
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.alumnos

-- DROP TABLE IF EXISTS public.alumnos;

CREATE TABLE IF NOT EXISTS public.alumnos
(
    idalumno integer NOT NULL DEFAULT nextval('alumnos_idalumno_seq'::regclass),
    identificadoralumno character varying(10) COLLATE pg_catalog."default",
    nombre character varying(50) COLLATE pg_catalog."default",
    edad integer,
    correo character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT alumnos_pkey PRIMARY KEY (idalumno)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alumnos
    OWNER to postgres;


-- Table: public.curso_alumno

-- DROP TABLE IF EXISTS public.curso_alumno;

CREATE TABLE IF NOT EXISTS public.curso_alumno
(
    idcurso integer,
    idalumno integer,
    CONSTRAINT curso_alumno_idalumno_fkey FOREIGN KEY (idalumno)
        REFERENCES public.alumnos (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT curso_alumno_idcurso_fkey FOREIGN KEY (idcurso)
        REFERENCES public.cursos (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.curso_alumno
    OWNER to postgres;

-- Table: public.cursos

-- DROP TABLE IF EXISTS public.cursos;

CREATE TABLE IF NOT EXISTS public.cursos
(
    idcurso integer NOT NULL DEFAULT nextval('cursos_idcurso_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default",
    idprofesor integer,
    CONSTRAINT cursos_pkey PRIMARY KEY (idcurso),
    CONSTRAINT cursos_idprofesor_fkey FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cursos
    OWNER to postgres;

-- Table: public.profesor

-- DROP TABLE IF EXISTS public.profesor;

CREATE TABLE IF NOT EXISTS public.profesor
(
    idprofesor integer NOT NULL DEFAULT nextval('profesor_idprofesor_seq'::regclass),
    identificadorprofesor character varying(10) COLLATE pg_catalog."default",
    nombre character varying(50) COLLATE pg_catalog."default",
    edad integer,
    correo character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT profesor_pkey PRIMARY KEY (idprofesor)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.profesor
    OWNER to postgres;

-- Table: public.salon

-- DROP TABLE IF EXISTS public.salon;

CREATE TABLE IF NOT EXISTS public.salon
(
    idsalon integer NOT NULL DEFAULT nextval('salon_idsalon_seq'::regclass),
    nombre character varying(10) COLLATE pg_catalog."default",
    anioescolar integer,
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.salon
    OWNER to postgres;

