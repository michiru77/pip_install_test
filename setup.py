import setuptools

with open("module1/README.md", "r") as fh:
    long_description1 = fh.read()

with open("module2/README.md", "r") as fh:
    long_description2 = fh.read()

setuptools.setup(
    name="module1",
    version="1.0",
    author="michiru77",
    author_email="XXX",
    description="module1 is my own python package",
    long_description=long_description1
    long_description_content_type="text/markdown",
    url="XXX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: XXX",
        "License :: OSI Approved :: XXX",
        "Operating System :: XXX",
    ]
)

setuptools.setup(
    name="module2",
    version="1.0",
    author="michiru77",
    author_email="XXX",
    description="module2 is my own python package",
    long_description=long_description2
    long_description_content_type="text/markdown",
    url="XXX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: XXX",
        "License :: OSI Approved :: XXX",
        "Operating System :: XXX",
    ]
)