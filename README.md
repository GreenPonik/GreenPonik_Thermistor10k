[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_thermistor_10k&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_thermistor_10k)

## GreenPonik_thermistor_10k.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read temperature with thermistor 10k sensor on i2c bus.


## Table of Contents

- [GreenPonik_thermistor_10k.py Library for Raspberry pi](#greenponikthermistor10kpy-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Example](#example)
- [Credits](#credits)
<snippet>
<content>

## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_thermistor_10k.git

or 

> pip install greenponik-thermistor-10k
```
```Python

from GreenPonik_thermistor_10k.GreenPonik_thermistor_10k import read_temp

```

## Methods

```python
"""
Get temperatue in celcius
"""
def read_temp():

```

## Example


```Python
import time
from GreenPonik_thermistor_10k.GreenPonik_thermistor_10k import read_temp


if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperature = .read_temp()
        print("celcius temp %.3f" % temperature)
        time.sleep(1)

```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2020
