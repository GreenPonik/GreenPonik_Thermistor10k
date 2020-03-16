import time
from GreenPonik_thermistor_10k import GreenPonik_thermistor_10k


if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperatures = GreenPonik_thermistor_10k.read_temp()
        print("celcius temp %.3f" % temperatures[0])
        print("fahrenheit temp %.3f" % temperatures[1])
        time.sleep(1)
    pass
