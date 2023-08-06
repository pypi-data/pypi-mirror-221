from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'A coding toolkit for python'
LONG_DESCRIPTION = 'This toolkit contains useful packages to make writing pyhton prograsms easier'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="codingtoolkit", 
        version=VERSION,
        author="flyingreshin",
        author_email="flyingreshin@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[''], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)