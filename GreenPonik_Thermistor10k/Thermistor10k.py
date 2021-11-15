#! /usr/bin/env python3

"""
Description
-----------
GreenPonik_thermistor_10k Read temperature on thermistor 10k\
with Python3 through i2c
"""

from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import _ADS1X15_CONFIG_GAIN
import adafruit_ads1x15.ads1015 as ADS_1015
import adafruit_ads1x15.ads1115 as ADS_1115


class Thermistor10k:
    """Thermistor10k"""

    DEFAULT_ADDR = 0x48
    DEFAULT_BUS = 1
    THERMISTOR_OFFSET = 2000

    def __init__(self, bus=DEFAULT_BUS, addr=DEFAULT_ADDR):
        """constructor method"""
        self._bus = bus
        self._addr = addr
        self._debug = False
        self._gains = [g for g in _ADS1X15_CONFIG_GAIN.keys()]

        # The ADS1015 and ADS1115 both have the same gain options.
        # GAIN    RANGE (V)
        # ----    ---------
        # 2/3    +/- 6.144
        # 1    +/- 4.096
        # 2    +/- 2.048
        # 4    +/- 1.024
        # 8    +/- 0.512
        # 16    +/- 0.256

        self._gain = self._gains[1]  # defautl gain to 1: 512 => 4.096V
        self._i2c = I2C(self._bus)
        self._ads = ADS_1115.ADS1115(
            i2c=self._i2c, gain=self._gain, address=self._addr
        )  # Create the ADS object # ads = ADS_1015.ADS1015()
        self._ads_chan_selector = ADS_1115.P2
        self._ads_chan = AnalogIn(
            self._ads, self._ads_chan_selector
        )  # AnalogIn(ads, ADS_1015.P2)

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
        """getter i2c bus instance

        Returns:
            ExtendedI2C: i2c bus instance
        """
        return self._i2c

    @property
    def ads_instance(self):
        """getter ads instance

        Returns:
            ADS_1115: ads instance
        """
        return self._ads

    @property
    def ads_channel_selector(self):
        """getter channel of the ADS

        Returns:
            Int: Number of the channel
        """
        return self._ads_chan_selector

    @ads_channel_selector.setter
    def ads_channel_selector(self, c):
        """getter channel of the ADS

        Args:
            c (int): [channel of ADS_1115]
        """
        assert c in [ADS_1115.P0, ADS_1115.P1, ADS_1115.P2, ADS_1115.P3]
        self._ads_chan_selector = c

    @property
    def ads_channel_read(self):
        """getter reads from ads channel selected

        Returns:
            int: analog value from 0 to 32767
        """
        return self._ads_chan

    @property
    def bus(self):
        """getter i2c bus number currently used

        Returns:
            int: the i2c bus number
        """
        return self._bus

    @bus.setter
    def bus(self, b):
        """[summary]

        Args:
            b ([type]): [description]
        """
        self._bus = b

    @property
    def address(self):
        """getter i2c address of the device

        Returns:
            int: i2c address of the device on the i2c bus
        """
        return self._addr

    @address.setter
    def address(self, a):
        """setter i2c address of the device

        Args:
            a (int): the new i2c address on the i2c bus
        """
        self._addr = a

    @property
    def gains(self):
        """getter gains

        Returns:
            list: list of possible gain available on the ADS
        """
        return self._gains

    @property
    def gain(self):
        """gain

        :return: get the current used gain on ADS
        :rtype: int
        """
        return self._gain

    @gain.setter
    def gain(self, g):
        """setter gain

        :param g: the new gain to be setted from self.gains list
        :type g: int
        """
        assert g in self._gains
        self._gain = g

    @property
    def debug(self):
        """debug property

        :getter: debug flag
        :setter: change debug flag

        Returns:
            bool: `True` if the debug mode is ON, `False` if not
        """
        return self._debug

    @debug.setter
    def debug(self, d: bool) -> None:
        """setter debug flag

        Args:
            d (bool): `True` to set debug mode ON, `False` to set debug mode OFF
        """
        self._debug = d

    def _steinhart_temperature(self, r, ro=10000.0, to=25.0, beta=3950.0):
        """steinhart formula for thermistor resistance conversion to celcius degrees

        :param r: thermistor calculated resistance
        :param ro: thermistor resistance @25°c
        :param beta: thermistor coefficient from data sheet
        :raises: Exception: Global Exception
        :return: Steinhart temperature
        :rtype: float
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
        """Read thermistor 10k temperature on raspberry pi i2c bus\
            Get temperatue in celcius

        :raises: Exception: Global Exception
        :return: Temperature from Thermistor 10k
        :rtype: float
        """
        # init temp value to default error code (convension GreenPonik)
        temp = 9999.999
        try:
            adc_channel = self._ads_chan
            value = adc_channel.value
            resistance = (10000 * value / (32767 - value)) - self.THERMISTOR_OFFSET

            temp = self._steinhart_temperature(resistance)

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
