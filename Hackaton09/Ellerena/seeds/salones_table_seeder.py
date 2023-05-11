from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        alum1 = self.db.table("alumnos").where("nombre", "Alonso Ulloa").first()
        alum2 = self.db.table("alumnos").where("nombre", "Willy Percy").first()
        alum3 = self.db.table("alumnos").where("nombre", "Yolanda Mercedez").first()

        prof1 = self.db.table("profesores").where("nombre", "Roberto Pineda").first()
        prof2 = self.db.table("profesores").where("nombre", "Sheyla Guerrero").first()
        prof3 = self.db.table("profesores").where("nombre", "Edgar Poma").first()

        self.db.table("salones").insert(
            {
                "nombre": "A",
                "periodo": "2023-1",
                "alumno_id": alum1.id,
                "profesor_id": prof1.id,
            }
        )
        self.db.table("salones").insert(
            {
                "nombre": "A",
                "periodo": "2023-1",
                "alumno_id": alum2.id,
                "profesor_id": prof1.id,
            }
        )
        self.db.table("salones").insert(
            {
                "nombre": "A",
                "periodo": "2023-1",
                "alumno_id": alum3.id,
                "profesor_id": prof2.id,
            }
        )
        self.db.table("salones").insert(
            {
                "nombre": "A",
                "periodo": "2023-1",
                "alumno_id": alum1.id,
                "profesor_id": prof3.id,
            }
        )