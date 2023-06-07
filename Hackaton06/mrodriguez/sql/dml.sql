SELECT * FROM notas;

SELECT id, nombre, dni, edad, correo FROM alumnos WHERE id = 1;

INSERT INTO notas(valor, id_alumno, id_curso, id_bimestre) VALUES (10, 4, 2, 2);

-- eliminar
DELETE FROM periodos WHERE id < 11;
-- eliminar columun
ALTER TABLE bimestres DROP nota_final;

ALTER SEQUENCE amlumnos_id_seq RESTART WITH 1;

-- eliminar tablas con fk
DROP TABLE notas CASCADE;