# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import sys
from unittest.mock import patch, MagicMock


class BoardMock:
    def __init__(self):
        self._scl = 18
        self._sda = 15

    def SCL(self):
        return self._scl

    def SDA(self):
        return self._sda


class BusioMock(MagicMock()):
    def I2C(self, sda, scl):
        return True


sys.modules["board"] = BoardMock()
sys.modules["busio"] = BusioMock()


class Test_GreenPonik_thermistor_10k(unittest.TestCase):
    @patch("GreenPonik_thermistor_10k.GreenPonik_thermistor_10k.ReadThermistor10k")
    def test_read_temp(self, Mock):
        th = Mock()
        expected = 17.65
        th.readTemp.return_value = expected
        ecValue = th.readTemp()
        self.assertIsNotNone(self, ecValue)
        self.assertTrue(self, type(ecValue).__name__ == "float")


if __name__ == "__main__":
    unittest.main()
