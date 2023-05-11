from orator.migrations import Migration


class CreateProfesoresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Profesores') as table:
            table.increments('id')
            table.text('name').unique()
            table.text('email').unique()
            table.integer('edad').unsigned()
            table.text('identificador')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Profesores')
