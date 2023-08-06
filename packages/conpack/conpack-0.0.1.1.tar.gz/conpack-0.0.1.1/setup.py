from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1.1'
DESCRIPTION = 'A small package'
LONG_DESCRIPTION = 'A large package'

# Setting up
setup(
    name="conpack",
    version=VERSION,
    author="conacts",
    author_email="<csheehan630@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Packaging'], 
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
