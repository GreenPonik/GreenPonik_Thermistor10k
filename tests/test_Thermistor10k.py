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
        th.readTemp.return_value = expected
        ec_value = th.readTemp()
        self.assertIsNotNone(self, ec_value)
        self.assertTrue(self, type(ec_value).__name__ == "float")


if __name__ == "__main__":
    unittest.main()
