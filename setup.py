import os
import pathlib
from setuptools import setup, find_packages

# Package meta-data.
NAME = "greenponik-thermistor10k"
DESCRIPTION = "Read temperature on thermistor \
10k through Python3 on raspberry pi"
URL = "https://github.com/GreenPonik/GreenPonik_Thermistor10k"
EMAIL = "contact@greenponik.com"
AUTHOR = "GreenPonik SAS"
REQUIRES_PYTHON = ">=3.6.0"

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    "adafruit-blinka",
    "adafruit-circuitpython-ads1x15",
    "adafruit-extended-bus",
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Load the package's version.py module as a dictionary.
about = {}
with open(os.path.join(here, "version.py")) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about["__version__"],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    license="MIT",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("docs")),
    python_requires=REQUIRES_PYTHON,
    project_urls={  # Optional
        "Source": "https://github.com/GreenPonik/GreenPonik_Thermistor10k/",
        "Bug Reports": "https://github.com/GreenPonik/GreenPonik_Thermistor10k/issues",
    },
    keywords="GreenPonik hydroponics thermistor 10k ohm \
         temperature reader python hardware diy iot raspberry pi",
)
