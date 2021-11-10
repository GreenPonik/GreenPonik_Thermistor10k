# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import sys
from unittest.mock import patch
# from functools import wraps

# PRINT_ON = True


# def toggle_print(p):
#     global PRINT_ON
#     PRINT_ON = p


# def printf(f):
#     @wraps(f)
#     def wrapped(*args, **kwargs):
#         r = f(*args, **kwargs)

#         if len(args):
#             c = str(args[0].__class__).split("'")[1]  # grab self from the class method
#         else:
#             c = ""  # no class

#         if PRINT_ON:
#             if r:
#                 print("{}.{}{}: {}".format(c, f.__name__, args[1:], r))
#             else:
#                 print("{}.{}{}".format(c, f.__name__, args[1:]))
#         return r

#     return wrapped


# class Base(object):
#     def __init__(self, name=None):
#         print("<<< WARNING: using fake waterbrain >>>")
#         if name:
#             print("<<< Using: {} >>>".format(name))


class SmbusMock():
    # simultate the smbus class just for tests
    pass


class FcntlMock():
    # simultate the fcntl class just for tests
    def ioctl(self):
        # simultate the FCNTL.ioctl method just for tests
        pass


class AdafruitExtendedBusMock:
    # simultate the adafruit_extended_bus class just for tests
    def init():
        pass

    class ExtendedI2C():
        # simultate the ExtendedI2C class just for tests
        # @printf
        # def __init__(self, bus_id=1, frequency=0):
        # Base.__init__(self, self.__class__)
        # pass

        pass

    pass


sys.modules["fcntl"] = FcntlMock()
sys.modules["smbus"] = SmbusMock()
sys.modules["adafruit_extended_bus"] = AdafruitExtendedBusMock()


class TestThermistor10k(unittest.TestCase):
    @patch("adafruit_extended_bus.ExtendedI2C")
    def test_properies(self, mock_i2c):
        from adafruit_ads1x15.ads1x15 import _ADS1X15_CONFIG_GAIN

        fixtures = {
            "bus": 1,
            "gain": [g for g in _ADS1X15_CONFIG_GAIN.keys()][1],
            "address": 12,
            "debug": True,
            "ads_channel_selector": 2,
        }
        from GreenPonik_Thermistor10k.Thermistor10k import Thermistor10k
        th = Thermistor10k()

        th.bus = fixtures["bus"]
        th.gain = fixtures["gain"]
        th.address = fixtures["address"]
        th.debug = fixtures["debug"]
        th.ads_channel_selector = fixtures["ads_channel_selector"]

        self.assertIsNotNone(th.bus)
        self.assertIsNotNone(th.gain)
        self.assertIsNotNone(th.address)
        self.assertIsNotNone(th.debug)
        self.assertIsNotNone(th.ads_channel_selector)
        self.assertTrue(th.bus, fixtures["bus"])
        self.assertTrue(th.gain, fixtures["gain"])
        self.assertTrue(th.address, fixtures["address"])
        self.assertTrue(th.debug, fixtures["debug"])
        self.assertTrue(th.ads_channel_selector, fixtures["ads_channel_selector"])

    @patch("GreenPonik_Thermistor10k.Thermistor10k.Thermistor10k")
    def test_read_temp(self, mock_th):
        th = mock_th()
        expected = 17.65
        th.read_temp.return_value = expected
        ec_value = th.read_temp()
        self.assertIsNotNone(self, ec_value)
        self.assertTrue(self, isinstance(ec_value, float))
        self.assertTrue(self, ec_value == expected)

    @patch("GreenPonik_Thermistor10k.Thermistor10k.Thermistor10k")
    def test_read_temp_return_error(self, mock_th):
        th = mock_th()
        expected = 9999.999
        th.read_temp.return_value = expected
        ec_value = th.read_temp()
        self.assertIsNotNone(self, ec_value)
        self.assertTrue(self, isinstance(ec_value, float))
        self.assertTrue(self, ec_value == expected)


if __name__ == "__main__":
    unittest.main()
