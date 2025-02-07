"""Module providing setup data to install myCLI."""

from setuptools import setup, find_packages

setup(
    name="myCLI",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "mycli = main:app",
        ],
    },
)
