import time

from mockito_demo.worker.worker import Worker


class Manager(object):

    def __init__(self):
        self.workers = []

    def run_jobs(self, jobs_to_run):
        job_num = 0
        for job in jobs_to_run:
            job_num = job_num + 1
            print("Manager starting new job [{}]".format(job_num))
            worker = Worker("My Worker " + str(job_num), job)
            worker.start()
            self.workers.append(worker)

    def is_done(self):
        for worker in self.workers:
            # This is dumb but I am a dumb python developer so it's okay
            while worker.isAlive():
                time.sleep(1)
        return True
