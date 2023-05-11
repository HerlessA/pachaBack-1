from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
            'nombre':'Felipe',
            'edad':'18',
            'correo':'felipe@gmail.com'
        })

