from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert(
        {
                'nombre': 'alumno1',
                'edad': 12,
                'correo': 'alum1@gmail.com',
                'notas': 10,
                'id_salon': 1
        })




        # alumno1 = Alumno(1,"alum1", 19, "alum1@gmail.com",[10,10,10],1)
        # alumno2 = Alumno(2,"alum2", 20, "alum2@gmail.com",[10,10,10],2)
        # alumno3 = Alumno(3,"alum3", 21, "alum3@gmail.com",[10,10,10],3)
        # alumno4 = Alumno(4,"alum4", 21, "alum4@gmail.com",[10,10,10],1)
        # alumno5 = Alumno(5,"alum5", 21, "alum5@gmail.com",[10,10,10],2)
        # alumno6 = Alumno(6,"alum6", 21, "alum6@gmail.com",[10,10,10],3)



