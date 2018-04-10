import random
import unittest

from mockito import when, mock, verify

from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob
from mockito_demo.manager.manager import Manager


class ManagerTestBad(unittest.TestCase):

    def test_when_giving_manager_jobs_to_run_ensure_all_jobs_run(self):
        # Create a Manager
        manager = Manager()

        # Create Work For Manager
        jobs = []
        for x in range(10):
            jobs.append(self.__generate_mock())

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

    def __generate_mock(self):
        coin_flip = random.randint(0,1)
        if coin_flip:
            my_mock = mock(SumJob)
            my_mock.result = 5
        else:
            my_mock = mock(LongJob)
            my_mock.result = True

        my_mock.name = "Mocked Thing"
        when(my_mock).execute().thenReturn(None)
        return my_mock


if __name__ == '__main__':
    unittest.main()
