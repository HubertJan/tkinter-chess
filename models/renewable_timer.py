from threading import Timer
import time


class RenewableTimer:

    def __init__(self, timeout, callback):
        self.timer = Timer(timeout, callback)

        self.start_time = None
        self.cancel_time = None

        self.timeout = timeout
        self.callback = callback

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.start_time = time.time()
        self.timer.start()

    def pause(self):
        self.cancel_time = time.time()
        self.timer.cancel()
        return self.get_remaining_time()

    def resume(self):
        self.timeout = self.get_remaining_time()
        self.timer = Timer(self.timeout, self.callback)
        self.start_time = time.time()
        self.timer.start()

    def get_remaining_time(self):
        if self.start_time is None or self.cancel_time is None:
            return self.timeout
        return self.timeout - (self.cancel_time - self.start_time)