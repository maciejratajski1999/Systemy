def find_most_used(times_loaded, memory):
    most_used = ('', 0)
    currently_loaded = [(page,n) for page, n in times_loaded.items() if page in memory]
    for page, n in currently_loaded:
        if n > most_used[1]:
            most_used = (page, n)
    return most_used[0]

def simulate_MFU(pages, memory_size):
    memory = []
    times_loaded = {page : 0 for page in pages}
    for page in pages:
        if page in memory:
            continue
        if len(memory) < memory_size:
            memory.append(page)
            times_loaded[page] += 1
        else:
            most_used = find_most_used(times_loaded, memory)
            memory.remove(most_used)
            memory.append(page)
            times_loaded[page] += 1
    return times_loaded