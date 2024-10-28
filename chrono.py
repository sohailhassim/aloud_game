import time

class Chrono:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        if self.start_time:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def is_finished(self):
        if self.start_time:
            return self.elapsed_time + time.time() - self.start_time >= self.duration
        else:
            return self.elapsed_time >= self.duration

    def get_remaining_time(self):
        if self.start_time:
            return self.duration - (self.elapsed_time + time.time() - self.start_time)
        else:
            return self.duration - self.elapsed_time
        
