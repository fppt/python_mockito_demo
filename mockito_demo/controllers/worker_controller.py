import random

from pyramid.response import Response
from pyramid.view import view_config

from mockito_demo.controllers.abstract_controller import AbstractController
from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob
from mockito_demo.worker.worker import Worker


class WorkerController(AbstractController):

    def __init__(self, request):
        super().__init__()
        self.request = request

    @view_config(route_name='worker', request_method='POST')
    def run_job(self):
        # Create Job
        job_type = self.request.matchdict["job-type"]
        if (job_type == "SumJob"):
            val1 = random.randint(1, 100)
            val2 = random.randint(1, 100)
            job = SumJob(val1, val2)
        elif (job_type == "LongJob"):
            job = LongJob()
        else:
            return Response("Job Not Found")

        # Create worker to run job
        worker = Worker("Rest Based Worker", job)
        worker.run()

        return Response(
            "Worker [{}] completed job [{}] with result [{}]".format(worker.name, worker.job.name, worker.job.result))
