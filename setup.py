#!/usr/bin/env python3
import os
import re

from setuptools import setup


def get_version():
    fn = os.path.join(os.path.dirname(__file__), "formasaurus", "__init__.py")
    with open(fn) as f:
        return re.findall(r'__version__ = "([\d\.\w]+)"', f.read())[0]


setup(
    name="formasaurus",
    version=get_version(),
    author="Mikhail Korobov",
    author_email="kmike84@gmail.com",
    license="MIT license",
    long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
    description="Formasaurus tells you the types of HTML forms and their fields using machine learning",
    url="https://github.com/scrapinghub/Formasaurus",
    zip_safe=False,
    packages=["formasaurus"],
    install_requires=[
        "docopt >= 0.4.0",
        "joblib >= 1.2.0",
        "lxml >= 4.5.2",
        "lxml-html-clean >= 0.1.0",
        "packaging >= 14.0",
        "parsel >= 1.1.0",
        "platformdirs >= 3.2.0",
        "requests >= 1.0.0",
        "scikit-learn >= 1.5.0",
        "scipy >= 1.6.2",
        "sklearn-crfsuite >= 0.5.0",
        "tldextract >= 1.2.0",
        "tqdm >= 2.0",
        "w3lib >= 1.13.0",
    ],
    package_data={
        "formasaurus": [
            "data/*.json",
            "data/html/*.html",
            "data/*.joblib",
        ],
    },
    extras_require={
        "annotation": [
            "ipython[notebook] >= 4.0",
            "ipywidgets",
            "Tornado>=4.0.0",
        ],
    },
    entry_points={"console_scripts": ["formasaurus = formasaurus.__main__:main"]},
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
