import re
import datetime
import sys

from .Angle import Angle
from .Bond import Bond
from .Atom import Atom

class LammpsInputFile():

    STYPES = ["Masses", "Nonbond Coeffs", "Bond Coeffs", "Angle Coeffs", "Dihedral Coeffs",
              "Improper Coeffs", "BondBond Coeffs", "BondAngle Coeffs", "MiddleBondTorsion Coeffs",
              "EndBondTorsion Coeffs", "AngleTorsion Coeffs", "AngleAngleTorsion Coeffs", "BondBond13 Coeffs",
              "AngleAngle Coeffs", "Atoms", "Velocities", "Bonds", "Angles", "Dihedrals", "Impropers"]
   
    def __init__(self, input_fname = ""):
        self.header = { "atoms" : 0,
                        "bonds" : 0,
                        "angles" : 0,
                        "dihedrals" : 0,
                        "impropers" : 0,
                        "atom types" : 0,
                        "bond types" : 0,
                        "angle types" : 0,
                        "dihedral types" : 0,
                        "improper types" : 0,
                      }
        self.box =  {   "xlo xhi" : None,
                        "ylo yhi": None,
                        "zlo zhi": None
                    }

        self.header_keys = self.header.keys()
        self.input_fname = input_fname
        self.output_fname = input_fname.strip() + ".out"
        self.input_file = None
        self.lines = []
        self.current_index = -1

        """!!!Order is important
              TODO - incomplete list
        """
        self.entries = {
            "Masses"    : [],
            "Atoms"     : [],
            #"Velocities": [],
            "Bonds"     : [],
            "Angles"    : []
        }

        """parse the file"""
        self.read_file()

    def get_header(self):
        return self.header

    def get_atoms(self):
        return self.entries["Atoms"]

    def set_atoms(self, l = []):
        self.entries["Atoms"] = l

    def get_masses(self):
        return self.entries["Masses"]

    def set_masses(self, l = []):
        self.entries["Masses"] = l

    def get_velocities(self):
        return self.entries["Velocities"]

    def set_velocities(self, l = []):
        self.entries["Velocities"] = l

    def get_bonds(self):
        return self.entries["Bonds"]

    def set_bonds(self, l = []):
        self.entries["Bonds"] = l

    def get_angles(self):
        return self.entries["Angles"]

    def set_angles(self, l = []):
        self.entries["Angles"] = l

    def parse_nonbond_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_bond_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_angle_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_dihedral_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_improper_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_bondbond_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_bondangle_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_middlebondtorsion_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_endbondtorsion_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_angletorsion_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_angleangletorsion_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_bondbond13_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_angleangle_coeffs(self):
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_dihedrals(self):
        print("Parsing Dihedrals starting at line #{}".format(self.current_index))
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_impropers(self):
        print("Parsing Impropers starting at line #{}".format(self.current_index))
        self.current_index = len(self.lines)
        print("Not implemented!")
        pass

    def parse_masses(self):
        N = self.header["atom types"]
        print("Parsing {} Masses starting at line #{}".format(N, self.current_index))

        start = self.current_index + 1
        end = start + N
        for l in self.lines[start:end]:
            tokens = l.split()
            #self.entries["Masses"][int(tokens[0])] = float(tokens[1])
            self.entries["Masses"].append((int(tokens[0]), float(tokens[1])))

        self.current_index = end

    def parse_atoms(self):
        N = self.header["atoms"]
        print("Parsing {} Atoms starting at line #{}".format(N, self.current_index))

        start = self.current_index + 1
        end = start + N
        for l in self.lines[start:end]:
            items = l.split()
            if len(items) >= 7:
                idx = int(items[0])
                tag = int(items[1])
                type = int(items[2])
                q = float(items[3])
                x = float(items[4])
                y = float(items[5])
                z = float(items[6])
            # else:
            #     idx = int(items[0])
            #     tag = 1
            #     type = int(items[1])
            #     q = float(items[2])
            #     x = float(items[3])
            #     y = float(items[4])
            #     z = float(items[5])
            # """it means we also have nx ny nz"""
            if len(items) == 10:
                nx = float(items[7])
                ny = float(items[8])
                nz = float(items[9])
                # atom = (idx, tag, type, q, x, y, z, nx, ny, nz)
                atom = Atom(idx, tag, type, q, x, y, z, nx, ny, nz)
            else:
                # atom = (idx, tag, type, q, x, y, z, 0, 0, 0)
                atom = Atom(idx, tag, type, q, x, y, z, 0, 0, 0)
            self.entries["Atoms"].append(atom)

        self.current_index = end

    # Added velocity as atom property
    def parse_velocities(self):
        N = self.header["atoms"]
        print("Parsing {} Velocities starting at line #{}".format(N, self.current_index))
        start = self.current_index + 1
        end = start + N
        for l in self.lines[start:end]:
            items = l.split()
            idx = int(items[0])
            vx = float(items[1])
            vy = float(items[2])
            vz = float(items[3])
            # vel = (idx, vx, vy, vz)
            # self.entries["Velocities"].append(vel)
            self.entries["Atoms"][idx - 1].set_velocities((vx, vy, vz))
        self.current_index = end

    def parse_bonds(self):
        N = self.header["bonds"]
        print("Parsing {} Bonds starting at line #{}".format(N, self.current_index))
        start = self.current_index + 1
        end = start + N
        for l in self.lines[start:end]:
            items = l.split()
            idx = int(items[0])
            bond_type = int(items[1])
            atom1 = int(items[2])
            atom2 = int(items[3])
            # bond = (idx, bond_type, atom1, atom2)
            # self.entries["Bonds"].append(bond)
            bond = Bond(idx, bond_type, atom1, atom2)
            self.entries["Bonds"].append(bond)
            
        self.current_index = end

    def parse_angles(self):
        N = self.header["angles"]
        print("Parsing {} Angles starting at line #{}".format(N, self.current_index))
        start = self.current_index + 1
        end = start + N
        for l in self.lines[start:end]:
            items = l.split()
            idx = int(items[0])
            angle_type = int(items[1])
            atom1 = int(items[2])
            atom2 = int(items[3])
            atom3 = int(items[4])
            # angle = (idx, angle_type, atom1, atom2, atom3)
            # self.entries["Angles"].append(angle)
            angle = Angle(int(items[0]), int(items[1]), int(items[2]), int(items[3]), int(items[4]))
            self.entries["Angles"].append(angle)

        self.current_index = end

    def parse_header(self):
        for i in range(len(self.lines)):
            sline = self.lines[i].strip()
            goto_next_line = False

            """empty line"""
            if sline == "":
                continue
            """comment"""
            if sline.startswith("#"):
                continue

            for key in self.header_keys:
                if sline.endswith(key):
                    token = sline.strip("\t {}".format(key))
                    self.header[key] = int(token)
                    goto_next_line = True
                    break

            if goto_next_line:
                continue

            if sline.endswith("xlo xhi"):
                tokens = sline.strip(" xlo xhi").split(" ")
                tokens = [i for i in tokens if i != ""]
                self.box["xlo xhi"] = (float(tokens[0]), float(tokens[1]))
            elif sline.endswith("ylo yhi"):
                tokens = sline.strip(" ylo yhi").split(" ")
                tokens = [i for i in tokens if i != ""]
                self.box["ylo yhi"] = (float(tokens[0]), float(tokens[1]))
            elif sline.endswith("zlo zhi"):
                tokens = sline.strip(" zlo zhi").split(" ")
                tokens = [i for i in tokens if i != ""]
                self.box["zlo zhi"] = (float(tokens[0]), float(tokens[1]))
            else:
                """It means we got out of header"""
                self.current_index = i
                return

    """Returns the line index for the last data point for this type of coeff
        or -1 if type is unknown. If -1 is returned, ignore until next found type"""
    def decide_what_comes_next(self):
        if self.current_index >= len(self.lines):
            return

        coeff_type = self.lines[self.current_index].split("#")[0].strip()
        if coeff_type not in LammpsInputFile.STYPES:
            print ("Something is wrong in the input file. Unknown type: {}".format(coeff_type))
            return

        method_name = "parse_" + coeff_type.lower().replace(" ", "_")
        method_to_call = getattr(self, method_name)
        method_to_call()
        self.decide_what_comes_next()

    def read_file(self):
        self.input_file = open(self.input_fname)
        """first two lines are ignored"""
        self.lines = self.input_file.readlines()[2:]
        self.lines = [re.sub(' +', ' ', i.strip()) for i in self.lines if i.strip() != ""]
        """parse the header"""
        self.parse_header()

        """See what is coming next in file"""
        self.decide_what_comes_next()

        print("Reading file: Done")


    # def dict_to_list(self, dict):
    #     l = []
    #     for key, value in dict.items():
    #         l.append((int(key), float(value)))
    #     return l

    # def class_dict_to_list(self, dict):
    #     l = []
    #     for key, value in dict.items():
    #         l.append((key, value))
    #     return l

    def write_to_file(self, output_file_name):
        if output_file_name is None:
            output_file = open(self.output_fname, "w+")
        else:
            output_file = open(output_file_name, "w+")
        
        out_string = ""
        """First two lines are ignored"""
        #output_file.write("LAMMPS Description ({})\n\n".format(datetime.datetime.now()))
        out_string += "LAMMPS Description ({})\n\n".format(datetime.datetime.now())
        empty_line = True

        for k in self.header:
            if k.endswith("types") and empty_line:
                #output_file.write("\n")
                out_string += "\n"
                empty_line = False

            if self.header[k] != 0:
                #output_file.write("{} {}\n".format(self.header[k], k))
                out_string += "{} {}\n".format(self.header[k], k)

        """Simulation box"""
        #output_file.write("\n")
        out_string += "\n"
        for k in self.box:
            #output_file.write("{} {} {}\n".format(self.box[k][0], self.box[k][0], k))
            out_string += "{} {} {}\n".format(self.box[k][0], self.box[k][0], k)
        #output_file.write("\n")
        out_string += "\n"
        output_file.write(out_string)

        for entry in self.entries:
            elist = self.entries[entry]
        
            if elist:
                # output_file.write("{}\n\n".format(entry))
                if entry == "Masses":
                    masses_string = "{}\n\n".format(entry)
                    for item in elist:
                        masses_string += " {}\t{:.12f}\n".format(item[0], item[1]).expandtabs()
                    output_file.write(masses_string + "\n")
                
                elif entry == "Atoms":
                    atoms_string = "{}\n\n".format(entry)
                    velocities_string = "{}\n\n".format("Velocities")
                    for item in elist:
                        atoms_string += item.print_atom()
                        velocities_string += item.print_velocity()
                    output_file.write(atoms_string + "\n")
                    output_file.write(velocities_string + "\n")
                elif entry == "Bonds":
                    bonds_string = "{}\n\n".format(entry)
                    for item in elist:
                        bonds_string += item.print_bond()
                    output_file.write(bonds_string + "\n")
                elif entry == "Angles":
                    angles_string = "{}\n\n".format(entry)
                    for item in elist:
                        angles_string += item.print_angle()
                    output_file.write(angles_string + "\n")

        output_file.close()

    def __del__(self):
        self.input_file.close()
        print("All cleared!")

    def __str__(self):
        res = "Header: " + str(self.header) + "\n"
        res += "Box: " + str(self.box) + "\n"
        if self.entries["Masses"]:
            res += "Masses: " + str(self.entries["Masses"]) + "\n"
        if self.entries["Atoms"]:
            res += "Atoms: [" + str(self.entries["Atoms"][0]) + "\n\t\t. . .\n\t" + str(self.entries["Atoms"][-1]) + "]\n"
        if self.entries["Velocities"]:
            res += "Velocities: [" + str(self.entries["Velocities"][0]) + "\n\t\t. . .\n\t" + str(self.entries["Velocities"][-1]) + "]\n"
        if self.entries["Bonds"]:
            res += "Bonds: [" + str(self.entries["Bonds"][0]) + "\n\t\t. . .\n\t" + str(self.entries["Bonds"][-1]) + "]\n"
        if self.entries["Angles"]:
            res += "Angles: [" + str(self.entries["Angles"][0]) + "\n\t\t. . .\n\t" + str(self.entries["Angles"][-1]) + "]\n"
        return res

