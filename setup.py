#!/usr/bin/env python

try:
    from setuptools import setup
    extra = dict(install_requires=[
    ],
        include_package_data=True,
        test_suite="tests.suite.load_tests",
    )
except ImportError:
    from distutils.core import setup
    extra = {}


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name="onetimesecret",
      version="1.0.0",
      description="Share secrets with onetimesecret.com",
      long_description=readme(),
      author="Kevin Coakley",
      author_email="kcoakley@sdsc.edu",
      scripts=[
          "bin/onetimesecret-csv",
          "bin/onetimesecret-openstack",
          "bin/onetimesecret-userpass",
      ],
      url="",
      packages=[
          "onetimesecret",
          "onetimesecret/py_onetimesecret",
      ],
      platforms="Posix; MacOS X",
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
      **extra
      )
