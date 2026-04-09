import matplotlib.pyplot as plt
from collections import deque

class Dashboard:
    def __init__(self, max_len=100):
        self.time_data = deque(maxlen=max_len)
        self.temp_data = deque(maxlen=max_len)
        self.setpoint_data = deque(maxlen=max_len)
        self.control_data = deque(maxlen=max_len)
        plt.ion()
        self.fig, (self.ax1, self.ax2) = plt.subplots(2,1, figsize=(8,6))
        self.line_temp, = self.ax1.plot([], [], label="Temp")
        self.line_set, = self.ax1.plot([], [], 'r--', label="Setpoint")
        self.line_control, = self.ax2.plot([], [], label="Control")
        self.ax1.legend(); self.ax1.grid()
        self.ax2.legend(); self.ax2.grid()
        self.ax2.set_xlabel("Time (s)")

    def update(self, t, temp, setpoint, control):
        self.time_data.append(t)
        self.temp_data.append(temp)
        self.setpoint_data.append(setpoint)
        self.control_data.append(control)

        self.line_temp.set_data(self.time_data, self.temp_data)
        self.line_set.set_data(self.time_data, self.setpoint_data)
        self.line_control.set_data(self.time_data, self.control_data)

        self.ax1.relim(); self.ax1.autoscale_view()
        self.ax2.relim(); self.ax2.autoscale_view()
        plt.pause(0.01)
