from pathlib import Path
import setuptools

setuptools.setup(
    name="tompdf_1",
    version="1.4",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["Data", "Tests"])
)
