class PID:
    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, u_min=0, u_max=100):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.u_min = u_min
        self.u_max = u_max
        self.integral = 0
        self.prev_error = 0

    def update(self, error, dt=1.0):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        u = self.Kp*error + self.Ki*self.integral + self.Kd*derivative

        # Saturation
        u = max(self.u_min, min(self.u_max, u))

        # Anti-windup
        if u == self.u_max or u == self.u_min:
            self.integral -= error * dt

        self.prev_error = error
        return u
