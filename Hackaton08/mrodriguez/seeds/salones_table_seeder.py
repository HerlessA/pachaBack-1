from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        alum1 = self.db.table("alumnos").where("nombre", "Mari R").first()
        alum2 = self.db.table("alumnos").where("nombre", "Luis Salaz").first()
        alum3 = self.db.table("alumnos").where("nombre", "Alicia Pérez").first()

        prof1 = self.db.table("profesores").where("nombre", "Roberto Pineda").first()
        prof2 = self.db.table("profesores").where("nombre", "María Rosales").first()
        prof3 = self.db.table("profesores").where("nombre", "Carlos Alcántara").first()

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
