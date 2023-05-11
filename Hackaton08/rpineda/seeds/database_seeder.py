from orator.seeds import Seeder
from .alumnos_table_seeder import AlumnosTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnosTableSeeder)

