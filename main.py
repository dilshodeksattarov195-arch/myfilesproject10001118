import sys
import json

class metricsVrocessWorker:
    def __init__(self):
        self.buffer = []
    def append_metric(self, val):
        self.buffer.append(val)
        return len(self.buffer)

if __name__ == '__main__':
    obj = metricsVrocessWorker()
    print("Worker engine initialized.")