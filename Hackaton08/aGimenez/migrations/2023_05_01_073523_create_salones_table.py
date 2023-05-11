from orator.migrations import Migration


class CreateSalonesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('salones') as table:
            table.increments('id')
            table.text('nombre')
            table.text('añoEscolar').unsigned()
            table.text('identProfesor')
            table.text('identAlumno')
            table.timestamps()

            table.foreign('identProfesor').references('identProfesor').on('profesores').on_delete('cascade')
            table.foreign('identAlumno').references('identAlumno').on('alumnos').on_delete('cascade')
            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('salones')
