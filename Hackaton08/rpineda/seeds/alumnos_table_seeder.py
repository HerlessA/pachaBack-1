from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("alumnos").insert(
            {
                "nombre": "Roberto Pineda",
                "identificador": "001575291",
                "edad": 40,
                "email": "rpineda@x-codec.net",
            }
        )
