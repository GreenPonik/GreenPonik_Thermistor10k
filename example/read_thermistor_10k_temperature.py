import time
from GreenPonik_thermistor_10k.GreenPonik_thermistor_10k import read_temp


if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperature = .read_temp()
        print("celcius temp %.3f" % temperature)
        time.sleep(1)
