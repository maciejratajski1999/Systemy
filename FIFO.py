from queue import Queue

def simulate_FIFO(pages, memory_size):
    queue = Queue()
    times_loaded = {page : 0 for page in pages}
    for page in pages:
        if len(queue) < memory_size:
            queue.enqueue(page)
            times_loaded[page] += 1
        else:
            queue.dequeue()
            queue.enqueue(page)
            times_loaded[page] += 1
    return times_loaded