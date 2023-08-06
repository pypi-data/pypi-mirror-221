from setuptools import setup, find_packages

setup(
    name='hgcal_state_machine',
    version='0.6.0',
    packages=['state_machine'],
    install_requires=[
        'transitions'
    ],
)
