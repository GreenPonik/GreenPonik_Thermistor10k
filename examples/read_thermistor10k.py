import time
from GreenPonik_Thermistor10k.Thermistor10k import Thermistor10k


if __name__ == "__main__":
    th = Thermistor10k()
    while True:
        temperature = th.read_temp()
        print("celcius temp %.3f °c" % temperature)
        time.sleep(1)
