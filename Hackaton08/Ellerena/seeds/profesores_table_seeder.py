from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert({
                'nombre': 'Juan Rodriguez',
                'identificador':'001575292',
                'edad':40,
                'email': 'JuanP@x-codec.net'
            })

