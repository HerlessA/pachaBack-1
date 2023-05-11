from orator.seeds import Seeder
from .Alumnos_table_seeder import AlumnosTableSeeder
from .Profesores_table_seeder import ProfesoresTableSeeder
from .Cursos_table_seeder import CursosTableSeeder
from .Salones_table_seeder import SalonesTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)
        self.call(ProfesoresTableSeeder)
        self.call(CursosTableSeeder)
        self.call(SalonesTableSeeder)

