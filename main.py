from data_utils import save_to_csv, csv_to_list, save_results_to_csv
from FCFS import simulate_FCFS
from RoundRobin import simulate_RoundRobin

if __name__ == '__main__':
    number_of_processes = [10, 100, 1000]
    max_arrival_time = 1000
    max_execution_time = 10
    # data_csv = [save_to_csv(n, max_arrival_time, max_execution_time) for n in number_of_processes]
    # csv_file_name = save_to_csv(n)
    # csv_file_name = "processes_x20_2023-01-16T14_00_54.csv"
    data_csv = ["processes_x10_2023-01-16T14_12_04.csv",
                "processes_x100_2023-01-16T14_12_04.csv",
                "processes_x1000_2023-01-16T14_12_04.csv"]
    for csv_file_name in data_csv:
        processes = csv_to_list(csv_file_name)

        FCFS_served_processes = simulate_FCFS(processes, max_arrival_time)
        save_results_to_csv(FCFS_served_processes, csv_file_name, "FCFS")

        quantum = 5
        RoundRobin_served_processes = simulate_RoundRobin(processes, quantum, max_arrival_time)
        save_results_to_csv(RoundRobin_served_processes, csv_file_name, "RR")