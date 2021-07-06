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
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import _ADS1X15_CONFIG_GAIN
import adafruit_ads1x15.ads1015 as ADS_1015
import adafruit_ads1x15.ads1115 as ADS_1115


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

    def slope_calculator(self, x_list, y_list):
        """
        slope m = DY/DX
        """
        slope = (y_list[1] - y_list[0]) / (x_list[1] - x_list[0])
        print("slope: %.3f" % slope)
        return slope

    def intercept_calculator(self, slope, x, y):
        """
        b = y -mx
        """
        intercept = y - slope * x
        print("intercept: %.3f" % intercept)
        return intercept

    def read_temp(self):
        """
        @brief Read thermistor 10k temperature on raspberry pi i2c bus
        Get temperatue in celcius
        """
        try:
            with I2C(self._bus) as i2c:
                """these points are determinated by lab test with both ec probe and manual thermometer"""
                x1 = 12272
                y1 = 25.9
                x2 = 10752
                y2 = 34.5

                SLOPE = self.slope_calculator([x1, x2], [y1, y2])
                INTERCEPT = self.intercept_calculator(SLOPE, x1, y1)

                if self.debug:
                    print("slope: ", SLOPE)
                    print("intercept: ", INTERCEPT)
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
                gains = [g for g in _ADS1X15_CONFIG_GAIN.keys()]
                # Create the ADS object
                # ads = ADS_1015.ADS1015(
                ads = ADS_1115.ADS1115(
                    i2c,
                    gain=gains[0],
                    address=self._addr,
                )
                # adc2 = AnalogIn(ads, ADS_1015.P2)
                adc2 = AnalogIn(ads, ADS_1115.P2)
                temp = (adc2.value * SLOPE) + INTERCEPT
                if self._debug:
                    print("adc2 analog: ", adc2.value)
                    print("adc2 voltage: ", adc2.voltage)
                    print("Thermistor 10k temperature: %.3f" % (temp))
                return temp
        except Exception as e:
            print("cannot read water temperature, An exception occurred: {}".format(e))
