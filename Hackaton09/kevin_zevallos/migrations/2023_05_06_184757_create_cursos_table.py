from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('cursos') as table:
            table.increments('id')
            table.string('nombre')
            table.string('profesor')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('cursos') as table:
            pass
