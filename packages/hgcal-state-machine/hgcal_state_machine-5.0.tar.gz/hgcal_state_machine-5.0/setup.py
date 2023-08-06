from setuptools import setup, find_packages

setup(
    name='hgcal_state_machine',
    version='5.0',
    packages=find_packages(),
    install_requires=[
        'transitions'
    ],
    include_package_data=True
)
