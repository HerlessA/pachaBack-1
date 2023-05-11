from orator.seeds import Seeder


class PeriodosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('periodos').insert({
            'nombre': '2023-A',
            'anio': 2023,
            'mes': 5,
        })


