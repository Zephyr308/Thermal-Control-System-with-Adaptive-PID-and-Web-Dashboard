import csv
import os
from datetime import datetime

class DataLogger:
    def __init__(self, folder="logs"):
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = os.path.join(folder, f"session_{timestamp}.csv")
        self.fields = ["time", "temperature", "setpoint", "control"]
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()

    def log(self, t, temp, setpoint, control):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writerow({
                "time": f"{t:.2f}",
                "temperature": f"{temp:.2f}",
                "setpoint": f"{setpoint:.2f}",
                "control": f"{control:.2f}"
            })
