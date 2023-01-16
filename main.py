from data_utils import save_to_csv, csv_to_list, save_results_to_csv
from FCFS import simulate

if __name__ == '__main__':
    n = 20
    csv_file_name = save_to_csv(n)
    processes = csv_to_list(csv_file_name)
    FCFS_served_processes = simulate(processes)
    print(FCFS_served_processes)
    save_results_to_csv(FCFS_served_processes, "FCFS")