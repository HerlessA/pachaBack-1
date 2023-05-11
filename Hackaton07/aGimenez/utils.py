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
            print(color.RED+"---------------"+"ESTE ES EL MENU " +
                  self.name.upper()+"---------------"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(key + color.PURPLE + " → " + color.END + value)
            print("")
            ans = input(
                color.DARKCYAN + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                print(color.GREEN + "Vuelvas prontos!" + color.END)
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.YELLOW + "Opción no valida, escoja una opción valida" + color.END)
                time.sleep(1)
        return ans

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()