from orator.migrations import Migration


class CreateProductosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('productos') as table:
            table.increments('id')
            table.string('producto')
            table.integer('stock')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('productos')
