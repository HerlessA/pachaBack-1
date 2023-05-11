from orator.migrations import Migration


class CreateProfesorsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profesors') as table:
            table.increments('id')
            table.text('nombre')
            table.text('identificador').unique()
            table.integer('edad').unsigned()
            table.string('correo').unique()
            table.integer('curso_id').unsigned()
            table.foreign('curso_id').references('id').on('cursos').on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profesors')
