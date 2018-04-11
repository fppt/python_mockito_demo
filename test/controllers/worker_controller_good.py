import unittest

from mockito import mock, when, ANY, verify, mockito, unstub
from pyramid import testing

from mockito_demo import job
from mockito_demo.controllers.worker_controller import WorkerController
from mockito_demo.job import sum_job, long_job
from mockito_demo.worker import worker
from mockito_demo.worker.worker import Worker
from test.tools import mock_helper


class WorkerControllerTestGood(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_when_submitting_jobs_ensure_results_returned(self):
        for job_num in range(10):
            # Produce and run Jobs Locally
            job_mock, val1, val2 = mock_helper.generate_mock_job()
            expected_result = job_mock.result

            # Configure Mock Worker
            worker_mock = mock(Worker)
            worker_mock.name = "My Super Amazing Ultra Cool I am Running Out Of Adjectives Mock"
            worker_mock.job = job_mock
            when(worker).Worker(ANY, ANY).thenReturn(worker_mock)
            when(worker_mock).run().thenReturn(None)

            # Configure Mock Job
            if job_mock.name == "SumJob":
                when(sum_job).SumJob(ANY, ANY).thenReturn(job_mock)

            if job_mock.name == "LongJob":
                when(long_job).LongJob().thenReturn(job_mock)

            # Now Run It Remotely
            request = testing.DummyRequest()
            request.matchdict = {'job_type': job_mock.name}
            request.params['val1'] = val1
            request.params['val2'] = val2

            # Execute Job
            controller = WorkerController(request)
            result = controller.run_job()

            # Assert Some Stuff
            print("\n --------------- Result ---------------")
            print(str(result))
            self.assertEquals(expected_result, result.json['result'])

            # Verify Mocks because we are nit picky bastards
            verify(worker_mock, times=1).run()
            verify(worker, times=1).Worker(ANY, ANY)
            verify(job_mock, times=0).execute()  # The worker was mocked so the job should have never been executed

            # Reset Mocks because we are good also because if I don't do this my colleagues will flog me
            unstub()
