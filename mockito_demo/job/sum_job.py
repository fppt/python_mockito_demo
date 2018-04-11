from mockito_demo.job.abstract_job import AbstractJob


class SumJob(AbstractJob):
    """
    Sums two number together. So fancy.
    """
    def __init__(self, val1, val2):
        super().__init__("SumJob")
        self.val1 = val1
        self.val2 = val2

    def execute(self):
        self.result = self.val1 + self.val2
