from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert({
            'nombre':'Jose',
            'edad':'35',
            'correo':'jose@gmail.com'
        })

