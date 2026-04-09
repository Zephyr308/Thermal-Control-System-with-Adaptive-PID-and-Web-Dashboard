import random

class ScenarioManager:
    def __init__(self):
        self.time = 0

    def update_time(self, dt):
        self.time += dt

    def inject_disturbance(self, temp):
        """
        Add environmental disturbance (like sudden cooling/heating)
        """
        if 20 < self.time < 30:  # seconds
            temp -= 5  # sudden cooling
        if 50 < self.time < 55:
            temp += 3  # sudden heating
        return temp

    def simulate_failure(self, temp, control):
        """
        Randomly simulate sensor or actuator failure
        """
        # Sensor spike
        if 35 < self.time < 36:
            temp += 50
        # Actuator stuck
        if 70 < self.time < 72:
            control = 0
        return temp, control
