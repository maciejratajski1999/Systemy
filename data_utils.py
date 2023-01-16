from random import randint, seed
from datetime import datetime
import csv

def iso_time_format():
    iso_time = datetime.now().isoformat()
    iso_time = iso_time.split('.')[0].replace(':', '_')
    return iso_time

def make_process(arrive_time, execution_time, name="unknown process"):
    return {'name': name,
            'arrive_time' : arrive_time,
            'execution_time' : execution_time}

def generate_processes(n, max_arrival_time, max_execution_time):
    processes = [make_process(randint(0, max_arrival_time),
                              randint(1, max_execution_time),
                              f"process{i}") for i in range(n)]
    return processes

def save_to_csv(n, max_arrival_time=100, max_execution_time=10, custom_seed=256435):
    processes = generate_processes(n, max_arrival_time, max_execution_time)
    # iso_time = iso_time_format()
    seed(custom_seed)
    csv_file_name = f"data\\processes_x{n}_{custom_seed}"
    with open(csv_file_name, 'w') as csv_file:
        csv_file.write('name,arrive_time,execution_time')
        for process in processes:
            csv_file.write('\n')
            values = [str(v) for v in process.values()]
            csv_file.write(','.join(values))
    return csv_file_name

def csv_to_list(csv_file_name):
    processes = []
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        keys = reader.__next__()
        for values in reader:
            values = [int(values[i]) if i > 0 else values[i] for i in range(len(values))]
            process = {keys[i] : values[i] for i in range(len(keys))}
            processes.append(process)
    return processes

def save_results_to_csv(finished_processes, name, prefix):
    name = name[5:]
    csv_file_name = f"{prefix}\\{name}"
    with open(csv_file_name, 'w') as csv_file:
        csv_file.write('name,arrive_time,execution_time,exit_time')
        for exit_time, process in finished_processes.items():
            csv_file.write('\n')
            values = [str(v) for v in process.values()] + [str(exit_time)]
            csv_file.write(','.join(values))
    return csv_file_name

def average_wait_time(finished_processes):

    wait_times = [process['exit_time'] - process['arrive_time'] - process['execution_time']
                  for process in finished_processes]
    return sum(wait_times) / len(wait_times)