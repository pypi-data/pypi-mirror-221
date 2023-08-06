# PyIono
[![ETH]( https://gitlab.ethz.ch/space-geodesy-open/pyiono/-/jobs/artifacts/master/raw/developer.svg?job=create_badges)](https://space.igp.ethz.ch/) [![TAG]( https://gitlab.ethz.ch/space-geodesy-open/pyiono/-/jobs/artifacts/master/raw/tag.svg?job=create_badges)](https://gitlab.ethz.ch/space-geodesy-open/pyiono/) [![pipeline status](https://gitlab.ethz.ch/space-geodesy-open/pyiono/badges/master/pipeline.svg)](https://gitlab.ethz.ch/space-geodesy-open/pyiono/-/pipelines)

Ionosphere-related processing based on the data from space-geodetic techniques:

- **geodetic very-long-baseline-interferometry (VLBI)**: legacy VLBI system
- **VLBI Global Observing System (VGOS)**: the next-generation VLBI system
- **Global Navigation Satellite System (GNSS)**: currently based on the custom TEC files with satellite-specific STEC values


## Installation

You can install PyIono from [PyPI](https://pypi.org/project/pyiono/):

    python3 -m pip install pyiono

PyIono is supported on Python 3.9 and above.

## How to use


PyIono is a command line application, named `pyiono`. To see a list of the arguments, call the program without any arguments:

```bash
$ pyiono
```

You can also call PyIono in your own Python code, by importing from the `pyiono` package:

```python
 from pyiono.math import square
 square(2)
```