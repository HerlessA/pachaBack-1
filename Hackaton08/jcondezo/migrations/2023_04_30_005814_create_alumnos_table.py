from orator.migrations import Migration


class CreateAlumnosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('alumnos') as table:
            table.increments('id')
            table.text('nombre')
            table.text('identificador').unique()
            table.integer('edad').unsigned()
            table.string('correo').unique()
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('alumnos')
