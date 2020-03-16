## GreenPonik_thermistor_10k.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read temperature with thermistor 10k sensor on i2c bus.


## Table of Contents

- [## GreenPonik_thermistor_10k.py Library for Raspberry pi](#h2-id%22greenponikthermistor10kpy-library-for-raspberry-pi-68%22greenponikthermistor10kpy-library-for-raspberry-pih2)
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
def read_temps():

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
Writter by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019