from queue import Queue
from system import System

def simulate_RoundRobin(processes, quantum, max_time):
    processes_queue = Queue()
    system = System()
    timer = 0
    quantum_flag = 1
    served_processes = {}
    current_process = None
    while len(processes_queue) != 0 or timer <= max_time or current_process is not None:
        system.listen(timer, processes, processes_queue)
        if current_process is None:
            current_process = processes_queue.dequeue()
        if current_process:
            # print(f"processor clock: {timer}, serving process {current_process['name']}")
            current_process['execution_time'] -= 1
            if current_process['execution_time'] == 0:
                for process in processes:
                    if process['name'] == current_process['name']:
                        current_process['execution_time'] = process['execution_time']
                # print(f"processor clock: {timer}, finished process {current_process['name']}")
                served_processes[timer+1] = current_process
                current_process = None
                quantum_flag = 1
            else:
                if quantum_flag == quantum:
                    # print(quantum_flag, current_process, timer)
                    quantum_flag = 1
                    processes_queue.enqueue(current_process)
                    current_process = None
                    timer += 1
                    continue
                else:
                    quantum_flag += 1
        else:
            pass
        timer += 1
    return served_processes
