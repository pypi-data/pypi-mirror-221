
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyyardian",
    version="0.0.1",
    author="Marty Sun",
    author_email="marty.sun@aeonmatrix.com",
    description="A package for interacting with the Yardian irrigation controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h3l1o5/pyyardian",
    packages=find_packages()
)