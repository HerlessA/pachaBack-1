from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cursos') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('id_profesor')
            table.timestamps()

            table.foreign('id_profesor').references('id').on('profesores').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cursos')
