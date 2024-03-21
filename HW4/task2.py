import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import logging
import time
import uuid

from multiprocessing import cpu_count
from datetime import datetime

logging.basicConfig(filename='artifacts/task2_logs.txt', level=logging.INFO, format='%(message)s')


def current_time():
    return datetime.now().strftime("%A, %d %B %Y, %I:%M:%S %p")


def worker(f, a, b, step):
    job_id = uuid.uuid4()
    logging.info(f"Job {job_id} started at {current_time()}")
    acc = 0
    for i in range(int((b - a) // step)):
        acc += f(a + i * step) * step
    logging.info(f"Job {job_id} ended at {current_time()}")
    return acc


def integrate(f, a, b, thread_pool, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    with thread_pool(max_workers=n_jobs) as executor:
        futures = {
            executor.submit(
                worker,
                f,
                a + i * chunk_size * step,
                a + (i + 1) * chunk_size * step,
                step,
            )
            for i in range(n_jobs)
        }
        return sum(
            future.result() for future in as_completed(futures)
        )


def compare_integrate(func, a, b, n_iter=10000000):
    cpu_num = cpu_count()
    with open("artifacts/task2_execution_time_comparison.txt", "w") as f:
        for pool in [ThreadPoolExecutor, ProcessPoolExecutor]:
            for n_jobs in range(1, 2*cpu_num + 1):
                start_time = time.time()
                result = integrate(func, a, b, pool, n_jobs=n_jobs, n_iter=n_iter)
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"{pool}, n_jobs: {n_jobs}, execution_time: {execution_time}", file=f)


if __name__ == "__main__":
    compare_integrate(math.cos, 0, math.pi / 2)
