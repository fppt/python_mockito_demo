import unittest
from mockito_demo.job.sum_job import SumJob


class SumJobTest(unittest.TestCase):

    def test_when_adding_two_values_return_sum(self):
        val1 = 3
        val2 = 4
        sum_job = SumJob(val1, val2)
        self.assertEqual(sum_job.execute(), 7)


if __name__ == '__main__':
    unittest.main()
