from orator.migrations import Migration


class CreateAlumnosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Alumnos') as table:
            table.increments('id')
            table.text('name').unique()
            table.text('email').unique()
            table.integer('edad').unsigned()
            table.text('identificador')
            table.integer('notas')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Alumnos')
