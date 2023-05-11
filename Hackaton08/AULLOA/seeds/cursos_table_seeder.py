from orator.seeds import Seeder


class CursosTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        prof1 = self.db.table("profesores").where("nombre", "Roberto Pineda").first()
        prof2 = self.db.table("profesores").where("nombre", "Sheyla Guerrero").first()
        prof3 = self.db.table("profesores").where("nombre", "Edgar Poma").first()

        self.db.table("cursos").insert(
            {
                "nombre": "Back-end",
                "profesor_id": prof1.id,
            }
        )
        self.db.table("cursos").insert(
            {
                "nombre": "Front-end",
                "profesor_id": prof2.id,
            }
        )
        self.db.table("cursos").insert(
            {
                "nombre": "UX/UI",
                "profesor_id": prof3.id,
            }
        )