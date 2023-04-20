import re
import datetime

"""Based on LAMMPS Data Format: https://lammps.sandia.gov/doc/2001/data_format.html"""
import sys

from LammpsInputFile import LammpsInputFile

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <desc_file>".format(sys.argv[0]))
        sys.exit(-1)
    l = LammpsInputFile(sys.argv[1])

    l.write_to_file()