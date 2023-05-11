from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Salones').insert({
            'name': 'A',
            'anhoescolar': 2013
        })

