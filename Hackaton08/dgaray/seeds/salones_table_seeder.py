from orator.seeds import Seeder


class SalonesTableSeeder(Seeder):

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


        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor1['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor2['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno1['id'],
            'profesor_id': profesor3['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor1['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor2['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno2['id'],
            'profesor_id': profesor3['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor1['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor2['id']
        })
        self.db.table('salones').insert({
            'ano_escolar': '1ro',
            'seccion': 'B',
            'alumno_id': alumno3['id'],
            'profesor_id': profesor3['id']
        })
        

