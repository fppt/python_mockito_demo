from threading import Thread


class Worker(Thread):

    def __init__(self, name, job):
        Thread.__init__(self)
        self.name = name
        self.job = job

    def run(self):
        """
        Executes a job.
        :return: The result of executing the job
        """
        self.job.execute()
        print("Worker [{}] executed job [{}] and got result [{}]".format(self.name, self.job.name, self.job.result))
