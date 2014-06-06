
import datetime
from nose.tools import assert_almost_equal, assert_equal

from .tidal_model import calculate_amplitude, to_hours, Constituent


def test_calculate_amplitude():
    test_data = [
        (-0.0873440613, 0, 187, 45, 0.088),
        (0.0235169771, 2.5, 187, 45, 0.088),
    ]

    for expected, time, phase, speed, amplitude in test_data:
        yield (_test_calculate_amplitude,
               expected,
               time,
               Constituent(
                   '', '',
                   phase=phase,
                   speed=speed,
                   amplitude=amplitude))


def _test_calculate_amplitude(expected_output, time, constituent):
    assert_almost_equal(
        expected_output,
        calculate_amplitude(time, constituent))


def test_to_hours():
    timedelta = datetime.timedelta(hours=3, minutes=45)
    assert_equal(3.75, to_hours(timedelta))
