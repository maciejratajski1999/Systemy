from data_utils import save_to_csv, csv_to_list, save_results_to_csv, average_wait_time
from FCFS import simulate_FCFS
from RoundRobin import simulate_RoundRobin
from sys import setrecursionlimit
from matplotlib import pyplot as plt


if __name__ == '__main__':
    setrecursionlimit(2000)
    number_of_processes = [10] + [50*i for i in range(1, 6)] + [100*i for i in range(3, 11)]
    max_arrival_time = 500
    max_execution_time = 10
    data_csv = [save_to_csv(n, max_arrival_time, max_execution_time) for n in number_of_processes]
    # csv_file_name = "processes_x20_2023-01-16T14_00_54.csv"
    # data_csv = ["data\\processes_x10_2023-01-16T14_28_55.csv",
    #             "data\\processes_x100_2023-01-16T14_28_55.csv",
    #             "data\\processes_x1000_2023-01-16T14_28_55.csv"]
    fcfs_average_wait_times = []
    rr_average_wait_times = []
    for csv_file_name in data_csv:
        processes = csv_to_list(csv_file_name)

        FCFS_served_processes = simulate_FCFS(processes, max_arrival_time)
        fcfs_csv_file_name = save_results_to_csv(FCFS_served_processes, csv_file_name, "fcfs")
        # print(f"Average wait time for FCFS for n={len(FCFS_served_processes)}:")
        fcfs_results_as_list = csv_to_list(fcfs_csv_file_name)
        fcfs_average_wait_times.append(average_wait_time(fcfs_results_as_list))


        quantum = 5
        RoundRobin_served_processes = simulate_RoundRobin(processes, quantum, max_arrival_time)
        rr_csv_file_name = save_results_to_csv(RoundRobin_served_processes, csv_file_name, "rr")
        # print(f"Average wait time for RoundRobin for n={len(RoundRobin_served_processes)}:")
        rr_results_as_list = csv_to_list(rr_csv_file_name)
        rr_average_wait_times.append(average_wait_time(rr_results_as_list))

    plt.plot(number_of_processes, fcfs_average_wait_times)
    plt.plot(number_of_processes, rr_average_wait_times)
    plt.legend(["FCFS", "RoundRobin"])
    plt.xlabel("n of processes")
    plt.ylabel("average wait time for a process to finish")
    plt.savefig("wait time comparison")
    plt.close()

    ratios = [rr_average_wait_times[i] / fcfs_average_wait_times[i]
              for i in range(len(number_of_processes))]
    
    plt.plot(number_of_processes, ratios)
    plt.title("ratio of average wait time")
    plt.xlabel("n of processes")
    plt.ylabel("ratio")
    plt.savefig("wait time ratio")