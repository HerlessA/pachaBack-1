from orator.migrations import Migration


class CreatePeriodosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('periodos') as table:
            table.increments('id')
            table.text('nombre')
            table.integer('anio')
            table.integer('mes')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('periodos')
