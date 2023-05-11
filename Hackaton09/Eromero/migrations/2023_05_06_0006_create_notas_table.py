from orator.migrations import Migration


class CreateNotasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('notas') as table:
            table.increments('id')
            table.integer('alumno_id').unsigned()
            table.foreign('alumno_id').references('id').on('alumnos')
            table.integer('profesor_id').unsigned()
            table.foreign('profesor_id').references('id').on('profesores')
            table.integer('bimestre_id').unsigned()
            table.foreign('bimestre_id').references('id').on('bimestres')
            table.integer('curso_id').unsigned()
            table.foreign('curso_id').references('id').on('cursos')
            table.integer('nota')
            table.string('comentario')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('notas')
