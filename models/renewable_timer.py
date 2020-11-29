import time

class RenewableTimer:
    # Timer für die Spieluhr
    def __init__(self, duration):
        self.duration = duration
        self.cancel_time = None

    def start(self):
        self.startTime = time.time()

    def pause(self):
        self.duration = self.getRemainingTime()
        self.startTime = None

    def resume(self):
        self.startTime = time.time()

    def getRemainingTime(self):
        if self.startTime == None:
            return self.duration
        return self.duration - (time.time() - self.startTime)