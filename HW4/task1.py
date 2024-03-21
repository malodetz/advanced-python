import time
import threading
import multiprocessing


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def fib_sequential(n):
    for i in range(10):
        fib(n)


def fib_threading(n):
    threads = []
    for i in range(10):
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def fib_multiprocessing(n):
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    n = 200000
    with open("artifacts/task1.txt", "w") as f:
        start = time.time()
        fib_sequential(n)
        end = time.time()
        print("Sequential execution time:", end - start, file=f)

        start = time.time()
        fib_threading(n)
        end = time.time()
        print("Multithreading execution time:", end - start, file=f)

        start = time.time()
        fib_multiprocessing(n)
        end = time.time()
        print("Multiprocessing execution time:", end - start, file=f)
