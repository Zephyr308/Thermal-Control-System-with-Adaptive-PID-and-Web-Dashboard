class Supervisor:
    def __init__(self, max_temp=80):
        self.max_temp = max_temp

    def check(self, temp):
        if temp > self.max_temp or temp < -10:  # Sensor validation
            return False
        return True
