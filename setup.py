import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "iptool",
    version = "0.0.1",
    author = "Pablo Collado Soto",
    author_email = "pcolladosoto@gmail.com",
    description = "A small package for managing IP addresses",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/pcolladosoto/iptool",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    entry_points = {
        "console_scripts": [
            "iptool = iptool:bootstrap"
        ]
    }
)