#!/usr/bin/env python
import sys

from setuptools import setup


def do_setup():
    setuptools_commands = set(['develop'])

    if setuptools_commands.intersection(sys.argv):

        extra_setuptools_args = dict(
            zip_safe=False,  # the package can run out of an .egg file
            include_package_data=True,
        )
    else:
        extra_setuptools_args = dict()

    setup(
        name='drimerpy',
        version='0.0.1',
        packages=['drimerpy'],
        license="BSD",
        description='Collection of random utility functions',
        author='Alberto Aguilera',
        author_email='drimer.aaj@gmail.com',
        url='https://github.com/drimer/drimerpy',
        keywords="utils",
        classifiers=[
            "Topic :: Utilities",
            "License :: BSD License",
        ],
        **extra_setuptools_args,
    )


if __name__ == '__main__':
    do_setup()
