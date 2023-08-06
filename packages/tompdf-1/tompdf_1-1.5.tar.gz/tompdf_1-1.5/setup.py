import setuptools
from pathlib import Path

setuptools.setup(
    name="tompdf_1",
    version="1.5",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["Data", "Tests"])
)