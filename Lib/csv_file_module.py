import csv


def save_all_into_csv(csv_file, rows, columns):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def add_single(csv_file, columns, rows):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(rows)


def read_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        lst = list(reader)
    return lst
