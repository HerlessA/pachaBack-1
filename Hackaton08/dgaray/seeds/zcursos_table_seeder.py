from orator.seeds import Seeder


class CursosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        alumno1 = self.db.table('alumnos').where('nombre', 'Diego Garay').first()
        alumno2 = self.db.table('alumnos').where('nombre', 'Diego2').first()
        alumno3 = self.db.table('alumnos').where('nombre', 'Diego3').first()

        profesor1 = self.db.table('profesores').where('nombre', 'Roberto Pineda').first()
        profesor2 = self.db.table('profesores').where('nombre', 'Roberto2').first()
        profesor3 = self.db.table('profesores').where('nombre', 'Roberto3').first()

        self.db.table('cursos').insert({
            'nombre_curso': 'python',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor1['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'python',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor1['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'python',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor1['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'orator',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor2['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'orator',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor2['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'orator',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor2['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'flask',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor3['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'flask',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor3['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        self.db.table('cursos').insert({
            'nombre_curso': 'flask',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor3['id'],
            'nota_bimestre1': 20,
            'nota_bimestre2': 15,
            'nota_bimestre3': 10,
            'nota_bimestre4': 13
        })
        