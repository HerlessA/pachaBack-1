from orator.seeds import Seeder


class ProfesorsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        curso = self.db.table('cursos').where('nombre', 'Algebra').first()

        self.db.table('profesors').insert({
            'nombre': 'Juan',
            'identificador': '04562312',
            'edad': 55,
            'correo': 'juan@gmail.com',
            'curso_id': curso['id']
        })

