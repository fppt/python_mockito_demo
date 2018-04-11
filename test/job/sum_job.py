import unittest
from mockito_demo.job.sum_job import SumJob


class SumJobTest(unittest.TestCase):

    def test_when_adding_two_values_return_sum(self):
        val1 = 3
        val2 = 4
        sum_job = SumJob(val1, val2)
        sum_job.execute()
        self.assertEqual(7, sum_job.result)

