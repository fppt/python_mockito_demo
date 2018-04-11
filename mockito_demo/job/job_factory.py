import random

from mockito_demo.job.long_job import LongJob
from mockito_demo.job.sum_job import SumJob


def generate_job():
    job_to_generate = random.randint(0, 1)
    if job_to_generate == 0:
        return generate_sum_job()
    elif job_to_generate == 1:
        return generate_long_job()


def generate_sum_job():
    val1 = random.randint(1, 100)
    val2 = random.randint(1, 100)
    return SumJob(val1, val2), val1, val2


def generate_long_job():
    return LongJob(), None, None
