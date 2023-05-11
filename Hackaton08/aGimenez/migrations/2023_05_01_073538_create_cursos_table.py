from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cursos') as table:
            table.increments('id')
            table.text('nombre')
            table.integer('profesor_id').unique()
            table.timestamps()

            table.foreign('profesor_id').references('id').on('profesores').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cursos')
