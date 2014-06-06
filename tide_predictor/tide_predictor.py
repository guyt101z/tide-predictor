from __future__ import unicode_literals

import json

from os.path import abspath, dirname, isfile, join as pjoin

from .tidal_model import TidalModel


def load_tidal_model(json_filename):
    filename = _find_file(json_filename)
    with open(filename, 'r') as f:
        data = json.loads(f.read())
        return TidalModel(data)


def _find_file(filename):
    filename = (_find_in_filesystem(filename)
                or _find_in_example_data(filename))
    if filename is None:
        raise RuntimeError("Failed to open: '{}'".format(filename))
    return filename


def _find_in_filesystem(filename):
    if isfile(filename):
        return filename


def _find_in_example_data(filename):
    example_dir = pjoin(abspath(dirname(__file__)), '..', 'examples')
    example_filename = pjoin(example_dir, filename)
    if isfile(example_filename):
        return example_filename
