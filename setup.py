#!/usr/bin/env python
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = ["sceptre>=2.0"]

setup(
    name="sceptre-aws-resolver",
    version="0.1",
    description="Sceptre AWS resolver",
    py_modules=["main"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jeshan G. BABOOA",
    author_email="j@jeshan.co",
    license="BSD-2-Clause",
    url="https://github.com/jeshan/sceptre-aws-resolver",
    entry_points={"sceptre.resolvers": ["aws = main:Aws"]},
    keywords="sceptre",
    install_requires=install_requirements,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
