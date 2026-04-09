from controller.pid import PID

class AdaptivePID(PID):
    def update_gains(self, error):
        # Simple gain scheduling based on error magnitude
        if abs(error) > 10:
            self.Kp, self.Ki, self.Kd = 3.5, 0.6, 1.2
        elif abs(error) < 2:
            self.Kp, self.Ki, self.Kd = 1.5, 0.3, 0.8
        else:
            self.Kp, self.Ki, self.Kd = 2.5, 0.4, 1.0

    def update(self, error, dt=1.0):
        self.update_gains(error)
        return super().update(error, dt)
