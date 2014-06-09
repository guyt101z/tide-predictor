# encoding: utf-8

from distutils.core import setup

import codecs
import os
import re


def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    here = os.path.abspath(os.path.dirname(__file__))

    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='tide_predictor',
    version=find_version('tide_predictor', '__init__.py'),
    description='Predict tidal heights using harmonic constituents.',
    author='Sea Level Reseach Ltd',
    author_email='hello@sealevelresearch.com',
    url='https://github.com/sealevelresearch/tide-predictor',
    install_requires=['docopt', 'pytz'],
    packages=['tide_predictor'],
    data_files={
        'examples': ['examples/*.json'],
    },
    entry_points={
        'console_scripts': [
            'tide-predictor=tide_predictor:main',
        ],
    },
)
