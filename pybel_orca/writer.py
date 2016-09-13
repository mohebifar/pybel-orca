from pybel import Molecule
from openbabel import OBElementTable

element_table = OBElementTable()
header = '# Generated using pybel-orca'


def write_orca_input(mol, **optional):
    if not isinstance(mol, Molecule):
        mol = Molecule(mol)

    # Comments
    orca_inp = get_comments(optional)

    # Keywords part
    orca_inp += get_keywords(optional)

    # xyz part
    orca_inp += get_xyz(mol)

    return orca_inp


def get_keywords(optional):
    result = '!'
    if 'keywords' in optional:
        result += ' '

        if isinstance(optional['keywords'], list):
            result += ' '.join(optional['keywords'])
        else:
            result += optional['keywords']

    return result + '\n'


def get_xyz(mol):
    xyz = ' '.join(
        map(str, [
            '*xyz',
            mol.OBMol.GetTotalCharge(),
            mol.OBMol.GetTotalSpinMultiplicity()
        ])
    ) + '\n'

    for atom in mol:
        atom_geometry_data = map(str, [
            element_table.GetSymbol(atom.atomicnum),
            atom.vector.GetX(),
            atom.vector.GetY(),
            atom.vector.GetZ()
        ])

        xyz += ' '.join(atom_geometry_data) + '\n'

    xyz += '*'

    return xyz


def get_comments(optional):
    comment = header + '\n'

    if 'comment' in optional:
        comment += '# ' + optional['comment']

    return comment + '\n'
