from orator.migrations import Migration

#create tables:
#crear estructura de tabla: python db.py make:migration create_users_table --table users --create
#confirmar creacion:  python db.py migrate
#confirmar migracion u operacion: python db.py migrate:status
class CreateAlumnosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('alumnos') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('edad')
            table.string('correo')
            table.enum(10,10,10,10) 
            table.integer('id_salon')
            table.timestamps()

            table.foreign('id_salon').references('id').on('salones').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('alumnos')
