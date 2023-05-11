from orator.migrations import Migration


class CreateSalonesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('salones') as table:
            table.increments('id')
            table.string('nombre')
            table.string('año_escolar')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('salones') as table:
            pass
