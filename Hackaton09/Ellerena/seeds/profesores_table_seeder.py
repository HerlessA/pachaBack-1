from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("profesores").insert(
            {
                "nombre": "Roberto Pineda",
                "dni": "73969270",
                "edad": 45,
                "email": "rprineda@gmail.com",
            }
        )
        self.db.table("profesores").insert(
            {
                "nombre": "Sheyla Guerrero",
                "dni": "73969271",
                "edad": 52,
                "email": "guerrero@gmail.com",
            }
        )
        self.db.table("profesores").insert(
            {
                "nombre": "Edgar Poma",
                "dni": "73969272",
                "edad": 64,
                "email": "poma@gmail.com",
            }
        )