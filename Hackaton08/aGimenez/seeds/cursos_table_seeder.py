from orator.seeds import Seeder


class CursosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        roberto = self.db.table('profesores').where('identProfesor', '001575291').first()
        ester = self.db.table('profesores').where('identProfesor', '33567234').first()
        pablo = self.db.table('profesores').where('identProfesor', '67589023').first()

        self.db.table('cursos').insert({'nombre': 'algebra', 'profesor_id': roberto.id})
        self.db.table('cursos').insert({'nombre': 'probabilidad', 'profesor_id': ester.id})
        self.db.table('cursos').insert({'nombre': 'base de datos', 'profesor_id': pablo.id})
