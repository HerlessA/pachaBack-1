import os
import time


class Menu:
    def __init__(self, menuName, optionsList):
        self.menuName = menuName
        self.optionsList = optionsList

    def showMenu(self):
        a = True
        while a:
            self.clearMenu()

            print(
                Color.PURPLE
                + "--- "
                + "MENÚ "
                + self.menuName.upper()
                + " ---"
                + Color.END
            )
            print("")
            print("OPCIONES")
            print("")
            for key, value in self.optionsList.items():
                print(key + Color.GREEN + " → " + Color.END + value)
            print("")

            resp = input(Color.YELLOW + "Por favor ingresa una opción: " + Color.END)
            print("")

            if resp == "0":
                print(Color.YELLOW + "Saliendo... OK.")
                time.sleep(2)
                break

            b = 0
            for key, value in self.optionsList.items():
                if value == resp:
                    b += 1
            if b > 0:
                a = False
            else:
                print(Color.RED + "❌ Ingresa una opción válida" + Color.END)
                time.sleep(2)

        return resp

    def clearMenu(self):
        def clear():
            return os.system("clear")

        clear()


class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
