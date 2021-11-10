[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_Thermistor10k&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_Thermistor10k)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_Thermistor10k/workflows/Upload%20Python%20Package/badge.svg?event=release)
![Python package](https://github.com/GreenPonik/GreenPonik_Thermistor10k/workflows/Python%20package/badge.svg?event=push)


## GreenPonik_Thermistor10k.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read temperature with thermistor 10k sensor on i2c bus.


## Table of Contents

- [GreenPonik_Thermistor10k.py Library for Raspberry pi](#greenponikthermistor10kpy-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Dev workflow](#dev-workflow)
- [Installation](#installation)
- [Methods](#methods)
- [Example](#example)
- [Credits](#credits)

## Dev workflow
create python virtual environnement
```shell
python3 -m venv venv
```
activate venv linux
```shell
source venv/bin/activate
```
activate venv windows
```
venv\Scripts\activate
```
install dependencies
```shell
pip install -r requirements.txt
```
build the documentation
```shell

```

## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_Thermistor10k.git
cd GreenPonik_Thermistor10k
pip3 install -r requirements.txt

or 

> pip install greenponik-thermistor10k
```
```Python

from GreenPonik_Thermistor10k.Thermistor10k import Thermistor10k

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
from GreenPonik_Thermistor10k.Thermistor10k import Thermistor10k


if __name__ == "__main__":
    th = Thermistor10k()
    while True:
        temperature = th.read_temp()
        print("celcius temp %.3f °c" % temperature)
        time.sleep(1)

```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2020
