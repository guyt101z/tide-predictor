# Tide Predictor

Creates minute-resolution tidal predictions based on given tidal constituents.

## Example command-line usage

```
tide-predictor --constituents two_constituents.json --start=2014-01-01 --end=2015-01-01
```

## Example library usage

```
>>> from datetime import datetime
>>> from tide_predictor import load_tidal_model

>>> model = load_tidal_model('1778000_apia_w_samoa.json')  # example data
>>> model.predict(datetime(2014, 5, 7, 18, 0)
10.764
```

## File format

For examples, see the `examples/` directory.

Fields:

- Epoch datetime: The moment from which all time measurements are taken. This
  point has a phase of zero. 

- Name: Common name used to refer to a particular constituent, subscript
  refers to the number of cycles per day

- Amplitude: One-half the range of a tidal constituent

- Phase: The phase lag of the observed tidal constituent relative to the
  theoretical equilibrium tide

- Speed: The rate change in the phase of a constituent, expressed in degrees
  per hour. The speed is equal to 360 degrees divided by the constituent
  period expressed in hours

- Description: The full name of the tidal constituent 

```json
{
  "time_datum": "2012-05-01T00:00:00T",
  "height_units": "metres",
  "constituents": [
  {
    "name": "Z0",
    "description": "Mean sea level above chart datum.",
    "amplitude": 3.6,
    "phase": 0.0,
    "speed": 0.0
  },
  {
    "name": "M2",
    "description": "Principal lunar semidiurnal constituent",
    "amplitude": 0.377,
    "phase": 212.1,
    "speed": 28.9841042
  },
  {
    "name": "S2",
    "description": "Principal solar semidiurnal constituent",
    "amplitude": 0.088,
    "phase": 187.0,
    "speed": 30.0
  }]
}
```
