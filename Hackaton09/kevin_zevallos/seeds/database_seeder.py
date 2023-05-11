from orator.seeds import Seeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .cursos_table_seeder import CursosTableSeeder
from .profesores_table_seeder import ProfesoresTableSeeder
from .salones_table_seeder import SalonesTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)
        self.call(CursosTableSeeder)
        self.call(ProfesoresTableSeeder)
        self.call(SalonesTableSeeder)

