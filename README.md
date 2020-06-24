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
```
```Python

from GreenPonik_thermistor_10k import GreenPonik_thermistor_10k

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
from GreenPonik_thermistor_10k import GreenPonik_thermistor_10k

if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperature = GreenPonik_thermistor_10k.read_temp()
        print("celcius temp %.3f" % temperature)
        time.sleep(1)
    pass

```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2020
