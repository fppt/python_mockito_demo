import unittest

from mockito import verify

from mockito_demo.manager.manager import Manager
from test.tools import mock_helper


class ManagerTestGood(unittest.TestCase):

    def test_when_giving_manager_jobs_to_run_ensure_all_jobs_run(self):
        # Create a Manager
        manager = Manager()

        # Create Work For Manager
        jobs = []
        for x in range(10):
            mock_job, _, _ = mock_helper.generate_mock_job()
            jobs.append(mock_job)

        # Run The Jobs
        manager.run_jobs(jobs)

        # Are we done yet?
        self.assertTrue(manager.is_done())

        # How Do The Results Look?
        for job, worker in zip(jobs, manager.workers):
            expected_result = job.result
            result = worker.job.result
            self.assertEqual(result, expected_result)

        # We can even check if methods were called as expected
        for job in jobs:
            verify(job, times=1).execute()

