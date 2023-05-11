from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("alumnos").insert(
            {
                "nombre": "Mari R",
                "dni": "73737373",
                "edad": 25,
                "email": "mari@abc.com",
            }
        )
        self.db.table("alumnos").insert(
            {
                "nombre": "Luis Salaz",
                "dni": "20202020",
                "edad": 18,
                "email": "luis@abc.com",
            }
        )
        self.db.table("alumnos").insert(
            {
                "nombre": "Alicia Pérez",
                "dni": "60504050",
                "edad": 28,
                "email": "alicia@abc.com",
            }
        )
