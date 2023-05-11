from orator.migrations import Migration


class CreateAlumnosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('alumnos') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('edad')
            table.string('correo')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('alumnos') as table:
            pass
