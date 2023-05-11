from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert({
                'nombre': 'Adriana Gimenez',
                'identAlumno':'005618467',
                'edad':30,
                'email': 'adri.gimnz@mail.com.ar'
            })
        self.db.table('alumnos').insert({
                'nombre': 'David Ortiz',
                'identAlumno':'76606397',
                'edad':29,
                'email': 'adog@com.pe'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Jonathan Gonzalez',
                'identAlumno':'51204429',
                'edad':21,
                'email': 'Jngg@mail.com.ar'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Estela Ramirez',
                'identAlumno':'13774136',
                'edad':35,
                'email': 'stella@mail.com.ar'
            })
        self.db.table('alumnos').insert({
                'nombre': 'Pablino Galarza',
                'identAlumno':'13959968',
                'edad':40,
                'email': 'pab@mail.com.ar'
            })
