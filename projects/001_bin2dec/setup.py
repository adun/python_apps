"""Configuration for Python packages installation."""
from setuptools import find_packages, setup

setup(
    name="bin2dec",
    version="0.1.0",
    url="https://github.com/adun/python_apps/projects/001_bin2dec",
    license="MIT",
    description="Converts a binary number to decimal",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "pytest-cov"]},
)
