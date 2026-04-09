import time
import threading
from collections import deque
from controller.adaptive import AdaptivePID
from hardware.sensor import TemperatureSensor
from hardware.actuator import Heater
from supervisor.safety import Supervisor
from utils.filters import MovingAverage
from utils.logger import DataLogger
from scenarios.simulation import ScenarioManager
from web.app import app, time_data, temp_data, setpoint_data, control_data, current_setpoint

# Initialize modules
sensor = TemperatureSensor()
heater = Heater()
pid = AdaptivePID()
supervisor = Supervisor()
filter_temp = MovingAverage()
logger = DataLogger()
scenario = ScenarioManager()

dt = 1.0
start_time = time.time()

# Control loop in separate thread
def control_loop():
    global current_setpoint
    while True:
        t_now = time.time() - start_time
        scenario.update_time(dt)

        # Read sensor + filter
        temp_raw = sensor.read()
        temp = filter_temp.filter(temp_raw)

        # Inject disturbances & simulate failures
        temp = scenario.inject_disturbance(temp)
        control = 0
        temp, control = scenario.simulate_failure(temp, control)

        # Safety
        if not supervisor.check(temp):
            heater.set_output(0)
            print("SAFETY STOP!")
            break

        # PID
        error = current_setpoint - temp
        control = pid.update(error, dt)
        heater.set_output(control)

        # Update dashboard shared variables
        time_data.append(t_now)
        temp_data.append(temp)
        setpoint_data.append(current_setpoint)
        control_data.append(control)

        # Log CSV
        logger.log(t_now, temp, current_setpoint, control)

        print(f"T={temp:.2f}°C | U={control:.1f}%")
        time.sleep(dt)

# Start control thread
threading.Thread(target=control_loop, daemon=True).start()

# Start web server
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)
