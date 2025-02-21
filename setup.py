from setuptools import setup, find_packages

setup(
    name="kaiwu_quantum_toolkit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.0.0",
        "pytest>=7.0.0",
        "matplotlib>=3.0.0",
        "networkx>=2.0",
    ],
) 