from orator.seeds import Seeder


class CursosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('cursos').insert({
            'nombre': 'Algebra'
        })
        
        self.db.table('cursos').insert({
            'nombre': 'Quimica'
        })

