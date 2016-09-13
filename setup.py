from setuptools import setup

setup(
    name='pybel-orca',
    version='0.1',
    py_modules=['bin/pybel-orca'],
    install_requires=[
        'Click',
        'openbabel',
    ]
)
