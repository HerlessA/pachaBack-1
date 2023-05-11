from orator.migrations import Migration


class CreateBimestresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('bimestres') as table:
            table.increments('id')
            table.string('nombre')
            table.string('descripcion')
            table.integer('anio_escolar')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('bimestres')
