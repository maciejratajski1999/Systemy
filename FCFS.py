from queue import Queue
import random

n = 20

def make_process(arrive_time, execution_time, name="unknown process"):
    return {'name': name,
            'arrive_time' : arrive_time,
            'execution_time' : execution_time}

def listen(timer, processes, processes_queue):
    for process in processes:
        if process['arrive_time'] == timer:
            processes_queue.enqueue(process)
            print(f"proessor clock: {timer}, enqueued process {process['name']}")

def serve_next(timer, current_process, processes_queue):
    current_process['begin_time'] = timer
    current_process['process'] = processes_queue.dequeue()
    if current_process['process'] is not None:
        print(f"processor clock: {timer}, started serving process {current_process['process']['name']}")
    return current_process

def serve(timer, current_process, processes_queue, served_processes):
    if current_process['process'] is None:
        current_process = serve_next(timer, current_process, processes_queue)
    else:
        if current_process['begin_time'] + current_process['process']['execution_time'] <= timer:
            served_processes[timer] = current_process['process']
            current_process = serve_next(timer, current_process, processes_queue)
        else:
            pass
    return current_process

processes = [make_process(random.randint(0, 100), random.randint(1, 10), f"process{i}") for i in range(n)]
processes_queue = Queue()
timer = 0
current_process = {'begin_time' : timer, 'process' : None}
served_processes = {}
while len(processes_queue) != 0 or timer < 100:
    listen(timer, processes, processes_queue)
    serve(timer, current_process, processes_queue, served_processes)
    timer += 1

print(served_processes)