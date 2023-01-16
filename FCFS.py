from queue import Queue
from system import System

def simulate_FCFS(processes, max_time):
    processes_queue = Queue()
    system = System()
    timer = 0
    current_process = {'begin_time' : timer, 'process' : None}
    served_processes = {}
    while len(processes_queue) != 0 or timer <= max_time or current_process['process'] is not None:
        system.listen(timer, processes, processes_queue)
        current_process = system.serve(timer, current_process, processes_queue, served_processes)
        timer += 1
    return served_processes
