from random import choice, seed
import csv

def generate_pages(n, n_of_pages):
    pages = [hex(i) for i in range(n_of_pages)]
    pages_to_load = [choice(pages) for _i in range(n)]
    return pages_to_load

def generate_to_csv(n, n_of_pages=16, custom_seed=256435):
    seed(custom_seed)
    pages = generate_pages(n, n_of_pages)
    csv_file_name = f"data\\pages_x{n}_{custom_seed}"
    with open(csv_file_name, 'w') as csv_file:
        csv_file.write('address')
        for page in pages:
            csv_file.write('\n')
            csv_file.write(str(page))
    return csv_file_name

def csv_to_list(file_name):
    pages = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        reader.__next__()
        for line in reader:
            pages.append(line[0])
    return pages