import time

from mockito_demo.job.abstract_job import AbstractJob


class LongJob(AbstractJob):

    def __init__(self):
        super().__init__("LongJob")

    def execute(self):
        time.sleep(10)  # This is just to represent a long running job like hitting the db
        self.result = True
