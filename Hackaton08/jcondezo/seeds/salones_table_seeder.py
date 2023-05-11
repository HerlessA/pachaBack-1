from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        periodo = self.db.table('periodos').where('nombre', '2023-A').first()
        alumno = self.db.table('alumnos').where('nombre', 'Jhon Condezo').first()
        profesor = self.db.table('profesors').where('nombre', 'Juan').first()

        self.db.table('salones').insert([
            {'periodo_id': periodo.id, 'alumno_id': alumno.id, 'profesor_id': profesor.id},
        ])

