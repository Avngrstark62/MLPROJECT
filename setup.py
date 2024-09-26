from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req for req in requirements if req!='\n']
    return requirements


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Abhijeet',
    author_email='thakurabhijeetsingh79@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)