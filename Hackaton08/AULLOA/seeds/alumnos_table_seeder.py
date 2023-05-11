from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
                'nombre': 'Alonso Ulloa',
                'dni':'73969282',
                'edad': 24,
                'email': 'grisol225@gmail.com'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Willy Percy',
                'dni':'73969281',
                'edad': 52,
                'email': 'willy@gmail.com'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Yolanda Mercedez',
                'dni':'SV73969283',
                'edad': 55,
                'email': 'yolanda@gmail.com'
            })