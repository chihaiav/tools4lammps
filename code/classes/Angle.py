class Angle:
    id = None
    angle_type = None
    atom_id1 = None
    atom_id2 = None
    atom_id3 = None

    def __init__(self, id, angle_type, atom_id1, atom_id2, atom_id3):
        self.id = id
        self.angle_type = angle_type
        self.atom_id1 = atom_id1
        self.atom_id2 = atom_id2
        self.atom_id3 = atom_id3

    def get_id(self):
        return self.id

    def get_angle_type(self):
        return self.angle_type

    def get_atoms(self):
        ids = (self.atom_id1, self.atom_id2, self.atom_id3)
        return ids

    def set_angle_type(self, angle_type):
        self.angle_type = angle_type

    def set_atom_ids(self, atom_id1, atom_id2, atom_id3):
        self.atom_id1 = atom_id1
        self.atom_id2 = atom_id2
        self.atom_id3 = atom_id3

    def print_angle(self):
        id = self.id
        angle_type = self.angle_type
        atom_id1 = self.atom_id1 
        atom_id2 = self.atom_id2
        atom_id3 = self.atom_id3
        str = " {}\t{}\t{}\t{}\t{}\n".format(id, angle_type, atom_id1, atom_id2, atom_id3).expandtabs()
        return str
