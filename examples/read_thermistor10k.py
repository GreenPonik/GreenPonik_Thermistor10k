import time
from GreenPonik_Thermistor10k.Thermistor10k import Thermistor10k


if __name__ == "__main__":
    try:
        th = Thermistor10k()
        th.debug = True  # used for debug
        while True:
            temperature = th.read_temp()
            print("celcius temp %.3f °c" % temperature)
            time.sleep(1)
    except Exception as e:
        print("oops there is an exception {}".format(e))
