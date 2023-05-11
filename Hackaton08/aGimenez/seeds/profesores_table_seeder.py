from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert({
                'nombre': 'Roberto Pineda',
                'identProfesor':'001575291',
                'edad':40,
                'email': 'rpineda@x-codec.net'
            })
        self.db.table('profesores').insert({
                'nombre': 'Ester Rojas',
                'identProfesor':'33567234',
                'edad':60,
                'email': 'ester@mail.com.ar'
            })
        self.db.table('profesores').insert({
                'nombre': 'Pablo Gimenez',
                'identProfesor':'67589023',
                'edad':45,
                'email': 'pablo@mail.com.ar'
            })