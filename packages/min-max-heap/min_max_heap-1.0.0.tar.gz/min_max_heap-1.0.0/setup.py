from setuptools import setup

name = "min_max_heap"

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

with open("README.md", "r") as fp:
    long_desc = fp.read()

setup(
    name=name,
    version="1.0.0",
    author="Yuan Yang",
    author_email="i@yangyuan.me",
    packages=[name],
    package_dir={name: "src"},
    url="https://github.com/hfi/min-max-heap",
    classifiers=classifiers,
    license="The MIT License (MIT)",
    description="A implementation of MinMaxHeap with Python language.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    platforms=["Any"],
)