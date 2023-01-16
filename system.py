class System:

    def listen(self, timer, processes, processes_queue):
        for process in processes:
            if process['arrive_time'] == timer:
                processes_queue.enqueue(dict(process))
                # print(f"proessor clock: {timer}, enqueued process {process['name']}")

    def __serve_next(self, timer, current_process, processes_queue):
        current_process['begin_time'] = timer
        current_process['process'] = processes_queue.dequeue()
        if current_process['process'] is not None:
            pass
            # print(f"processor clock: {timer}, started serving process {current_process['process']['name']}")
        return current_process

    def serve(self, timer, current_process, processes_queue, served_processes):
        if current_process['process'] is None:
            current_process = self.__serve_next(timer, current_process, processes_queue)
        else:
            if current_process['begin_time'] + current_process['process']['execution_time'] <= timer:
                served_processes[timer] = current_process['process']
                current_process = self.__serve_next(timer, current_process, processes_queue)
            else:
                pass
        return current_process

    # def serve_quantum_time(self, timer, current_process, processes_queue, served_processes, quantum):
    #     if current_process['process'] is None:
    #         current_process = self.__serve_next(timer, current_process, processes_queue)