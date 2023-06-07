import os.path


class fileManager:
    def _init_(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo, "r")
            return file.read()
        except Exception as e:
            return e

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual + "\\" + self.nombreArchivo
        if os.path.isfile(path):
            try:
                os.remove(path)
                print("removiendo archivo")
            except Exception as error:
                print(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual + "\\" + self.nombreArchivo
            print(path)
            if os.path.isfile(path):
                try:
                    file = open(self.nombreArchivo, "a")
                    file.write(linea + "\n")
                except Exception as e:
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, "w")
                file.close()
                file = open(self.nombreArchivo, "a")
                file.write(linea + "\n")
        except Exception as error:
            print(error)
