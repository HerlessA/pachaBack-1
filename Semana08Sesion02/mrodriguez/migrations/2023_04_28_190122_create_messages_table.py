from orator.migrations import Migration


class CreateMessagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("messages") as table:
            table.increments("id")
            # agregando campos de la tabla
            table.text("content")
            table.integer("user_id").unsigned()  # para fk
            table.timestamps()

            # creando foreign key
            # .on_delete("cascade"): si en caso se borra el message, se boran los datos asociados
            table.foreign("user_id").references("id").on("users").on_delete("cascade")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("messages")
