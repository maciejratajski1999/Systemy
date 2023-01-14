from queue import Queue
import random

n = 20

def make_process(arrive_time, execution_time, name="unknown process"):
    return {'name': name,
            'arrive_time' : arrive_time,
            'execution_time' : execution_time}

processes = [make_process(random.randint(0, 100), random.randint(0, 10), f"process{i}") for i in range(n)]
processes_queue = Queue()
timer = 0
while len(processes_queue) != n:
    for process in processes:
        if process['arrive_time'] == timer:
            processes_queue.enqueue(process)
            print(f"proessor clock: {timer}, enqueued process {process['name']}")
    timer += 1

print(processes_queue)