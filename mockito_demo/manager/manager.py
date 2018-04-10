import time

from mockito_demo.worker.worker import Worker


class Manager(object):

    def __init__(self):
        self.workers = []
        self.job_num = 0

    def run_jobs(self, jobs_to_run):
        for job in jobs_to_run:
            self.run_job(job)

    def run_job(self, job_to_run):
        self.job_num = self.job_num + 1
        print("Manager starting new job [{}]".format(self.job_num))
        worker = Worker("My Worker " + str(self.job_num), job_to_run)
        worker.start()
        self.workers.append(worker)

    def is_done(self):
        for worker in self.workers:
            # This is dumb but I am a dumb python developer so it's okay
            while worker.isAlive():
                time.sleep(1)
        return True
