#!/usr/bin/env python
# encoding: utf-8

"""
Tide predictor: generate tidal predictions from harmonic constituents.


Usage:
    tide-predictor --constituents=<file.json> [--start=<datetime>]
                   [--end=<datetime>]
    tide-predictor -h | --help
    tide-predictor --version

Options:
    --start=<start> Date/time of when to start, eg 2014-01-01T00:00:00T
    --end=<end>     Date/time of when to end, eg 2014-01-01T00:00:00T
"""

from __future__ import unicode_literals

import datetime

import pytz

from dateutil.parser import parse as parse_datetime
from docopt import docopt

from .tide_predictor import load_tidal_model


def main():
    from __init__ import __version__
    arguments = docopt(
        __doc__, version='tide-predictor {}'.format(__version__))

    constituents, start_datetime, end_datetime = _parse_args(arguments)
    model = load_tidal_model(constituents)

    for dt in _generate_minute_intervals(start_datetime, end_datetime):
        print('{},{:.2f}'.format(dt.isoformat(), model.predict(dt)))


def _parse_args(arguments):
    if arguments['--start'] is not None:
        start_datetime = _make_utc(parse_datetime(arguments['--start']))
    else:
        start_datetime = datetime.datetime.now(pytz.UTC).replace(
            second=0, microsecond=0)

    if arguments['--end'] is not None:
        end_datetime = _make_utc(parse_datetime(arguments['--end']))
    else:
        end_datetime = start_datetime + datetime.timedelta(minutes=30)
    return arguments['--constituents'], start_datetime, end_datetime


def _make_utc(dt):
    if dt.tzinfo is None:  # naive - no timezone. assume UTC.
        return dt.replace(tzinfo=pytz.UTC)
    else:
        return dt.astimezone(pytz.UTC)


def _generate_minute_intervals(start, end):
    delta = end - start
    minutes = _count_minutes(delta)
    for minute_offset in range(minutes):
        yield start + datetime.timedelta(minutes=minute_offset)


def _count_minutes(timedelta):
    return (timedelta.days * 24 * 60) + (timedelta.seconds / 60)
