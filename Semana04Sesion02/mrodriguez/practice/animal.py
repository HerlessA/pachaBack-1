# import pickle


# class Animal:
#     def __init__(self, name):
#         # contextos:
#         self.name = name
#         # self.weight = weight
#         self.species = []

#     def add_animal(self, species):
#         self.species.append(species)

#     def average_weight(self):
#         if self.weight == None:
#             return 0
#         else:
#             return sum(self.weight) / len(self.species)


# class AnimalAdmin:
#     def __init__(self, file):
#         self.file = file
#         self.animal = {}

#     def add_animal(self, name):
#         animal = Animal(name)
#         self.animal[name] = animal

#     def animal_to_list(self):
#         with open(self.file, "rb"):
#             self.animal = pickle.load()

#     # def upload_weight(self):


# # para validar tipo de variable __name__ = str
# # si se almacena se guarda el dato con esa sintaxis __dato__
# if __name__ == "__main__":
#     file = "zooSystem.pkl"
#     admin = AnimalAdmin(file)

#     option = ""

#     while option != "q":
#         print("1.- Guardar nombre del animal")
#         print("2.- Guardar información")
#         print("3.- Guardar animal")
#         print("4.- Guardar animal")
#         print("5.- Guardar animal")
#         print("q.- Salir")

#         option = input("Ingresa una opción: ")
#         if option == "1":
#             name = input("Ingresar nombre del animal: ")
#             admin.add_animal(name)
#             print("Animal ingresado correctamente")
#         elif option == "2":
#             admin.animal_to_list()
#             print("OK")
#             break
#         else:
#             print("X")
#         # with open("zooSystem.pkl", "rb") as f:
#         #     data = pickle.load(f)
#         # print(data)
