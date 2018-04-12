from mockito_demo.job.abstract_job import AbstractJob


class CombineJob(AbstractJob):
    def __init__(self, job1, job2):
        super().__init__("CombinerJob")
        self.job1 = job1
        self.job2 = job2

    def execute(self):
        self.result = self.job1.execute() + self.job2.execute()
        return self.result
