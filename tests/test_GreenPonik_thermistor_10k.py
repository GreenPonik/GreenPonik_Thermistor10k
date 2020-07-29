# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from GreenPonik_thermistor_10k.GreenPonik_thermistor_10k import read_temp


class TestGreenPonik_thermistor_10k(unittest.TestCase):
    def test_read_temps(self):
        self.assertTrue(self, type(read_temp()).__name__ == "list")


if __name__ == "__main__":
    unittest.main()
