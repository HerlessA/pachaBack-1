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
            table.integer('curso_id').unsigned()
            table.foreign('curso_id').references('id').on('cursos')
            table.float('nota')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('notas')
