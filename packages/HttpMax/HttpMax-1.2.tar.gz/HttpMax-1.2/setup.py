#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of HttpMax requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)

requires = [
    'certifi',
    'httpcore>=0.15.0,<0.18.0',
    'idna',
    'sniffio',
]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "HttpMax", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["HttpMax"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"HttpMax": "HttpMax"},
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    extras_require={
        'brotli': [
            'brotli; platform_python_implementation == \'CPython\'',
            'brotlicffi; platform_python_implementation != \'CPython\'',
            ],
        'cli': [
            'click==8.*',
            'pygments==2.*',
            'rich>=10,<14',
            ],
        'http2': ['h2>=3,<5'],
        'socks': ['socksio==1.*']
    },
    project_urls={
        "Documentation": "https://github.com/shayanheidari01/HttpMax",
        "Source": "https://github.com/shayanheidari01/HttpMax",
    },
)