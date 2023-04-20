
# parameters unlikely to need changing
class CONSTANTS:
    mxpartic = 1000000
    lstmembuf = 5
    mxlist = mxpartic * lstmembuf
    mxfirst = mxlist + 1
#    constants
    PI = 3.14

    ir_data = 1
    ir_dump = 2
    iw_data = 3
    db_file = "debug.dbg"
    unit_style = "REAL"


# set units
class UNITS_LJ:
    boltz = 1.0
    hplanck = 0.18292026
    mvv2e = 1.0
    ftm2v = 1.0
    mv2d = 1.0
    nktv2p = 1.0
    qqr2e = 1.0
    qe2f = 1.0
    vxmu2f = 1.0
    xxt2kmu = 1.0
    e_mass = 0.0
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0
    femtosecond = 1.0
    qelectron = 1.0

    dt = 0.005
    skin = 0.3

class UNITS_REAL:
    boltz = 0.0019872067
    hplanck = 95.306976368
    mvv2e = 48.88821291 * 48.88821291
    ftm2v = 1.0 / 48.88821291 / 48.88821291
    mv2d = 1.0 / 0.602214179
    nktv2p = 68568.415
    qqr2e = 332.06371
    qe2f = 23.060549
    vxmu2f = 1.4393264316e4
    xxt2kmu = 0.1
    e_mass = 1.0/1836.1527556560675
    hhmrr2e = 0.0957018663603261
    mvh2r = 1.5339009481951
    angstrom = 1.0
    femtosecond = 1.0
    qelectron = 1.0

    dt = 1.0
    skin = 2.0 

class UNITS_METAL:
    boltz = 8.617343e-5
    hplanck = 4.135667403e-3
    mvv2e = 1.0364269e-4
    ftm2v = 1.0 / 1.0364269e-4
    mv2d = 1.0 / 0.602214179
    nktv2p = 1.6021765e6
    qqr2e = 14.399645
    qe2f = 1.0
    vxmu2f = 0.6241509647
    xxt2kmu = 1.0e-4
    e_mass = 0.0        
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0
    femtosecond = 1.0e-3
    qelectron = 1.0

    dt = 0.001
    skin = 2.0

class UNITS_SI:
    boltz = 1.3806504e-23
    hplanck = 6.62606896e-34
    mvv2e = 1.0
    ftm2v = 1.0
    mv2d = 1.0
    nktv2p = 1.0
    qqr2e = 8.9876e9
    qe2f = 1.0
    vxmu2f = 1.0
    xxt2kmu = 1.0
    e_mass = 0.0
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0e-10
    femtosecond = 1.0e-15
    qelectron = 1.6021765e-19

    dt = 1.0e-8
    skin = 0.001

class UNITS_CGS:
    boltz = 1.3806504e-16
    hplanck = 6.62606896e-27
    mvv2e = 1.0
    ftm2v = 1.0
    mv2d = 1.0
    nktv2p = 1.0
    qqr2e = 1.0
    qe2f = 1.0
    vxmu2f = 1.0
    xxt2kmu = 1.0
    e_mass = 0.0
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0e-8
    femtosecond = 1.0e-15
    qelectron = 4.8032044e-10

    dt = 1.0e-8
    skin = 0.1

class UNITS_ELECTRON:
    boltz = 3.16681534e-6
    hplanck = 0.1519829846
    mvv2e = 1.06657236
    ftm2v = 0.937582899
    mv2d = 1.0
    nktv2p = 2.94210108e13
    qqr2e = 1.0
    qe2f = 1.94469051e-10
    vxmu2f = 3.39893149e1
    xxt2kmu = 3.13796367e-2
    e_mass = 0.0
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.88972612
    femtosecond = 0.0241888428
    qelectron = 1.0

    dt = 0.001
    skin = 2.0

class UNITS_MICRO:
    boltz = 1.3806504e-8
    hplanck = 6.62606896e-13
    mvv2e = 1.0
    ftm2v = 1.0
    mv2d = 1.0
    nktv2p = 1.0
    qqr2e = 8.9876e30
    qe2f = 1.0
    vxmu2f = 1.0
    xxt2kmu = 1.0
    e_mass = 0.0
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0e-4
    femtosecond = 1.0e-9
    qelectron = 1.6021765e-19

    dt = 2.0
    skin = 0.1

