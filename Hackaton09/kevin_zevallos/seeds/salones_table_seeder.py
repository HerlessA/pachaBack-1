from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('salones').insert({
            'nombre':'Salon Ciencias',
            'año escolar':'1'
        })

