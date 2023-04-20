from config.global_setting import *
import random
from classes.LammpsInputFile import *
from .periodic import Periodic
from .memory_management import Memory_handler


ERROR = -1
SUCCES = 0

class Switcher:

    inputfile_handler = None

    def indirect(self, index):

        command = index.split()
        method_name = 'func_'+ str(command[0])
        method = getattr(self, method_name, lambda :'Invalid')

        return method(command)


    def func_GLOBAL_VAR(self, command):
        

        #Global_var seed iseed[integer] {reinit|other}
        if command[1] == "SEED" :
            if command[2].isnumeric():
                OTHER_DEFAULTS.iseed = int(command[2])
            else:
                print("Bad syntax in command : ")
                print(command)
            
            if command[3] == "REINIT":
                # TODO : 
                pass
            else:
                print("Bad syntax in command : ")
                print(command)

        #Global_var unit_style  <lj/real/metal/si/cgs/electron/micro/nano>           
        if command[1] == "UNIT_STYLE":
            unit_style = command[2]
            if unit_style in ['LJ', 'REAL', 'METAL', 'SI', 'CGS', 'ELECTRON', 'MICRO', 'NANO']:
                OTHER_DEFAULTS.unit_style = unit_style.upper()
                CONSTANTS.unit_style = unit_style.upper()
            else:
                print("INVALID UNIT STYLE in command:")
                print(command)
                return ERROR
            
           
        #Global_var atom_style  integer (2 or 5)
        #1=angle 2=atomic     3=body  4=bond    5=charge    6=dipole 7=electron 8=ellipsoid 9=full 10=line 
        # 11=meso 12=molecular 13=peri 14=sphere 15=template 16=tri   17=wavepacket" 

        if command[1] == "ATOM_STYLE":
            atom_style = command[2]
            if (int(atom_style) < 1) or (int(atom_style) > 17):
                print("Invalid choice")
                return ERROR
            if (int(atom_style) != 2) and (int(atom_style) != 5):
                print("Currently not implemented:")
                print(command)
            OTHER_DEFAULTS.atomstyle = int(atom_style)

        if command[1] == "NMOLECULAR":
            nmolecular = command[2]
            if (int(nmolecular) != 0) and (int(nmolecular) != 1):
                    print("NMOLECULAR should be 0 or 1:")
                    print(command)
            else:
                OTHER_DEFAULTS.nmolecular = nmolecular


        #Global_var XBox  xlo xhi (real, xlo<xhi)   ! case (21)
        if command[1] == "XBOX":
            
            if len(command) != 4:
                print("Invalid choice of xdimensions in command")
                print(command)
                return ERROR
            xlo = float(command[2])
            xhi = float(command[3])

            if xlo > xhi:
                print("Xhi must be greater than xlo")
                print(command)
            else:           
                OTHER_DEFAULTS.box["xlo xhi"] = (xlo, xhi)
                Periodic.set_prd()


        if command[1] == "YBOX":
            if len(command) != 4:
                print("Invalid choice of xdimensions in command")
                print(command)
                return ERROR
            ylo = float(command[2])
            yhi = float(command[3])

            if ylo > yhi:
                print("Xhi must be greater than xlo")
                print(command)
            else:           
                OTHER_DEFAULTS.box["ylo yhi"] = (ylo, yhi)
                Periodic.set_prd()
        
        if command[1] == "ZBOX":
            if len(command) != 4:
                print("Invalid choice of xdimensions in command")
                print(command)
                return ERROR
            zlo = float(command[2])
            zhi = float(command[3])

            if zlo > zhi:
                print("Xhi must be greater than xlo")
                print(command)
            else:           
             
                OTHER_DEFAULTS.box["zlo zhi"] = (zlo, zhi)
                Periodic.set_prd()

        return SUCCES


    def func_READ(self, command):

        if command[1] == "DATA_FILE":
            if len(command) < 3:
                print("No data file provided")
                return ERROR
            filename = command[2]
            try:
                input_file = open(filename)
                # Already read a data file?
                if (len(command) == 4) and (command[3] == "DELETE"):
                    if OTHER_DEFAULTS.isalloc:
                        # TODO - delete previous saved list of atoms?
                        # call free_atom_memory()
                        Memory_handler.free_atom_memory()
                        self.inputfile_handler = None
                        OTHER_DEFAULTS.isalloc = False
                self.inputfile_handler = LammpsInputFile(filename)
                self.inputfile_handler.read_file()
                OTHER_DEFAULTS.isalloc = True
                # Update box dimensions with the one read from file
                OTHER_DEFAULTS.box = self.inputfile_handler.box
                Periodic.set_prd()
                
                input_file.close()

            except FileNotFoundError:
                print("Input file provided does not exist")
                return ERROR
        
        else:
            # Other types currently not implemented
            pass
        return SUCCES
    
    def func_WRITE(self, command):
        if command[1] == "DATA_FILE":
            if len(command) < 3:
                print("No data file provided")
                return ERROR
            filename = command[2]
            self.inputfile_handler.write_to_file(filename)
        else:
            # Other types currently not implemented
            pass
        return SUCCES
