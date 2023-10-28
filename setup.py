from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="housing-predictor"
VERSION = "0.0.1"
AUTHOR = "SKORM1700"
DESCRIPTION = "iNMLP1"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as f:
        return f.readlines().remove("-e .")
    
#we removed "-e ." because we added it in the requirements.txt file and we are using find_packages()




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #PACKAGES, find_packages() do the same task as "-e .", it looks for folder with __init__ file and returns package (folder name)
    install_requires = get_requirements_list()          #all other external required libraries/packages are installed using this
    #any python script is called as module
    #any folder with __init__ py script is called package
)