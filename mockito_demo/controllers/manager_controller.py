import random

from pyramid.response import Response
from pyramid.view import view_config

from mockito_demo.controllers.abstract_controller import AbstractController
from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob


class ManagerController(AbstractController):

    def __init__(self, request, manager):
        super().__init__(request)
        self.manager = manager

    @view_config(route_name='manager-get', request_method='GET')
    def get_manager_jobs_results(self):
        results = {}
        for worker in self.manager.workers:
            results[worker.name] = worker.job.result
        return Response(results)

    @view_config(route_name='manager-post', request_method='POST')
    def post_manager_job(self):
        job_type = self.request.matchdict["job-type"]
        if (job_type == "SumJob"):
            val1 = random.randint(1, 100)
            val2 = random.randint(1, 100)
            self.manager.run_job(SumJob(val1, val2))
        elif (job_type == "LongJob"):
            self.manager.run_job(LongJob())
        else:
            return Response("Job Not Found")
