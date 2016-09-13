#!/usr/bin/python
from openbabel import OBConversion, OBMol
from pybel_orca import write_orca_input

# Create an instance of OBMol and OBConversion
mol = OBMol()
converter = OBConversion()

# Read a pdb file
converter.SetInFormat('pdb')
converter.ReadFile(mol, 'formaldehyde.pdb')

# Write orca input file
result = write_orca_input(
    mol,
    comment='This is a comment',
    keywords=[
        'RI',
        'PBE',
        'def2-SVP',
        'def2-SVP/J',
        'opt'
    ]
)

print result
