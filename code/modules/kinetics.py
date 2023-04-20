from config.global_setting import *
from config.global_setting import *
from classes.Atom import Atom
from classes.LammpsInputFile import *
from math import sqrt

class Kinetics:

    # HELPER function
    #  method used to set up default values depending on the unit style 
    @staticmethod
    def determine_default_unit_values(unit_style):

        if OTHER_DEFAULTS.unit_style == 'REAL':
           return UNITS_REAL()
        elif OTHER_DEFAULTS.unit_style == 'LJ':
            return UNITS_LJ()
        elif OTHER_DEFAULTS.unit_style == 'METAL':
           return UNITS_METAL()
        elif OTHER_DEFAULTS.unit_style == 'SI':
            return UNITS_SI()
        elif OTHER_DEFAULTS.unit_style == 'CGS':
            return UNITS_CGS()
        elif OTHER_DEFAULTS.unit_style == 'ELECTRON':
            return UNITS_ELECTRON()
        elif OTHER_DEFAULTS.unit_style == 'MICRO':
            return UNITS_MICRO()
        elif OTHER_DEFAULTS.unit_style == 'NANO':
            return UNITS_NANO()

    @staticmethod
    def calc_mc_pos(atom_list, lif_object, point):
        masses = lif_object.get_masses()
        xcm = 0
        ycm = 0
        zcm = 0
        wgrp = 0
        if len(atom_list) == 0:
            return
        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            xcm = xcm + wi * atom.x
            ycm = ycm + wi * atom.y
            zcm = zcm + wi * atom.z
            wgrp = wgrp + wi

        if (wgrp == 0):
            print('Wrgp is zero, division by zero not possible')
            return
        point.append(xcm / wgrp)
        point.append(ycm / wgrp)
        point.append(zcm / wgrp)

        print("Mass center of the list is : " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]))

    # Mass center for given set of coordinates
    @staticmethod
    def calc_mc_pos2(np, xyz, masses, point):
        xcm = 0
        ycm = 0
        zcm = 0
        wgrp = 0
        if(np == 0):
            return
        for i in range(0, np):
            wi = masses[i]
            xcm = xcm + wi * xyz[i][0]
            ycm = ycm + wi * xyz[i][1]
            zcm = zcm + wi * xyz[i][2]
            wgrp = wgrp + wi
            if (wgrp == 0):
                print('Wrgp is zero, division by zero not possible')
                return
        point.append(xcm / wgrp)
        point.append(ycm / wgrp)
        point.append(zcm / wgrp)

        print("Mass center is: " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]))

        
    # Calculate linear momentum of a set of aprticles
    @staticmethod
    def calc_lin_mom(atom_list, lif_object):

        px = 0
        py = 0
        pz = 0

        if len(atom_list) == 0:
            return

        masses = lif_object.get_masses()

        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            px = px + wi * atom.get_velocities()[0]
            py = py + wi * atom.get_velocities()[1]
            pz = pz + wi * atom.get_velocities()[2]

        print(" Px, Py, Pz are: " + str(px) + " " + str(py) + " " + str(pz))
        return (px, py, pz)

    @staticmethod
    def calc_mc_vel(atom_list, lif_object):

        if len(atom_list) == 0:
            return

        masses = lif_object.get_masses()
        wgrp = 0
        for atom in atom_list:
            wgrp = wgrp + [item for item in masses if item[0] == atom.atom_type][0][1]

        if wgrp <= (1e-10):
            return

        (px, py, pz) = Kinetics.calc_lin_mom(atom_list, lif_object)

        vxcm = px / wgrp
        vycm = py / wgrp	
        vzcm = pz / wgrp

        print("Vxcm, Vyxm, Vzcm are: " + str(vxcm) + " " + str(vycm) + " " + str(vzcm))
        return (vxcm, vycm, vzcm)

    @staticmethod
    def calc_ang_mom(atom_list, lif_object, point):
        angm = [0, 0, 0]

        if len(atom_list) == 0:
            return
        masses = lif_object.get_masses()
        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            xi = atom.x - point[0]
            yi = atom.y - point[1]
            zi = atom.z - point[2]
            vels = atom.get_velocities()

            angm[0] = angm[0] + wi * ( yi * vels[2] - zi * vels[1])
            angm[1] = angm[1] + wi * ( zi * vels[0] - xi *vels[2])
            angm[2] = angm[2] + wi * ( xi * vels[1] - yi * vels[0])

        print("Angm0, Angm1, Angm2 are: " + str(angm[0]) + " " + str(angm[1]) + " " + str(angm[2]))
        return angm

    # calculate the inertia tensor of a set of particles, relative to a point (point = [p1, p2, p3])
    @staticmethod
    def calc_inertia_mom(atom_list, lif_object, point):
        
        eps = 0.000001
        imom = [[0,0,0],[0,0,0],[0,0,0]]
        size_atom_list = len(atom_list)
        
        if  size_atom_list == 0:
            return
        xx = 0
        xy = 0
        xz = 0
        yy = 0
        yz = 0
        zz = 0

        masses = lif_object.get_masses()
        for atom in atom_list:
            xi = atom.x - point[0]
            yi = atom.y - point[1]
            zi = atom.z - point[2]
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            xx = xx + wi * xi * xi
            xy = xy + wi * xi * yi
            xz = xz + wi * xi * zi
            yy = yy + wi * yi * yi
            yz = yz + wi * yi * zi
            zz = zz + wi * zi * zi

            imom[0][0] = yy + zz
            imom[0][1] = -xy
            imom[0][2] = -xz
            imom[1][0] = -xy
            imom[1][1] = xx + zz
            imom[1][2] = -yz
            imom[2][0] = -xz
            imom[2][1] = -yz
            imom[2][2] = xx + yy

            # Avoid division by zero
            if size_atom_list <= 2:
                imom[0][0] = imom[0][0] + eps
                imom[1][1] = imom[1][1] + eps
                imom[2][2] = imom[2][2] + eps

            print('Inertia momentum is:')
            print(imom)
            return imom
   
    # compute current temperature
    @staticmethod
    def calc_temperature(atom_list, lif_object, frozendof):
        
        temp = 0
        size_atom_list = len(atom_list)
        mvv2e = 0
        boltz = 0

        if  size_atom_list == 0:
            return

        masses = lif_object.get_masses()
        for atom in atom_list:
            vel = atom.get_velocities()
            atom_type_mass =  [item for item in masses if item[0] == atom.atom_type][0][1]
            temp = temp + (vel[0] * vel[0] + vel[1] * vel[1] + vel[2] * vel[2]) * atom_type_mass

        
        Unit_style = Kinetics.determine_default_unit_values(OTHER_DEFAULTS.unit_style)
        mvv2e = Unit_style.mvv2e
        boltz = Unit_style.boltz
        ndof = OTHER_DEFAULTS.idimension * size_atom_list - frozendof
        temp = temp * mvv2e / (ndof * boltz)

        print('Temperature of fragment:')
        print(temp)
        return temp

    
    # rescale temperature to target temp T0
    @staticmethod
    def temp_rescale(atom_list, lif_object, T0, Temp):

        factor = sqrt(T0/ Temp)
        size_atom_list = len(atom_list)

        if size_atom_list == 0:
            return

        for atom in atom_list:
            vels = atom.get_velocities()
            atom.set_velocities((vels[0] *factor, vels[1] * factor,  vels[2] * factor))
        
        temp = Kinetics.calc_temperature(atom_list, lif_object, 6)
        print(temp)
        return temp

    

    # compute temperature contributions from trans,vib,rotation
    # vt, vv, vr = [[vx, vy, vz]...]
    @staticmethod
    def calc_tvr_temperature(atom_list, lif_object, nat, vt, vv, vr):
        j = 0
        Tt = 0
        Tr = 0
        Tv = 0
        
        masses = lif_object.get_masses()
        for atom in atom_list:
            mass =  [item for item in masses if item[0] == atom.atom_type][0][1]
            vt1 = vt[j]
            vr1 = vr[j]
            vv1 = vv[j]
            Tt = Tt + (vt1[0] * vt1[0] + vt1[1] * vt1[1] + vt1[2] * vt1[2]) * mass 
            Tr = Tr + (vr1[0] * vr1[0] + vr1[1] * vr1[1] + vr1[2] * vr1[2]) * mass
            Tv = Tv + (vv1[0] * vv1[0] + vv1[1] * vv1[1] + vv1[2] * vv1[2]) * mass
            j = j + 1

            ndof = OTHER_DEFAULTS.idimension * nat

            unit_style_class = Kinetics.determine_default_unit_values(OTHER_DEFAULTS.unit_style)
            mvv2e = unit_style_class.mvv2e
            boltz = unit_style_class.boltz

            Tt = Tt * mvv2e / ( ndof * boltz)
            Tr = Tr * mvv2e / ( ndof * boltz)
            Tv = Tv * mvv2e / ( ndof * boltz)


