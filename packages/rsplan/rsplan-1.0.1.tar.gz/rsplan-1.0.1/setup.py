# setup.py

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rsplan",
    version = "1.0.1",
    author = "Built Robotics",
    author_email = "tarakapoor9@gmail.com",
    description = ("Reeds-Shepp algorithm implementation in Python."),
    license = "MIT",
    keywords = "reeds-shepp path planning",
    url = "https://github.com/builtrobotics/rs",
    packages=['rsplan'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
