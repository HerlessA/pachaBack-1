from orator.migrations import Migration

class CreateProfesoresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profesores') as table:
            table.increments('id')
            table.string('nombre')
            table.string('apellido')
            table.string('correo').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profesores')
