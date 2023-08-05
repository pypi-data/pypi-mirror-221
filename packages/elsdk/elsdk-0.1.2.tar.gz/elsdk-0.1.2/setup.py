# Third Party Library
from setuptools import find_packages, setup

setup(
    name="elsdk",
    version="0.1.2",
    description="SDK for Scheduling and Managing EL Platform",
    author="EinstonLabs",
    author_email="info@einstonlabs.com",
    keywords="elp,einston,sdk",
    license="All Rights Reserved by Einston Labs",
    url="https://einstonlabs.com",
    python_requires="~=3.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    project_urls={
        'Documentation': 'https://docs.einstonlabs.com'
    },
    install_requires=[
        "requests==2.31.0",
        "pycryptodome==3.18.0",
        "PyJWT==2.7.0",
        "python-dateutil==2.8.2",
        "python-json-logger==2.0.7",
    ]
)
