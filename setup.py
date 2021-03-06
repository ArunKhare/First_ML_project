from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME ="housing-predictor"
VERSION = '0.0.4'
AUTHOR = "ARUN KHARE" 
DESCRIPTION = "This is my first machine learning project"
# PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    ''' 
    Description : This function is going to return list mention in requirements.txt file
    return: This funtion is foing to return a list which contain list of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')   # .pop('-e .') / .remove('-e .')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    # packages=PACKAGES
    packages=find_packages(),
    install_requires=get_requirements_list()
)

# if __name__=="__main__":
#     print(get_requirements_list())
