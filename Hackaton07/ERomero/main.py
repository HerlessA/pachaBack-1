from clases import Alumno, Salon, Curso, Profesor

def obtener_input(nombre_campo):
    valor = input(f"Ingrese el {nombre_campo}: ")
    while not valor:
        print(f"El {nombre_campo} no puede estar vacío.")
        valor = input(f"Ingrese el {nombre_campo}: ")
    return valor


def menu_profesor():
    while True:
        print("Menú de Profesores")
        print("1. Agregar profesor")
        print("2. Actualizar profesor")
        print("3. Eliminar profesor")
        print("4. Buscar profesor")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = obtener_input("nombre del profesor")
            identificador = obtener_input("identificador del profesor")
            edad = obtener_input("edad del profesor")
            correo = obtener_input("correo del profesor")
            profesor = Profesor(nombre, identificador, edad, correo)
            profesor.insertar()
            print("Profesor agregado con éxito.")
        elif opcion == "2":
            identificador = obtener_input("identificador del profesor")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                nombre = obtener_input(f"nuevo nombre para {profesor.nombre}")
                edad = obtener_input(f"nueva edad para {profesor.edad}")
                correo = obtener_input(f"nuevo correo para {profesor.correo}")
                profesor.nombre = nombre
                profesor.edad = edad
                profesor.correo = correo
                profesor.actualizar()
                print("Profesor actualizado con éxito.")
        elif opcion == "3":
            identificador = obtener_input("identificador del profesor")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                profesor.eliminar()
                print("Profesor eliminado con éxito.")
        elif opcion == "4":
            identificador = obtener_input("identificador del profesor")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                print("Nombre:", profesor.nombre)
                print("Identificador:", profesor.identificador)
                print("Edad:", profesor.edad)
                print("Correo:", profesor.correo)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_curso():
    while True:
        print("\nMenú de Cursos")
        print("1. Agregar curso")
        print("2. Actualizar curso")
        print("3. Eliminar curso")
        print("4. Buscar curso")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del curso: ")
            identificador_profesor = input("Ingrese el identificador del profesor: ")
            profesor = Profesor.seleccionar(identificador_profesor)

            if profesor is None:
                print("El profesor no existe")
                continue

            curso = Curso(nombre, profesor)
            curso.insertar()
            print("El curso ha sido agregado correctamente")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del curso: ")
            curso = Curso.seleccionar(nombre)

            if curso is None:
                print("El curso no existe")
                continue

            identificador_profesor = input("Ingrese el identificador del nuevo profesor: ")
            profesor = Profesor.seleccionar(identificador_profesor)

            if profesor is None:
                print("El profesor no existe")
                continue

            curso.profesor = profesor
            curso.actualizar()
            print("El curso ha sido actualizado correctamente")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del curso: ")
            curso = Curso.seleccionar(nombre)

            if curso is None:
                print("El curso no existe")
                continue

            curso.eliminar()
            print("El curso ha sido eliminado correctamente")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del curso: ")
            curso = Curso.seleccionar(nombre)

            if curso is None:
                print("El curso no existe")
                continue

            print(f"Nombre del curso: {curso.nombre}")
            print(f"Profesor asignado: {curso.buscar_profesor()}")
        elif opcion == "5":
            break
        else:
            print("Opción no válida")


def menu_salon():
    while True:
        print("\nMenú de Salones")
        print("1. Agregar salón")
        print("2. Actualizar salón")
        print("3. Eliminar salón")
        print("4. Buscar salón")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del salón: ")
            anio_escolar = input("Ingrese el año escolar del salón: ")
            salon = Salon(nombre, anio_escolar)
            salon.insertar()
            print("Salón agregado exitosamente.")
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del salón a actualizar: ")
            anio_escolar = input("Ingrese el nuevo año escolar del salón: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                salon.anio_escolar = anio_escolar
                salon.actualizar()
                print("Salón actualizado exitosamente.")
                
        elif opcion == "3":
            nombre = input("Ingrese el nombre del salón a eliminar: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                salon.eliminar()
                print("Salón eliminado exitosamente.")
                
        elif opcion == "4":
            nombre = input("Ingrese el nombre del salón: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                print(f"Nombre:{salon.nombre}")
                print(f"Año escolar:{salon.anio_escolar}")
                
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_alumno():
    while True:
        print("\nMenú de Alumnos")
        print("1. Agregar alumno")
        print("2. Actualizar alumno")
        print("3. Eliminar alumno")
        print("4. Buscar alumno")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            identificador = input("Ingrese el identificador del alumno: ")
            edad = input("Ingrese la edad del alumno: ")
            correo = input("Ingrese el correo del alumno: ")
            alumno = Alumno(nombre, identificador, edad, correo)
            alumno.insertar()
            print("Alumno agregado con éxito.")
            
        elif opcion == "2":
            identificador = input("Ingrese el identificador del alumno a actualizar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                nombre = input(f"Ingrese el nuevo nombre para el alumno {alumno.nombre}: ")
                edad = input(f"Ingrese la nueva edad para el alumno {alumno.nombre}: ")
                correo = input(f"Ingrese el nuevo correo para el alumno {alumno.nombre}: ")
                alumno.nombre = nombre
                alumno.edad = edad
                alumno.correo = correo
                alumno.actualizar()
                print("Alumno actualizado con éxito.")
                
        elif opcion == "3":
            identificador = input("Ingrese el identificador del alumno a eliminar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                alumno.eliminar()
                print(f"Alumno {alumno.nombre} eliminado exitosamente")

        elif opcion == "4":
            identificador = input("Ingrese el identificador del alumno a buscar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                print(f"Nombre: {alumno.nombre}")
                print(f"Identificador: {alumno.identificador}")
                print(f"Edad: {alumno.edad}")
                print(f"Correo: {alumno.correo}")

        elif opcion == "5":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

def main():
    while True:
        print("Menú principal")
        print("1. Profesores")
        print("2. Cursos")
        print("3. Salones")
        print("4. Alumnos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_profesor()
        elif opcion == "2":
            menu_curso()
        elif opcion == "3":
            menu_salon()
        elif opcion == "4":
            menu_alumno()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()