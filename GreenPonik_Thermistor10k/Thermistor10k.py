#! /usr/bin/env python3

"""
####################################################################
####################################################################
#################### GreenPonik_thermistor_10k #####################
################# Read temperature on thermistor 10k ###############
#################### with Python3 through i2c ######################
####################################################################
####################################################################
Description
-----------
GreenPonik Library for thermistor 10k use on WaterBrain
"""

from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import _ADS1X15_CONFIG_GAIN
import adafruit_ads1x15.ads1015 as ADS_1015
import adafruit_ads1x15.ads1115 as ADS_1115


class Thermistor10k:
    """
    @brief class Thermistor10k
    """

    DEFAULT_ADDR = 0x48
    DEFAULT_BUS = 1
    THERMISTOR_OFFSET = 2000

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

    # def slope_calculator(self, x_list, y_list):
    #     """
    #     slope m = DY/DX
    #     """
    #     slope = (y_list[1] - y_list[0]) / (x_list[1] - x_list[0])
    #     return slope

    # def intercept_calculator(self, slope, x, y):
    #     """
    #     b = y -mx
    #     """
    #     intercept = y - slope * x
    #     return intercept

    def steinhart_temperature_C(r, Ro=10000.0, To=25.0, beta=3950.0):
        """
        @brief steinhart formula for thermistor resistance conversion to celcius degrees
        """
        try:
            import math

            steinhart = math.log(r / Ro) / beta  # log(R/Ro) / beta
            steinhart += 1.0 / (To + 273.15)  # log(R/Ro) / beta + 1/To
            steinhart = (1.0 / steinhart) - 273.15  # Invert, convert to C
            return steinhart
        except Exception as e:
            print("An exception occurred in steinhart_temperature_C(): {}".format(e))

    def read_temp(self):
        """
        @brief Read thermistor 10k temperature on raspberry pi i2c bus
        Get temperatue in celcius
        """
        try:
            # init temp value to default error code (convension GreenPonik)
            temp = 9999.999
            with I2C(self._bus) as i2c:
                # DEPRECATED ####
                # """these points are determinated by lab test with both ec probe and manual thermometer"""
                # # x1 = 12272
                # # y1 = 25.9
                # # x2 = 10752
                # # y2 = 34.5

                # # SLOPE = self.slope_calculator([x1, x2], [y1, y2])
                # # INTERCEPT = self.intercept_calculator(SLOPE, x1, y1)

                # # if self._debug is True:
                # #     print("slope: ", SLOPE)
                # #     print("intercept: ", INTERCEPT)
                # DEPRECATED ####
                """The ADS1015 and ADS1115 both have the same gain options.
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
                value = adc2.value
                resistance = (10000 * value / (32767 - value)) - self.THERMISTOR_OFFSET

                temp = self.steinhart_temperature_C(resistance)

                # temp = (adc2.value * SLOPE) + INTERCEPT
                if self._debug is True:
                    print("adc2 analog: ", adc2.value)
                    print("adc2 voltage: ", adc2.voltage)
                    print("thermistor resistance: ", resistance)
                    print("Thermistor 10k temperature: %s" % (temp))

                # DEPRECATED ####
                # if adc2.value >= 17500 or adc2.voltage >= 3.25:
                #     return 9999.999  # return error code can allow user to know if thermistor doesn't connected
                # else:
                #     return temp
                # DEPRECATED ####
                return temp
        except Exception as e:
            print("An exception occurred in read_temp(): {}".format(e))
            pass
        finally:
            return temp
