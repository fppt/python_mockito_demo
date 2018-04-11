import unittest

from mockito_demo.job.abstract_job import AbstractJob
from mockito_demo.manager.manager import Manager


class MockJob(AbstractJob):

    def __init__(self):
        super().__init__("Mock Job")

    def execute(self):
        return True


class ManagerTestWorse(unittest.TestCase):

    def test_when_giving_manager_jobs_to_run_ensure_all_jobs_run(self):
        # Create a Manager
        manager = Manager()

        # Create Work For Manager
        jobs = []
        for x in range(10):
            jobs.append(MockJob())

        # Run The Jobs
        manager.run_jobs(jobs)

        # Are we done yet?
        self.assertTrue(manager.is_done())

        # How Do The Results Look?
        for job, worker in zip(jobs, manager.workers):
            expected_result = job.result
            result = worker.job.result
            self.assertEqual(result, expected_result)

