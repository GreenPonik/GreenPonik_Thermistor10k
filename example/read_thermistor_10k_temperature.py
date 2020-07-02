import time
from GreenPonik_thermistor_10k import GreenPonik_thermistor_10k


if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperature = GreenPonik_thermistor_10k.read_temp()
        print("celcius temp %.3f" % temperature)
        time.sleep(1)
