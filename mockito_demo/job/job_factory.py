import random

from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob


def generate_job():
    job_to_generate = random.randint(0, 1)
    if job_to_generate == 0:
        return __generate_sum_job()
    elif job_to_generate == 1:
        return __generate_long_job()


def __generate_sum_job():
    val1 = random.randint(1, 100)
    val2 = random.randint(1, 100)
    return SumJob(val1, val2)


def __generate_long_job():
    return LongJob()
