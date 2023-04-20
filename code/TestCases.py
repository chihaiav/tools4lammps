from typing import List
from classes.LammpsInputFile import LammpsInputFile
from modules.periodic import Periodic
from modules.geometry import Geometry
from config.global_setting import *
from modules.lists import Lists
from modules.kinetics import Kinetics

def divide_cells(lammps_input):
    with open('TEST_Divide_cells.out', 'w') as fil:
        # first_atoms = atom_list[:10]
        # region =  {
        # "xlo xhi" : (-10, 3),
        # "ylo yhi": (-10, 3),
        # "zlo zhi": (-10, 3)
        # }
        # box =  {
        # "xlo xhi" : (-18, 4),
        # "ylo yhi": (-15, 6),
        # "zlo zhi": (-15, 7)
        # }
        # nx = 2
        # ny = 5
        # nz = 4

        atoms = Lists.divide_cells(l.get_atoms(), l.box, l.box)
        # for a in first_atoms:
        #     s = str(a.id) + " " + str(a.x) + " " + str(a.y) + " " + str(a.z) + " "
        #     fil.write( s + " " + "\n")

        sum = 0
        for key in atoms:
            write_string = str(key) + " -> "
            for v in atoms[key]:
                write_string = write_string + str(v.id) + " "
            fil.write(write_string + "\n")
            sum += len(atoms[key])
        fil.write("Total # of Atoms = " + str(sum) + "\n")
        return atoms

if __name__ == "__main__":

    l = LammpsInputFile("in/333_LA2.DATA")
    atom_list = l.get_atoms()
    OTHER_DEFAULTS.box = l.box
    
    # Testing divide_cells
    atoms_indexed = divide_cells(l)
    #print(atoms_indexed)
    Lists.get_hilbert_curve_crossing(l)
  
    #   Checked periodic functions from Periodic
    # Periodic.pbc(atom_list)
    # atom_list[1].x, atom_list[1].y, atom_list[1].z = Periodic.minimg(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # atom_list[1].x, atom_list[1].y, atom_list[1].z = Periodic.get_image_index(atom_list[1].true)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z)

    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z, atom_list[1].true)
    # atom_list[1].true= Periodic.get_itrue(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z, atom_list[1].true)
 
    # print(OTHER_DEFAULTS.xprd)
    # Periodic.set_prd()
    # print(OTHER_DEFAULTS.xprd)

    # #Checked translate function from velocity
    # Geometry.translate(atom_list, (1, 2, 3))
    # l.write_to_file("TEST_translate_velocity.out")

    # # Check find_molecules function
    # with open('TEST_original_molecule.out', 'w') as the_file2:
    #     for a in atom_list:
    #         the_file2.write(str(a.molecule_tag) + "\n")
    # # Test for find molecules
    # Geometry.find_molecules(atom_list, l.get_bonds())
    # with open('TEST_modified_molecule.out', 'w') as the_file2:
    #     for a in atom_list:
    #         the_file2.write(str(a.id) + " " + str(a.molecule_tag) + "\n")

    # with open('TEST_bonds.out', 'w') as the_file2:
    #     for b in l.get_bonds():
    #         the_file2.write(str(b.get_atoms_id()) + "\n")

    # #Test for displace_atoms
   
    # with open('TEST_displace_atoms.out', 'w') as the_file2:
    #     Geometry.displace_atoms(atom_list, 2)
    #     for a in atom_list:
    #         v = a.get_velocities()
    #         s = str(a.x) + " " + str(a.y) + " " + str(a.x) + " "
    #         vv = str(v[0]) + " " +  str(v[1]) + " " +  str(v[2])
    #         the_file2.write( s + vv + "\n")

    # #Test for atoms within sphere function

    # with open('TEST_atom_within_sphere.out', 'w') as the_file2:
    #     first_atoms = atom_list[:10]
    #     result_list = []
    #     Geometry.get_atoms_within_sphere(first_atoms, (-9, -7, -9), 5, result_list)
    #     for a in first_atoms:
    #         s = str(a.x) + " " + str(a.y) + " " + str(a.z) + " "
    #         the_file2.write( s + " " + "\n")
   
    #     the_file2.write( "\n\n\n")
    #     for a in result_list:
    #         s = str(a.x) + " " + str(a.y) + " " + str(a.z) + " "
    #         the_file2.write( s + " " + "\n")



# Check calc_mc_pos function from kinetics module
    # print('\nTest calc_mc_pos')
    # first_atoms = atom_list[:10]
    # point_res = []
    # Kinetics.calc_mc_pos(first_atoms, l, point_res)
  

    # # Check calc_mc_pos2
    # print('\nTest calc_mc_pos2')
    # xyz=[(1, 1, 2), (2, 3, 4), (1, 1.5, 1.3)]
    # masses = [2, 3, 3.5]
    # point_res2 = []
    # Kinetics.calc_mc_pos2(3, xyz, masses, point_res2)

    # # Check calc_lin_mom
    # print('\nTest calc_lin_mom')
    # first_atoms = atom_list[:10]
    # (px, py, pz) = Kinetics.calc_lin_mom(first_atoms, l)
    
    # # Check calc_mc_vel
    # print('\nTest calc_mc_vel')
    # first_atoms = atom_list[:10]
    # (vxcm, vycm, vzcm) = Kinetics.calc_mc_vel(first_atoms, l)
    
    # print('\nTest calc_ang_mom')
    # first_atoms = atom_list[:10]
    # angm = Kinetics.calc_ang_mom(first_atoms, l, [1, 1, 1])

    # print('\n Test calc_inertia_mom')
    # first_atoms = atom_list[:10]
    # inm = Kinetics.calc_inertia_mom(first_atoms, l, [1,1, 1])

    # print('\n Test calc_temperature')
    # first_atoms = atom_list[:10]
    # temp = Kinetics.calc_temperature(first_atoms, l,1)

    # print('\n Test temp_rescale')
    # first_atoms = atom_list[:10]
    # temp = Kinetics.temp_rescale(first_atoms, l, 20, 3)

    print('\n Test calc_tvr_temperature')
    first_atoms = atom_list[:10]
    vv=[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3], ]
    vt=[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3], ]
    vr=[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3], ]
    

    temp = Kinetics.calc_tvr_temperature(first_atoms, l, 20, vt, vv, vr)

