
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

-- Table: public.salon

-- DROP TABLE IF EXISTS public.salon;

CREATE TABLE IF NOT EXISTS public.salon
(
    idsalon integer NOT NULL DEFAULT nextval('salon_idsalon_seq'::regclass),
    nombre character varying(10) COLLATE pg_catalog."default",
    anioescolar integer,
    identificadorsalon character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.salon
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

-- Table: public.curso_profesor

-- DROP TABLE IF EXISTS public.curso_profesor;

CREATE TABLE IF NOT EXISTS public.curso_profesor
(
    idcurso integer,
    idprofesor integer,
    CONSTRAINT curso_profesor_idcurso_fkey FOREIGN KEY (idcurso)
        REFERENCES public.cursos (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT curso_profesor_idprofesor_fkey FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.curso_profesor
    OWNER to postgres;

-- Table: public.cursos

-- DROP TABLE IF EXISTS public.cursos;

CREATE TABLE IF NOT EXISTS public.cursos
(
    idcurso integer NOT NULL DEFAULT nextval('cursos_idcurso_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default",
    identificadorcurso character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT cursos_pkey PRIMARY KEY (idcurso)
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
    identificadorsalon character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.salon
    OWNER to postgres;

-- Table: public.salon_curso

-- DROP TABLE IF EXISTS public.salon_curso;

CREATE TABLE IF NOT EXISTS public.salon_curso
(
    idsalon integer,
    idcurso integer,
    CONSTRAINT salon_curso_idcurso_fkey FOREIGN KEY (idcurso)
        REFERENCES public.cursos (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT salon_curso_idsalon_fkey FOREIGN KEY (idsalon)
        REFERENCES public.salon (idsalon) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.salon_curso
    OWNER to postgres;

