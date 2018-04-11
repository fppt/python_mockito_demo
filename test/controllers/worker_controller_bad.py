import unittest

from pyramid import testing

from mockito_demo.controllers.worker_controller import WorkerController
from mockito_demo.job import job_factory


class WorkerControllerTestBad(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_when_submitting_jobs_ensure_results_returned(self):
        for job_num in range(10):
            # Produce and run Jobs Locally
            job, val1, val2 = job_factory.generate_job()
            job.execute()
            expected_result = job.result

            # Now Run It Remotely
            request = testing.DummyRequest()
            request.matchdict = {'job_type': job.name}
            request.params['val1'] = val1
            request.params['val2'] = val2

            # Execute Job
            controller = WorkerController(request)
            result = controller.run_job()
            self.assertEquals(expected_result, result.json['result'])


