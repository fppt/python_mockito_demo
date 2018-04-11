import json

from pyramid.response import Response
from pyramid.view import view_config

from mockito_demo.controllers.abstract_controller import AbstractController
from mockito_demo.job import sum_job, long_job
from mockito_demo.worker import worker


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
            job = sum_job.SumJob(val1, val2)
        elif job_type == "LongJob":
            job = long_job.LongJob()
        else:
            return Response("Job Not Found")

        # Create worker to run job
        worker_rest = worker.Worker("Rest Based Worker", job)
        worker_rest.run()

        # Send result
        result = json.dumps({'worker_name': worker_rest.name, 'job_name': worker_rest.job.name, 'result': worker_rest.job.result})
        response = Response()
        response.json = json.loads(result)

        return response
