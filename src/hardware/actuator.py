import RPi.GPIO as GPIO

class Heater:
    def __init__(self, pwm_pin=18, freq=10):
        GPIO.setmode(GPIO.BCM)
        self.pwm_pin = pwm_pin
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, freq)
        self.pwm.start(0)
        self.prev_output = 0
        self.du_max = 10  # rate limit per step

    def set_output(self, duty_cycle):
        # Rate limiter
        du = duty_cycle - self.prev_output
        if abs(du) > self.du_max:
            duty_cycle = self.prev_output + (self.du_max if du > 0 else -self.du_max)

        self.pwm.ChangeDutyCycle(duty_cycle)
        self.prev_output = duty_cycle

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup()
