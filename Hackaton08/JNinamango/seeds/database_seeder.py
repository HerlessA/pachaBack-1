from orator.seeds import Seeder
from .cursos_table_seeder import CursosTableSeeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .profesores_table_seeder import ProfesoresTableSeeder
from .salones_table_seeder import SalonesTableSeeder
class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(SalonesTableSeeder)
        self.call(AlumnosTableSeeder)
        self.call(ProfesoresTableSeeder)
        self.call(CursosTableSeeder)

