import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Finance",
    version = "0.0.1",
    author = "Josh Saunders",
    author_email = "joshsaunderstm@gmail.com",
    description = ("Basic functions for financial calculations"),
    license = "Proprietary Level 1",
    keywords = "finance amortization compounding",
    packages=find_packages(),
    long_description=read('README.md'),
    # package_dir = {'': 'finance'},
    # py_modules=['finance'],
    )
