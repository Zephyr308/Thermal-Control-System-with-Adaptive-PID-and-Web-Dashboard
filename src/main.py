import time
from controller.adaptive import AdaptivePID
from hardware.sensor import TemperatureSensor
from hardware.actuator import Heater
from supervisor.safety import Supervisor
from utils.filters import MovingAverage
from ui.dashboard import Dashboard

# Initialize modules
sensor = TemperatureSensor()
heater = Heater()
pid = AdaptivePID()
supervisor = Supervisor()
filter_temp = MovingAverage()
dashboard = Dashboard()

setpoint = 50
dt = 1.0
start_time = time.time()

try:
    while True:
        t_now = time.time() - start_time
        temp_raw = sensor.read()
        temp = filter_temp.filter(temp_raw)

        # Safety check
        if not supervisor.check(temp):
            heater.set_output(0)
            print("SAFETY STOP!")
            break

        error = setpoint - temp
        control = pid.update(error, dt)
        heater.set_output(control)

        dashboard.update(t_now, temp, setpoint, control)
        print(f"T={temp:.2f}°C | U={control:.1f}%")
        time.sleep(dt)

except KeyboardInterrupt:
    heater.stop()
