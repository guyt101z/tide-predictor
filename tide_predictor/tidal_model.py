from __future__ import unicode_literals

import pytz
import math
from functools import partial

from dateutil.parser import parse as parse_datetime
from collections import namedtuple

Constituent = namedtuple(
    'Constituent', 'name,description,amplitude,phase,speed')


class TidalModel(object):
    def __init__(self, constituent_data):
        self.constituents = None
        self.time_datum = None

        self._parse(constituent_data)

    def predict(self, when):
        """
        Predict a tidal height at a given point in time.
        """
        assert when.tzinfo == pytz.UTC, 'datetime timezone must be UTC'
        t_hours = to_hours(when - self.time_datum)
        amplitudes = map(
            partial(calculate_amplitude, t_hours),
            self.constituents)
        return sum(amplitudes)

    def __unicode__(self):
        return '<TidalModel, {} constituents>'.format(len(self.constituents))

    def __str__(self):
        return self.__unicode__().encode('ascii')

    def _parse(self, data):
        assert data['height_units'] == 'metres'

        self.time_datum = parse_datetime(data['time_datum'])

        self.constituents = TidalModel._parse_constituents(
            data['constituents'])

    @staticmethod
    def _parse_constituents(constituents):
        return [Constituent(
                name=c['name'],
                description=c.get('description', ''),
                amplitude=float(c['amplitude']),
                phase=float(c['phase']),
                speed=float(c['speed'])) for c in constituents]


def to_hours(timedelta):
    return timedelta.total_seconds() / 3600


def calculate_amplitude(time_hours, constituent):

    angle = math.radians((constituent.speed * time_hours) - constituent.phase)
    return constituent.amplitude * math.cos(angle)
