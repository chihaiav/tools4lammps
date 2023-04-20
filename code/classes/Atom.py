class Atom:
    id = None
    new_id = None
    molecule_tag = None
    atom_type = None
    q = None
    x = None 
    y = None
    z = None
    nx = None
    ny = None
    nz = None
    #  True flag for each atom to replace true from OTHER DEFAULTS
    true = None

    # Velocities Vx    Vy    Vz
    velocity = (None, None, None)

    def __init__(self, id, molecule_tag, atom_type, q, x, y, z, nx, ny, nz):
        self.id = id
        self.molecule_tag = molecule_tag
        self.atom_type = atom_type
        self.q = q
        self.x = x
        self.y = y
        self.z = z
        self.nx = nx
        self.ny = ny
        self.nz = nz
        # True flag for each atom
        self.true = 500500500

    def get_velocities(self):
        return self.velocity

    def set_velocities(self, velocity):
        self.velocity = velocity

    def set_new_id(self, new_id):
        self.new_id = new_id

    def get_new_id(self):
        return self.new_id        

    def print_atom(self):
        str = "\t{}\t{}\t{}\t{:.18f}\t{:.18f}\t{:.18f}\t{:.18f}\t{}\t{}\t{}\n".format(self.id,  self.molecule_tag, self.atom_type, self.q, self.x, self.y, self.z, self.nx, self.ny, self.nz).expandtabs()
        return str

    def print_velocity(self):
        str = "\t{}\t{:.18f}\t{:.18f}\t{:.18f}\n".format(self.id, self.velocity[0], self.velocity[1], self.velocity[2]).expandtabs()
        return str