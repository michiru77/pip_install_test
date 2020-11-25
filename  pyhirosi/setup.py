import setuptools

with open("pyhirosi/README.md", "r") as fh:
    hirosi_long_description = fh.read()

setuptools.setup(
    name="pyhirosi",
    version="1.0",
    author="michiru77",
    author_email="XXX",
    description="module1 is my own python package",
    long_description=hirosi_long_description,
    long_description_content_type="text/markdown",
    url="XXX",
    packages=setuptools.find_packages('pyhirosi'),
    classifiers=[
        "Programming Language :: Python :: XXX",
        "License :: OSI Approved :: XXX",
        "Operating System :: XXX",
    ]
)