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
# import board
# import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import math


class ReadThermistor10k:

    def __init__(self, bus=None):
        # self._scl_pin = scl_pin if None is not scl_pin else board.SCL
        # self._sda_pin = sda_pin if None is not sda_pin else board.SDA
        self._bus = bus if None is not bus else self.DEFAULT_BUS

    @property
    def bus(self):
        return self._bus

    # @property
    # def scl_pin(self):
    #     return self._scl_pin

    # @property
    # def sda_pin(self):
    #     return self._sda_pin

    def read_temp(self):
        """
        @brief Read thermistor 10k temperature on raspberry pi i2c bus
        Get temperatue in celcius
        """
        try:
            # Create the I2C bus
            # i2c = busio.I2C(self._scl_pin, self._sda_pin)
            i2c = I2C(self._bus)
            # Create the ADS object
            ads = ADS.ADS1115(i2c)
            device_vcc = 5.0
            voltage = 0.0
            thermistor_25 = 10000
            ref_current = 0.0001
            # The ADS1015 and ADS1115 both have the same gain options.
            #
            #       GAIN    RANGE (V)
            #       ----    ---------
            #        2/3    +/- 6.144
            #          1    +/- 4.096
            #          2    +/- 2.048
            #          4    +/- 1.024
            #          8    +/- 0.512
            #         16    +/- 0.256
            #
            gains = (2 / 3, 1, 2, 4, 8, 16)
            ads.gain = gains[0]
            adc2 = AnalogIn(ads, ADS.P2)
            print("adc2 analog: %.3f" % adc2.value)
            voltage = adc2.value * (device_vcc / 65535)
            print("voltage: %.3f" % voltage)
            # Using Ohm's Law to calculate resistance of thermistor
            resistance = voltage / ref_current
            print("resistance: %.3f" % resistance)
            # Log of the ratio of thermistor resistance
            # and resistance at 25 deg. C
            ln = math.log(resistance / thermistor_25)
            print("ln: %.3f" % ln)
            # Using the Steinhart-Hart Thermistor
            # Equation to calculate temp in K
            kelvin = (
                1 / (0.0033540170 + (0.00025617244 * ln))
                + (0.0000021400943 * ln ** 2)
                + (-0.000000072405219 * ln ** 3)
            )
            print("kelvin: %.3f" % kelvin)
            temp = kelvin - 273.15  # Converting Kelvin to Celcius
            print("temperature: %.3f" % (temp))
            i2c.deinit()
            return temp
        except BaseException as e:
            print("cannot read water temperature")
            print("An exception occurred: {}".format(e))
