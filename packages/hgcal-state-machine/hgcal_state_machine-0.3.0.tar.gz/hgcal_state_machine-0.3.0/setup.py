from setuptools import setup, find_packages

setup(
    name='hgcal_state_machine',
    version='0.3.0',
    py_modules=['hgcal_state_machine'],
    install_requires=[
        'transitions'
    ],
)