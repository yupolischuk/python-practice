import datetime
from cmd import Cmd

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



class Prompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.sw = Stopwatch()

    def do_start(self, args):
        print("started")
        self.sw.start()

    def do_stop(self, args):
        print("stopped")
        self.sw.stop()
        print(self.sw.get_lapsed_time())

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = Prompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')

