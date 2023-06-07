import os
import os.path


class Animal:
    def _init_(self, nombre):
        self.nombre = nombre
        self.especies = []

    def agregar_especie(self, especie):
        self.especies.append(especie)

    def peso_promedio(self):
        if not self.especies:
            return 0
        else:
            return sum(especie.peso for especie in self.especies) / len(self.especies)


class AdministrarAnimales:
    def _init_(self, archivo):
        self.archivo = archivo
        self.animales = {}

    def agregar_animal(self, nombre):
        animal = Animal(nombre)
        self.animales[nombre] = animal

    def guardar_animales(self, nombre):
        if not os.path.isfile(self.archivo):
            print(f"El archivo {self.archivo} no existe.")
            return

        ruta_archivo = os.path.join(os.getcwd(), "prueba.txt")
        with open(ruta_archivo, "w") as archivo:
            archivo.write(nombre + "/")

    def cargar_animales(self):
        if not os.path.isfile(self.archivo):
            print(f"El archivo {self.archivo} no existe.")
            return

        ruta_archivo = os.path.join(os.getcwd(), "prueba.txt")

        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)


if __name__ == "__main__":
    archivo = "prueba.txt"
    admin = AdministrarAnimales(archivo)

    opcion = ""
    while opcion != "q":
        print("1.- Guardar nombre del animal")
        print("2.- Cargar información")
        print("3.- Guardar animal")
        print("4.- Listar animales")
        print("q.- Salir")

        opcion = input("Ingrese una opcion:")

        if opcion == "1":
            nombre = input("Ingrese el nombre del animal a guardar: ")
            admin.guardar_animales(nombre)
            print("Animal ingresado correctamente")
        elif opcion == "2":
            admin.cargar_animales()
            print("Animales cargados correctamente")
        elif opcion == "3":
            admin.guardar_animales()
            print("Animales guardados correctamente")
        elif opcion == "4":
            for nombre, animal in admin.animales.items():
                print(
                    f"{nombre}: {len(animal.especies)} especies, peso promedio: {animal.peso_promedio()}"
                )
        else:
            print("Opción inválida")
