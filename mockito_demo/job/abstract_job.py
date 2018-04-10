from abc import abstractmethod


class AbstractJob(object):
    """
    The base definition of a job.
    Defines jobs for :func:`~mockito_demo.worker.worker.execute` to execute.
    """
    def __init__(self, name):
        self.name = name
        self.result = None

    @abstractmethod
    def execute(self):
        pass

