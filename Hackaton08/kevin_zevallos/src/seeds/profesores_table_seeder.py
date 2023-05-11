from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert({
            'nombre':'jose',
            'edad':33,
            'correo':'jose@gmail.com'
        })

