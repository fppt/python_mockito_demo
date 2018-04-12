import unittest

from mockito import ANY, when, arg_that

from mockito_demo.job import job_factory, sum_job


class JobFactoryTest(unittest.TestCase):

    def test_having_fun_with_mocking(self):
        when(job_factory).generate_sum_job(1, ANY).thenReturn(sum_job.SumJob(-1, 0))
        when(job_factory).\
            generate_sum_job(arg_that(lambda val: val % 2 == 0), arg_that(lambda val: val % 2 == 0)).\
            thenReturn(sum_job.SumJob(-2, 0))

        result = job_factory.generate_sum_job(1, 3).execute()
        self.assertEqual(-1, result)
        print(result)

        result = job_factory.generate_sum_job(4, 8).execute()
        self.assertEqual(-2, result)
        print(result)
