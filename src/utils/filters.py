from collections import deque

class MovingAverage:
    def __init__(self, window_size=5):
        self.window = deque(maxlen=window_size)

    def filter(self, value):
        self.window.append(value)
        return sum(self.window)/len(self.window)
