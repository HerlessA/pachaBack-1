from orator.seeds import Seeder


class CursosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Cursos').insert({
            'name': 'Historia',
            'profesor':'Luis'
        })

