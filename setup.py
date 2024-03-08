from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """
    this function will return list of requirements
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
# To enable simulataneous installments of requirements.tx packages and building the project 
# we add "-e . in requirements.txt file so that it runs the setup.py at the same time"  
# It should also be not read during the run of setup.py      
setup(
    name='mlproject',
    version='0.0.1',
    author='Srinivas Padhy',
    author_email='srinivaspadhybm@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)