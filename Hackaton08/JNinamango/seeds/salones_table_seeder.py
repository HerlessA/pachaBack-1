from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('salones').insert(
            {
                'nombre': 'salon1',
                'fecha': "2020-04-05"
            }
        )

