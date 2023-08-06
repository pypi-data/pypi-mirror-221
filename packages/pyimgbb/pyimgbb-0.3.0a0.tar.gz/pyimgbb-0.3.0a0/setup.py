import pathlib
from setuptools import setup

long_description = pathlib.Path("README.md").read_text()

setup(
    name="pyimgbb",
    version="0.3.0-alpha",
    packages=["imgbb"],
    author="Adivhaho Mavhungu",
    author_email="adivhahomavhungu@outlook.com",
    description="A simple client for uploading images to imgbb.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mavhungutrezzy/imgbb",
    install_requires=["requests", "pillow", "python-decouple"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
