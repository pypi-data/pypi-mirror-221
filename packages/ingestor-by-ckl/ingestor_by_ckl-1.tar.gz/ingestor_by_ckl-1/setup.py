import os
import logging
from importlib.machinery import SourceFileLoader
from setuptools import setup, find_packages, Command


def is_comment_or_empty(line):
    stripped = line.strip()
    return stripped == "" or stripped.startswith("#")

setup(
    name="ingestor_by_ckl",
    version='1',
    packages=find_packages(exclude=["tests", "tests.*"]),
    author="Databricks",
    description="MLflow: A Platform for ML Development and Productionization",
    long_description_content_type="text/x-rst",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.5",
)
