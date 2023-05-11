from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("profesores").insert(
            {
                "nombre": "Roberto Pineda",
                "dni": "40124578",
                "edad": 40,
                "email": "rprineda@abcd.com",
            }
        )
        self.db.table("profesores").insert(
            {
                "nombre": "María Rosales",
                "dni": "50201478",
                "edad": 52,
                "email": "mrosales@abcd.com",
            }
        )
        self.db.table("profesores").insert(
            {
                "nombre": "Carlos Alcántara",
                "dni": "60101478",
                "edad": 44,
                "email": "alcantara@abcd.com",
            }
        )
