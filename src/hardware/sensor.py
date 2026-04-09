import glob
import time

class TemperatureSensor:
    def __init__(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            with open(self.device_file, 'r') as f:
                lines = f.readlines()
        temp_string = lines[1].split('t=')[-1]
        return float(temp_string) / 1000.0
