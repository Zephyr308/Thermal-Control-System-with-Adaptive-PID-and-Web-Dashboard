import time
from controller.adaptive import AdaptivePID
from hardware.sensor import TemperatureSensor
from hardware.actuator import Heater
from supervisor.safety import Supervisor
from utils.filters import MovingAverage
from ui.dashboard import Dashboard
from utils.logger import DataLogger
from scenarios.simulation import ScenarioManager

# Initialize modules
sensor = TemperatureSensor()
heater = Heater()
pid = AdaptivePID()
supervisor = Supervisor()
filter_temp = MovingAverage()
dashboard = Dashboard()
logger = DataLogger()
scenario = ScenarioManager()

setpoint = 50
dt = 1.0
start_time = time.time()

try:
    while True:
        t_now = time.time() - start_time
        scenario.update_time(dt)

        # Read sensor + filter
        temp_raw = sensor.read()
        temp = filter_temp.filter(temp_raw)

        # Inject disturbances & simulate failures
        temp = scenario.inject_disturbance(temp)
        control = 0  # initial placeholder
        temp, control = scenario.simulate_failure(temp, control)

        # Safety check
        if not supervisor.check(temp):
            heater.set_output(0)
            print("SAFETY STOP!")
            break

        # PID update (adaptive)
        error = setpoint - temp
        control = pid.update(error, dt)
        heater.set_output(control)

        # Update dashboard
        dashboard.update(t_now, temp, setpoint, control)

        # Log data
        logger.log(t_now, temp, setpoint, control)

        print(f"T={temp:.2f}°C | U={control:.1f}%")
        time.sleep(dt)

except KeyboardInterrupt:
    heater.stop()
