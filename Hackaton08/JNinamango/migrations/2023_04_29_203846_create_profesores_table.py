from orator.migrations import Migration


class CreateProfesoresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profesores') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('edad')
            table.string('correo')
            table.integer('id_salon')
            table.timestamps()

            table.foreign('id_salon').references('id').on('salones').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profesores')
