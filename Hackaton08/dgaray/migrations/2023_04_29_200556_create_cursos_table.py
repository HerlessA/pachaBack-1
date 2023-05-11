from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cursos') as table:
            table.increments('id')
            table.string('nombre_curso')
            table.integer('alumno_id').unsigned()
            table.integer('profesor_id').unsigned()
            table.integer('nota_bimestre1')
            table.integer('nota_bimestre2')
            table.integer('nota_bimestre3')
            table.integer('nota_bimestre4')
            table.timestamps()

            table.foreign('alumno_id').references('id').on('alumnos').on_delete('cascade')
            table.foreign('profesor_id').references('id').on('profesores').on_delete('cascade')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cursos')
