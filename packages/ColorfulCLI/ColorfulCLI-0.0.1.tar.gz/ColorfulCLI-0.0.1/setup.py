
from setuptools import setup, find_packages

setup(
    name="ColorfulCLI",
    version="0.0.1",
    author="Dave Bowlin",
    author_email="davebowlin@gmail.com",
    description="A simple, effective way to add color to your CLI apps.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
    