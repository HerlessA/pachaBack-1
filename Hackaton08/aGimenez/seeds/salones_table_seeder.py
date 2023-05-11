from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        #Profesores
        roberto = self.db.table('profesores').where('identProfesor', '001575291').first()
        ester = self.db.table('profesores').where('identProfesor', '33567234').first()
        pablo = self.db.table('profesores').where('identProfesor', '67589023').first()

        #Alumnos
        adriana = self.db.table('alumnos').where('identAlumno', '005618467').first()
        david = self.db.table('alumnos').where('identAlumno', '76606397').first()
        jonathan = self.db.table('alumnos').where('identAlumno', '51204429').first()
        estela = self.db.table('alumnos').where('identAlumno', '13774136').first()
        pablino = self.db.table('alumnos').where('identAlumno', '13959968').first()

        self.db.table('salones').insert({'nombre': '102', 'añoEscolar': '2022', 'identProfesor': roberto.identProfesor, 'identAlumno': adriana.identAlumno})
        self.db.table('salones').insert({'nombre': '102', 'añoEscolar': '2022', 'identProfesor': roberto.identProfesor, 'identAlumno': estela.identAlumno})
        self.db.table('salones').insert({'nombre': '104', 'añoEscolar': '2022','identProfesor': ester.identProfesor, 'identAlumno': pablino.identAlumno})
        self.db.table('salones').insert({'nombre': '105', 'añoEscolar': '2023','identProfesor': pablo.identProfesor, 'identAlumno': estela.identAlumno})
        self.db.table('salones').insert({'nombre': '105', 'añoEscolar': '2023','identProfesor': pablo.identProfesor, 'identAlumno': pablino.identAlumno})
    