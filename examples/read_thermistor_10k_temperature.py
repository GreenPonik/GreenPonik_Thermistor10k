import time
from GreenPonik_thermistor_10k import ReadThermistor10k


if __name__ == "__main__":
    th = ReadThermistor10k()
    while True:
        temperature = th.read_temp()
        print("celcius temp %.3f °c" % temperature)
        time.sleep(1)
