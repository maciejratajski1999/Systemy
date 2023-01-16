def find_most_used(times_loaded):
    return 

def simulate_MFU(pages, memory_size):
    memory = []
    times_loaded = {page : 0 for page in pages}
    for page in pages:
        if len(memory) < memory_size:
            memory.enqueue(page)
            times_loaded[page] += 1
        else:
            memory.dequeue()
            memory.enqueue(page)
            times_loaded[page] += 1
    return times_loaded