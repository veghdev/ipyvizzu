#!/usr/bin/env python3
from setuptools import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

with open("README.md") as fp:
    long_description = fp.read()

version = "1.0.0"

setup(
    name="pyvizzu",
    version=version,
    description="pyvizzu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=['pyvizzu'],
    package_dir={'pyvizzu': 'src/pyvizzu'},
    package_data={'pyvizzu': ['templates/*.js']},
    python_requires='>=3.6',
    install_requires=["pandas"],
    url="https://github.com/vizzuhq/ipyvizzu",
    project_urls={
        "Documentation": "https://ipyvizzu.vizzuhq.com/",
        "Source": "https://github.com/vizzuhq/ipyvizzu",
        "Tracker": "https://github.com/vizzuhq/ipyvizzu/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)

setup(
    name="ipyvizzu",
    version=version,
    description="ipyvizzu is the Jupyter Notebook integration of Vizzu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=['ipyvizzu'],
    package_dir={'ipyvizzu': 'src/ipyvizzu'},
    package_data={'ipyvizzu': ['templates/*.js']},
    python_requires='>=3.6',
    install_requires=["IPython", "pyvizzu"],
    url="https://github.com/vizzuhq/ipyvizzu",
    project_urls={
        "Documentation": "https://ipyvizzu.vizzuhq.com/",
        "Source": "https://github.com/vizzuhq/ipyvizzu",
        "Tracker": "https://github.com/vizzuhq/ipyvizzu/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
