
Organiser votre projet : Assurez-vous que votre projet est bien organisé avec une structure de répertoires appropriée. Un package Python typique contient un fichier spécial appelé __init__.py dans chaque répertoire pour en faire un package. Vous devriez également placer votre script principal (celui que vous souhaitez rendre installable) dans un répertoire distinct.
Ajouter un fichier setup.py : Le fichier setup.py est un script Python qui définit les métadonnées de votre projet et les dépendances requises pour son installation. Créez un fichier setup.py à la racine de votre projet avec le contenu suivant :

from setuptools import setup, find_packages


setup(
   name='hgcal_state_machine',
   version='0.4.0',
   packages=find_packages(),
   install_requires=[
       'transitions'
   ],
)


python setup.py sdist

twine upload dist/hgcal_state_machine-0.4.0.tar.gz
