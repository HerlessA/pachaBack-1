from orator.migrations import Migration


class CreateSalonesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Salones') as table:
            table.increments('id'),
            table.string('name').unique(),
            table.integer('anhoescolar')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Salones')
