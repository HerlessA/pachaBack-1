from orator.seeds import Seeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .profesores_table_seeder import ProfesoresTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)
        self.call(ProfesoresTableSeeder)

