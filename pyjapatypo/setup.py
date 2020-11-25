import setuptools

with open("pyjapatypo/README.md", "r") as fh:
    japatypo_long_description = fh.read()

setuptools.setup(
    name="pyjapatypo",
    version="1.0",
    author="michiru77",
    author_email="XXX",
    description="module2 is my own python package",
    long_description=japatypo_long_description,
    long_description_content_type="text/markdown",
    url="XXX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: XXX",
        "License :: OSI Approved :: XXX",
        "Operating System :: XXX",
    ]
)