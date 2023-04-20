from config.global_setting import OTHER_DEFAULTS 


class Periodic:


    # Remap the point (xx,yy,zz) into the periodic box,
    # no matter how far away it is. Adjust true flag accordingly.
    @staticmethod
    def remap(xx, yy, zz, itrue):

        if OTHER_DEFAULTS.perflagx  == 0:
            while xx < OTHER_DEFAULTS.box["xlo xhi"][0] :
                xx = xx + OTHER_DEFAULTS.xprd
                itrue = itrue - 1
            while xx >= OTHER_DEFAULTS.box["xlo xhi"][1] :
                xx = xx - OTHER_DEFAULTS.xprd
                itrue = itrue + 1
        
        if OTHER_DEFAULTS.perflagy == 0:
            while yy < OTHER_DEFAULTS.box["ylo yhi"][0] :
                yy = yy + yy + OTHER_DEFAULTS.yprd
                itrue = itrue - 1000
            while yy >= OTHER_DEFAULTS.box["ylo yhi"][1] :
                yy = yy - OTHER_DEFAULTS.yprd
                itrue = itrue + 1000
        
        if OTHER_DEFAULTS.perflagz == 0:
            while zz < OTHER_DEFAULTS.box["zlo zhi"][0] :
                zz = zz + OTHER_DEFAULTS.zprd
                itrue = itrue - 1000000
            while zz >= OTHER_DEFAULTS.box["zlo zhi"][1] :
                zz = zz - OTHER_DEFAULTS.zprd
                itrue = itrue + 1000000

        return xx, yy, zz, itrue


    #  enforce PBC on appropriate dims, no matter which box image the particles are in
    @staticmethod
    def pbc(atom_list):

        for atom in atom_list:
            atom.x, atom.y, atom.z, atom.true =  Periodic.remap(atom.x, atom.y, atom.z, atom.true)
            
        print(atom.x, atom.y, atom.z, atom.true)


    @staticmethod
    def minimg(dx, dy, dz):

        if OTHER_DEFAULTS.perflagx == 0:
            if abs(dx) > OTHER_DEFAULTS.xprd_half:
                if dx < 0.0:
                    dx = dx + OTHER_DEFAULTS.xprd
                else:
                    dx = dx - OTHER_DEFAULTS.xprd

        if OTHER_DEFAULTS.perflagy == 0:
            if abs(dy) > OTHER_DEFAULTS.yprd_half:
                if dy < 0.0:
                    dy = dy + OTHER_DEFAULTS.yprd
                else:
                    dy = dy - OTHER_DEFAULTS.yprd

        if OTHER_DEFAULTS.perflagz == 0:
            if abs(dz) > OTHER_DEFAULTS.zprd_half:
                if dz < 0.0:
                    dz = dz + OTHER_DEFAULTS.zprd
                else:
                    dz = dz -OTHER_DEFAULTS.zprd
        
        return dx, dy, dz

    # Returns the image indices ix,iy,iz of the box, according to the true-flag
    @staticmethod
    def get_image_index2(iat):
        ix = 0
        iy = 0
        iz = 0
        return ix, iy, iz
    @staticmethod
    def get_image_index(itrue):

        d = itrue
        rem = d % 1000
        ix = rem - 500
        d = d / 1000
        rem = d % 1000
        iy = rem - 500
        d = d / 1000
        rem = d % 1000
        iz =  rem - 500
        return ix, iy, iz

    # Returns the true-flag, according to the image indices ix,iy,iz of the box
    @staticmethod
    def get_itrue(ix, iy, iz):
        
        itrue = (500 + iz) * 1000000 + + (500 + iy) * 1000 + (500 + ix)
        return itrue

    # Sets *prd and *prd_half - call every time the box size changes
    @staticmethod
    def set_prd():
        
        OTHER_DEFAULTS.xprd = OTHER_DEFAULTS.box["xlo xhi"][1] - OTHER_DEFAULTS.box["xlo xhi"][0]
        OTHER_DEFAULTS.xprd_half = OTHER_DEFAULTS.xprd * 0.5
        OTHER_DEFAULTS.yprd = OTHER_DEFAULTS.box["ylo yhi"][1] - OTHER_DEFAULTS.box["ylo yhi"][0]
        OTHER_DEFAULTS.yprd_half = OTHER_DEFAULTS.yprd * 0.5
        OTHER_DEFAULTS.zprd = OTHER_DEFAULTS.box["zlo zhi"][1] - OTHER_DEFAULTS.box["zlo zhi"][0]
        OTHER_DEFAULTS.zprd_half = OTHER_DEFAULTS.zprd * 0.5

        @staticmethod
        def clean_edges():
            pass
        
        @staticmethod
        def x_unclean_edges():
            pass