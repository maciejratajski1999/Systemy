from pages_data_utils import generate_to_csv, csv_to_list
from sys import setrecursionlimit
from FIFO import simulate_FIFO

if __name__ == '__main__':
    setrecursionlimit(2000)
    n_of_pages = 16
    n_of_page_loads = [10] + [50 * i for i in range(1, 6)] + [100 * i for i in range(3, 11)]
    memory_size = 10
    fifo_average_times_loaded = []
    for n in n_of_page_loads:
        pages_file_name = generate_to_csv(n, n_of_pages)
        pages_to_load = csv_to_list(pages_file_name)
        times_loaded = simulate_FIFO(pages_to_load, memory_size)
        fifo_times_loaded = [value for value in times_loaded.values()]
        fifo_average = sum(fifo_times_loaded) / len(fifo_times_loaded)
        fifo_average_times_loaded.append(fifo_average)
        print(fifo_average_times_loaded)