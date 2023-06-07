# setup.py
from setuptools import setup, find_packages

setup(
    name="mcda",
    version="0.1",
    packages=find_packages(),
    author="Molly McDonough",
    author_email="mrm6464@psu.edu",
    description="A Python package for analyzing materials characterization data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mollyrmcdonough/mcda",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
