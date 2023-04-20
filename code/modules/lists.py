import random
import numpy as np
import math
from hilbert import decode, encode
from config.global_setting import OTHER_DEFAULTS
from classes.LammpsInputFile import *

class Lists: 

    @staticmethod
    def list_reorder_random(lif_object):
        atoms_number = lif_object.get_header()["atoms"]
        l = np.arange(1, atoms_number+1, 1)
        random.shuffle(l)
        
        atoms_list = lif_object.get_atoms()

        for atom in atoms_list:
            atom.set_new_id(l[atoms_list.index(atom)])
        atoms_list.sort(key=lambda atom: atom.get_new_id())

    # take region as    
    # region =  {
    # "xlo xhi" : None,
    # "ylo yhi": None,
    # "zlo zhi": None
    # }
    @staticmethod
    def divide_cells(atom_list, region, box):
       
        atoms_indexed = None

        if (region["xlo xhi"][0] > region["xlo xhi"][1]) or (region["ylo yhi"][0] > region["ylo yhi"][1]) or (region["zlo zhi"][0] > region["zlo zhi"][1]):
            print("ERROR x|y|z hi must be greater than x|y|z lo")
            return atoms_indexed
        
        if (not all(box["xlo xhi"][0] <= a <= box["xlo xhi"][1] for a in [region["xlo xhi"][0],region["xlo xhi"][1]])) or( not all(box["ylo yhi"][0] <= a <= box["ylo yhi"][1] for a in [region["ylo yhi"][0],region["ylo yhi"][1]])) or (not all(box["zlo zhi"][0] <= a <= box["zlo zhi"][1] for a in [region["zlo zhi"][0],region["zlo zhi"][1]])):
            print("Region for x not in box")
            return atoms_indexed

        atoms_indexed = {}

        nx = math.ceil(abs(region["xlo xhi"][1] - region["xlo xhi"][0]))
        ny = math.ceil(abs(region["ylo yhi"][1] - region["ylo yhi"][0]))
        nz = math.ceil(abs(region["zlo zhi"][1] - region["zlo zhi"][0]))
        
        keys_list = []
        for atom in atom_list:
            dx = (atom.x - region["xlo xhi"][0]) / OTHER_DEFAULTS.r_cutoff
            dy = (atom.y - region["ylo yhi"][0]) / OTHER_DEFAULTS.r_cutoff
            dz = (atom.z - region["zlo zhi"][0]) / OTHER_DEFAULTS.r_cutoff

            if ((nx > dx >= 0) and (ny > dy >= 0) and (nz > dz >= 0)):
                # Cell position
                ix = int(dx)
                iy = int(dy)
                iz = int(dz)
                #ilist = iz + nz * iy + nz * ny * ix
                ilist = ix + nx * iy + nx * ny * iz
                keys_list.append(ilist)
                if ilist in atoms_indexed:
                    atoms_indexed[ilist].append(atom)
                else:
                    atoms_indexed[ilist] = [atom]
        
       
        # print(len(keys_list))
        # print(max(keys_list))
        return atoms_indexed

    @staticmethod
    def get_hilbert_curve_crossing(lammps_input):
        
        region = lammps_input.box
        nx = math.ceil(abs(region["xlo xhi"][1] - region["xlo xhi"][0]))
        ny = math.ceil(abs(region["ylo yhi"][1] - region["ylo yhi"][0]))
        nz = math.ceil(abs(region["zlo zhi"][1] - region["zlo zhi"][0]))

        num_cels = nx*ny*nz

        # print("nx = " + str(nx))
        # print("ny = " + str(ny))
        # print("nz = " + str(nz))
        print(num_cels)

        maximum_cells = max(nx, ny, nz)

        print(maximum_cells)

        bit_resolution = 0
        power_of_2 = 1
        while (power_of_2 < maximum_cells):
            power_of_2 = power_of_2 << 1
            bit_resolution += 1

        print(power_of_2)
        print(bit_resolution)
        cells = np.arange(0, num_cels, 1)
        print(cells)
        print(np.array(cells))
        hilbert_curve = decode(np.array(cells), 3, bit_resolution)
        print(hilbert_curve)

        crossing_order = [e[0] + nx * e[1] + nx * ny * e[2] for e in hilbert_curve]

        # print(crossing_order)
        print(len(crossing_order))
        print(max(crossing_order))  
        
            