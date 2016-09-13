#!/usr/bin/env python

from openbabel import OBConversion, OBMol
from pybel_orca import write_orca_input

import click

# Create an instance of OBMol and OBConversion
mol = OBMol()
converter = OBConversion()


@click.command()
@click.option('--input_type', default='pdb', help='Input file type', type=click.STRING)
@click.option('--keywords', help='ORCA input Keywords', type=click.STRING)
@click.argument('input_file', type=click.Path(readable=True, exists=True))
@click.argument('output_file', type=click.Path(writable=True, resolve_path=True))
def convert(input_type, keywords, input_file, output_file):
    """Welcome to pybel orca converter!"""

    # Read a pdb file
    converter.SetInFormat(str(input_type))
    converter.ReadFile(mol, str(input_file))

    # Write orca input file
    result = write_orca_input(
        mol,
        # comment=comment,
        keywords=keywords
    )

    file = open(output_file, 'w')
    file.write(result)
    file.close()

    click.echo('ORCA input file successfully generated at:\n=> %s' % output_file)


if __name__ == '__main__':
    convert()
