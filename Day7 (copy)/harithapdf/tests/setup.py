import setuptools
from pathlib import Path

setuptools.setup(
    name="harithapdf",
    version="1.0",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
