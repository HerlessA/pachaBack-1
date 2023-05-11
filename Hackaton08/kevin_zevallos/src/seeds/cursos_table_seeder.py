from orator.seeds import Seeder


class CursosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
            'nombre':'programacion 1',
            'profesor':'jose'
        })

