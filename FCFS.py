from queue import Queue
from system import System

def simulate(processes):
    processes_queue = Queue()
    system = System()
    timer = 0
    current_process = {'begin_time' : timer, 'process' : None}
    served_processes = {}
    while len(processes_queue) != 0 or timer < 100:
        system.listen(timer, processes, processes_queue)
        system.serve(timer, current_process, processes_queue, served_processes)
        timer += 1
    return served_processes
