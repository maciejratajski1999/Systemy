from pages_data_utils import generate_to_csv, csv_to_list
from sys import setrecursionlimit
from FIFO import simulate_FIFO
from MFU import simulate_MFU
from matplotlib import pyplot as plt

if __name__ == '__main__':
    setrecursionlimit(4000)
    n_of_pages = 32
    n_of_page_loads = [100] + [200 * i for i in range(1, 11)]
    memory_size = 10
    fifo_average_times_loaded = []
    mfu_average_times_loaded = []
    for n in n_of_page_loads:
        pages_file_name = generate_to_csv(n, n_of_pages)
        pages_to_load = csv_to_list(pages_file_name)
        fifo_times_loaded = simulate_FIFO(pages_to_load, memory_size)
        fifo_times_loaded = [value for value in fifo_times_loaded.values()]
        fifo_average = sum(fifo_times_loaded) / len(fifo_times_loaded)
        fifo_average_times_loaded.append(fifo_average)

        mfu_times_loaded = simulate_MFU(pages_to_load, memory_size)
        mfu_times_loaded = [value for value in mfu_times_loaded.values()]
        mfu_average = sum(mfu_times_loaded) / len(mfu_times_loaded)
        mfu_average_times_loaded.append(mfu_average)
    plt.plot(n_of_page_loads, fifo_average_times_loaded)
    plt.plot(n_of_page_loads, mfu_average_times_loaded)
    plt.legend(["FIFO", "MFU"])
    plt.xlabel("n of pages loaded")
    plt.ylabel("average times a single page was loaded into memory")
    plt.savefig("times loaded comparison")
    plt.close()

    ratios = [mfu_average_times_loaded[i] / fifo_average_times_loaded[i]
              for i in range(len(n_of_page_loads))]

    plt.plot(n_of_page_loads, ratios)
    plt.title(f"ratio of average times loaded for memory size={memory_size}")
    plt.xlabel("n of pages loaded")
    plt.ylabel("ratio MFU/FIFO")
    plt.savefig("times loaded ratio")