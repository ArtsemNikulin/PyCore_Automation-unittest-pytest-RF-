import datetime
import os
from contextlib import ContextDecorator
import time


class LogFile(ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_date_time = datetime.datetime.now()
        self.start_time = time.time()

    def __enter__(self):
        self.file = open(self.name, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.run = str(datetime.timedelta(seconds=time.time() - self.start_time))
        log_line = f'Start: {self.start_date_time} | Run: {self.run} | An error occurred: {exc_val}\n'
        self.file.write(log_line)
        self.file.close()


@LogFile('my_trace.log')
def some_func(self):
    print('some f')
