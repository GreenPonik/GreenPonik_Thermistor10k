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

    def __init__(self, bus=DEFAULT_BUS, addr=DEFAULT_ADDR):
        self._bus = bus
        self._addr = addr
        self._debug = False
        self._gains = [g for g in _ADS1X15_CONFIG_GAIN.keys()]
        self._gain = self._gains[1]  # defautl gain to 1: 512 => 4.096V
        self._i2c = I2C(self._bus)
        self._ads = ADS_1115.ADS1115(
            i2c=self._i2c, gain=self._gain, address=self._addr
        )  # Create the ADS object # ads = ADS_1015.ADS1015()
        self._ads_chan_selector = ADS_1115.P2
        self._ads_chan = AnalogIn(self._ads, self._ads_chan_selector)  # AnalogIn(ads, ADS_1015.P2)

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    @property
    def i2c(self):
        return self._i2c

    @property
    def ads_instance(self):
        return self._ads

    @property
    def ads_channel_selector(self):
        return self._ads_chan_selector

    @ads_channel_selector.setter
    def ads_channel_selector(self, c):
        assert(c in [ADS_1115.P0, ADS_1115.P1, ADS_1115.P2, ADS_1115.P3])
        self._ads_chan_selector = c

    @property
    def ads_channel_read(self):
        return self._ads_chan

    @property
    def bus(self):
        return self._bus

    @bus.setter
    def bus(self, b):
        self._bus = b

    @property
    def address(self):
        return self._addr

    @address.setter
    def address(self, a):
        self._addr = a

    @property
    def gains(self):
        return self._gains

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, g):
        assert(g in self._gains)
        self._gain = g

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, d):
        self._debug = d

    def steinhart_temperature(self, r, ro=10000.0, to=25.0, beta=3950.0):
        """
        @brief steinhart formula for thermistor resistance conversion to celcius degrees
        parameters:
        r is thermistor calculated resistance
        ro is thermistor resistance @25°c
        beta is thermistor coefficient from data sheet
        """
        try:
            import math

            steinhart = math.log(r / ro) / beta  # log(R/Ro) / beta
            steinhart += 1.0 / (to + 273.15)  # log(R/Ro) / beta + 1/To
            steinhart = (1.0 / steinhart) - 273.15  # Invert, convert to C
            return steinhart
        except Exception as e:
            print("An exception occurred in steinhart_temperature(): {}".format(e))

    def read_temp(self):
        """
        @brief Read thermistor 10k temperature on raspberry pi i2c bus
        Get temperatue in celcius
        """
        # init temp value to default error code (convension GreenPonik)
        temp = 9999.999
        try:
            adc_channel = self._ads_chan
            value = adc_channel.value
            resistance = (10000 * value / (32767 - value)) - self.THERMISTOR_OFFSET

            temp = self.steinhart_temperature(resistance)

            if self._debug is True:
                print("adc2 analog: ", adc_channel.value)
                print("adc2 voltage: ", adc_channel.voltage)
                print("thermistor resistance: ", resistance)
                print("Thermistor 10k temperature: %s" % (temp))

            if temp >= 100 or temp <= 0:
                return 9999.999
            else:
                return temp
        except Exception as e:
            print("An exception occurred in read_temp(): {}".format(e))
