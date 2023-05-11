from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
            'nombre':'programacion 1',
            'año_escolar':'1'
        })

