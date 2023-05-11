from orator.seeds import Seeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .profesores_table_seeder import ProfesoresTableSeeder
from .zcursos_table_seeder import CursosTableSeeder
from .salones_table_seeder import SalonesTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)
        self.call(ProfesoresTableSeeder)
        self.call(CursosTableSeeder)
        self.call(SalonesTableSeeder)

