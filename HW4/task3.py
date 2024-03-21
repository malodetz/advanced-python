import time
import codecs

from multiprocessing import Queue, Pipe, Process
from task2 import current_time


def process_a(queue_a, pipe_ab):
    while True:
        if not queue_a.empty():
            message = queue_a.get()
            message = message.lower()
            pipe_ab.send(message)
            time.sleep(5)


def process_b(child_conn_ab, pipe_bout):
    while True:
        message = child_conn_ab.recv()
        message = codecs.encode(message, 'rot_13')
        pipe_bout.send(message)


if __name__ == "__main__":
    queue_a = Queue()
    pipe_ab, child_conn_ab = Pipe()
    pipe_bout, child_conn_bout = Pipe()

    p1 = Process(target=process_a, args=(queue_a, pipe_ab), daemon=True)
    p2 = Process(target=process_b, args=(child_conn_ab, pipe_bout), daemon=True)

    p1.start()
    p2.start()

    with open("artifacts/task3.txt", "w") as f:
        try:
            while True:
                user_input = input()
                print(f"{current_time()}, user input:{user_input}", file=f)
                if not user_input:
                    break
                queue_a.put(user_input)
                output = child_conn_bout.recv()
                print(output)
                print(f"{current_time()}, system output:{output}", file=f)
        finally:
            p1.terminate()
            p2.terminate()
            p1.join()
            p2.join()
