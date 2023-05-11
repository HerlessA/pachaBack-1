from orator.seeds import Seeder


class ProfesoresTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesores').insert({
                'nombre': 'Roberto Pineda',
                'identificador':'001575291',
                'edad':40,
                'email': 'rpineda@x-codec.net'
            })
        self.db.table('profesores').insert({
                'nombre': 'Roberto2',
                'identificador':'001575292',
                'edad':40,
                'email': 'rpineda2@x-codec.net'
            })
        self.db.table('profesores').insert({
                'nombre': 'Roberto3',
                'identificador':'001575293',
                'edad':40,
                'email': 'rpineda3@x-codec.net'
            })

