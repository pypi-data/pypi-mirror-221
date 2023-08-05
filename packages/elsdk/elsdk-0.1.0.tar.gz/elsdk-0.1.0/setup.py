# Third Party Library
from setuptools import find_packages, setup

setup(
    name="elsdk",
    version="0.1.0",
    description="SDK for Scheduling and Managing EL Platform",
    author="EinstonLabs",
    author_email="",
    keywords="",
    license="All Rights Reserved by Einston Labs",
    url="",
    python_requires="~=3.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    install_requires=[
        "requests==2.31.0",
        "pycryptodome==3.18.0",
        "PyJWT==2.7.0",
        "python-dateutil==2.8.2",
        "python-json-logger==2.0.7",
    ]
)
