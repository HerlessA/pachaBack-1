from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
                'nombre': 'Diego Garay',
                'identificador':'SV44796970',
                'edad': 35,
                'email': 'diegogaraycullas@gmail.com'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Diego2',
                'identificador':'SV44796971',
                'edad': 35,
                'email': 'diego2@gmail.com'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Diego3',
                'identificador':'SV44796972',
                'edad': 35,
                'email': 'diego3@gmail.com'
            })

