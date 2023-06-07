import json
import utils
import time


class Person:
    def __init__(
        self,
        name,
        lastname,
        age,
        idCard,
    ):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.idCard = idCard


class Student(Person):
    def __init__(
        self,
        name,
        lastname,
        age,
        idCard,
        gradeMax,
        gradeMin,
        gradesAverage,
        role="student",
    ):
        super().__init__(name, lastname, age, idCard)
        self.role = role
        self.gradeMax = gradeMax
        self.gradeMin = gradeMin
        self.gradesAverage = gradesAverage

    def toStudentDictionary(self):
        studentDictionary = {
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "idCard": self.idCard,
            "gradeMax": self.gradeMax,
            "gradeMin": self.gradeMin,
            "gradesAverage": self.gradesAverage,
            "role": self.role,
        }
        return studentDictionary

    def toSingleStudentDictionary(self):
        studentDictionary = {
            "student": self.name + " " + self.lastname,
            "gradeMax": self.gradeMax,
            "gradeMin": self.gradeMin,
            "gradesAverage": self.gradesAverage,
        }
        return studentDictionary


class Teacher(Person):
    def __init__(self, name, lastname, age, idCard, role="teacher"):
        super().__init__(name, lastname, age, idCard)
        self.role = role

    def toTeacherDictionary(self):
        teacherDictionary = {
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "idCard": self.idCard,
            "role": self.role,
        }
        return teacherDictionary

    def toSingleTeacherDictionary(self):
        teacherDictionary = {
            "teacher": self.name + " " + self.lastname,
            "age": self.age,
            "idCard": self.idCard,
        }
        return teacherDictionary


def saveData(list, data, file):
    list.append(data)
    jsonString = json.dumps(list)
    file.removeFile()  # to no recreate lines
    file.writeFile(jsonString)


optionsMenuMain = {"- Estudiantes": "1", "- Docentes": "2", "- Salir": "0"}
menuMain = utils.Menu("principal", optionsMenuMain)

studentDictList = []
studentList = []
singleStudentDict = []
teacherDictList = []
teacherList = []
singleTeacherDict = []

studentFile = utils.FileManager("student.txt")
teacherFile = utils.FileManager("teacher.txt")


def initialCharge():
    resp1 = studentFile.readFile()
    resp2 = teacherFile.readFile()
    if resp1 != "":
        temporaryStudentList = json.loads(resp1)
        for dict in temporaryStudentList:
            newStudent = Student(
                dict["name"],
                dict["lastname"],
                dict["age"],
                dict["idCard"],
                dict["gradeMax"],
                dict["gradeMin"],
                dict["gradesAverage"],
            )
            studentDictList.append(newStudent.toStudentDictionary())
            studentList.append(newStudent)
    if resp2 != "":
        temporaryTeacherList = json.loads(resp2)
        for dict in temporaryTeacherList:
            newTeacher = Teacher(
                dict["name"],
                dict["lastname"],
                dict["age"],
                dict["idCard"],
            )
            teacherDictList.append(newTeacher.toTeacherDictionary())
            teacherList.append(newTeacher)


initialCharge()

openMenu = True
while openMenu:
    resp1 = menuMain.showMenu()
    if resp1 == "1":
        print(("Ingresa datos del estudiante").strip().upper())
        name = input("Nombre: ").strip().lower()
        lastname = input("Apellido: ").strip().lower()
        age = input("Edad: ")
        idCard = input("Número de DNI: ")
        print("")

        print("Ingresa notas del estudiante")
        gradesList = []
        for i in range(1, 5):
            grade = int(input(f"{i}° Nota: "))
            gradesList.append(grade)
            gradesSorted = sorted(gradesList)
            gradeMax = str(gradesSorted[-1])
            gradeMin = str(gradesSorted[0])
            gradesAverage = str(sum(gradesSorted) / len(gradesSorted))

        confirm = True
        while confirm:
            print("")
            print(
                f"¿Esta seguro de agregar datos del estudiante {(name).upper()} {lastname.upper()}? (si/no)"
            )
            resp2 = input(utils.Color.YELLOW + "Respuesta: " + utils.Color.END)
            if resp2.strip().lower() == "si":
                studentN = Student(
                    name,
                    lastname,
                    age,
                    idCard,
                    gradeMax,
                    gradeMin,
                    gradesAverage,
                )
                studentList.append(studentN)
                saveData(studentDictList, studentN.toStudentDictionary(), studentFile)
                singleStudentFile = utils.FileManager(f"S_{idCard}.txt")
                saveData(
                    singleStudentDict,
                    studentN.toSingleStudentDictionary(),
                    singleStudentFile,
                )
                singleStudentDict = []

                print(utils.Color.GREEN + f"✅ Registro exitoso." + utils.Color.END)
                time.sleep(1)
                break
            elif resp2.strip().lower() == "no":
                break
            else:
                print(utils.Color.RED + "❌Ingresa una opción valida." + utils.Color.END)

    elif resp1 == "2":
        print(("Ingresa datos del docente").strip().upper())
        name = input("Nombre: ").strip().lower()
        lastname = input("Apellido: ").strip().lower()
        age = input("Edad: ")
        idCard = input("Número de DNI: ")
        print("")

        confirm = True
        while confirm:
            print(
                f"¿Esta seguro de agregar datos del docente {name.upper()} {lastname.upper()}? (si/no)"
            )
            resp2 = input(utils.Color.YELLOW + "Respuesta: " + utils.Color.END)
            if resp2.strip().lower() == "si":
                teacherN = Teacher(
                    name,
                    lastname,
                    age,
                    idCard,
                )
                teacherList.append(teacherN)
                saveData(teacherDictList, teacherN.toTeacherDictionary(), teacherFile)
                singleTeacherFile = utils.FileManager(f"T_{idCard}.txt")
                saveData(
                    singleTeacherDict,
                    teacherN.toSingleTeacherDictionary(),
                    singleTeacherFile,
                )
                singleTeacherDict = []

                print(utils.Color.GREEN + f"✅ Registro exitoso." + utils.Color.END)
                time.sleep(1)
                break
            elif resp2.strip().lower() == "no":
                break
            else:
                print(utils.Color.RED + "❌Ingresa una opción valida." + utils.Color.END)
    elif resp1 == "0":
        openMenu = False
