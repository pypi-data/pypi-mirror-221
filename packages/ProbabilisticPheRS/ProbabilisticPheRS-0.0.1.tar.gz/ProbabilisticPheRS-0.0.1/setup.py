#!python

import setuptools
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('ProbabilisticPheRS/ProbabilisticPheRS.py').read(),
    re.M).group(1)


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ProbabilisticPheRS",
    version=version,
    author="David Blair",
    author_email="david.blair@ucsf.edu",
    description="A semi-supervised probability model for estimating the likelihood that a patient has a rare disease based on their observed symptoms.",
    long_description_content_type="text/markdown",
    url="https://github.com/daverblair/ProbabilisticPheRS",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'torch',
        'PiecewiseBeta',
        'tqdm',
        'sklearn',
        'pytorch-minimize',
        'tensordict'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
