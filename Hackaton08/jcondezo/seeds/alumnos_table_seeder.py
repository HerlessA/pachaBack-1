from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
            'nombre': 'Jhon Condezo',
            'identificador': '45612301',
            'edad': 38,
            'correo': 'jcondezo@gmail.com'
        })