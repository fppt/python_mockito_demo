from mockito_demo.job.abstract_job import AbstractJob


class SubtractJob(AbstractJob):
    def __init__(self, val1, val2):
        super().__init__("SubtractJob")
        self.val1 = val1
        self.val2 = val2

    def execute(self):

        self.result = self.val1 - self.val2
        return self.result
