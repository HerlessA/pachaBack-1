from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cursos') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('salon_id').unsigned()
            table.foreign('salon_id').references('id').on('salones')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cursos')