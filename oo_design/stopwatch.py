import datetime


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def stop(self):
        self.stop_time = datetime.datetime.now()

    def get_lapsed_time(self):
        return self.stop_time - self.start_time
