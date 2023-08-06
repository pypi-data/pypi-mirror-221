from setuptools import setup, find_packages

setup(
    name='hgcal_state_machine',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transitions'
    ],
)
