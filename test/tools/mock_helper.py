import random

from mockito import when, mock

from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob


def generate_mock_job():
    coin_flip = random.randint(0, 1)
    if coin_flip:
        my_mock = mock(SumJob)
        val1 = 2
        val2 = 3
        my_mock.result = 5
        my_mock.name = "SumJob"
    else:
        my_mock = mock(LongJob)
        val1 = None
        val2 = None
        my_mock.result = True
        my_mock.name = "LongJob"

    when(my_mock).execute().thenReturn(None)
    return my_mock, val1, val2
