from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('Profesores').insert({
            'name': 'Luis',
            'email': 'Luis@tgmail.com',
            'edad': 31,
            'identificador': '341289'
        })

