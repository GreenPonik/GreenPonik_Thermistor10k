#! /usr/bin/env python3

"""
####################################################################
####################################################################
#################### GreenPonik_thermistor_10k #####################
################# Read temperature on thermistor 10k ###############
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
import math


class Thermistor10k:

    DEFAULT_ADDR = 0x48
    DEFAULT_BUS = 1

    def __init__(self, bus=DEFAULT_BUS, addr=DEFAULT_ADDR):
        self._bus = bus
        self._addr = addr
        self._debug = False

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    @property
    def bus(self):
        return self._bus

    @property
    def address(self):
        return self._addr

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, d):
        self._debug = d

    def read_temp(self):
        """
        @brief Read thermistor 10k temperature on raspberry pi i2c bus
        Get temperatue in celcius
        """
        try:
            with I2C(self._bus) as i2c:
                device_vcc = 5.0
                voltage = 0.0
                thermistor_25 = 10000
                ref_current = 0.0001

                """ The ADS1015 and ADS1115 both have the same gain options.
                       GAIN    RANGE (V)
                       ----    ---------
                        2/3    +/- 6.144
                          1    +/- 4.096
                          2    +/- 2.048
                          4    +/- 1.024
                          8    +/- 0.512
                         16    +/- 0.256
                """
                gains = (2 / 3, 1, 2, 4, 8, 16)
                # Create the ADS object
                ads = ADS.ADS1115(
                    i2c,
                    gain=gains[0],
                    data_rate=None,
                    mode=Mode.SINGLE,
                    address=self._addr,
                )
                adc2 = AnalogIn(ads, ADS.P2)
                voltage = adc2.value * (device_vcc / 65535)
                # Using Ohm's Law to calculate resistance of thermistor
                resistance = voltage / ref_current
                # Log of the ratio of thermistor resistance
                # and resistance at 25 deg. C
                ln = math.log(resistance / thermistor_25)
                # Using the Steinhart-Hart Thermistor
                # Equation to calculate temp in K
                kelvin = (
                    1 / (0.0033540170 + (0.00025617244 * ln))
                    + (0.0000021400943 * ln ** 2)
                    + (-0.000000072405219 * ln ** 3)
                )
                temp = kelvin - 273.15  # Converting Kelvin to Celcius
                if self._debug:
                    print("adc2 analog: %.3f" % adc2.value)
                    print("voltage: %.3f" % voltage)
                    print("resistance: %.3f" % resistance)
                    print("ln: %.3f" % ln)
                    print("kelvin: %.3f" % kelvin)
                    print("Thermistor 10k temperature: %.3f" % (temp))
                return temp
        except Exception as e:
            print("cannot read water temperature, An exception occurred: {}".format(e))
