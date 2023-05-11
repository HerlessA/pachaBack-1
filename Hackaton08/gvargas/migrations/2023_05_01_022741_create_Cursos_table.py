from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Cursos') as table:
            table.increments('id'),
            table.string('name').unique(),
            table.string('profesor')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Cursos')
