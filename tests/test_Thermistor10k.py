# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import sys
from unittest.mock import patch


class SmbusMock():
    # simultate the smbus method just for tests
    pass


class FCNTLMock:
    def ioctl(self):
        # simultate the FCNTL.ioctl method just for tests
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class TestThermistor10k(unittest.TestCase):
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
