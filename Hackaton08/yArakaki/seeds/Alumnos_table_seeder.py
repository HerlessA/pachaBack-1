from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """

        self.db.table('Alumnos').insert({
            'name': 'twittor',
            'email': 'twittor@twittor.com',
            'edad': 11,
            'notas': 16,
            'identificador': '432789'
        })

