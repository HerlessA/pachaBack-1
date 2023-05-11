from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
            'nombre':'kevin',
            'edad':23,
            'correo':'kevin@gmail.com'
        })

