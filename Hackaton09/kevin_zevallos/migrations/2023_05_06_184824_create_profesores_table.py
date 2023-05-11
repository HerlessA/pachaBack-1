from orator.migrations import Migration


class CreateProfesoresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('profesores') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('edad')
            table.string('correo')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('profesores') as table:
            pass
