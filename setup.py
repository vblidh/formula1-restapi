import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

NAME="restapi"
VERSION = None

with open("README.md", "r") as fh:
    long_description = fh.read()



# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setuptools.setup(
    name=NAME, # Replace with your own username
    version=VERSION,
    author="Viktor Blidh",
    author_email="victor.blidh@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vblidh/formula1-restapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8',
)