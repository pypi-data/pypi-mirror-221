from setuptools import setup, find_packages

setup(
    name='hgcal_state_machine',
    version='0.2.0',
    py_modules=['state_machine'],
    install_requires=[
        'transitions'
    ],
)