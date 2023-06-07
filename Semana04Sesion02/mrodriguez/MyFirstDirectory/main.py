import os
import shutil

currentDirectory = os.getcwd()
print(currentDirectory)

# Crear directorio
# os.makedirs("MyFirstDirectory")  # Crear directorio
# os.removedirs("MyFirstDirectory")  # Remover directorio


# directoriesList = os.listdir("../") #muestra todas las carpetas de ruta mayor
# directoriesList = os.listdir("../..")  # muestra solo la carpeta dentro de la ruta
directoriesList = os.listdir(".")  # muestra solo la carpeta dentro de la ruta
# print(directoriesList)


# Ruta absoluta: ruta  imperativa, se coloca toda la secuencia de carpetas, estas no pueden modificarse
# Ruta relativa: depende de donde estoy posicionada


# copiar un file
# IMPORTANTE: para esto primero debe de estar creada la carpeta destino (Ejm: MiFirstDirectory)
fileOrigin = "main.py"
destineDirectory = f"{currentDirectory}\MyFirstDirectory"
shutil.copy(fileOrigin, destineDirectory)
print(directoriesList)

# lectura de archivos
try:
    file = open("data.txt", "r")  # modo r, read
    print(file.read())
except Exception as ex:
    print(ex)

# lectura de archivos with readlines():
try:
    file = open("data.txt", "r")
    for line in file.readlines():
        # if(line == "Mari"):
        #     print("Este es un Alterejo")
        print(line)
except Exception as ex:
    print(ex)

    # sobreescritura de archivos
    file = open("names.txt", "w")
    file.write("Mari 2")
except Exception as ex:
    print(ex)

# agregando texto sin sobreescritura
try:
    file = open("names.txt", "a")  # modo a: add
    file.write("Mari R")
    file.write("\n")
except Exception as ex:
    print(ex)

# verificando texto sin sobreescritura
try:
    file = open("names.txt", "r")  # modo r: read
    print(file.read())
except Exception as ex:
    print(ex)


#
class Person:
    def __init__(self, name, lastname, age, sex):
        self.name = name


class File:
    def __init__(self, filename):
        self.filename = filename

    def showFile(self):
        try:
            file = open(self.filename, "r")
            for line in file.readlines():
                print(line)
        except Exception as ex:
            print(ex)
        else:
            file.close()

    def addPerson(self, person):
        try:
            file = open(self.filename, "a")
            addText = f"{person.name}, {person.lastname}, {person.age}, {person.sex}"
            file.write(addText)
        except Exception as ex:
            print(ex)
        else:
            file.close()
            print(file)


person = Person("Mari", "Rod", 25, "Female")
file = file("myself.txt")
file.addPerson(person)
file.showFile()
