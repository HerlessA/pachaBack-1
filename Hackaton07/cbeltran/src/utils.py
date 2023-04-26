import os
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("")
            print(color.CYAN+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                    self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(color.YELLOW + key + color.END + color.RED + " → " + color.END + color.GREEN + value + color.END)
            print("")
            ans = input(
                color.GREEN + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                self.limpiarPantalla()
                print("Hasta Pronto")
                
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED + "Opción no valida, escoja una opción valida" + color.END)
                time.sleep(2)
        return ans

    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()