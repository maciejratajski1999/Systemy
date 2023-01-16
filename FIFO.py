from queue import Queue

def simulate_FIFO(pages, memory_size):
    memory = Queue()
    times_loaded = {page : 0 for page in pages}
    for page in pages:
        if page in memory.to_list():
            continue
        if len(memory) < memory_size:
            memory.enqueue(page)
            times_loaded[page] += 1
        else:
            memory.dequeue()
            memory.enqueue(page)
            times_loaded[page] += 1
    return times_loaded