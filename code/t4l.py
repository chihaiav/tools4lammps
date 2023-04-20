from switcher import Switcher
from global_setting import *
from LammpsInputFile import LammpsInputFile
from lists import Lists
from periodic import Periodic
from geometry import Geometry

ERROR = -1
SUCCES = 0

def show_menu():
    f = open("show_menu.in", "r")
    print(f.read())
   

def read_choice():

    sw = Switcher()

    input_script = input("Enter input script:")
    try:
        script_file = open(input_script)
        while True:
            command = script_file.readline().strip()

            if "EXIT" in command:
                print("Exiting...")
                break

            if command:
                output = sw.indirect(command)
                if output == ERROR:
                    print("Error found while applying operation from input script.Exiting...")
                    return

 
           

        script_file.close()
    except FileNotFoundError:
        print("Input file provided does not exist")
        return
    

if __name__ == "__main__":

    # show_menu()
    # read_choice()
    l = LammpsInputFile("333_LA2.DATA")
    # Lists.list_reorder_random(l)
    # l.write_to_file("test.out")

    atom_list = l.get_atoms()
    OTHER_DEFAULTS.box = l.box