# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import sys
from unittest.mock import patch


class SmbusMock():
    pass


class FCNTLMock:
    def __init__(self):
        pass

    def ioctl(self):
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


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