class UNITS_NANO:
    boltz = 0.013806503
    hplanck = 6.62606896e-4
    mvv2e = 1.0
    ftm2v = 1.0
    mv2d = 1.0
    nktv2p = 1.0
    # qqr2e = 8.9876e39   # Error: Real constant overflows its kind
    qe2f = 1.0
    vxmu2f = 1.0
    xxt2kmu = 1.0
    e_mass = 0.0       
    hhmrr2e = 0.0
    mvh2r = 0.0
    angstrom = 1.0e-1
    femtosecond = 1.0e-6
    qelectron = 1.6021765e-19

    dt = 0.00045
    skin = 0.1


class OTHER_DEFAULTS:

    unit_style = "REAL"
   
# global settings and flags
    idimension = 3
    nsteps = 0
    itime = None
    newton_bond = 1
    # dt = None
    isalloc = False

# domain
    xprd = 0
    yprd = 0
    zprd = 0

    xprd_half = 0
    yprd_half = 0
    zprd_half = 0

    box =  {"xlo xhi" : None,
            "ylo yhi": None,
            "zlo zhi": None
            }

    # Define a cell length of 2 Angstrom
    r_cutoff = 2

    perflagx = 0
    perflagy = 0
    perflagz = 0

# Not implemented -> substitute with Atom/Bond class from atom.py module ?
# - atoms
# - bonds

    # TODO
    # ATOMS
    npartic = 0
    ntypes = 0
    natomtypes = 0
    rvdw = None #[]
    # mass = None # []
    # x = None # [][]
    # v = None # [][]
    # x_unclean = None # [][]
    # q = None # []
    # tag = None #[]
    itype = None # []
    # molecule = None # []
    # true = [] #[]
    ibox = None #[]
    # atomtype = None #[]
    atypes_total = None #[]
    
    # bond connectivity for each atom

    numbond = None #(:)
    bondtype = None #(:,:)
    bondatom = None #(:,:)

    r_nbonds = 0
    r_nangles = 0
    r_ndihedrals = 0
    r_nimpropers = 0
    r_nbonds_list = 0
    r_nangles_list = 0
    r_ndihedrals_list = 0
    r_nimpropers_list = 0
    r_bonds = None #(:,:)
    r_angles = None #(:,:)
    r_dihedrals = None #(:,:)
    r_impropers = None #(:,:)
    r_nangletypes = 0
    r_nbondtypes = 0 
    r_ndihedraltypes = 0
    r_nimpropertypes = 0
    r_bondtype = None #(:)
    r_angletype = None #(:)
    r_dihedraltype = None #(:)
    r_impropertype = None #(:)
    
    bindex_list = None #(:)
    aindex_list = None #(:)
    dindex_list = None #(:)
    iindex_list = None #(:)
                    
    r_natypes_list = 0
    r_nbtypes_list = 0
    r_ndtypes_list = 0
    r_nitypes_list = 0

# temperature creation
    rotationflag = None


# input
    trueflag = None
    ndumpatom = None
    ndumpvel = None
    ndumpforce = None
    atomstyle = None

# diagnostics
    idebug = 0
    idbg = 100
    iEtrans = 101
    iErot = 102
    temptest = 103

# fragments
    # list = None # []
    # first = None # []
    # nlist = 0
    # isrange = None #[]

# velocity analysis
    Emax = None #
    vmax = None
    nvbin = None
    nEbin = None
    vbin = None #[]
    Ebin_size = None
    Ebin_sizemol = None
    bin_size = None
    v_tr = None
    v_rot = None
    v_vib = None
    v_rovib = None
    ddisp = None
    ddisp_v = None
    displacements = None
    d_k = None

# random number global seed
    
    tgvar = 0
    # TODO random number
    iseed = 0
    seed_global = iseed

# read write things
    nm_nmol = None
    ffoffset = 0
    nm_modes = None
    nm_natpermol = None
    nm_ncols = None
    nm_refxyz = None
    nm_modes = None
    nm_paxes = None
    nm_com = None
    nm_masses = None
    nm_paxsorted = None
# read write things
    vcorr0 = None
    # 3-dimensional
    vcorrt = None
    spect = None
    v0 = None
  


# others defined in t4l
    maxbondper = 8
    nmolecular = 0

# files in t4l
    etrans = "Etrans.out"
    erot = "Erot.out"
    temptest = "temptest.out"



