class Bond:
    id = None
    bond_type = None
    atom_id1 = None
    atom_id2 = None

    def __init__(self, id, bond_type, atom_id1, atom_id2):
        self.id = id
        self.bond_type = bond_type
        self.atom_id1 = atom_id1
        self.atom_id2 = atom_id2

    def get_id(self):
        return self.id   

    def get_bond_type(self):
        return self.bond_type

    def get_atoms_id(self):
        ids = (self.atom_id1, self.atom_id2)
        return ids

    def set_bond_type(self, bond_type):
        self.bond_type = bond_type

    def set_atoms_id(self, atom_id1, atom_id2):
        self.atom_id1 = atom_id1
        self.atom_id2 = atom_id2

    def print_bond(self):
        bond_id = self.id
        bond_type = self.bond_type
        atom_id1 = self.atom_id1 
        atom_id2 = self.atom_id2
        str = " {}\t{}\t{}\t{}\n".format(bond_id, bond_type, atom_id1, atom_id2).expandtabs()
        return str

