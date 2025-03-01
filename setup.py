"""ZARP CLI package definition"""

import os
from typing import List

from setuptools import setup, find_packages

from zarp import __version__

root_dir: str = os.path.dirname(os.path.abspath(__file__))

# Read long description from file
FILE_NAME: str = os.path.join(root_dir, "README.md")
if os.path.isfile(FILE_NAME):
    with open(FILE_NAME, encoding="utf-8") as _f:
        LONG_DESCRIPTION: str = _f.read()

# Read requirements from file
FILE_NAME: str = os.path.join(root_dir, "requirements.txt")
if os.path.isfile(FILE_NAME):
    with open(FILE_NAME, encoding="utf-8") as _f:
        INSTALL_REQUIRES: List = _f.read().splitlines()

setup(
    name="zarp",
    version=__version__,
    description=(
        "User-friendly command-line interface for the ZARP RNA-Seq analysis "
        "pipeline"
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://git.scicore.unibas.ch/zavolan_group/tools/zarp-cli",
    author="Zavolan Lab",
    author_email="zavolab-biozentrum@unibas.ch",
    maintainer="Zavolan Lab",
    maintainer_email="zavolab-biozentrum@unibas.ch",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Utilities",
    ],
    entry_points={
        'console_scripts': [
            'zarp = zarp.zarp:main',
        ],
    },
    keywords=[
        'bioinformatics',
        'workflow',
        'ngs',
        'high-throughput sequencing',
    ],
    project_urls={
        "Repository":
        "https://git.scicore.unibas.ch/zavolan_group/tools/zarp-cli",
        "Tracker":
        "https://git.scicore.unibas.ch/zavolan_group/tools/zarp-cli/-/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    setup_requires=[
        "setuptools_git == 1.2",
    ],
)
