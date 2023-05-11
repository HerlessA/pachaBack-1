from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert(
        {
            'nombre': 'profe1',
            'edad': 121,
            'correo': 'profe1@gmail.com',
            'id_salon': 1
        })

