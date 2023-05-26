from orator.migrations import Migration


class CreateVentasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('ventas') as table:
            table.increments('id')
            table.string('producto')
            table.integer('precio')
            table.integer('cantidad')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('ventas')
