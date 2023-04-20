from config.global_setting import OTHER_DEFAULTS
from classes.Atom import Atom
from math import sqrt

class Geometry:

    @staticmethod
    def translate(atom_list, disp):
        for atom in atom_list:
            x = atom.x + disp[0]
            y = atom.y + disp[1]
            z = atom.z + disp[2]
            # velocity = atom.get_velocities()
            # new_vel = tuple(item1 + item2 for item1, item2 in zip(velocity, disp))
            # atom.set_velocities(new_vel)
            atom.x = x;
            atom.y = y;
            atom.z = z;

        return atom_list

    @staticmethod
    def find_molecules(atom_list, bonds_list):
        nats = len(atom_list)
        mol = 0
        #assign molecule id 0 to all atoms
        for atom in atom_list:
            atom.molecule_tag = 0
        stack = []
        #dfs
        for atom in atom_list:
            if atom.molecule_tag == 0:
                mol = mol + 1
                atom.molecule_tag = mol
                # nstack =1
                stack.append(atom)
                while (len(stack) != 0):
                    atom_j = stack.pop()
                   
                    # nstack = nstack - 1
                    for bond in bonds_list:                     
                        atoms = bond.get_atoms_id()
                        if atom_j.id in atoms:
                            if atoms.index(atom_j.id) == 0:
                                atom_k_id = atoms[1]
                            else:
                                atom_k_id = atoms[0]
                            if atom_list[atom_k_id - 1].molecule_tag == 0:
                                atom_list[atom_k_id - 1].molecule_tag = mol
                                # nstack = nstack + 1
                                stack.append(atom_list[atom_k_id - 1])

        
        # return atom_list


    @staticmethod
    def displace_atoms(atom_list, ts):
        
        for atom in atom_list:
            atom.x = atom.x + atom.get_velocities()[0] * ts
            atom.y = atom.y + atom.get_velocities()[1] * ts
            atom.z = atom.z + atom.get_velocities()[2] * ts

    # return atom_list

    @staticmethod
    def get_atoms_within_sphere(atom_list, point, radius, result_atom_list):

        for atom in atom_list:
            dx = point[0] - atom.x
            dy = point[1] - atom.y
            dz = point[2] - atom.z
            d = sqrt(dx **2 + dy **2 + dz **2)
            if d < radius:
                result_atom_list.append(atom)



    # @staticmethod
    # def make_supercell(atom_list, cell_thick, idimension, npartic):
      
    #     nats = len(atom_list)
    #     if nats == 0:
    #         print("Empty atom list...Read data file first")
    #         return
        
    #     if cell_thick < 1:
    #         print("Invalid choice! [cell thick < 1]")
    #         return
    #     # Total number of cells
    #     ncell1d = cell_thick * 2 + 1
    #     ncells = ncell1d ** idimension

    #     # Skip timeshift options - no dump file handling for now

    #     npartic_new = npartic + nats * ncells


