from orator.seeds import Seeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .cursos_table_seeder import CursosTableSeeder
from .profesors_table_seeder import ProfesorsTableSeeder
from .periodos_table_seeder import PeriodosTableSeeder
from .salones_table_seeder import SalonesTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)
        self.call(CursosTableSeeder)
        self.call(ProfesorsTableSeeder)
        self.call(PeriodosTableSeeder)
        self.call(SalonesTableSeeder)

