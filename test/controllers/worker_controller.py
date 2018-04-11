import unittest

from pyramid import testing

from mockito_demo.controllers.worker_controller import WorkerController


class WorkerControllerTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_when_submitting_bad_job_get_error(self):
        # Create Dummy Request
        print("Hello")
        request = testing.DummyRequest()
        request.matchdict = {'job_type': 'crap'}

        # Create Controller
        controller = WorkerController(request)

        # Execute Job
        result = controller.run_job()
        self.assertTrue("Not Found" in str(result.body))
