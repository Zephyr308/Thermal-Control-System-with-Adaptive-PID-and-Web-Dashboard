# Thermal Control System with Adaptive PID

## Overview
This project implements a **robust industrial-grade thermal control system** using Raspberry Pi.  
It features:
- Adaptive PID control
- Scenario-based disturbances and failures
- Safety supervisor for fault handling
- Live web dashboard for remote monitoring
- Data logging with CSV export for reporting

## Features
- Real-time temperature control
- Adaptive PID tuning based on error magnitude
- Sensor/actuator fault simulation
- Live plotting and setpoint control via browser
- CSV logs for analysis and reports

## Hardware Requirements
- Raspberry Pi 3/4
- DS18B20 Temperature Sensor
- Heater controlled via PWM
- Optional: Relay or MOSFET for high-power heater

## Software Requirements
- Python 3.10+
- Dash, Plotly, numpy, matplotlib
- RPi.GPIO (for Raspberry Pi GPIO control)

## Folder Structure
# Thermal Control System with Adaptive PID

## Overview
This project implements a **robust industrial-grade thermal control system** using Raspberry Pi.  
It features:
- Adaptive PID control
- Scenario-based disturbances and failures
- Safety supervisor for fault handling
- Live web dashboard for remote monitoring
- Data logging with CSV export for reporting

## Features
- Real-time temperature control
- Adaptive PID tuning based on error magnitude
- Sensor/actuator fault simulation
- Live plotting and setpoint control via browser
- CSV logs for analysis and reports

## Hardware Requirements
- Raspberry Pi 3/4
- DS18B20 Temperature Sensor
- Heater controlled via PWM
- Optional: Relay or MOSFET for high-power heater

## Software Requirements
- Python 3.10+
- Dash, Plotly, numpy, matplotlib
- RPi.GPIO (for Raspberry Pi GPIO control)

## Folder Structure
```
thermal-control-system/
├── main.py
├── controller/
├── hardware/
├── supervisor/
├── scenarios/
├── utils/
├── web/
└── logs/
```


## Installation
1. Clone the repository:
```bash
git clone https://github.com/<username>/thermal-control-system.git
cd thermal-control-system
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Connect your sensor and heater to the Raspberry Pi GPIO.
2. Run the main control loop with web dashboard:
```
python main.py
```

## CSV Logs
All temperature, setpoint, and control signals are automatically logged in `logs/`.

## License

This project is licensed under MIT License.
