import json

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
        """
        Bad rest controller is bad. Look at that encapsulated constructor
        :return:
        """
        # Create Job
        job_type = self.request.matchdict["job_type"]
        if job_type == "SumJob":
            val1 = int(self.request.params['val1'])
            val2 = int(self.request.params['val2'])
            job = SumJob(val1, val2)
        elif job_type == "LongJob":
            job = LongJob()
        else:
            return Response("Job Not Found")

        # Create worker to run job
        worker = Worker("Rest Based Worker", job)
        worker.run()

        # Send result
        result = json.dumps({'worker_name': worker.name, 'job_name': worker.job.name, 'result': worker.job.result})
        response = Response()
        response.json = json.loads(result)

        return response
