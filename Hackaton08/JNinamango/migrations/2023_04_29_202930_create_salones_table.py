from orator.migrations import Migration

#create tables:
#crear estructura de tabla: python db.py make:migration create_users_table --table users --create
#confirmar creacion:  python db.py migrate
#confirmar migracion u operacion: python db.py migrate:status
class CreateSalonesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('salones') as table:
            table.increments('id')
            table.string('nombre')
            table.string("fecha")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('salones')
